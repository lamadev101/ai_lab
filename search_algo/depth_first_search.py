class DFS:
    def __init__(self, routes):
        self.routes = routes

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.routes:
            return []

        paths = []
        for node in self.routes[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.routes:
            return None

        shortest_path = None
        for node in self.routes[start]:
            if node not in path:
                sp = self.get_shortest_paths(node, end, path)
                # if sp:
                for i in range(len(sp)):
                    if shortest_path is None or len(sp[i]) < len(shortest_path[i]):
                        shortest_path = sp
        return shortest_path

if __name__=='__main__':
    graphs = {
        1:[2,3],
        2:[4,6,8],
        3:[4],
        4:[5,7],
        5:[7,8],
        6:[7],
        7:[8]
    }
    route_graph = DFS(graphs)
    st=1
    en = 8

    print(f"All paths between: {st} and {en}:", route_graph.get_paths(st,en))
    print(f"Shorest paths between: {st} and {en}:", route_graph.get_shortest_paths(st, en))
