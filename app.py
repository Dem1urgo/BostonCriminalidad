import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import joblib
from datetime import datetime


# importamos la libreria

st.title("Criminalidad Boston")
# titulo de la pagina

st.image("https://res.cloudinary.com/hello-tickets/image/upload/c_limit,f_auto,q_auto,w_1920/v1666319015/nav1fqffqinlkkhgps5i.jpg",
            width=400)

st.header('Prediccion de la criminalidad en Boston')


d = st.date_input("Escoge fecha")
dia = d.weekday() + 1
anio = d.year
mes = d.month

hora = st.slider('Escoge hora (Formato 24H)', 0, 23, 0)

distrito = st.selectbox(
    'Selecciona el distrito',
    ('A1', 'A15', 'A7', 'B2', 'B3', 'C11', 'C6', 'D14', 'D4', 'E13',
       'E18', 'E5'))
st.write('Has escogido:', distrito)


if st.button("Calcula la salida", key='b3'):
  
    model = joblib.load("crime_prediction_model.pkl") # llama al modelo

    X = pd.DataFrame([
        [anio, mes, dia, hora, distrito]],
        columns = ["YEAR", "MONTH", "DAY_OF_WEEK", "HOUR", "DISTRICT"]
        )

    X = X.replace(['A1', 'A15', 'A7', 'B2', 'B3', 'C11', 'C6', 'D14', 'D4', 'E13',
       'E18', 'E5'],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    prediccion = int(model.predict(X)[0])
    st.text(f"La cantidad de delitos en la fecha, hora y distrito solicitado será de aproximadamente de : {prediccion} delitos.")