# Best Independent Set problem
## Solving by iterative deepening and hill climbing with random restart

###  The “Best Independent Set” problem
- Input: An undirected graph G, in which each vertex is marked by a positive value ;
and a target value T.
- Goal: A set of vertices S such that 
  - no two vertices in S are connected by an edge
in G; and 
  - the total value of the vertices in S is at least T.

### Input
Input should be a text file named "input.txt" in the same working directory as the code with the following contents:
- Line 1: The target (a positive integer) and flags: "V" for verbose output or "C" for compact output. For the hill-climbing program, the number of random restarts to run.
- Each vertex. Name (you may assume that this is a single alphabetic character) and value (a positive integer), 1 per line.
- Blank line
- Each edge: the names of the two ends. 1 per line.

Example: [input.txt](./input.txt)

### Output
The program should print out to standard output:
- If a solution is found, the solution (just a sequence of vertices).
- If no solution is found, then "No solution found"
- If the "verbose" flag is set then a trace of the search sequence.

Example: 
  - iterative deepening: [iterativeDeepening_output.txt](iterativeDeepening_output.txt)
  - hill climbing: [hillClimbing_output.txt](./hillClimbing_output.txt)
