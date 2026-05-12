import streamlit as st

st.title("🎈Ikan Goreng  ")
st.header("Aplikasi Operasi Aritmatika, divider=1True)
number1 = st.number_input("masukkan angka 1")          
number2 = st.number_input("masukkan angka 2")      
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
