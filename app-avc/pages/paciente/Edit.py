# carregando as bibliotecas
import streamlit as st
import Controllers.PacienteController as PacienteController
import models.Paciente as paciente

def exibir_formulario_paciente(paciente):
    """
    Exibe o formulário para edição dos dados do paciente.
    """
    #with st.form(key="edite_paciente"):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """<span style='font-size:24px; font-weight:bold; color:#666666; font-family:Roboto;'>Dados pessoais</span>""",
            unsafe_allow_html=True)
        update_nome = st.text_input(label="Nome completo", placeholder="Informe o nome completo", value=paciente[2])
        # update_cpf = st.text_input(label="CPF", placeholder="Informe o CPF", value=paciente[4])
        update_telefone = st.text_input(label="Telefone", placeholder="Informe o telefone", value=paciente[5])
        update_profissao = st.text_input(label="Profissão", placeholder="Informe a profssião", value=paciente[3])

    with col2:
        st.markdown(
            """<span style='font-size:24px; font-weight:bold; color:#666666; font-family:Roboto;'>Informações de endereço</span>""",
            unsafe_allow_html=True)
        update_estado = st.text_input(label="Estado", placeholder="Informe o estado", value=paciente[6])
        update_cidade = st.text_input(label="Cidade", placeholder="Informe o cidade", value=paciente[7])
        update_bairro = st.text_input(label="Bairro", placeholder="Informe o bairro", value=paciente[9])
        update_rua = st.text_input(label="Rua", placeholder="Informe a rua", value=paciente[8])
        update_numero = st.text_input(label="Nº", placeholder="Informe o número da residência", value=paciente[10])

    button_update = st.button('Alterar')

    if button_update:
        PacienteController.Alterar(update_nome, update_telefone, update_profissao,
                                   update_estado, update_cidade, update_bairro, update_rua,
                                   update_numero,
                                   paciente[0])
        st.success('Paciente alterado com sucesso!!!')

def alterar():
    cpf = st.number_input(label='Informe o CPF', format='%d', step=1)

    if cpf:  # se o CPF foi preenchido pelo usuário
        paciente = PacienteController.SelecionarId(cpf)
        if paciente:
            exibir_formulario_paciente(paciente[0])
        else:
            st.error('CPF não encontrado no banco de dados.')

