import streamlit as st
import pandas

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/myphoto.jpeg", width=550)

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


text1 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(text1)

col3, space_col,  col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

