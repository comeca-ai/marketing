import streamlit as st
import requests
from bs4 import BeautifulSoup
# from googleapiclient.discovery import build # Para PageSpeed Insights no futuro

def evaluate_site_structure(soup):
    """Avalia a estrutura básica do site (headings, parágrafos)."""
    report = {"headings": {"h1": 0, "h2": 0, "h3": 0}, "paragraphs": 0, "links": 0}
    for i in range(1, 4):
        report["headings"][f"h{i}"] = len(soup.find_all(f"h{i}"))
    report["paragraphs"] = len(soup.find_all("p"))
    report["links"] = len(soup.find_all("a"))

    recommendations = []
    if report["headings"]["h1"] == 0:
        recommendations.append("Crítico: Ausência de tag H1. Adicione um H1 único e descritivo por página.")
    elif report["headings"]["h1"] > 1:
        recommendations.append("Alerta: Múltiplas tags H1. Utilize apenas uma tag H1 por página.")
    if report["headings"]["h2"] < 2 and report["paragraphs"] > 500: # Heurística simples
        recommendations.append("Sugestão: Poucas tags H2 para um conteúdo extenso. Considere adicionar mais H2 para melhor estruturação.")
    if report["paragraphs"] < 5:
        recommendations.append("Alerta: Pouco conteúdo textual (parágrafos). LLMs valorizam conteúdo detalhado.")

    return report, recommendations

def evaluate_meta_tags(soup):
    """Avalia as meta tags principais (title, description)."""
    report = {"title": "", "description": ""}
    recommendations = []

    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        report["title"] = title_tag.string.strip()
        if len(report["title"]) < 30:
            recommendations.append("Alerta: Título (meta title) muito curto. Tente algo entre 50-60 caracteres.")
        if len(report["title"]) > 65:
            recommendations.append("Alerta: Título (meta title) muito longo. Tente algo entre 50-60 caracteres.")
    else:
        recommendations.append("Crítico: Meta title ausente. Adicione um título otimizado para cada página.")

    description_tag = soup.find("meta", attrs={"name": "description"})
    if description_tag and description_tag.get("content"):
        report["description"] = description_tag.get("content").strip()
        if len(report["description"]) < 70:
            recommendations.append("Alerta: Meta description muito curta. Tente algo entre 120-150 caracteres.")
        if len(report["description"]) > 160:
            recommendations.append("Alerta: Meta description muito longa. Tente algo entre 120-150 caracteres.")
    else:
        recommendations.append("Crítico: Meta description ausente. Adicione uma descrição concisa e atrativa.")

    return report, recommendations

def evaluate_structured_data(soup):
    """Verifica a presença de alguns tipos comuns de dados estruturados (JSON-LD)."""
    report = {"found_types": []}
    recommendations = []

    scripts = soup.find_all("script", type="application/ld+json")
    if not scripts:
        recommendations.append("Sugestão: Nenhum dado estruturado (JSON-LD) detectado. Considere adicionar para melhor interpretação por IAs.")
        return report, recommendations

    for script in scripts:
        try:
            import json
            data = json.loads(script.string)
            if "@type" in data:
                type_val = data["@type"]
                if isinstance(type_val, list):
                    report["found_types"].extend(type_val)
                else:
                    report["found_types"].append(type_val)
        except json.JSONDecodeError:
            recommendations.append("Alerta: Erro ao decodificar um script JSON-LD. Verifique a sintaxe.")

    if not report["found_types"]:
        recommendations.append("Sugestão: Dados estruturados (JSON-LD) presentes, mas nenhum @type identificado claramente. Revise a implementação.")
    else:
        recommendations.append(f"Info: Tipos de dados estruturados detectados: {', '.join(list(set(report['found_types'])))}.")

    return report, recommendations

def evaluate_speed_basic(url):
    """Avaliação básica de velocidade (tempo de resposta)."""
    report = {"response_time_ms": None}
    recommendations = []
    try:
        response = requests.get(url, timeout=10)
        report["response_time_ms"] = response.elapsed.total_seconds() * 1000
        if report["response_time_ms"] > 2000: # 2 segundos
            recommendations.append(f"Alerta: Tempo de resposta alto ({report['response_time_ms']:.0f}ms). Otimize a velocidade do servidor/aplicação.")
        else:
            recommendations.append(f"Info: Tempo de resposta: {report['response_time_ms']:.0f}ms.")
    except requests.RequestException as e:
        recommendations.append(f"Erro: Não foi possível acessar a URL para teste de velocidade: {e}")
    return report, recommendations

