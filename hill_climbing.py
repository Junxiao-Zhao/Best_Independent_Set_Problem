from utils import read_input, write_output
from random import randint


# generate random starting point
def random_start(adj: dict) -> list:
    cur_state = []
    for v in adj.keys():
        if randint(0, 1):
            cur_state.append(v)

    return cur_state


# calculate the cose
def cost(vertex_vals: dict, u: str, v: str) -> int:
    return min(vertex_vals[u], vertex_vals[v])


# calculate the error
def error(adj: dict, vertex_vals: dict, state: list, trg: int) -> int:
    err1 = max(0, trg - sum(vertex_vals[i] for i in state))
    err2 = 0

    for key in state:
        for v in adj[key]:
            if v in state:
                err2 += cost(vertex_vals, key, v)

    return int(err1 + err2 / 2)


def hill_climbing(target: int, vertex_vals: dict, adj: dict, cur_state: list) -> list:
    logs = []

    # calcuate error and value
    cur_err = error(adj, vertex_vals, cur_state, target)
    cur_val = sum(vertex_vals[i] for i in cur_state)

    # log the state
    str_state = " ".join(cur_state)
    logs.append("Randomly chosen start state: " + str_state + "\n")
    logs.append(str_state + f" Value={cur_val}. Error={cur_err}.\n")

    store = dict()  # store previous states

    # set minimum record
    min_state_err = float("inf")
    min_err_state = []
    min_state_val = 0

    while True:
        logs.append("Neighbors:\n")  # start log neighbors

        for v in adj.keys():
            add_back = False

            # modify the state to its neighbors
            if v in cur_state:
                cur_state.remove(v)
                add_back = True
            else:
                cur_state.append(v)
            cur_state.sort()

            str_state = " ".join(cur_state)
            # if not visited
            if store.setdefault(str_state, True):
                store[str_state] = False  # mark as visited
                # calculate this neighbor's error and value
                neigh_err = error(adj, vertex_vals, cur_state, target)
                neigh_val = sum(vertex_vals[i] for i in cur_state)

                if str_state == "":  # empty set
                    logs.append("{} Value=0. Error=18.\n")
                else:
                    logs.append(str_state + f" Value={neigh_val}. Error={neigh_err}.\n")

                # update minimum
                if min_state_err > neigh_err:
                    min_state_err = neigh_err
                    min_err_state = cur_state.copy()
                    min_state_val = neigh_val

                # Found solution
                if min_state_err == 0:
                    logs.append("\n")
                    logs.append(
                        "Found solution "
                        + " ".join(min_err_state)
                        + f" Value={target}. Error={min_state_err}.\n"
                    )
                    return logs

            # restore the state
            if add_back:
                cur_state.append(v)
            else:
                cur_state.remove(v)

        # Search failed
        if min_state_err >= cur_err:
            logs.append("\n")
            logs.append("Search failed\n\n")
            return logs

        cur_state = min_err_state
        cur_err = min_state_err
        logs.append(
            "\nMove to "
            + " ".join(cur_state)
            + f" Value={min_state_val}. Error={cur_err}.\n"
        )


if __name__ == "__main__":
    first_line, vertex_vals, adj = read_input()  # read input.txt
    logs = []
    store_start = dict()

    i = 0
    while i < int(first_line[2]):
        cur_state = random_start(adj)
        str_cur = " ".join(cur_state)

        # avoid same start point
        if store_start.setdefault(str_cur, True):
            store_start[str_cur] = False
            logs += hill_climbing(int(first_line[0]), vertex_vals, adj, cur_state)
            # found
            if logs[-1][:5] == "Found":
                break
            i += 1

    if first_line[1] == "V":  # verbose
        write_output(logs, True)
    else:
        write_output(logs)
