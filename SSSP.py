#Single source shortest path

class Graph:
    def __init__(self,gdict=None) -> None:
        self.gdict=gdict

    def bfs(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            path=queue.pop(0)
            #print(path)
            node=path[-1]
            #print(node)
            # reached shortest path
            if node==end:
                return path
            for adjacent in self.gdict.get(node,[]):
                new_path=list(path)
                #print("new_path: ",new_path)
                new_path.append(adjacent)
                queue.append(new_path)
                #print("queue: ",queue)


customDict={"a":["b","c"],
            "b":["d","g"],
            "c":["d","e"],
            "d":["f"],
            "e":["f"],
            "g":["f"]
}

g=Graph(customDict)
print(g.bfs("a","c"))
