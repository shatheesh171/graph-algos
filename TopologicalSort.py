from collections import defaultdict

class Graph:
    def __init__(self,numberOfVertices) -> None:
        self.graph=defaultdict(list)
        self.numberOfVertices=numberOfVertices

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self,v,visited,stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)

        stack.insert(0,v)

    def topologicalSort(self):
        visited=[]
        stack=[]

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k,visited,stack)

        print(stack)


customGraph=Graph(8)
customGraph.addEdge("a","c")
customGraph.addEdge("c","e")
customGraph.addEdge("e","h")
customGraph.addEdge("e","f")
customGraph.addEdge("f","g")
customGraph.addEdge("b","d")
customGraph.addEdge("b","c")
customGraph.addEdge("d","f")

customGraph.topologicalSort()