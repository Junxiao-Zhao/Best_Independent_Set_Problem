from collections import defaultdict


# Read input.txt
def read_input() -> set:
    try:
        f = open("input.txt", "r", encoding="utf-8-sig")
        contents = f.readlines()
        f.close()

    except Exception as e:
        print(e)
        return None

    # includes target, verbose, and num of random if hillclimbing
    first_line = contents[0].strip("\n").split(" ")

    vertex_vals = dict()  # store names and values
    adj = defaultdict(list)  # store edges as adjacent list

    switch = False
    for line in contents[1:]:
        line = line.strip("\n").split(" ")

        # blank line
        if line[0] == "":
            switch = True
            continue

        # The vertex name & value
        if not switch:
            vertex_vals[line[0]] = int(line[1])
        # The edges
        else:
            adj[line[0]].append(line[1])
            adj[line[1]].append(line[0])

    return (first_line, vertex_vals, dict(adj))


# write output.txt
def write_output(logs: list, verbose: bool = False):
    try:
        f = open("output.txt", "w", encoding="utf-8-sig")

        if verbose:  # write all states
            f.writelines(logs)
        else:  # only write result
            f.write(logs[-1])

        f.close()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    print(read_input())
