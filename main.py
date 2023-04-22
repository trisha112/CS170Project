def main():
    print("Welcome to #25 8 puzzle solver.")
    puzzleChoice = input("Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n")
    if puzzleChoice == 1:
        # default puzzle code
        print("#1")
    elif puzzleChoice == 2:
        print("Enter your puzzle, use a zero to represent the blank")
        first = input(print("Enter the first row, use space or tabs between numbers "))
        second = input(print("Enter the second row, use space or tabs between numbers"))
        third = input(print("Enter the third row, use space or tabs between numbers "))
        # enter your own puzzle code
    algChoice = input("Enter your choice of algorithm\n1. Uniform Cost Search\n2. A* with the Misplaced Tile heuristic.\n3. A* with the Euclidean distance heuristic.\n")
    if algChoice == "1":
        print("uniform cost search code here")
    elif algChoice == "2":
        print("A* with the Misplaced Tile heuristic code here")
    elif algChoice == "3":
        print("A* with the Euclidean distance heuristic. code here")
    else:
        print("invalid algorithm chosen")

main()
