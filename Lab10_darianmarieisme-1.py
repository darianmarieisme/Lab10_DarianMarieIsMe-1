'''Word Count Lab 10 Programming Assignment
Darian Marie Bruce
This program determines the word count from an assortment
of files
03/29/2026'''

from pathlib import Path


#color codes ansi escape sequences

orange: str = "\033[38;5;208m"
blue: str = "\033[38;5;27m"
purple: str = "\033[38;5;129m"
green: str = "\033[38;5;46m"
reset: str = "\033[0m"


def main() -> None:

    is_running: bool = True

    files: dict[str, tuple[str, Path]] = {
    "1": ("The Count of Monte Cristo", Path("texts/monte_cristo.txt")),
    "2": ("A Princess of Mars", Path("texts/princess_mars.txt")),
    "3": ("Tarzan of the Apes", Path("texts/Tarzan.txt")),
    "4": ("Treasure Island", Path("texts/treasure_island.txt"))
}

    while is_running == True:

        print("-"*3,"Word Analyzer", "-"*3)
        print("Please select a file to analyze:")

        for key, (name, _) in files.items():
            print(f"{orange}{key}.{reset} {name}")

        print(f"{orange}5. {reset}Exit")
        print()
        user_choice: str = input(f"Enter your {blue}choice{orange} (1 -5):{reset} ").strip()

        if user_choice == "5":
           print()
           print("Goodbye!")
           is_running = False

        elif user_choice not in files:
            print(f"Invalid choice. Please select from {orange}1-5{reset}.")
            input(f"Press Enter to {purple}return{reset} to the menu.")
            continue

        else:
            name: str
            path: Path
            name, path = files[user_choice]
            print()
            print(f"Processing {green}'{path.name}'{reset} ...")
            print()


if __name__ == "__main__":
    main()