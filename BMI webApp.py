import streamlit as st
st.title("---------- BMI CALCULATOR -----------")
n=st.text_input("Enter Your Name","Type Here...")
st.radio("Select Your Gender:",('Male','Female'))
st.number_input('Enter Your Age:')
st.text_input("Enter Your Address:","Type Here...")
st.text("Enter Your Hobbies: ")
st.checkbox("Dancing")
st.checkbox("Reading")
st.checkbox("Writting")
st.checkbox("Coding")
st.checkbox("Sports")

a=st.number_input('Enter Your Weight in kg:')
b=st.number_input('Enter Your Height in cms:')
b=b/100
try:
    
    c=a/(b**2)
except:
    print("division by zero not allowed")

form = st.form("my_form")
submitted = form.form_submit_button("Calculate")

if submitted:
    st.success("Hello Your BMI Calculated is {}".format(c))

