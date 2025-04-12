class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        if dest not in self.adj_list[src]:
            self.adj_list[src].append(dest)
        if src not in self.adj_list[dest]:
            self.adj_list[dest].append(src)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                if vertex in self.adj_list[neighbor]:
                    self.adj_list[neighbor].remove(vertex)
            del self.adj_list[vertex]

    def remove_edge(self, src, dest):
        if src in self.adj_list and dest in self.adj_list[src]:
            self.adj_list[src].remove(dest)
        if dest in self.adj_list and src in self.adj_list[dest]:
            self.adj_list[dest].remove(src)

    def has_edge(self, src, dest):
        return src in self.adj_list and dest in self.adj_list[src]

    def get_vertices(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                if (neighbor, vertex) not in edges:
                    edges.append((vertex, neighbor))
        return edges

    def dfs(self, start, visited=None):
        if start not in self.adj_list:
            return []
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]
        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        return result

    def bfs(self, start):
        if start not in self.adj_list:
            return []
        visited = set()
        queue = [start]
        result = []
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([n for n in self.adj_list[vertex] if n not in visited])
        return result

    def has_cycle_util(self, v, visited, parent):
        visited.add(v)
        for neighbor in self.adj_list[v]:
            if neighbor not in visited:
                if self.has_cycle_util(neighbor, visited, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    def has_cycle(self):
        visited = set()
        for vertex in self.adj_list:
            if vertex not in visited:
                if self.has_cycle_util(vertex, visited, None):
                    return True
        return False

    def count_components(self):
        visited = set()
        count = 0
        for vertex in self.adj_list:
            if vertex not in visited:
                self.dfs(vertex, visited)
                count += 1
        return count

    def display(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])
