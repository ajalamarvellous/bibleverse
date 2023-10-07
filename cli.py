from base import verse_for_theme, get_objects


def main():
    print("Welcome to the Bible Verse Finder")
    name = input("what is your name: ")
    feeling = input(f"Hello 👋 {name}, how are you feeling today: ")

    print(
        f"Welcome once again {name} and we are glad you came here, \n\
        let us fetch a Bible passage for you and hopefully, we pray it speaks to you"
        )
    bible_map, embedding = get_objects()
    another = "y"
    while another == "y":
        verse = verse_for_theme(feeling, bible_map, embedding)
        print(verse)
        another = input("Do you want another verse? (y/n): ").lower()
        if another == "y":
            feeling = input("what are you also currently feeling that you need a word about: ")
        else:
            break
    print("we hope it speaks to you and long to see you another time")

if __name__ == "__main__":
    main()