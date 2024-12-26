import streamlit as st
from streamlit.components.v1 import html
import streamlit_scrollable_textbox as stx


def run():
    st.video(f"C:\\Users\\User\\vscode_project\\labs\\labs\\{radiobtn}\\video.mp4")


def display():
    with open(f"C:\\Users\\User\\vscode_project\\labs\\labs\\{radiobtn}\\lab.py") as code_f:
        code = code_f.read()

    with open(f"C:\\Users\\User\\vscode_project\\labs\\labs\\{radiobtn}\\README.md") as readme_f:
        readme = readme_f.read()
    container = st.container(height=300)

    with container:
        st.code(code, language='python')

    with st.container(height=300):
        st.code(readme, language=None)


options = ["lab1", "lab2", "lab3",  "lab4", "lab5", "lab6", "lab7", "lab8"]
st.sidebar.write('LABS LIST')
radiobtn = st.sidebar.radio('Choose a lab you want to try out: ', options)

st.sidebar.button("run", on_click=run)


display()
