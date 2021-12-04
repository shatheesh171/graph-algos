from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.nodes=set()
        self.edges=defaultdict(list)
        self.distances={}

    def addNode(self,value):
        self.nodes.add(value)

    def addEdge(self,fromNode,toNode,distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode,toNode)]=distance

def dijkstra(graph,initial):
    visited={initial:0}
    path=defaultdict(list)

    nodes=graph.nodes
    #print(nodes)
    while nodes:
        minNode=None
        for node in nodes:
            #print("Node: ",node)
            #print("MinNode: ",minNode)
            if node in visited:
                if minNode is None:
                    minNode=node
                elif visited[node]<visited[minNode]:
                    minNode=node

        #If inital value is not in graph vertex at all
        if minNode is None:
            #print("Comes here")
            break

        nodes.remove(minNode)
        #print(nodes)
        currentWeight=visited[minNode]
        #print(minNode,currentWeight)
        for edge in graph.edges[minNode]:
            weight=currentWeight+graph.distances[(minNode,edge)]
            
            if edge not in visited or weight<visited[edge]:
                visited[edge]=weight
                path[edge].append(minNode)

    return visited,path



customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

print(dijkstra(customGraph, "A"))
#print(customGraph.edges)