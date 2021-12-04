class Graph:
    def __init__(self,gdict=None) -> None:
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        # a list of visited vertices, so as not to go on infinite loop
        visited=[vertex]
        queue=[vertex]
        while queue:
            deVertex=queue.pop(0)
            print(deVertex)
            for adjVertex in self.gdict[deVertex]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    queue.append(adjVertex)


    def dfs(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            popVertex=stack.pop()
            print(popVertex)
            for adjVertex in self.gdict[popVertex]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    stack.append(adjVertex)


customDict={"a":["b","c"],
            "b":["a","d","e"],
            "c":["a","e"],
            "d":["b","e","f"],
            "e":["d","f"],
            "f":["d","e"]
            }

graph=Graph(customDict)
graph.addEdge("e","c")
print(graph.gdict)
graph.bfs("a")
print("dfs:")
graph.dfs("a")