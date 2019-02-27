# word-search
This project aims to make a word search solver that solves from a photo of the word search. Using Google's text recognition apis,
the text in the word search can be passed into a Python function that prints a matrix that shows where all of the words are
found.

## Usage
To use the solver, include the solver.py file in your working directory. The solver can be imported using `import solver`. This
includes the solver function as well as a results display function.

### solver.solve(puzzle, words)
solver.solve() takes two arguments.
- puzzle: a list of strings that represent the wordsearch itself
  - all items in puzzle must have an equal length
  - puzzle is not case-sensitive
- words: a list of words to find in the puzzle
  - words is not case-sensitive

Example:
```py
import solver

puzzle = [
  'feowur',
  'dofhda',
  'ecodnb'
]

words = ['foo', 'bar']

solution = solver.solve(puzzle, words)
```

Solution is:
```txt
iuegwbrfwiubgwiu
```

solver.solve() can return either a string or a dictionary. A string is returned in case of an error.
- If the puzzle is invalid, a string is returned detailing the issue
- If the puzzle is valid, a dictionary is returned with the following values
  - words: a list of the original words to look for
  - found: a list of the words that were found
  - Matrix: a matrix that highlights the locations of the solutions
