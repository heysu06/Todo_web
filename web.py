import streamlit as st
import functions as fc
#streamlit run web.py

todos = fc.read_user_tasks()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fc.write_user_tasks(todos)


st.title("My To-dos")
st.text_input(label="" , placeholder="Add a To-do . . ." ,
                on_change=add_todo , key="new_todo")

for items in todos:
    st.checkbox(items)

st.session_state