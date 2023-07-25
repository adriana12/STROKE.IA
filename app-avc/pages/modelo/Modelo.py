import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import Controllers.PacienteController as PacienteController
import Controllers.Quadro_cController as Quadro_cController
import models.Quadro_c as quadro_c
import Controllers.BaseController as BaseController
import models.Base as base
import datetime
from streamlit_modal import Modal




baseDados = BaseController.RecuperaBase()
df = pd.DataFrame(baseDados)
#st.write(df.shape)

def criarModelo(avc):
    X = df.iloc[:, 0:20].values  # Atributos/Features
    print(X.shape)
    y = df.iloc[:, 20].values  # Classes/Labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    rf = RandomForestClassifier(criterion='entropy', max_depth=None, max_features='sqrt',
                       min_samples_leaf=10, min_samples_split=2, n_estimators=200, n_jobs=-1,
                       random_state=42)
    rf.fit(X_train, y_train)
    prediction_proba = rf.predict_proba(avc)
    prediction = rf.predict(avc)
    return prediction_proba, prediction


def Modelo():
    opcoes = PacienteController.Selecionarcpf()
    dict = {}
    for i in range(len(opcoes)):
        dict[opcoes[i][0]] = opcoes[i][1:]

    user_input = st.selectbox("Selecione o nome e CPF do paciente", options=opcoes, format_func=lambda option: f"{option[0]} - {option[1]}")

    col1, col2 = st.columns(2)

    radio1_options = ['Sim', 'Não']
    radio1_values = {'Sim': 1, 'Não': 0}

    radio2_options = ['Sim', 'Não', 'Não informado']
    radio2_values = {'Sim': 1, 'Não': 0, 'Não informado': 2}

    sexo_options = ['Feminino', 'Masculino']
    sexo_values = {'Feminino': 0, 'Masculino': 1}

    status_fumante_options = ['Nunca fumou', 'Ex-fumante', 'Fuma atualmente']
    status_fumante_values = {'Nunca fumou': 1, 'Ex-fumante': 2, 'Fuma atualmente': 3}

    status_diabete_options = ['Normal', 'Diminuição da tolerância a glicose', 'Diabetes']
    status_diabete_values = {'Normal': 1, 'Diminuição da tolerância a glicose': 2, 'Diabetes': 3}

    rd_options = ['Sim', 'Não', 'Indeterminado']
    rd_values = {'Sim': 1, 'Não': 0, 'Indeterminado': 2}

    # --------------------------------------------------

    with col1:
        st.markdown(
            """<span style='font-size:24px; font-weight:bold; color:#666666; font-family:Roboto;'>Fatores de risco</span>""",
            unsafe_allow_html=True)
        # Dados gerias
        #codigo_adm = st.text_input("Informe o códgio do adm")
        cpf = st.text_input("CPF (campo obrigatório)", placeholder="Digite o CPF apresentado acima")
        dataAT = st.date_input("Data do atendimento", datetime.date(2023, 1, 25))

        # Fatores de risco
        idade = st.number_input("Idade", format='%d', step=1)
        peso = st.number_input("Peso (em kg)")
        altura = st.number_input("Altura (em m)")
        glicose = st.number_input("Nível de glicose")
        # Base
        SUPSYS16 = st.number_input("Pressão sistólica", format='%d', step=1)
        SUPDIA16 = st.number_input("Pressão diastólica", format='%d', step=1)

        diabetes_value = st.radio(
            "Diabetes?", options=status_diabete_options)
        DIABETES = status_diabete_values.get(diabetes_value)

        # BMI = peso / (altura * altura)
        # st.write(BMI)

        historico_avc_value = st.radio(
            "Tem histórico de AVC na família?", options=radio1_options)
        FHSTK = radio1_values.get(historico_avc_value)

        BEAT14 = st.number_input("Frequência cardíaca")

        doenca_pulmao_value = st.radio(
            "Tem alguma doença no pulmão?", options=radio1_options)
        HEAR01 = radio1_values.get(doenca_pulmao_value)

        transtorno_nervoso_value = st.radio(
            "Tem algum transtorno nervoso?", options=radio1_options)
        NERV01 = radio1_values.get(transtorno_nervoso_value)

        cancer_value = st.radio(
            "Tem câncer?", options=radio1_options)
        DIAG01 = radio1_values.get(cancer_value)

        doenca_cardiaca_value = st.radio(
            "Tem alguma doença cardíaca?", options=radio1_options)
        HEART01 = radio1_values.get(doenca_cardiaca_value)

        sexo_value = st.radio(
            "Informe o sexo do paciente", options=sexo_options)
        GEND01 = sexo_values.get(sexo_value)

        status_fumante_value = st.radio(
            "É fumante?", options=status_fumante_options)
        SMOKE = status_fumante_values.get(status_fumante_value)

    with col2:
        st.markdown(
            """<span style='font-size:24px; font-weight:bold; color:#666666; font-family:Roboto;'>Sinais indicativos</span>""",
            unsafe_allow_html=True)
        tontura_value = st.radio(
            "Teve tontura?", options=radio1_options)
        DIZZYP07 = radio1_values.get(tontura_value)

        fadiga_value = st.radio(
            "Teve fadiga?", options=radio1_options)
        FATIGP07 = radio1_values.get(fadiga_value)

        visao_value = st.radio(
            "Consegue ver bem o suficiente?", options=radio1_options)
        RECOGN08 = radio1_values.get(visao_value)

        dor_no_peito_value = st.radio(
            "Teve dor ou desconforto no peito?", options=radio1_options)
        CHSTPN07 = radio1_values.get(dor_no_peito_value)

        dor_nas_pernas_value = st.radio(
            "Teve dor nas pernas ao andar?", options=radio1_options)
        LEGWLK07 = radio1_values.get(dor_nas_pernas_value)

        palpitacoes_value = st.radio(
            "Teve palpitações?", options=radio1_options)
        PALPIP07 = radio1_values.get(palpitacoes_value)

        escutar_value = st.radio(
            "Escuta bem para conversar?", options=radio1_options)
        CONVER08 = radio1_values.get(escutar_value)

        levantar_value = st.radio(
            "Tem dificuldades para levantar?", options=radio2_options)
        LIFTNG09 = radio2_values.get(levantar_value)

        st.markdown(
            """<span style='font-size:24px; font-weight:bold; color:#666666; font-family:Roboto;'>Probabilidade de AVC</span>""",
            unsafe_allow_html=True)
        prev = st.radio("Tem probabilidade AVC?", options=rd_options)
        previsao = rd_values.get(prev)
        pred = st.number_input("Informe a probabilidade (sim, não ou indeterminado)")

    def defineEntrada():
        if altura != 0:
            BMI = peso / (altura * altura)
        else:
            BMI = 0
        user_data = {'SUPSYS16': SUPSYS16, 'SUPDIA16': SUPDIA16,
                     'DIABETES': DIABETES, 'BMI': BMI, 'FHSTK': FHSTK,
                     'BEAT14': BEAT14, 'HEAR01': HEAR01, 'NERV01': NERV01,
                     'DIAG01': DIAG01, 'HEART01': HEART01,
                     'GEND01': GEND01, 'SMOKE': SMOKE, 'DIZZYP07': DIZZYP07,
                     'FATIGP07': FATIGP07, 'RECOGN08': RECOGN08,
                     'CHSTPN07': CHSTPN07, 'LEGWLK07': LEGWLK07, 'PALPIP07': PALPIP07,
                     'CONVER08': CONVER08, 'LIFTNG09': LIFTNG09}

        features = pd.DataFrame(user_data, index=[0])
        user_input_variables = features
        return user_input_variables

    def obterResultado(entrada):
        prediction, pred = criarModelo(entrada)
        if pred == 0:
            probaAvc0 = round(prediction[0][0] * 100, 3)
            return pred, probaAvc0
        elif pred == 1:
            probaAvc1 = round(prediction[0][1] * 100, 3)
            return pred, probaAvc1
        else:
            probaAvc2 = round(prediction[0][2] * 100, 3)
            return pred, probaAvc2

    def atualizarBase(predict):
        base.SUPSYS16 = SUPSYS16
        base.SUPDIA16 = SUPDIA16
        base.DIABETES = DIABETES
        if altura != 0:
            base.BMI = (peso / (altura * altura))
        else:
            base.BMI = 0
        base.FHSTK = FHSTK
        base.BEAT14 = BEAT14
        base.HEAR01 = HEAR01
        base.NERV01 = NERV01
        base.DIAG01 = DIAG01
        base.HEART01 = HEART01
        base.GEND01 = GEND01
        base.SMOKE = SMOKE
        base.DIZZYP07 = DIZZYP07
        base.FATIGP07 = FATIGP07
        base.RECOGN08 = RECOGN08
        base.CHSTPN07 = CHSTPN07
        base.LEGWLK07 = LEGWLK07
        base.PALPIP07 = PALPIP07
        base.CONVER08 = CONVER08
        base.LIFTNG09 = LIFTNG09
        base.STRKBASE = predict

        BaseController.Atualiza(base)

    def atualizar_quadro_clinico(predicao,predicao_proba):
        quadro_c.codigo_adm = 1
        quadro_c.cpf = cpf
        quadro_c.data_AT = dataAT
        quadro_c.peso = peso
        quadro_c.altura = altura
        quadro_c.idade = idade
        quadro_c.glicose = glicose
        quadro_c.SUPSYS16 = SUPSYS16
        quadro_c.SUPDIA16 = SUPDIA16
        quadro_c.DIABETES = DIABETES
        if altura != 0:
            quadro_c.BMI = (peso / (altura * altura))
        else:
            quadro_c.BMI = 0
        quadro_c.FHSTK = FHSTK
        quadro_c.BEAT14 = BEAT14
        quadro_c.HEAR01 = HEAR01
        quadro_c.NERV01 = NERV01
        quadro_c.DIAG01 = DIAG01
        quadro_c.HEART01 = HEART01
        quadro_c.GEND01 = GEND01
        quadro_c.SMOKE = SMOKE
        quadro_c.DIZZYP07 = DIZZYP07
        quadro_c.FATIGP07 = FATIGP07
        quadro_c.RECOGN08 = RECOGN08
        quadro_c.CHSTPN07 = CHSTPN07
        quadro_c.LEGWLK07 = LEGWLK07
        quadro_c.PALPIP07 = PALPIP07
        quadro_c.CONVER08 = CONVER08
        quadro_c.LIFTNG09 = LIFTNG09
        quadro_c.STRKBASE = predicao
        quadro_c.proba_AVC = predicao_proba

        Quadro_cController.Incluir(quadro_c)
        st.success("Quadro Clínico cadastrado com sucesso!")

    def salvar(resultadopred, resultadoproba):
        atualizarBase(resultadopred)
        atualizar_quadro_clinico(resultadopred, resultadoproba)


    sim = st.button('Confirmar probabilidade')
    if sim:
        if not (cpf):
            st.error("O CPF é obrigatório, por favor preencha-o")
        else:
            salvar(previsao, pred)

    modal = Modal("Classificando o paciente", key="unique_modal_key")
    open_modal = st.button("Gerar probabilidade")

    if open_modal:
        if not (cpf):
            st.error("O CPF é obrigatório, por favor preencha-o")
        else:
            modal.open()

    if modal.is_open():
        with modal.container():
            html_string = '''
            <h2>HTML string in RED</h2>

            <script language="javascript">
              document.querySelector("h1").style.color = "red";
            </script>
            '''
            #components.html(html_string)
            with st.spinner('Aguarde, estamos carregando as informações...'):
                entrada = defineEntrada()
                resultadopred, resultadoproba = obterResultado(entrada)
                if resultadopred == 0:
                    st.write("Baseando-se no quadro cliníco apresentado o paciente tem", resultadoproba,
                             "% de probabilidade de não ter um AVC.")
                elif resultadopred == 1:
                    st.write("Baseando-se no quadro cliníco apresentado o paciente tem", resultadoproba,
                             "% de probabilidade de ter um AVC.")
                else:
                    st.write("Baseando-se no quadro cliníco apresentado o paciente tem", resultadoproba,
                             "% de indeterminação para o AVC")

            confirmacao = False
            with st.container():
                st.write('Deseja salvar essa probabilidade?')
                col1, col2 = st.columns(2)
                if col1.button('Sim'):
                    confirmacao = True
                if col2.button('Não'):
                    confirmacao = False
                    modal.close()  # fechar o modal

            if confirmacao:
                with st.spinner('Salvando...'):
                    salvar(resultadopred, resultadoproba)









