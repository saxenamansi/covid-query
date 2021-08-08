import streamlit as st
from tfidf import *

def main(st):
    st.title("Covid-19 FAQs")
    st.write("# Welcome! \nHope you are keeping safe in this pandemic! For further informstion on covid-19, ask your queries below and get reliable expert answers!")
    input_query = st.text_input(label = "What is your Covid-19 query?")
    st.sidebar.title("Developer's Contact")
    st.sidebar.markdown('[![Mansi-Saxena]'
                            '(https://img.shields.io/badge/Author-Mansi%20Saxena-brightgreen)]'
                            '(https://www.linkedin.com/in/mansi-saxena-084b681a2/)' 
                        '\n[![Raksha-Kannusami]'
                            '(https://img.shields.io/badge/Author-Raksha%20Kannusami-brightgreen)]'
                            '(https://www.linkedin.com/in/raksha-kannusami/)')
    st.sidebar.title("For any queries contact us via email:")
    st.sidebar.markdown("\n*immansi@gmail.com*\n*rakshakannu@gmail.com*")
    i1, i2, i3 = ask_question_tfidf(input_query)
    if len(input_query) != 0:
        st.write("\nTop 3 questions retrieved: ")
        q1 = st.button(df['Question'].iloc[i1])
        q2 = st.button(df['Question'].iloc[i2])
        q3 = st.button(df['Question'].iloc[i3])
        if q1:
            st.write(df['Answers'].iloc[i1])
        if q2:
            st.write(df['Answers'].iloc[i2])
        if q3:
            st.write(df['Answers'].iloc[i3])

if __name__ == '__main__':
    main(st)