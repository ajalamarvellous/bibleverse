import streamlit as st
from base import verse_for_theme


def main():
    st.title("Welcome to the Bible Verse Finder")
    name = st.text_input("what is your name: ")
    feeling = st.text_input(f"Hello 👋 {name}, how are you feeling today: ")

    with st.status(
        f"Welcome once again {name} and we are glad you came here, \n\
        let us fetch a Bible passage for you and hopefully, we pray it speaks to you"
        ):
        verse = verse_for_theme(feeling)
    
    st.write(verse)

    st.write("we hope it speaks to you and long to see you another time")

if __name__ == "__main__":
    main()