# --- Funções de Análise Específica para LLMs (Placeholder) ---
def analyze_for_chatgpt(soup, base_recommendations):
    """Analisa o site sob a ótica do ChatGPT."""
    llm_specific_recs = []
    # ChatGPT valoriza conteúdo aprofundado, bem escrito e original.
    # Poderia verificar a contagem de palavras, complexidade do texto (Flesch-Kincaid), etc.
    paragraphs = soup.find_all("p")
    word_count = sum(len(p.get_text().split()) for p in paragraphs)

    if word_count < 500:
        llm_specific_recs.append("ChatGPT: Conteúdo textual parece curto (<500 palavras). Considere expandir com mais detalhes e profundidade.")
    elif word_count > 2000:
         llm_specific_recs.append("ChatGPT: Conteúdo extenso detectado. Certifique-se de que está bem estruturado e fácil de ler.")

    # Originalidade (difícil de automatizar, mas podemos dar dicas)
    llm_specific_recs.append("ChatGPT: Garanta que o conteúdo seja original e não apenas cópia de outras fontes. LLMs podem penalizar conteúdo duplicado ou de baixa qualidade.")
    llm_specific_recs.append("ChatGPT: Use linguagem natural e conversacional, mas mantenha a precisão e clareza.")
    return llm_specific_recs

def analyze_for_gemini(soup, base_recommendations, speed_report):
    """Analisa o site sob a ótica do Gemini."""
    llm_specific_recs = []
    # Gemini (Google) tende a valorizar velocidade, mobile-friendliness, e dados estruturados.
    if speed_report.get("response_time_ms", 0) > 1500:
        llm_specific_recs.append(f"Gemini: Tempo de resposta ({speed_report.get('response_time_ms', 'N/A'):.0f}ms) pode ser um fator. Otimize para melhor performance.")

    has_structured_data = any("Sugestão: Nenhum dado estruturado" not in rec for rec in base_recommendations["structured_data"])
    if not has_structured_data:
         llm_specific_recs.append("Gemini: A ausência de dados estruturados pode dificultar a compreensão do conteúdo. Implemente Schema.org.")
    else:
        llm_specific_recs.append("Gemini: Dados estruturados detectados são um bom sinal para a compreensão do conteúdo.")

    # Mobile-friendliness (difícil de testar diretamente sem ferramentas mais avançadas)
    llm_specific_recs.append("Gemini: Certifique-se de que o site é responsivo e oferece uma boa experiência em dispositivos móveis.")
    return llm_specific_recs

def analyze_for_grok(soup, base_recommendations):
    """Analisa o site sob a ótica do Grok."""
    llm_specific_recs = []
    # Grok (X/Twitter) pode valorizar informações atuais, verificáveis e com fontes claras.
    # Links para fontes externas, datas de publicação/atualização.
    external_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http') and 'example.com' not in a['href']] # Substituir example.com pela URL base
    if len(external_links) < 2 and len(soup.find_all("p")) > 10 : # Poucos links externos para um conteúdo razoável
        llm_specific_recs.append("Grok: Poucos links para fontes externas. Considere adicionar referências para aumentar a verificabilidade.")
    else:
        llm_specific_recs.append(f"Grok: {len(external_links)} links externos detectados. Isso pode ajudar na verificação da informação.")

    # Verificar datas (simplificado)
    # Idealmente, procurar por meta tags de data de publicação ou dados estruturados.
    # Aqui, apenas uma sugestão genérica.
    llm_specific_recs.append("Grok: Indique claramente as datas de publicação e atualização do conteúdo para demonstrar atualidade.")
    llm_specific_recs.append("Grok: Se aplicável, cite fontes e autores para aumentar a credibilidade.")
    return llm_specific_recs

def analyze_for_perplexity(soup, base_recommendations):
    """Analisa o site sob a ótica do Perplexity AI."""
    llm_specific_recs = []
    # Perplexity AI foca em fornecer respostas diretas com citações.
    # Clareza, bom uso de headings e respostas concisas a possíveis perguntas.

    h1_tags = soup.find_all("h1")
    h2_tags = soup.find_all("h2")

    if not h1_tags:
        llm_specific_recs.append("Perplexity: Ausência de H1. Uma H1 clara ajuda o Perplexity a entender o tópico principal.")
    if len(h2_tags) < 2 and len(soup.find_all("p")) > 10:
        llm_specific_recs.append("Perplexity: Poucas H2s. Headings bem definidas ajudam a estruturar a informação para respostas diretas.")

    llm_specific_recs.append("Perplexity: Formule o conteúdo de forma que partes dele possam servir como respostas diretas a perguntas.")
    llm_specific_recs.append("Perplexity: Utilize listas e marcadores para facilitar a extração de informações chave.")
    return llm_specific_recs

