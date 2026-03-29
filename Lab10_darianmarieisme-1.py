'''Word Count Lab 10 Programming Assignment
Darian Marie Bruce
This program determines the word count from an assortment
of files
03/29/2026'''


#color codes ansi escape sequences

orange: str = "\033[38;5;208m"
blue: str = "\033[38;5;27m"
purple: str = "\033[38;5;129m"
green: str = "\033[38;5;46m"
reset: str = "\033[0m"

exit: bool = False

def main() -> None:

    while exit == False:

        print("-"*3,"Word Analyzer", "-"*3)
        print("Please select a file to analyze:")
        print(f"""
            {orange}1.{reset} The Count of Monte Cristo {orange}(Chapter 1)
            2. {reset}A Princess of Mars {orange}(Chapter 1)
            3. {reset}Tarzan of the Apes {orange}(Chapter 1)
            4. {reset}Treasure Island {orange}(Chapter 1)
            5. {reset}Exit
            """)
        choice: str = input(f"Enter your {blue}choice{orange}(1 -5):{reset} ")