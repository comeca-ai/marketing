import streamlit as st
from utils.custom_css import apply_custom_css
import time # Import time for simulating delay

st.set_page_config(layout="wide", page_title="Gerador de Artigos")
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
st.title("📄 Gerador de Artigos")
st.markdown("Descreva o tema ou as palavras-chave sobre as quais você deseja gerar um artigo completo.")

# Initialize session state
if 'generated_article' not in st.session_state:
    st.session_state.generated_article = ""
if 'article_prompt' not in st.session_state:
    st.session_state.article_prompt = ""

prompt = st.text_area("Digite seu prompt para o artigo:",
                      value=st.session_state.article_prompt,
                      height=150,
                      key="article_prompt_input", # Unique key
                      help="Forneça detalhes como tema, tom desejado, palavras-chave principais, etc.")

if st.button("Gerar Artigo", type="primary", use_container_width=True, key="btn_generate_article"): # Unique key
    if prompt:
        st.session_state.article_prompt = prompt
        with st.spinner("Gerando seu artigo... Por favor, aguarde."):
            time.sleep(2) # Simulate generation time
            # Placeholder for actual content generation
            st.session_state.generated_article = (
                f"### Artigo Gerado com Base no Seu Prompt:\n\n"
                f"**Prompt Fornecido:**\n```\n{prompt}\n```\n\n"
                f"---\n\n"
                f"**Conteúdo do Artigo (Exemplo):**\n\n"
                f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                f"Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                f"Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
                f"Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n\n"
                f"*Observação: Este é um conteúdo de exemplo. A integração com o modelo de IA real fornecerá o artigo completo.*"
            )
        st.success("Artigo gerado com sucesso!")
    else:
        st.error("Por favor, insira um prompt para gerar o artigo.")

if st.session_state.generated_article:
    st.subheader("Resultado:")
    with st.container(border=True):
        st.markdown(st.session_state.generated_article)
    
    if st.button("Limpar Resultado", key="btn_clear_article", use_container_width=True): # Unique key
        st.session_state.generated_article = ""
        st.session_state.article_prompt = "" # Optionally clear prompt too
        st.rerun()

st.markdown("---")
st.caption("Dica: Seja específico em seu prompt para obter os melhores resultados.")
