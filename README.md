# 8PuzzleSolver
Python assignment for edx.org course "ColumbiaX: CSMM.101x Artificial Intelligence (AI)"


----------


**INSTRUCTIONS**

In this assignment you will create an agent to solve the 8-puzzle game. You may visit mypuzzle.org/sliding for a refresher of the rules of the game. You will implement and compare several search algorithms and collect some statistics related to their performances. Please read all sections of the instructions carefully:

**I. Introduction**

An instance of the N-puzzle game consists of a board holding N = m^2 − 1 (m = 3, 4, 5, ...) distinct movable tiles, plus an empty space. The tiles are numbers from the set {1, …, m^2 − 1}. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this assignment, we will represent the blank space with the number 0 and focus on the m = 3 case (8-puzzle).

Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order ⟨0, 1, …, m^2 − 1⟩. The search space is the set of all possible states reachable from the initial state.

The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time. The cost of moving from one configuration of the board to another is the same and equal to one. Thus, the total cost of path is equal to the number of moves made from the initial state to the goal state.


----------


**II. Algorithm Review**

Recall from the lectures that searches begin by visiting the root node of the search tree, given by the initial state. Among other book-keeping details, three major things happen in sequence in order to visit a node:
First, we remove a node from the frontier set.
Second, we check the state against the goal state to determine if a solution has been found.
Finally, if the result of the check is negative, we then expand the node. To expand a given node, we generate successor nodes adjacent to the current node, and add them to the frontier set. Note that if these successor nodes are already in the frontier, or have already been visited, then they should not be added to the frontier again.

This describes the life-cycle of a visit, and is the basic order of operations for search agents in this assignment—(1) remove, (2) check, and (3) expand. In this assignment, we will implement algorithms as described here. Please refer to lecture notes for further details, and review the lecture pseudocode before you begin the assignment.
IMPORTANT: Note that you may encounter implementations elsewhere that attempt to short-circuit this order by performing the goal-check on successor nodes immediately upon expansion of a parent node. For example, Russell & Norvig's implementation of breadth-first search does precisely this. Doing so may lead to edge-case gains in efficiency, but do not alter the general characteristics of complexity and optimality for each method. For simplicity and grading purposes in this assignment, do not make such modifications to algorithms learned in lecture.


----------


**IV. What Your Program Outputs**

When executed, your program will create / write to a file called output.txt, containing the following statistics:

**path_to_goal:** the sequence of moves taken to reach the goal

**cost_of_path:** the number of moves taken to reach the goal

**nodes_expanded:** the number of nodes that have been expanded

**search_depth:** the depth within the search tree when the goal node is found

**max_search_depth:**  the maximum depth of the search tree in the lifetime of the algorithm

**running_time:** the total running time of the search instance, reported in seconds

**max_ram_usage:** the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes


----------


**Example #1: Breadth-First Search**

Suppose the program is executed for breadth-first search as follows:
$ python driver.py bfs 1,2,5,3,4,0,6,7,8
Which should lead to the following solution to the input board:

![](https://studio.edx.org/asset-v1:ColumbiaX+CSMM.101x+1T2017+type@asset+block@pset1_diagram.png)

The output file (example) will contain exactly the following lines:
path_to_goal: ['Up', 'Left', 'Left']
cost_of_path: 3
nodes_expanded: 10
search_depth: 3
max_search_depth: 4
running_time: 0.00188088
max_ram_usage: 0.07812500

**Example #2: Depth-First Search**

Suppose the program is executed for depth-first search as follows:
$ python driver.py dfs 1,2,5,3,4,0,6,7,8
Which should lead to the following solution to the input board:


The output file (example) will contain exactly the following lines:
path_to_goal: ['Up', 'Left', 'Left']
cost_of_path: 3
nodes_expanded: 181437
search_depth: 3
max_search_depth: 66125
running_time: 5.01608433
max_ram_usage: 4.23940217


----------


**V. Important Information**

Please read the following information carefully. Since this is the first programming project, we are providing many hints and explicit instructions. Before you post a clarifying question on the discussion board, make sure that your question is not already answered in the following sections.

1. Implementation
You will implement the following three algorithms as demonstrated in lecture. In particular:
Breadth-First Search. Use an explicit queue, as shown in lecture.
Depth-First Search. Use an explicit stack, as shown in lecture.
A-Star Search. Use a priority queue, as shown in lecture. For the choice of heuristic, use the Manhattan priority function; that is, the sum of the distances of the tiles from their goal positions. Note that the blanks space is not considered an actual tile here.

2. Order of Visits
In this assignment, where an arbitrary choice must be made, we always visit child nodes in the "UDLR" order; that is, [‘Up’, ‘Down’, ‘Left’, ‘Right’] in that exact order. Specifically:
Breadth-First Search. Enqueue in UDLR order; dequeuing results in UDLR order.
Depth-First Search. Push onto the stack in reverse-UDLR order; popping off results in UDLR order.
A-Star Search. Since you are using a priority queue, what happens when there are duplicate keys? What do you need to do to ensure that nodes are retrieved from the priority queue in the desired order?