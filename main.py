from Problem import Problem
#from Node import Node
#from Tree import Tree
from UniformCostSearch import *
def main():
    initial = []
    print("Welcome to #25 8 puzzle solver.")
    goalState = [1,2,3,4,5,6,7,8,9]
    puzzleChoice = input("Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n")
    if puzzleChoice == "1":
        defaultPuzzle = [1,0,3,4,2,6,7,5,8]
        problemVal = Problem(defaultPuzzle, goalState)

    if puzzleChoice == "2":
        print("Enter your puzzle, use a zero to represent the blank")
        first = input("Enter the first row, use space or tabs between numbers: ").split()
        second = input("Enter the second row, use space or tabs between numbers: ").split()
        third = input("Enter the third row, use space or tabs between numbers: ").split()
        initial = first + second + third
        initialState = [int(x) for x in initial]
        problemVal = Problem(initialState,goalState)
    algChoice = input("Enter your choice of algorithm\n1. Uniform Cost Search\n2. A* with the Misplaced Tile heuristic.\n3. A* with the Euclidean distance heuristic.\n")
    if algChoice.strip() == "1":
        print("uniform cost search code here")
        print(UniformCostSearch(problemVal))
    elif algChoice.strip() == "2":
        print("A* with the Misplaced Tile heuristic code here")
    elif algChoice.strip() == "3":
        print("A* with the Euclidean distance heuristic. code here")
    else:
        print("invalid algorithm chosen")

main()
