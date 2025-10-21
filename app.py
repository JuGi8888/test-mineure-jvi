import streamlit as st
import pandas as pd

st.header("Mes soeurs adorées :")

soeurs = ["Diane", "Louise"]
age = [30, 24]

d = {"soeurs": soeurs, "age": age}
data = pd.DataFrame(d)

st.dataframe(data)

st.header("AIMEZ-MOI JULIE")

# Un slider
love = st.slider("A quel point vous aimez Julie ?", 0, 100, 25)
st.write("Vous aimez Julie à :", love)

# Une liste de sélection
option = st.selectbox(
    'Quand est-ce que vous aimeriez voir Julie?',
    ('Dès que possible <3', 'Quand on pourra', 'Jamais elle gaze'))
st.write('Vous aimeriez voir Julie.... :', option)

# Un bouton
if st.button('Cliquez ici !'):
    st.write('Vous avez cliqué ! Bravo vive JULIE !! PS : I love you my sisters Diane & Louise')

