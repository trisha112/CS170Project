from Problem import Problem
from Node import Node
#from Tree import Tree
from queue import PriorityQueue
def UniformCostSearch(problem):
    print("in uniformCostSearch function")
    node = Node(problem.initial_state, 0)
    q = PriorityQueue()
    q.put(node)
    explored = set()
    while q.qsize != 0:
        print("in while")
        if q.empty():
            print("failure")
            return "failure"
        node = q.get()
        if problem.goal_test(node.state):
            print("problem.goal_test(node.state)")
            return node
        explored.add(tuple(node.state))
        print("explored.put(node.state)")
        for action in problem.actions(node.state):
            child = child.node(problem,node,action)
            print("forloop")
            if (child.state not in explored) & (child.state not in q):
                q.put(child,q)
