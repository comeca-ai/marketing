import streamlit as st
import datetime
import pandas as pd # Using pandas for a slightly better table display
from utils.custom_css import apply_custom_css

st.set_page_config(layout="wide", page_title="Meus Conteúdos")
apply_custom_css()

st.title("📚 Meus Conteúdos Gerados") # Icon already here
st.page_link("app.py", label="⬅️ Voltar ao Dashboard", icon="🏠")
st.markdown("---") # Optional divider
st.markdown("Aqui você pode visualizar, gerenciar e exportar os conteúdos que você criou.")

# --- Mock Data and Session State Management ---
# Initialize mock content in session state if it doesn't exist
if 'meus_conteudos' not in st.session_state:
    st.session_state.meus_conteudos = [
        {"id": 1, "tipo": "Artigo", "titulo": "Inteligência Artificial no Marketing", "conteudo": "Conteúdo completo do artigo sobre IA no Marketing...", "data_criacao": datetime.date(2023, 10, 1)},
        {"id": 2, "tipo": "Headline", "titulo": " manchete Impactante para Vendas", "conteudo": "Esta é A Manchete Que Você Precisava!", "data_criacao": datetime.date(2023, 10, 2)},
        {"id": 3, "tipo": "Post Rede Social", "titulo": "Post sobre novo produto X", "conteudo": "Confira o lançamento do nosso novo produto X! #inovacao", "data_criacao": datetime.date(2023, 10, 3)},
    ]

if not st.session_state.meus_conteudos:
    st.info("Você ainda não tem nenhum conteúdo salvo. Gere conteúdo nas ferramentas para vê-los aqui.")
else:
    # Display content in a more structured way
    for index, item in enumerate(st.session_state.meus_conteudos):
        st.subheader(f"{item['tipo']}: {item['titulo']}")
        st.caption(f"Criado em: {item['data_criacao'].strftime('%d/%m/%Y')}")

        with st.expander("Visualizar/Copiar Conteúdo"):
            st.markdown(item['conteudo'])
            # It's tricky to have a button copy to clipboard directly without external libraries in pure Streamlit
            # Usually, you'd show the text in a text area for easy manual copy.
            st.text_area("Copie o conteúdo abaixo:", item['conteudo'], height=150, key=f"copy_area_{item['id']}")

        # Action buttons in columns
        col1, col2, col3 = st.columns([1,1,1]) # Adjusted to 3 columns as per final code in prompt

        with col1:
            if st.button("Excluir", key=f"delete_{item['id']}", type="secondary", use_container_width=True):
                # Confirm deletion
                # For simplicity in this step, direct delete. A confirmation modal would be better.
                st.session_state.meus_conteudos.pop(index)
                st.success(f"'{item['titulo']}' excluído com sucesso!")
                st.rerun()
        
        with col2:
            # Placeholder for TXT download
            # Actual implementation requires generating a file and using st.download_button
            st.download_button(
                label="Baixar TXT",
                data=item['conteudo'], # Direct string data
                file_name=f"{item['titulo'].replace(' ', '_').lower()}.txt",
                mime="text/plain",
                key=f"txt_{item['id']}",
                use_container_width=True
            )

        with col3:
            # Placeholder for PDF download
            # Actual implementation requires a PDF generation library (e.g., fpdf2)
            if st.button("Baixar PDF", key=f"pdf_{item['id']}", disabled=True, use_container_width=True):
                st.info("Funcionalidade de download em PDF ainda não implementada.")
        
        st.markdown("---")

# Note: A proper "Save content" mechanism should be added to the tool pages
# to populate st.session_state.meus_conteudos. For now, it's pre-filled.
