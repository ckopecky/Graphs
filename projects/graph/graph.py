"""
Simple graph implementation
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex, edges=()):
        """
        Add a vertex to the graph.
        """
        if vertex in self.vertices:
            raise Exception("Error: vertex already exists!")
        self.vertices[vertex] = set(edges)

    def add_edge(self, startVertex, endVertex, bidirectional=False):

        """
        Add a directed edge to the graph. directed == one direction
        """
        if startVertex not in self.vertices or endVertex not in self.vertices:
            raise Exception("supplied a vertex not in graph!")
        self.vertices[startVertex].add(endVertex)
        if bidirectional:
            self.vertices[endVertex].add(startVertex)
        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        #create q
        queue = []
        #keep track of explored
        visited = set()

        #add starting vert to queue

        queue.append(starting_vertex)

        while queue:
            current = queue.pop(0)
            visited.add(current)
            queue.extend(self.vertices[current] - visited)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        stack = []

        stack.append(starting_vertex)

        visited = set()

        while stack:
            current = stack.pop()
            visited.add(current)
            stack.extend(self.vertices[current] - visited)
        return visited

    
    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        visited.add(starting_vertex)
        print(starting_vertex)

        for child in self.vertices[starting_vertex]:
            if child not in visited:
                self.dft_recursive(child, visited)

        return visited





    def bfs(self, starting_vertex, destination_vertex):
        
        #instantiate a queue

        q = []
        #add start vertex
        q.append(starting_vertex)

        #instantiate a visited set

        visited = set()

        while len(q) > 0:
            vertex = q.pop(0)
            if vertex not in visited:
                if vertex == destination_vertex:
                    return True
                visited.add(vertex)
                for child in self.vertices[vertex]:
                    q.append(child)

    def bfs_shortest_path(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        #instantiate q

        q = []
        q.append([starting_vertex]) 
        #we encapsulate this in a list so that we can keep track of paths
        visited = set()

        while len(q) > 0: 
            #pop the front of the queue
            path = q.pop(0)
            #path is an array of vertexes. If the last element matches the destination element, we have found our target. If not, we add it to the 
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for child in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(child)
                    q.append(new_path)
        return None
            
        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = []
        stack.append([starting_vertex])
        visited = set()
        while len(stack) > 0:
            path = stack.pop()
            print("path", path)
            vertex = path[-1]
            print("vert", vertex)
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
            
                visited.add(vertex)
                print("visited", visited)
                for child in self.vertices[vertex]:
                    new_path = list(path)
                    print("new", new_path)
                    new_path.append(child)
                    stack.append(new_path)
                    print(stack)
        return None

    def print(self):
        print(self)




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print(graph.dft(1))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # print(graph.bft(1))

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print("recursive", graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6), "bfs")
    # print(graph.bfs_shortest_path(1, 6), "shortest")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6), "dfs")
