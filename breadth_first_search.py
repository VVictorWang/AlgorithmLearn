from collections import deque


def bfs_search(graph, target):
    search_queue = deque()
    search_queue += graph[target]
    searched = []
    while search_queue:
        src = search_queue.popleft()
        if not src in searched:
            if src_is_found(src):
                print(src + " is Found")
                return True
            else:
                search_queue += graph[src]
                searched.append(src)
    return False


def src_is_found(src):
    return src[len(src) - 1] == 's'


graph = {}
graph["me"] = ["Bob", "Milis", "Hello"]
graph["Bob"] = ["Linda"]
graph["Linda"] = []
graph["Milis"] = []
graph["Hello"] = []

bfs_search(graph, "me")
