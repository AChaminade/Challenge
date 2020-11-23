
st.title('Aeropuertos por pasajero')

n = st.number_input('Insertar número de aeropuertos que desea')

st.write(json.dumps(df.head(n).to_json()))

streamlit run app.py
