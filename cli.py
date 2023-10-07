from base import verse_for_theme


def main():
    print("Welcome to the Bible Verse Finder")
    name = input("what is your name: ")
    feeling = input(f"Hello 👋 {name}, how are you feeling today: ")

    print(
        f"Welcome once again {name} and we are glad you came here, \n\
        let us fetch a Bible passage for you and hopefully, we pray it speaks to you"
        )
    
    verse = verse_for_theme(feeling)
    print(verse)

    print("we hope it speaks to you and long to see you another time")

if __name__ == "__main__":
    main()