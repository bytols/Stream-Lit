#Streamlit run <nome do app>.py

import streamlit as st

st.title("streamlit test")

st.write("this is my app")

button1 = st.button("click me")

if button1:
    st.write("the button is true")

like = st.checkbox("Do you like this app?")

button2 = st.button("Submit")

if button2:
    if like:
        st.write("thy. i like it too")
    if like == False:
        st.write("blehhhh")

st.header("Start of the radio")

animal = st.radio("What animal is your favorite?" , ("lions" , "tigers" , "bears"))

button3 = st.button("butao 3")

if button3:
    st.write(animal)
    if animal ==  "lions":
        st.write("rei da florestas")

button4 = st.selectbox("what animal is  your favorite?", ("lion" ,"tiger" , "bear"))


st.header("multiselect Section")

options = st.multiselect("what animal do you like" , ["lion" , "tiger" , "bear"])

st.header("start of the slider")

epochs_num = st.slider("how many epochs?" , 1,100,10)
                                        #(start , end , default)

user_text =  st.text_input("whats your favorite movie?" , "Whiplash?" )

user_int = st.number_input("whats the day of your birth?" )

txt = st.text_area('''
só textando um textão de 
multiplas linhas, alegriaaa
e fé
''')

#st.write("texto" , function )