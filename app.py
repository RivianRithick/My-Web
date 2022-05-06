import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage",page_icon=':tada:',layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ngzwzxib.json")

with st.container():
    st.title("About me! :dizzy:")
    st.header("Hi, I am Rithickshival M :wave:")
    st.subheader("B.E Graduate From India")
    st.write("I am a passionate technology enthusiast. I take great pleasure in learning new technologies and finding ways in which this can aid people every day.")
    st.write("To see my resume, click below! :point_down:")
    st.write("[My Resume :file_folder:](https://drive.google.com/file/d/1ssH8E-C7BmSPtWqMWbbAwp-z5ucl9W0Q/view?usp=sharing)")

with st.container():
    st.write("---")
    left_column, right_cloumn = st.columns(2)
    with left_column:
        st.title("About My Projects")
        st.write('##')
        st.header('AUTOMATION USING PIR SENSOR AND ULTRASONIC SENSOR.')
        st.write(":small_blue_diamond:The purpose of the project is to design a smart automatic system which targets the energy saving and automatic ON/OFF of appliances, when there is a human presence.")
        st.write(":small_blue_diamond:PIR Sensor is used to turn ON the light by sensing the existence of human and it automatically turns OFF, after a limited period of time.")
        st.write(":small_blue_diamond:Ultrasonic sensor is used to turn ON the light when there is human presence and automatically turns OFF at the instance when the presence is not detected, this can be used in office cabin, etc")
        st.write(":small_blue_diamond:Arduino UNO is used here to upload the code and receive the signal from the sensor and according to the code, it sends the signal to the relay to ON/OFF the illumination system.")



        st.header('ULTRASONIC SENSOR BASED DRIPS MONITORING SYSTEM IN HOSPITALS.')
        st.write(":small_blue_diamond:An Arduino Uno, an HC SR-04 Ultrasonic Sensor, an LDR, a light source, and an ESP8266-01 Wi-Fi module make up the system.")
        st.write(":small_blue_diamond:The sensors are linked to a drip bottle operated by an Arduino microcontroller.")
        st.write(":small_blue_diamond:The data is gathered and sent to the website through the wifi module, where it can be readily displayed.")
        st.write(":small_blue_diamond:The data is retrieved from the cloud via the android app, which alerts medical staff to the production of bubbles and the amount of fluid remaining in the drip")

    with right_cloumn:
        st_lottie(lottie_coding, height=500, key="coding")


