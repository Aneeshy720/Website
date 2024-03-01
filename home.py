import streamlit as st
t1,t2,t3 = st.tabs(["Greetings","About Me", "Free time activities"])
with t1:
    st.header("Hello!")
    st.subheader("This is a simple website about me and what I like to do to pass time 😃.")
    st.image("Lambo.jpeg",width = 400)
    st.image("bugatti.jpeg", width = 500)
with t2: 
    st.header("Anish Vobilisetti")
    st.subheader("Hi, my name  is Anish and I live in Pleasanton California. I go to Thomas Hart Middle School.")
    st.subheader("My phone number is 925-344-3261")
with t3:
    st.header("Free time activities")
    st.subheader("In my free time, I like to go to the park and play basketball or soccer with my friends. When I'm at home, I like to play Fortnite on my xbox. Also, I like to spend time with my family.")