import streamlit as st
import pickle

st.markdown("""### :books: **Repositório Github: [Projeto Predição Diabetes](https://github.com/OviedoVR/PredicaoDiabetes.git)**""")

st.markdown('##')
st.markdown("""**Objetivo:** Prever, com acurácia maior ou igual a 70%, se um paciente tem
            diabetes ou não, com base em atributos como **idade**; **IMC**; nível de **glicose**, **LDL** e **HDL**; 
            **pressão sanguínea (sístole)** e  **pressão sanguínea (diástole)**.
            """)
st.markdown("""<hr style="height:1.0px;width:700px;border:none;
            color:#333;background-color:#333" /> """, 
            unsafe_allow_html=True)
            

st.markdown("""### **Variáveis preditoras**""")

st.markdown(':wrench: <span style="color:RoyalBlue"> <b> Informe a idade </b> </span> :hammer: ',
            unsafe_allow_html=True)                           
idade = st.number_input('Faixa: 19-84', min_value=19, max_value=84, step=1)
#
st.markdown(':wrench: <span style="color:RoyalBlue"> <b> Informe o IMC </b> </span> :hammer: ',
            unsafe_allow_html=True)                           
imc = st.number_input('Faixa: 15-40', min_value=15, max_value=40, step=5)
#
st.markdown(':wrench: <span style="color:RoyalBlue"> <b> Informe o valor da glicose </b> </span> :hammer: ',
            unsafe_allow_html=True)
glicose = st.number_input('Faixa:48-371', min_value=48, max_value=371, step=10)
#
st.markdown(':wrench: <span style="color:RoyalBlue"> <b> Informe o valor do LDL </b> </span> :hammer: ',
            unsafe_allow_html=True)
ldl = st.number_input('Faixa: 78-342', min_value=78, max_value=342, step=10)

st.markdown(':wrench: <span style="color:RoyalBlue"> <b> Informe o valor do HDL </b> </span> :hammer: ',
            unsafe_allow_html=True)
hdl = st.number_input('Faixa: 12-120', min_value=12, max_value=120, step=10)
#
razao_ldl_hdl = ldl/hdl
#
st.markdown(""":wrench: <span style="color:RoyalBlue"> <b> Informe a pressão sanguínea (sístole) </b> 
            </span> :hammer:
            """, unsafe_allow_html=True)   
ps_sistole = st.number_input('Faixa: 90-230', 
                        min_value=90, max_value=230, step=10)

st.markdown(""":wrench: <span style="color:RoyalBlue"> <b> Informe a pressão sanguínea (diástole) </b> 
            </span> :hammer:
            """, unsafe_allow_html=True)   
ps_diastole = st.number_input('Faixa: 48-124', 
                        min_value=48, max_value=124, step=4)                        

regressao_logistica = open('regressao_logistica.pkl', 'rb')
modelo = pickle.load(regressao_logistica)

# Sidebar --------------
st.sidebar.markdown("""<hr style="height:3px;width:300px;border:none;
            color:#333;background-color:#333" /> """, 
            unsafe_allow_html=True)

st.sidebar.markdown("""<h2 style="color:black;text-align:justify"> <b> 
                    &#128269 MODELO PARA PREVER SE UM PACIENTE TEM DIABETES
                    </b> </h2>
                    """, unsafe_allow_html=True)

st.sidebar.markdown("""<hr style="height:3px;width:300px;border:none;
            color:#333;background-color:#333" /> """, 
            unsafe_allow_html=True)

st.sidebar.markdown("""<span style="color:black"> Desenvolvido por **Vinícius Oviedo**
                    </span>""", unsafe_allow_html=True)
#  --------------------
st.markdown('#####')


botao = st.button('Predizer')

if botao == 1:
    predicao = modelo.predict(
                        [[
                        ldl, glicose, hdl, razao_ldl_hdl,
                        idade, imc, ps_sistole, ps_diastole
                        ]])  
    if predicao == [0]:
        resultado = """
                    <h3>
                    <b> Resultado: <span style="color:RoyalBlue"> Não tem diabetes </span> </b>
                    </h3>
                    """
        st.markdown(resultado, unsafe_allow_html=True)
    else:
        resultado = """
                    <h3>
                    <b> Resultado: <span style="color:RoyalBlue"> Tem diabetes </span> </b>
                    </h3>
                    """
        st.markdown(resultado, unsafe_allow_html=True)

st.markdown("""<hr style="height:1.5px;width:700px;border:none;
            color:#333;background-color:#333" /> """, 
            unsafe_allow_html=True)

st.markdown("""### **Métricas de performance do modelo**""")

st.markdown('#### **Matriz de confusão**')
st.image('Confusao_RegLog.png')

st.markdown('#### **Performance**')

st.markdown("""
**Acurácia**: 87%

**Precisão**: 87%

**Sensibilidade (% taxa de acertos)**: 87%

**Score F1 (média harmônica entre sensibilidade e especificidade)**: 87%   
""")

st.markdown('#### **Curva ROC e AUC**')
st.image('ROC_AUC.png')

st.markdown("""<hr style="height:1.5px;width:700px;border:none;
            color:#333;background-color:#333" /> """, 
            unsafe_allow_html=True)

st.markdown("""### **Conclusão**""")

st.markdown("""Conforme podemos ver, o objetivo foi alcançado, isto é, conseguimos prever se um 
            paciente tem diabates como base em 7 atributos e com uma acurácia de **87%**. 
            """)
