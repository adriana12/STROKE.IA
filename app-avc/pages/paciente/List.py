from unittest import main
import streamlit as st
import Controllers.PacienteController as PacienteController
from PIL import Image
import models.Paciente as paciente
import pages.paciente.Create as pageCreatepaciente
import pages.paciente.Edit as pageEditpaciente
import pandas as pd


def List():
    if st.button("Carregar"):
        st.experimental_rerun()
    lista = PacienteController.Selecionar()
    if lista is not None:
        # Define o tamanho da página e o número de páginas
        page_size = 10
        num_pages = len(lista) // page_size + (1 if len(lista) % page_size > 0 else 0)

        # Obtém a página atual armazenada em st.session_state ou define como 0 se não existir
        page = st.session_state.get("page", 0)

        # Obtém os dados da página atual
        start = page * page_size
        end = start + page_size
        data = lista[start:end]


        # Cria a tabela com os dados da página atual
        colunas = ['Nome', 'CPF', 'Telefone', 'Profissão', 'Estado', 'Cidade']
        data = [[item[2], item[4], item[5], item[3], item[6], item[7]] for item in data]


        # Define o CSS que será injetado na página
        hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

        # Injeta o CSS na página usando a função markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        # Mostra a tabela sem a primeira coluna de índice
        st.table(pd.DataFrame(data, columns=colunas))


        # Cria botões de navegação
        st.write(f"Página {page + 1}/{num_pages}")
        if page > 0:
            if st.button("Anterior"):
                st.session_state["page"] = page - 1
        if page < num_pages - 1:
            if st.button("Próxima"):
                st.session_state["page"] = page + 1

    else:
        image = Image.open("imagens/emply.png")
        st.image(image, width=400)
        st.write("No momento não existe nenhum paciente cadastrado!")


