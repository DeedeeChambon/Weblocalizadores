import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
)

option = st.sidebar.selectbox(
    'Selecciona la vista',
    ('Home', 'Visualizaciones','Mapa'),
    index=0)


datos = pd.read_csv(r"data\red_recarga_acceso_publico_2021.csv", sep=";")
uploaded_file = st.sidebar.file_uploader("Elige el csv", type=["csv"])
if uploaded_file is not None:
    datos = pd.read_csv(uploaded_file)


st.title("CARGATRON")

if option == "Home":

    st.subheader("Home")

    st.title("My APP - Landing page")

    st.image('https://statics.forbesargentina.com/2022/12/crop/63a1aa07f3f5c__822x822.webp', width=600, caption="GOAT")

    with st.expander("Quien es este crack - Haz click para expandir"):
        st.write("""
        Esto es una aplicación para rendirle pleistesía al GOAT:
        -7 balones de oro
        -1 mundial
        -3 champions
        """)


    st.write(datos)
    st.balloons()

    with st.echo():
        st.write(datos)

    with st.echo():
        #codigo para generar numeros pares
        lista=list(range(10))
        even_list = [x for x in lista if x%2==0]
        st.write(even_list)

elif option == "Mapa":

    st.subheader("Mapa")

    datos_arreglados= datos[["latidtud", "longitud"]]
    datos_arreglados.columns = ["lat", "lon"]
    st.subheader("Mapa cargadores")
    st.map(datos_arreglados)

elif option == "Visualizaciones":

    st.subheader("Visualizaciones")

    datos_barchart= datos.groupby("DISTRITO")[["Nº CARGADORES"]].sum().reset_index()
    st.subheader("Número de cargadores por distrito")
    st.bar_chart(datos_barchart, x="DISTRITO", y="Nº CARGADORES")



