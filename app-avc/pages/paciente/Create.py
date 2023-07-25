import this
from turtle import onclick
import streamlit as st;
import Controllers.PacienteController as PacienteController
import models.Paciente as paciente

with open("style.css") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)



def Create():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """<span style='font-size:24px; font-weight:bold; color:#666666; font-family:Roboto;'>Dados pessoais</span>""",
            unsafe_allow_html=True)
        nome = st.text_input(label="Nome completo", placeholder="Informe o nome completo")
        cpf = st.text_input(label="CPF", placeholder="Informe o CPF")
        telefone = st.text_input(label="Telefone", placeholder="Informe o telefone")
        profissao = st.text_input(label="Profissão", placeholder="Informe a profssião")

    with col2:
        st.markdown(
            """<span style='font-size:24px; font-weight:bold; color:#666666; font-family:Roboto;'>Informações de endereço</span>""",
            unsafe_allow_html=True)
        estado = st.text_input(label="Estado", placeholder="Informe o estado")
        cidade = st.text_input(label="Cidade", placeholder="Informe o cidade")
        bairro = st.text_input(label="Bairro", placeholder="Informe o bairro")
        rua = st.text_input(label="Rua", placeholder="Informe a rua")
        numero = st.text_input(label="Nº", placeholder="Informe o número da residência")

    submitted = st.button('Cadastrar')
    if submitted:
        if not (nome and cpf and telefone and profissao and estado and cidade and bairro and rua and numero):
            st.error("Todos os campos são obrigatórios, por favor preencha-os")
        else:
            # Verificar se o CPF já está cadastrado
            if PacienteController.verificar_cpf_existente(cpf):
                st.error("Este CPF já está cadastrado no sistema. Por favor, insira um CPF diferente.")
            else:
                paciente.codigo_adm = 1
                paciente.nome = nome
                paciente.cpf = cpf
                paciente.telefone = telefone
                paciente.profissao = profissao
                paciente.estado = estado
                paciente.cidade = cidade
                paciente.bairro = bairro
                paciente.rua = rua
                paciente.numero = numero
                PacienteController.Incluir(paciente)
                st.success("Paciente cadastrado com sucesso!")

