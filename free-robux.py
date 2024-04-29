import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title="free robux", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Header section
with st.container():
    st.subheader("Hi, I am huy :wave:")
    st.title("This is how you get free robux")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/7a110907-3d03-40d7-898c-55a89d89a595/37NyEgw8KI.json")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What you do")
        st.write("##")
        st.write(
            """
            - click "[click here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)" and close your eyes
            - watch the tutorial then receive the robux
            """
        )
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")