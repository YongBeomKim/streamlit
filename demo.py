import streamlit as st

# http://www.coffeesnoopers.com/contents/general/general.asp?page_str_menu=12

## HTML div Text Areas
st.title("커피 스누퍼스 인공지능 모델링")
st.header("Header")
st.subheader("Sub Header")
st.text("Link this video and subscribe to our site")

## MarkDown Text Areas
st.markdown(
    """
# h1 Tag
## h2 Tag
### h3 Tag
:moon:<br>
:sunglasses:
** bold **
_ italics _
""", True)

# Latex Funtion Testing
st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')

# General Write Texts
st.write("Python", "Flask", "Streamlit")
doc = {"name": "Harsh", "language": "Python", "topic": "Streamlit"}
st.write(doc)

st.write(st)  # How to Use Streamlit Document
st.write(max)  # Python built in Function Document
