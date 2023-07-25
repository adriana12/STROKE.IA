import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pages.paciente.List as pageListpaciente
import pages.paciente.Create as pageCreatepaciente
import pages.modelo.Modelo as pageModelopaciente
import pages.paciente.Inicio as pageIniciopaciente
import pages.paciente.Edit as pageEditpaciente
import pages.modelo.ListQC as pageListQC


with st.sidebar:
    choose = option_menu("Stroke predict", ["Início", "Pacientes", "Quadro clínico"],
                         icons=['house-door', 'people', 'clipboard'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "#F0F2F6"},
                             "icon": {"color": "#131F34", "font-size": "25px"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                          "--hover-color": "#eee"},
                             "nav-link-selected": {"background-color": "#29A0BA"},
                         }
                         )
    #button_Login = st.button("Login")
    #button_Login = st.button("Cadastro")
if choose == "Início":
    st.header("Dashboard")
    col1, col2 = st.columns([4, 4])


    with col1:  # To display the header text using css style
        st.markdown(
            """<span style='font-size:24px; font-weight:bold; color:#666666; font-family:Roboto;'>Dados gerais</span>""",
            unsafe_allow_html=True)
        st.write("Probabilidade de ocorrência do AVC")
        pageIniciopaciente.Inicio()

    with col2:
        st.markdown(
            """<span style='font-size:24px; font-weight:bold; color:#666666; font-family:Roboto;'>Dados por paciente</span>""",
            unsafe_allow_html=True)
        st.write("Selecione um paciente")
        pageIniciopaciente.InicioPac()



elif choose == "Pacientes":
    tab1, tab2, tab3 = st.tabs(["Visualizar paciente", "Cadastrar paciente", "Buscar paciente"])
    with tab1:
        pageListpaciente.List()

    with tab2:
        st.markdown(""" <style> .font {
            font-size:24px ; font-family: 'Roboto'; color: #131F34; font-weight: bolder;} 
            </style> """, unsafe_allow_html=True)
        pageCreatepaciente.Create()
    with tab3:
        pageEditpaciente.alterar()

elif choose == "Quadro clínico":
    tab1, tab2 = st.tabs(["Visualizar Quadros clínicos", "Cadastrar Quadros clínicos"])
    with tab1:
        pageListQC.ListQC()
    with tab2:
        pageModelopaciente.Modelo()

