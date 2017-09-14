graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["final"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["final"] = 5

graph["final"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["final"] = infinity

parents = {}
parents["start"] = None
parents["a"] = "start"
parents["b"] = "start"
parents["final"] = None

procecced = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if lowest_cost > cost and node not in procecced:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        procecced.append(node)
        node = find_lowest_cost_node(costs)


dijkstra()
print(costs)
routes = []
temp = "final"
while temp is not None:
    routes.append(temp)
    temp = parents[temp]

while routes:
    print(routes.pop() + "---->")
