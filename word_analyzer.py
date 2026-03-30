'''Word Count Lab 10 Programming Assignment
Darian Marie Bruce
This program contains the class that
determines the word count from an assortment
of files
03/29/2026'''

from pathlib import Path

import string

class WordAnalyzer:

    def __init__(self, filepath: str):
        self._path: Path = Path(filepath)
        self._word_counts: dict[str, int] = {}

    def process_file(self) -> bool:


        try: 
            if not self._path.exists():
                return False
            
            extra_punctuation: str = "\u201c\u201d\u2018\u2019\u2014\u2022"

            translator: dict[int, None] = str.maketrans('', '', string.punctuation + extra_punctuation)

            with self._path.open('r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translator)
                    words = line.split()

                    for word in words:
                        if word in self._word_counts:
                            self._word_counts[word] += 1
                        else:
                            self._word_counts[word] = 1

            return True
    
        except FileNotFoundError:
            return False
        
    def print_report(self):

        #color code ansi escape sequences
        orange: str = "\033[38;5;208m"
        purple: str = "\033[38;5;129m"
        reset: str = "\033[0m"

        for word in sorted(self._word_counts.keys()):
            print(f"{word:<10} :: {orange}{self._word_counts[word]}{reset}")

        print()
        print(f"Press Enter to {purple}return{reset} to the menu...")
        input()