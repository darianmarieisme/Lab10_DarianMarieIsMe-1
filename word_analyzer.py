'''Word Count Lab 10 Programming Assignment
Darian Marie Bruce
This program contains the class that
determines the word count from an assortment
of files
03/29/2026'''

from pathlib import Path

class WordAnalyzer:

    def __init__(self, filepath: str):
        self._path: Path = Path(filepath)
        self._word_counts: dict[str, int] = {}

    def process_file(self) -> bool:
        import string

        try: 
            if not self._path.exists():
                return False
            
            translator = str.maketran('', '', string.punctuation)

            with self._path.open('r') as file:
                for line in file:
                    line = line.lower
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