st.set_page_config(layout="wide", page_title="Análise de Sites para LLMs")
# apply_custom_css() # Se você tiver um custom_css.py

st.title("🤖 Análise de Sites para Indexação por LLMs")
st.caption("Avalie seu site e receba recomendações para melhor rankeamento em buscadores de IA.")

url_input = st.text_input("Insira a URL do site que você deseja analisar:", placeholder="https://www.exemplo.com.br")

if st.button("Analisar Site", use_container_width=True, type="primary"):
    if not url_input or not (url_input.startswith("http://") or url_input.startswith("https://")):
        st.error("Por favor, insira uma URL válida (ex: https://www.exemplo.com.br).")
    else:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(url_input, headers=headers, timeout=15)
            response.raise_for_status() # Verifica se houve erro HTTP (4xx ou 5xx)
            soup = BeautifulSoup(response.content, "html.parser")

            st.markdown("---")
            st.header("📊 Resultados da Análise")

            # --- Análise Inicial ---
            with st.expander("1. Avaliação Inicial do Site", expanded=True):
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Estrutura do Conteúdo")
                    structure_report, structure_recs = evaluate_site_structure(soup)
                    st.json(structure_report)
                    for rec in structure_recs:
                        if "Crítico" in rec: st.error(rec)
                        elif "Alerta" in rec: st.warning(rec)
                        else: st.info(rec)

                    st.subheader("Meta Tags Principais")
                    meta_report, meta_recs = evaluate_meta_tags(soup)
                    st.json(meta_report)
                    for rec in meta_recs:
                        if "Crítico" in rec: st.error(rec)
                        elif "Alerta" in rec: st.warning(rec)
                        else: st.info(rec)

                with col2:
                    st.subheader("Velocidade Básica (Tempo de Resposta)")
                    speed_report, speed_recs = evaluate_speed_basic(url_input)
                    st.json(speed_report)
                    for rec in speed_recs:
                         if "Erro" in rec: st.error(rec)
                         elif "Alerta" in rec: st.warning(rec)
                         else: st.info(rec)

                    st.subheader("Dados Estruturados (Schema.org - JSON-LD)")
                    structured_data_report, structured_data_recs = evaluate_structured_data(soup)
                    st.json(structured_data_report)
                    base_recommendations_for_llms = {"structured_data": structured_data_recs} # Passar para LLMs
                    for rec in structured_data_recs:
                        if "Alerta" in rec: st.warning(rec)
                        else: st.info(rec)

                    # E-A-T (Placeholder para discussão)
                    st.subheader("E-A-T (Expertise, Authoritativeness, Trustworthiness)")
                    st.info("A avaliação E-A-T para LLMs envolve demonstrar conhecimento profundo, autoridade no assunto e confiabilidade. Isso pode ser alcançado através de conteúdo original e bem pesquisado, biografias de autores claras, links para fontes confiáveis e um design de site profissional.")
                    st.warning("Esta análise automatizada não pode avaliar completamente o E-A-T, que requer uma análise mais qualitativa.")

            # --- Análise Específica para Plataformas de IA ---
            with st.expander("2. Análise Específica para Plataformas de IA", expanded=False):
                st.info("As recomendações abaixo são baseadas em características conhecidas de cada LLM e como elas tendem a processar e valorizar informações da web.")

                # ChatGPT
                st.subheader("🤖 ChatGPT")
                chatgpt_recs = analyze_for_chatgpt(soup, base_recommendations_for_llms)
                for rec in chatgpt_recs:
                    st.markdown(f"- {rec}")

                # Gemini
                st.subheader("✨ Gemini (Google AI)")
                gemini_recs = analyze_for_gemini(soup, base_recommendations_for_llms, speed_report)
                for rec in gemini_recs:
                    st.markdown(f"- {rec}")

                # Grok
                st.subheader("⚡ Grok (X AI)")
                grok_recs = analyze_for_grok(soup, base_recommendations_for_llms)
                for rec in grok_recs:
                    st.markdown(f"- {rec}")

                # Perplexity
                st.subheader("❓ Perplexity AI")
                perplexity_recs = analyze_for_perplexity(soup, base_recommendations_for_llms)
                for rec in perplexity_recs:
                    st.markdown(f"- {rec}")

            # --- Plano de Ação Prático ---
            with st.expander("3. Plano de Ação Prático", expanded=False):
                st.subheader("Prioridades Sugeridas")

                all_recommendations = structure_recs + meta_recs + speed_recs + structured_data_recs + chatgpt_recs + gemini_recs + grok_recs + perplexity_recs

                urgentes = [rec for rec in all_recommendations if "Crítico:" in rec]
                importantes = [rec for rec in all_recommendations if "Alerta:" in rec]
                estrategicas = [rec for rec in all_recommendations if "Sugestão:" in rec or "Info:" in rec or ":" not in rec.split(" ")[0]] # Recomendações gerais de LLMs

                if urgentes:
                    st.error("**🔴 URGENTES (Resolver imediatamente):**")
                    for item in list(set(urgentes)): # Remover duplicatas
                        st.markdown(f"- {item.replace('Crítico: ', '')}")

                if importantes:
                    st.warning("**🟡 IMPORTANTES (Resolver em seguida):**")
                    for item in list(set(importantes)): # Remover duplicatas
                        st.markdown(f"- {item.replace('Alerta: ', '')}")

                if estrategicas:
                    st.info("**🔵 ESTRATÉGICAS (Melhoria contínua e otimização para LLMs):**")
                    # Filtrar recomendações específicas de LLMs que já não estejam em urgentes/importantes
                    estrategicas_llm = chatgpt_recs + gemini_recs + grok_recs + perplexity_recs
                    estrategicas_llm_filtered = [rec for rec in estrategicas_llm if not any(keyword in rec for keyword in ["Crítico:", "Alerta:"])]

                    # Adicionar outras sugestões e infos
                    outras_sugestoes = [rec for rec in (structure_recs + meta_recs + speed_recs + structured_data_recs) if "Sugestão:" in rec or "Info:" in rec]

                    for item in list(set(outras_sugestoes + estrategicas_llm_filtered)): # Remover duplicatas
                        st.markdown(f"- {item.replace('Sugestão: ', '').replace('Info: ', '')}")

                if not urgentes and not importantes and not estrategicas:
                    st.success("🎉 Parece que muitos aspectos básicos e específicos para LLMs estão bem encaminhados! Continue monitorando e refinando.")

                st.subheader("Como Medir o Sucesso?")
                st.markdown("""
                - **Monitoramento de Posição (Indireto):** Embora não haja "ranking" direto em LLMs como nos buscadores tradicionais, observe se o seu conteúdo é citado ou referenciado por elas em respostas a prompts relevantes.
                - **Qualidade das Citações:** Verifique se as informações do seu site são usadas de forma precisa e útil pelas IAs.
                - **Tráfego de Referência (se aplicável):** Algumas IAs podem incluir links para fontes. Monitore seu analytics para tráfego vindo de domínios associados a essas IAs.
                - **Feedback do Usuário:** Se usuários mencionarem ter encontrado seu site através de uma IA, isso é um bom indicador.
                - **Re-análise Periódica:** Use esta ferramenta periodicamente para verificar progressos e novas áreas de melhoria.
                """)
                st.markdown("Lembre-se que a otimização para LLMs é um campo novo e em evolução. Mantenha-se atualizado sobre as melhores práticas.")

        except requests.exceptions.HTTPError as http_err:
            st.error(f"Erro HTTP ao tentar acessar a URL: {http_err}. Verifique se a URL está correta e acessível.")
        except requests.exceptions.ConnectionError as conn_err:
            st.error(f"Erro de conexão: Não foi possível conectar à URL: {conn_err}. Verifique sua conexão e a URL.")
        except requests.exceptions.Timeout as timeout_err:
            st.error(f"Erro de Timeout: A requisição para a URL demorou muito para responder: {timeout_err}.")
        except requests.exceptions.RequestException as req_err:
            st.error(f"Ocorreu um erro ao tentar acessar a URL: {req_err}")
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado durante a análise: {e}")
            st.error("Verifique a URL e tente novamente. Se o problema persistir, pode ser um problema com o formato do site ou com a ferramenta.")

st.markdown("---")
st.caption("Esta ferramenta fornece uma análise automatizada e sugestões. A interpretação e implementação final são de sua responsabilidade.")
