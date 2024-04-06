import langchain_helper as lch
import streamlit as st

st.title("pet name finder")

user_animal_type = st.sidebar.selectbox("which animal is your pet?", ("cat","dog", "parrot", "fish"))

if user_animal_type:
    user_pet_color = st.sidebar.text_area(label=f"what color is your {user_animal_type}?", max_chars=15)

if user_pet_color:
    response = lch.generate_pet_name(user_animal_type, user_pet_color)
    st.text(response['pet_name'])
