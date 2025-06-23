import streamlit as st
from utils.custom_css import apply_custom_css

st.set_page_config(layout="wide", page_title="AI Content Tools") # Removed initial_sidebar_state
apply_custom_css()

# --- Main Page Content (Dashboard) ---
st.title("🚀 Bem-vindo(a) de volta!")
st.markdown("Seu assistente de criação de conteúdo com Inteligência Artificial está pronto para ajudar.")
st.markdown("---")

st.header("✨ Ferramentas Principais e Conteúdos") # Updated header
st.markdown("Acesse rapidamente nossas ferramentas e seus conteúdos salvos.")

# --- Cards Layout ---
# Row 1: Three tools
cols_row1 = st.columns(3)

with cols_row1[0]:
    with st.container(border=True):
        st.subheader("📄 Gerador de Artigos")
        st.caption("Crie artigos completos e otimizados sobre qualquer tema em segundos.")
        if st.button("Acessar Gerador de Artigos", key="btn_artigos", use_container_width=True):
            st.switch_page("pages/01_Artigos.py")

with cols_row1[1]:
    with st.container(border=True):
        st.subheader("💡 Gerador de Headlines")
        st.caption("Gere headlines persuasivas e criativas para seus textos e anúncios.")
        if st.button("Acessar Gerador de Headlines", key="btn_headlines", use_container_width=True):
            st.switch_page("pages/02_Headlines.py")

with cols_row1[2]:
    with st.container(border=True):
        st.subheader("📱 Posts para Redes Sociais")
        st.caption("Crie posts engajadores para diversas plataformas de mídia social.")
        if st.button("Acessar Criador de Posts", key="btn_posts", use_container_width=True):
            st.switch_page("pages/03_Posts_Redes_Sociais.py")

# Row 2: One tool and Meus Conteudos
cols_row2 = st.columns(2) # Or st.columnsSpec to make them more centered if desired

with cols_row2[0]:
    with st.container(border=True):
        st.subheader("✂️ Resumidor de Conteúdos")
        st.caption("Resuma textos longos, artigos ou documentos de forma rápida e precisa.")
        if st.button("Acessar Resumidor", key="btn_resumos", use_container_width=True):
            st.switch_page("pages/04_Resumos.py")

with cols_row2[1]:
    with st.container(border=True):
        st.subheader("📚 Meus Conteúdos") # New Card
        st.caption("Acesse e gerencie todos os seus conteúdos criados anteriormente.")
        if st.button("Acessar Meus Conteúdos", key="btn_meus_conteudos", use_container_width=True):
            st.switch_page("pages/05_Meus_Conteudos.py") # Ensure this path is correct

# Row 3: New Tool - Site Analysis
cols_row3 = st.columns(3) # Match the layout of row 1 for consistency, even with one item

with cols_row3[0]: # Place it in the first column, it will appear centered if it's the only one in a 'columns(3)'
    with st.container(border=True):
        st.subheader("🤖 Análise de Sites para LLMs")
        st.caption("Avalie seu site para otimização em buscadores de Inteligência Artificial.")
        if st.button("Analisar Site", key="btn_analise_ia", use_container_width=True):
            st.switch_page("pages/06_Analise_IA_Sites.py")


st.markdown("---")
st.markdown("Escolha uma opção acima para começar.") # Updated footer text
