from utils import read_input, write_output


# iterative deepening
def ids(target: int, vertex_vals: dict, adj: dict) -> list:

    vertices = list(adj.keys())  # get all vertices in the graph

    # add root to the graph and set value to 0
    vertex_vals["root"] = 0
    adj["root"] = []

    # keep track of states
    logs = []

    # Depth-First Search
    def dfs(src: str, trg: int, depth: int, path: list) -> bool:
        # Base cases
        if vertex_vals[src] >= trg:
            return True
        if depth <= 0:
            return False

        # vertices should not be chose
        neighbors = adj[src].copy()
        neighbors += path
        for pre_v in path:
            neighbors += adj[pre_v]
        # vertices to be chose
        choices = sorted(list(set(vertices).difference(set(neighbors))))

        for v in choices:
            # v should be alphabetically later than the vertices in path
            if len(path) > 0 and ord(v) <= ord(path[-1]):
                continue

            # log the current state
            path_cp = path.copy()
            path_cp.append(v)
            cur_vals = sum(vertex_vals[each] for each in path_cp)
            logs.append(" ".join(path_cp) + f" Value={cur_vals}.\n")

            if dfs(v, trg - vertex_vals[src], depth - 1, path_cp):
                return True

        return False

    i = 1  # count the depth
    pre_states = None  # num of depth K-1 states
    cur_states = 0  # num of depth K states

    # Stop if none of the states at depth K-1 have any successors
    while pre_states != cur_states:

        pre_logs = len(logs)  # num of states before depth K
        logs.append(f"Depth={i}.\n")  # log current depth

        # Find solution
        if dfs("root", target, i, []):
            logs.append("\nFound solution " + logs[-1][:-1] + "\n")
            return logs
        i += 1
        logs.append("\n")

        # update the num of states
        pre_states = cur_states
        cur_states = len(logs) - pre_logs

    # No solution found
    logs.append("No solution found\n")
    return logs


if __name__ == "__main__":
    first_line, vertex_vals, adj = read_input()  # read input.txt
    logs = ids(int(first_line[0]), vertex_vals, adj)  # get all states

    if first_line[1] == "V":  # verbose
        write_output(logs, True)
    else:
        write_output(logs)
