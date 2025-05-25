import streamlit as st
from utils.custom_css import apply_custom_css
import time # Import time for simulating delay

st.set_page_config(layout="wide", page_title="Posts para Redes Sociais")
apply_custom_css()

# --- Page Content ---
st.title("📱 Criador de Posts para Redes Sociais")
st.page_link("app.py", label="⬅️ Voltar ao Dashboard", icon="🏠")
st.markdown("---") # Optional divider
st.markdown("Especifique a plataforma, o tema e o tom para gerar posts criativos e engajadores.")

# Initialize session state
if 'generated_post' not in st.session_state:
    st.session_state.generated_post = ""
if 'post_prompt' not in st.session_state:
    st.session_state.post_prompt = ""

prompt = st.text_area("Digite seu prompt para o post:",
                      value=st.session_state.post_prompt,
                      height=150,
                      key="post_prompt_input", # Unique key
                      help="Plataforma: Instagram. Tema: Lançamento de novo ebook sobre marketing digital.")

if st.button("Gerar Post", type="primary", use_container_width=True, key="btn_generate_post"): # Unique key
    if prompt:
        st.session_state.post_prompt = prompt
        with st.spinner("Gerando post... Por favor, aguarde."):
            time.sleep(2) # Simulate generation time
            st.session_state.generated_post = (
                f"### Post Gerado com Base no Seu Prompt:\n\n"
                f"**Prompt Fornecido:**\n```\n{prompt}\n```\n\n"
                f"---\n\n"
                f"**Exemplo de Post para Redes Sociais:**\n\n"
                f"🚀 **Prepare-se para a novidade!** 🚀\n\n"
                f"Estamos super animados em anunciar o lançamento do nosso mais novo produto/serviço, pensado especialmente para você que busca {prompt.lower().split(' ')[-1] if prompt else 'soluções inovadoras'}!\n\n"
                f"✨ Descubra como podemos te ajudar a {prompt.lower().split(' ')[0] if prompt else 'alcançar seus objetivos'}.\n\n"
                f"👉 Saiba mais no link da bio! #Lançamento #Novidade #{prompt.lower().split(' ')[1] if len(prompt.split()) > 1 else 'MarketingDigital'}\n\n"
                f"*Observação: Este é um post de exemplo. A IA real criará conteúdo adaptado à plataforma e ao seu prompt específico.*"
            )
        st.success("Post gerado com sucesso!")
    else:
        st.error("Por favor, insira um prompt para gerar o post.")

if st.session_state.generated_post:
    st.subheader("Resultado:")
    with st.container(border=True):
        st.markdown(st.session_state.generated_post)
    
    if st.button("Limpar Resultado", key="btn_clear_post", use_container_width=True): # Unique key
        st.session_state.generated_post = ""
        st.session_state.post_prompt = ""
        st.rerun()

st.markdown("---")
st.caption("Dica: Inclua a plataforma desejada (Instagram, Facebook, Twitter/X, LinkedIn) no seu prompt.")
