import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Add Anime to Watch")
st.subheader("This app can store Anime list.")
st.write("This app can track your progress.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]


st.text_input(label="",
              placeholder="Add a new anime..",
              on_change=add_todo,
              key='new_todo')