import streamlit as st
from PIL import Image
import Controllers.Quadro_cController as Quadro_cController
import models.Quadro_c as quadro_c
from datetime import datetime
import pandas as pd


def ListQC():
    if st.button("Carregar"):
        st.experimental_rerun()
    lista = Quadro_cController.Selecionar()

    if lista is not None:

        # Define o tamanho da página e o número de páginas
        page_size = 10
        num_pages = len(lista) // page_size + (1 if len(lista) % page_size > 0 else 0)

        # Obtém a página atual armazenada em st.session_state ou define como 0 se não existir
        page = st.session_state.get("page", 0)


        # Obtém os dados da página atual
        start = page * page_size
        end = start + page_size
        #data = lista[start:end]

        data = []
        campos = ['CPF', 'Data do atendimento', 'Idade', 'Sexo', 'Classificação', 'Probabilidade']
        for item in lista:
            cpf = item[2]
            data_str = item[3].strftime('%d/%m/%Y')
            idade = item[6]
            sexo = 'Masculino' if item[13] == 0 else 'Feminino'
            classificacao = 'Não' if item[28] == 0 else ('Sim' if item[28] == 1 else 'Indefinido')
            probabilidade = item[29]
            data.append([cpf, data_str, idade, sexo, classificacao, '{:.1%}'.format(probabilidade/100)])


        df = pd.DataFrame(data, columns=campos).iloc[start:end]
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
        st.table(df)

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






