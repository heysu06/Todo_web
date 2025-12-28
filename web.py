import streamlit as st
import functions as fc

#to run the web app use: streamlit run web.py   in the terminal

todos = fc.read_user_tasks()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fc.write_user_tasks(todos)


st.title("My To-dos")
st.text_input(label="" , placeholder="Add a To-do . . ." ,
                on_change=add_todo , key="new_todo")

for index , todo in enumerate(todos):
    checkbox = st.checkbox(todo , key=todo)
    if checkbox:
        todos.pop(index)
        fc.write_user_tasks(todos)
        del st.session_state[todo]
        st.rerun()