import streamlit as st

def apply_custom_css():
    custom_css = """
    <style>
        /* General body style - for font and text color if not overridden by theme */
        body {
            font-family: 'sans serif'; /* Ensure consistency */
            color: #1F2937; /* Tailwind Cool Gray 800 */
        }

        /* --- Card Styling (imitating Tailwind shadow and rounded corners) --- */
        div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div.stContainer[border='true'],
        div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div.stContainer[border='true'] { /* For cards on dashboard and tool output */
            border-radius: 0.5rem; /* Tailwind rounded-lg */
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); /* Tailwind shadow-md */
            border: 1px solid #E5E7EB; /* Tailwind Cool Gray 200 border */
            background-color: #FFFFFF; /* White background for cards */
        }
        
        /* --- Button Styling (primary buttons) --- */
        div[data-testid="stButton"] > button[kind="primary"] {
            background-color: #6366F1; /* Tailwind Indigo 500 */
            color: white;
            border-radius: 0.375rem; /* Tailwind rounded-md */
            border: none;
            padding: 0.5rem 1rem;
        }
        div[data-testid="stButton"] > button[kind="primary"]:hover {
            background-color: #4F46E5; /* Tailwind Indigo 600 */
            color: white;
        }
        div[data-testid="stButton"] > button[kind="primary"]:focus {
            box-shadow: 0 0 0 3px #A5B4FC; /* Tailwind Indigo 300 focus ring */
        }

        /* --- Button Styling (secondary buttons) --- */
        div[data-testid="stButton"] > button[kind="secondary"] {
            background-color: #E5E7EB; /* Tailwind Cool Gray 200 */
            color: #374151; /* Tailwind Cool Gray 700 */
            border-radius: 0.375rem; /* Tailwind rounded-md */
            border: 1px solid #D1D5DB; /* Tailwind Cool Gray 300 */
            padding: 0.5rem 1rem;
        }
        div[data-testid="stButton"] > button[kind="secondary"]:hover {
            background-color: #D1D5DB; /* Tailwind Cool Gray 300 */
        }
        
        /* --- Styling for st.text_area --- */
        div[data-testid="stTextArea"] textarea {
            border-radius: 0.375rem; /* Tailwind rounded-md */
            border: 1px solid #D1D5DB; /* Tailwind Cool Gray 300 */
        }
        
        /* --- Improve sidebar visuals slightly --- */
        div[data-testid="stSidebarUserContent"] { /* Targets the content area of the sidebar */
             padding-top: 1rem; /* Add some padding at the top */
        }
        div[data-testid="stSidebarUserContent"] .stButton > button { 
            /* Make sidebar buttons less prominent or match theme */
        }

        /* --- Header styling in sidebar --- */
        div[data-testid="stSidebarUserContent"] h1 { /* App Title in Sidebar */
            font-size: 1.5em; /* Slightly larger */
            color: #4F46E5; /* Indigo 600 */
        }
         div[data-testid="stSidebarUserContent"] h3 { /* Section headers like "Ferramentas" */
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #6B7280; /* Gray 500 */
        }

        /* Hide Streamlit's default sidebar */
        div[data-testid="stSidebar"] {
            display: none;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
