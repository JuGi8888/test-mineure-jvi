import streamlit as st
import pandas as pd

st.header("mon application")

nombres = [1, 2, 4, 7]
carre = [1**2, 2**2, 4**2, 7**2]

d = {"nombres": nombres, "carre": carre}
data = pd.DataFrame(d)

st.dataframe(data)


st.header("Widgets Interactifs (partie du cours")

st.header("LOVE JULIE")

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

