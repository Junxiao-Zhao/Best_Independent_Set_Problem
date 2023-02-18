# Best Independent Set problem
## Solving by iterative deepening and hill climbing with random restart

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
