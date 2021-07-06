import streamlit as st
import webbrowser
from PIL import Image
import pandas as pd
import numpy as np
import time

logo_image = './media/logo.png'
url = 'http://www.coffeesnoopers.com/contents/general/general.asp?page_str_menu=12'
image = Image.open(logo_image)

# <Headers>
st.title("")
st.image(image, caption='과학적이고 정량적인 커피 분석을 향한 길')
st.markdown("# **커피 스누퍼스 인공지능 모델링**")
if st.button('홈페이지 바로가기'):
    webbrowser.open_new_tab(url)
# https://discuss.streamlit.io/t/how-to-link-a-button-to-a-webpage/1661/2
# st.markdown("# **[커피 스누퍼스 인공지능 모델링]()**")
# st.title("커피 스누퍼스 인공지능 모델링")
# if st.checkbox('checkbox'):
#     st.image(banner_image)

## Chapter 3 Pandas Data
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = np.array(a)
nd = n.reshape((2, 4))
dic = {"name": ["harsh", "Gupta"], "age": [21, 32], "city": ["noida", "delhi"]}
data = pd.read_csv("media/Salary_Data.csv")

# st.dataframe(data, width="100%", height=500)
st.dataframe(data.head(5), width=600, height=500)
st.table(data.head(3))
st.table(dic)
st.json(dic)
st.write(dic)


@st.cache
def ret_time(a):
    time.sleep(3)
    return "모델 정확도 : 0.982142354"
    # return time.time()


if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))

## Chapter 1, 2 Display Texts
# <Contents>
st.header("Header")
st.subheader("Sub Header")
st.text("Link this video and subscribe to our site")

## <Contents> MarkDown Text
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
