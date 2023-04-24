from Problem import Problem
from Node import Node
#from Tree import Tree
from queue import PriorityQueue

def UniformCostSearch(problem):
    node = Node(problem.initial_state, 0)
    q = []
    q.append(node)
    explored = []
    while len(q) != 0:
        if len(q) == 0:
            return "failure"
        node = q[0]
        if problem.goal_test(node.state):
            return node
        explored.append(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem,node,action)
            if (child.state != explored) or (child.state != q):
                print("if statement 1")
                if problem.goal_test(child.state):
                    print("if statement 2")
                    return child
                q.append(child)
    return q
