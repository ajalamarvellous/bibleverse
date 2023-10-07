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
            bible_map, embedding = get_objects()
            another = "y"
            while another == "y":
                verse = verse_for_theme(feeling, bible_map, embedding)
                st.write(verse)
                another = st.text_input("Do you want another verse? (y/n): ").lower()
                if another == "y":
                    feeling = st.text_input("what are you also currently feeling that you need a word about: ")
                else:
                    break

    st.write("we hope it speaks to you and long to see you another time")

if __name__ == "__main__":
    main()