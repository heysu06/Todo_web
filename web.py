import streamlit as st
import functions as fc


todos = fc.read_user_tasks()

st.title("My To-dos")
st.text_input(label="" , placeholder="Add a To-do . . .")

for items in todos:
    st.checkbox(items)