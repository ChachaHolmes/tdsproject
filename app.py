import streamlit as st


def largest_number(a, b, c):
    return max(a, b, c)


st.title("Find the largest among 3 numbers")
st.write("Enter the values of the 3 numbers below:")

a = st.number_input("Enter the first number:", value=0, step=1)
b = st.number_input("Enter the second number:", value=0, step=1)
c = st.number_input("Enter the third number:", value=0, step=1)

if st.button("Find the largest number"):
    result = largest_number(a, b, c)
    st.write(f"The largest number is {result}.")
