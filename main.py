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

datos = pd.read_csv("data//red_recarga_acceso_publico_2021.csv", sep=";")
uploaded_file = st.sidebar.file_uploader("Elige el csv", type=["csv"])
if uploaded_file is not None:
    datos = pd.read_csv(uploaded_file)

datos.rename(columns={"latidtud": "lat", "longitud":"lon"}, inplace=True)

datos1 = datos

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
    
    distrito = st.sidebar.checkbox('Distrito')
    if distrito:

        filtro_distrito = st.sidebar.selectbox(
        'Selecciona Distrito',
        ('Arganzuela', 'Barajas', 'Carabanchel', 'Centro', 'Chamartin', 'Chamberí', 'Ciudad Lineal', 'Hortaleza', 'Latina', 'Puente de Vallecas', 'Retiro', 'Salamanca', 'Villa de Vallecas'),
        index=0)
        #datosextra = datos.groupby("Distrito")[[filtro_distrito]].
        datos1 = datos1[datos["DISTRITO"] == filtro_distrito]

    operador = st.sidebar.checkbox('Operador')
    if operador:
        filtro_operador = st.sidebar.selectbox(
        'Selecciona Operador',
        ('DRIVE THE CITY', 'ECOLINERAS', 'ELECTRIC CHARGE SPAIN', 'EMT', 'GIC', 'GIC /CEPSA', 'GIC/GALP', 'IBERDROLA', 'NATURGY', 'REPSOL', ),
        index=0)
        datos1 = datos1[datos["OPERADOR"] == filtro_operador]

    cargadores = st.sidebar.checkbox('Cargadores')
    if cargadores:
        min_cargadores = datos["Nº CARGADORES"].min()
        max_cargadores = datos["Nº CARGADORES"].max()

        num_cargadores = st.sidebar.select_slider("Selecciona el número de cargadores por estación",
                                    options=list(range(min_cargadores, (max_cargadores+1))))

        datos1 = datos1[datos["Nº CARGADORES"] == num_cargadores]

    if datos1.empty == True:
        st.warning('No hay valores que coincidan con la búsqueda')
    
    else: 
        st.write(datos1)
        

#    st.balloons()

    # with st.echo():
    #     st.write(datos)

    # with st.echo():
    #     #codigo para generar numeros pares
    #     lista=list(range(10))
    #     even_list = [x for x in lista if x%2==0]
    #     st.write(even_list)

elif option == "Mapa":

    st.subheader("Mapa")
    st.subheader("Mapa cargadores")
    st.map(datos1)


elif option == "Visualizaciones":

    st.subheader("Visualizaciones")

    datos_barchart= datos.groupby("DISTRITO")[["Nº CARGADORES"]].sum().reset_index()
    st.subheader("Número de cargadores por distrito")
    st.bar_chart(datos_barchart, x="DISTRITO", y="Nº CARGADORES")

    

