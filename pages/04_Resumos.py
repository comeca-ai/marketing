import streamlit as st
from utils.custom_css import apply_custom_css
import time # Import time for simulating delay

st.set_page_config(layout="wide", page_title="Resumidor de Conteúdos")
apply_custom_css()

# --- Page Content ---
st.title("✂️ Resumidor de Conteúdos")
st.page_link("app.py", label="⬅️ Voltar ao Dashboard", icon="🏠")
st.markdown("---") # Optional divider
st.markdown("Cole o texto que você deseja resumir ou forneça um link para um artigo online.")

# Initialize session state
if 'generated_summary' not in st.session_state:
    st.session_state.generated_summary = ""
if 'summary_prompt' not in st.session_state:
    st.session_state.summary_prompt = ""

prompt = st.text_area("Cole aqui o texto que você deseja resumir:",
                      value=st.session_state.summary_prompt,
                      height=200,
                      key="summary_prompt_input", # Unique key
                      help="Você pode colar um texto longo ou até mesmo um link para um artigo (a funcionalidade de link será implementada).")

if st.button("Gerar Resumo", type="primary", use_container_width=True, key="btn_generate_summary"): # Unique key
    if prompt:
        st.session_state.summary_prompt = prompt
        with st.spinner("Gerando resumo... Por favor, aguarde."):
            time.sleep(2) # Simulate generation time
            st.session_state.generated_summary = (
                f"### Resumo Gerado com Base no Texto Fornecido:\n\n"
                f"**Início do Texto Original:**\n```\n{prompt[:200]}...\n```\n\n"  # Show a snippet
                f"---\n\n"
                f"**Resumo do Conteúdo (Exemplo):**\n\n"
                f"Este é o ponto principal do texto. O autor argumenta que A, B e C são fatores cruciais. "
                f"Adicionalmente, destaca-se a importância de X para o resultado Y. "
                f"Em conclusão, o texto sugere que futuras pesquisas deveriam focar em Z.\n\n"
                f"*Observação: Este é um resumo de exemplo. A IA real analisará o texto completo para fornecer um resumo preciso e conciso.*"
            )
        st.success("Resumo gerado com sucesso!")
    else:
        st.error("Por favor, insira um texto para gerar o resumo.")

if st.session_state.generated_summary:
    st.subheader("Resultado:")
    with st.container(border=True):
        st.markdown(st.session_state.generated_summary)
    
    if st.button("Limpar Resultado", key="btn_clear_summary", use_container_width=True): # Unique key
        st.session_state.generated_summary = ""
        st.session_state.summary_prompt = ""
        st.rerun()

st.markdown("---")
st.caption("Dica: Para melhores resultados, forneça textos com boa estrutura e clareza.")
