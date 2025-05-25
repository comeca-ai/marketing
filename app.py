import streamlit as st
from utils.custom_css import apply_custom_css # Import the function

# Page Configuration
st.set_page_config(layout="wide", page_title="AI Content Tools", initial_sidebar_state="expanded")
apply_custom_css() # Apply CSS

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("📝 AI Content Suite") # Icon already here
    st.page_link("app.py", label="Dashboard", icon="🏠")
    st.header("Ferramentas") # This is a header, not a page link, no direct icon parameter
    st.page_link("pages/01_Artigos.py", label="Gerador de Artigos", icon="📄")
    st.page_link("pages/02_Headlines.py", label="Gerador de Headlines", icon="💡")
    st.page_link("pages/03_Posts_Redes_Sociais.py", label="Posts para Redes Sociais", icon="📱")
    st.page_link("pages/04_Resumos.py", label="Resumidor de Conteúdos", icon="✂️")
    st.divider()
    st.page_link("pages/05_Meus_Conteudos.py", label="Meus Conteúdos", icon="📚")

# --- Main Page Content (Dashboard) ---

# Personalized Greeting (Placeholder)
# TODO: Replace with actual user name if login is implemented
st.title("🚀 Bem-vindo(a) de volta!") # Icon already here
st.markdown("Seu assistente de criação de conteúdo com Inteligência Artificial está pronto para ajudar.")
st.markdown("---")

st.header("✨ Ferramentas Mais Populares") # Icon already here
st.markdown("Acesse rapidamente nossas ferramentas mais usadas e comece a criar.")

# Tool cards
# Using columns for layout
cols = st.columns(4) 

# Card 1: Gerador de Artigos
with cols[0]:
    with st.container(border=True):
        st.subheader("📄 Gerador de Artigos") # Icon already here
        st.caption("Crie artigos completos e otimizados sobre qualquer tema em segundos.")
        if st.button("Acessar Gerador de Artigos", key="btn_artigos", use_container_width=True):
            st.switch_page("pages/01_Artigos.py") # Navigate to the page

# Card 2: Gerador de Headlines
with cols[1]:
    with st.container(border=True):
        st.subheader("💡 Gerador de Headlines") # Icon already here
        st.caption("Gere headlines persuasivas e criativas para seus textos e anúncios.")
        if st.button("Acessar Gerador de Headlines", key="btn_headlines", use_container_width=True):
            st.switch_page("pages/02_Headlines.py")

# Card 3: Criador de Posts para Redes Sociais
with cols[2]:
    with st.container(border=True):
        st.subheader("📱 Posts para Redes Sociais") # Icon already here
        st.caption("Crie posts engajadores para diversas plataformas de mídia social.")
        if st.button("Acessar Criador de Posts", key="btn_posts", use_container_width=True):
            st.switch_page("pages/03_Posts_Redes_Sociais.py")

# Card 4: Resumidor de Conteúdos
with cols[3]:
    with st.container(border=True):
        st.subheader("✂️ Resumidor de Conteúdos") # Icon already here
        st.caption("Resuma textos longos, artigos ou documentos de forma rápida e precisa.")
        if st.button("Acessar Resumidor", key="btn_resumos", use_container_width=True):
            st.switch_page("pages/04_Resumos.py")

st.markdown("---")
st.markdown("Explore todas as ferramentas no menu à esquerda e potencialize sua produtividade!")
