import streamlit as st

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/myphoto.jpeg", width=600)

with col2:
    st.title("Nanda Datta Buri")
    content = """
    I am Nanda Datta Buri, a recent Computer Science graduate from Dr. Hima Sekhar Degree College (Class of 2023).
    My expertise lies in web development and programming, with a solid command of languages like Python. 
    I have developed a Python-based to-do app that features functionalities for adding, showing, editing, 
    and completing tasks stored in a text file. My academic excellence and practical experience are further underscored 
    by internships in cyber security and digital marketing. I am passionate about continuous learning and applying my 
    skills to solve real-world problems.
    """
    st.info(content)

