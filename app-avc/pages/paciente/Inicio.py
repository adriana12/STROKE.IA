import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import Controllers.Quadro_cController as Quadro_cController
import matplotlib.dates as mdates
import pandas as pd
import Controllers.PacienteController as PacienteController



def Inicio():
    proba = Quadro_cController.SelecionarProba()
    valores = []
    dict = {}
    for i in range(len(proba)):
        dict[proba[i][0]] = proba[i][1:]

    for chave, valor in dict.items():
        valores.append(chave)

    altos = 0
    medios = 0
    baixos = 0

    for valor in valores:
        if valor is not None:
            int_valor = int(valor)
            if int_valor >= 0 and int_valor <= 33:
                baixos += 1
            elif int_valor > 33 and int_valor <= 66:
                medios += 1
            else:
                altos += 1

    #print("Quantidade de valores altos:", altos)
    #print("Quantidade de valores médios:", medios)
    #print("Quantidade de valores baixos:", baixos)


    

    #probalidade = ['Baixo probabilidade (0% -33%)', 'Média probabilidade (34% - 66%)', 'Alta probabilidade (67% -100%)']
    probalidade = ['Baixa', 'Média', 'Alta']
    casos = [baixos, medios, altos]
    colors = ['green', 'yellow', 'red']
    plt.bar(probalidade, casos, color=colors)

    # Aqui definimos as legendas de cada barra no eixo X
    plt.xticks(probalidade)

    # A label para o eixo Y
    #plt.ylabel('Probabilidade')

    # A label para o eixo X
    #plt.xlabel('Casos de ocorrência de AVC (%)')

    # Chamamos o método show() para mostrar o gráfico na tela
    #plt.show()
    st.pyplot(plt)




def retornar_dados(cpf):
    dados = Quadro_cController.retornar_dados_paciente(cpf)

    # Cria um DataFrame a partir da lista de dados
    df = pd.DataFrame(dados, columns=['data_atendimento', 'classe', 'idade', 'probabilidade'])

    # Converte a coluna "data_atendimento" para o tipo datetime
    df['data_atendimento'] = pd.to_datetime(df['data_atendimento'])
    df['classe'] = df['classe'].replace({0: 'Não', 1: 'Sim', 2: 'Indeterminado'})

    # Retorna as informações do paciente como listas
    idades = df['idade'].tolist()
    classes = df['classe'].tolist()
    datas = df['data_atendimento'].tolist()
    probabilidades = df['probabilidade'].tolist()

    return datas, classes, idades, probabilidades





def gerargrafico(cpf):
    if cpf:
        datas, classes, idades, probabilidades = retornar_dados(cpf)

        print("idades:", idades)
        print("classes:", classes)
        print("datas:", datas)
        print("probabilidades:", probabilidades)

        # Define as faixas de probabilidade e as cores correspondentes
        cores = []
        for p in probabilidades:
            if p >= 0 and p <= 33:
                cores.append('green')
            elif p > 33 and p <= 66:
                cores.append('yellow')
            else:
                cores.append('red')

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(range(len(probabilidades)), probabilidades, color=cores)
        ax.set_xlabel('Atendimento')
        ax.set_ylabel('Probabilidade')
        ax.set_xticks(range(len(datas)))
        ax.set_xticklabels([d.strftime('%d/%m/%Y') for d in datas], rotation=45)

        # Adiciona o valor da probabilidade e a classe em cada barra
        for i, (p, c) in enumerate(zip(probabilidades, classes)):
            ax.text(i, p + 0.01, f'{round(p, 1)}% (P) - {c}(C)', ha='center')

        # Aqui você mostra o gráfico na página
        st.pyplot(fig)




def InicioPac():
    cpf = st.number_input(label='Informe o CPF', format='%d', step=1)
    if cpf:  # se o CPF foi preenchido pelo usuário
        paciente = PacienteController.SelecionarId(cpf)
        if paciente:
            gerargrafico(cpf)
        else:
            st.error('CPF não encontrado no banco de dados.')

