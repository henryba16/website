import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title="About me", page_icon=":tada:", layout="wide")

# Header section
with st.container():
    st.subheader("Hi, I'm Nguyen Ba but you can call me Henry :wave:")
    st.title("A young programmer From VietNam")
    st.write("I'm finding ways to use Python to be more efficient and effective in business.")
    st.write("[Learn More >](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/7a110907-3d03-40d7-898c-55a89d89a595/37NyEgw8KI.json")
# ---- WHAT I DO ----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - looking for a way to leverage the power of Python in these day to work.
            - inpove python code like working with python and thought - "there has to be a better way."
            """
        )
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/henrytran511@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
