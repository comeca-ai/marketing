import streamlit as st
from utils.custom_css import apply_custom_css
import time # Import time for simulating delay

st.set_page_config(layout="wide", page_title="Gerador de Headlines")
apply_custom_css()

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("📝 AI Content Suite")
    st.page_link("app.py", label="Dashboard", icon="🏠")
    st.header("Ferramentas")
    st.page_link("pages/01_Artigos.py", label="Gerador de Artigos", icon="📄")
    st.page_link("pages/02_Headlines.py", label="Gerador de Headlines", icon="💡")
    st.page_link("pages/03_Posts_Redes_Sociais.py", label="Posts para Redes Sociais", icon="📱")
    st.page_link("pages/04_Resumos.py", label="Resumidor de Conteúdos", icon="✂️")
    st.divider()
    st.page_link("pages/05_Meus_Conteudos.py", label="Meus Conteúdos", icon="📚")

# --- Page Content ---
st.title("💡 Gerador de Headlines")
st.markdown("Forneça informações sobre seu produto, serviço ou tema para gerar headlines chamativas e eficazes.")

# Initialize session state
if 'generated_headlines' not in st.session_state:
    st.session_state.generated_headlines = ""
if 'headline_prompt' not in st.session_state:
    st.session_state.headline_prompt = ""

prompt = st.text_area("Digite seu prompt para as headlines:",
                      value=st.session_state.headline_prompt,
                      height=150,
                      key="headline_prompt_input", # Unique key
                      help="Exemplo: Produto: Novo Software de IA. Benefício: Aumenta a produtividade.")

if st.button("Gerar Headlines", type="primary", use_container_width=True, key="btn_generate_headline"): # Unique key
    if prompt:
        st.session_state.headline_prompt = prompt
        with st.spinner("Gerando headlines... Por favor, aguarde."):
            time.sleep(2) # Simulate generation time
            st.session_state.generated_headlines = (
                f"### Headlines Geradas com Base no Seu Prompt:\n\n"
                f"**Prompt Fornecido:**\n```\n{prompt}\n```\n\n"
                f"---\n\n"
                f"**Exemplos de Headlines:**\n\n"
                f"1.  **Headline Criativa 1:** Descubra como {prompt.lower().split(' ')[-1] if prompt else 'transformar seu dia'}!\n"
                f"2.  **Headline Direta 2:** A Solução Definitiva para {prompt.lower().split(' ')[0] if prompt else 'seus problemas'}.\n"
                f"3.  **Headline com Benefício 3:** Alcance {prompt.lower().split(' ')[1] if len(prompt.split()) > 1 else 'resultados incríveis'} com esta novidade.\n\n"
                f"*Observação: Estas são headlines de exemplo. A IA real criará opções mais diversificadas e personalizadas.*"
            )
        st.success("Headlines geradas com sucesso!")
    else:
        st.error("Por favor, insira um prompt para gerar as headlines.")

if st.session_state.generated_headlines:
    st.subheader("Resultado:")
    with st.container(border=True):
        st.markdown(st.session_state.generated_headlines)
    
    if st.button("Limpar Resultado", key="btn_clear_headline", use_container_width=True): # Unique key
        st.session_state.generated_headlines = ""
        st.session_state.headline_prompt = ""
        st.rerun()

st.markdown("---")
st.caption("Dica: Teste diferentes ângulos e benefícios em seu prompt.")
