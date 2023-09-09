from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/db664498-4f57-41d8-9d90-709ba5062150/6dGma5IClk.json")
img_contact_form = Image.open("images/kalkuban.png")
img_lottie_animation = Image.open("images/yt-2.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I'm Rico :wave:")
    st.title("A Backend Developer and Data Scientist From SMKN 26 Jakarta")
    st.write(" am someone who is interested in the development of technology, especially in the field of programming and data, responsive in learning, always enthusiastic in solving problems, and has a high desire for what is my goal.")
    st.write("[Learn More >](https://streamlit.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            
            I enjoy learning about various data analysis methods, such as statistics, machine learning, and visualization. The program language I learned and the tools:
            - Python
            - Mysql
            - Tableau
            - PHP
            - Ruby
            - Laravel

            If you have any questions, click message on the bottom yaw .Hope you enjoy with me and bye bye ^_^.

            """
        )
        st.write("[My Github >](https://github.com/Rizxh)")
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("----")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Create a calculation program from build space")
        st.write(
            """

            Menghitung semua jenis bangun ruang dengan cepat, 
            tepat, dan pastinya langsung saja sikat

            """
        )
        st.markdown("[Kalkuban](https://kalkuban.streamlit.app/)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """

            Learn how to use Lottie files in streamlit!
            Animations make our web app more engaging and fun, and lottie files are the easiest way to do!
            In this tutorial , I'll show you exactly how do to it

            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/ryuhuzu@gmail.com" method="POST">
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