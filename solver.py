def solve(puzzle, words):
    # Some notes about this solution:
    # * Puzzle must be a list with strings of equal lengths. In other words, the
    #   puzzle needs to be rectangular

    # check that all lines are equal length
    if len(set(len(line) for line in puzzle)) != 1:
        return 'Invalid input error: lines in input are not of equal length'

    # create a matrix to represent the solution
    Matrix = []
    for line in puzzle:
        row = []
        for i in range(len(line)):
            row.append('*')
        Matrix.append(row)
    
    # put everything in lowercase
    for i in range(len(words)):
        words[i] = words[i].lower()
    for i in range(len(puzzle)):
        puzzle[i] = puzzle[i].lower()

    found = []

    # rather than scanning the entire puzzle at once, this program searches for
    # one word at a time which is slower, but seems to be easier to program
    for word in words:
        # check horizontals
        for i in range(len(puzzle)):
            if word in puzzle[i]:
                found.append(word)
                start = puzzle[i].index(word)
                end = start + len(word)
                for j in range(len(word)):
                    Matrix[i][j + start] = word[j].upper()
            elif word in puzzle[i][::-1]:
                found.append(word)
                start = len(puzzle[i]) - puzzle[i][::-1].index(word) - 1
                end = start - len(word) + 1
                for j in range(len(word)):
                    Matrix[i][start - j] = word[j].upper()
        # check verticals
        for i in range(len(puzzle[0])):
            # i is the column, j is the row
            row_string = ''
            for j in range(len(puzzle)):
                row_string += puzzle[j][i]
            if word in row_string:
                found.append(word)
                start = row_string.index(word)
                end = start + len(word)
                for k in range(len(word)):
                    Matrix[start + k][i] = word[k].upper()
            elif word in row_string[::-1]:
                found.append(word)
                start = len(row_string) - row_string[::-1].index(word) - 1
                end = start - len(word) + 1
                for k in range(len(word)):
                    Matrix[start - k][i] = word[k].upper()
        # check diagonals
        for i in range(len(puzzle)):
            diag = ''
            for j in range(len(puzzle[0]) - i):
                if i + j == len(puzzle):
                    break
                diag += puzzle[i + j][j]
            if word in diag:
                found.append(word)
                start = diag.index(word)
                end = start + len(word)
                for k in range(len(word)):
                    Matrix[i + start + k][start + k] = word[k].upper()
            elif word in diag[::-1]:
                found.append(word)
                start = diag[::-1].index(word) - 1
                end = start - len(word) + 1
                for k in range(len(word)):
                    Matrix[start - i - k][start - k] = word[k].upper()
                
        for i in range(len(puzzle[0])):
            # Skip the first diagonal
            if i == 0:
                continue
            
            diag = ''
            for j in range(len(puzzle) - i):
                if j + i == len(puzzle[0]):
                    break
                diag += puzzle[j][j + i]
            if word in diag:
                found.append(word)
                start = diag.index(word)
                end = start + len(word) - 1
                for k in range(len(word)):
                    Matrix[i + start + k - 1][i + start + k] = word[k].upper()
            elif word in diag[::-1]:
                found.append(word)
                start = diag[::-1].index(word) - 1
                end = start - len(word) - 1
                for k in range(len(word)):
                    Matrix[len(word) - k][(i + len(word)) - k] = word[k].upper()
        # more diagonal checks
        for i in range(len(puzzle)):
            diag = ''
            for j in range(len(puzzle[0])):
                if i - j < 0:
                    break
                diag += puzzle[i - j][j]
                diag = diag[:i + 1]
            if word in diag:
                found.append(word)
                start = diag.index(word)
                end = start + len(word) - 1
                for k in range(len(word)):
                    Matrix[start + i - k][start + k] = word[k].upper()
            elif word in diag[::-1]:
                found.append(word)
                start = len(diag) - diag[::-1].index(word) - 1
                end = start - len(word) + 1
                for k in range(len(word)):
                    Matrix[i - start + k][start - k] = word[k].upper()
        # the last diagonal checks
        for i in range(len(puzzle[0])):
            if i == 0:
                continue
            diag = ''
            for j in range(len(puzzle)):
                if i + j == len(puzzle[0]):
                    break
                diag += puzzle[len(puzzle) - 1 - j][i + j]
            if word in diag:
                found.append(word)
                start = diag.index(word)
                end = start + len(word) - 1
                for k in range(len(word)):
                    Matrix[len(Matrix) - 1 - start - k][i + start + k] = word[k].upper()
            elif word in diag[::-1]:
                found.append(word)
                start = len(diag) - diag.index(word[::-1]) - 1
                end = start - len(word)
                for k in range(len(word)):
                    Matrix[len(puzzle) - start + k][i + start - k - 1] = word[k].upper()

    return {
        'words': words,
        'found': found,
        'Matrix': Matrix
    }


def print_results(solution):
    if str(solution) is solution:
        print(solution)
        return
    words = solution['words']
    found = solution['found']
    Matrix = solution['Matrix']

    if words == found:
        print('All words found.')
    else:
        for word in words:
            if word not in found:
                print('!!! {} was not found !!!'.format(word))
            else:
                print('{} was found.'.format(word))

    for line in Matrix:
        for char in line:
            print(char, end='')
        print()


if __name__ == '__main__':
    puzzle = [
        'EFHNAAACOPCTTL',
        'UBSENNDESRIMLH',
        'SSUUBROHTIERES',
        'IORTPCEWILLEEE',
        'NSUEUEDAMETTOL',
        'AAPSEORIWNNNAY',
        'TGUMCSYPFALUBT',
        'EPPNWOHUELOHNS',
        'SUFEWMREOTERIU',
        'BUUBCALORWESFH',
        'EUNYSHCROCIRFU',
        'MTRNBCNUCENIIY',
        'LTFOCIPEMTTERW',
        'RRLEORIPAHSDGR'
    ]

    words = ['chamos', 'hunter', 'will', 'shapiro', 'nate', 'griffin', 'dame',
             'youtube', 'ben', 'peter', 'cool', 'super', 'epic', 'style']

    first = solve(puzzle, words)
    print_results(first)

    p2 = [
        'JRRRATATAJF',
        'NANWOKVUPIS',
        'NIBGQIAVOGQ',
        'HCRENPPNKGU',
        'SHEOEWOMELI',
        'YUPQOVRLMYR',
        'KGRINLEMOPT',
        'GQIWKLOENUL',
        'FLAREONAFFE',
        'GLACEONCBFE',
        'PIKACHUKTXU'
    ]

    w2 = ['jigglypuff', 'pikachu', 'ratata', 'vaporeon', 'raichu', 'glaceon',
          'eevee', 'flareon', 'pokemon', 'squirtle']

    second = solve(p2, w2)
    print_results(second)
