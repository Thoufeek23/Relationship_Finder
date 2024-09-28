import heapq

class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph[node] = []

    def add_edge(self, node1, node2, weight):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append((node2, weight))
            self.graph[node2].append((node1, weight))  

    def find_min_distances(self, start_node):
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0

        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


weighted_graph = WeightedGraph()


nodes = ["ali", "farzana", "shafeek", "thoufeek", "rahmathali", "kareema", "minnathullah", "nasira", "wasif", "sajidha", "riyaz", "lathifa", "asim", "noor", "fazlina", "sharief", "saliha"]
for node in nodes:
    weighted_graph.add_node(node)


weighted_graph.add_edge("ali", "farzana", 1)
weighted_graph.add_edge("ali", "shafeek", 2)
weighted_graph.add_edge("ali", "thoufeek", 2)
weighted_graph.add_edge("farzana", "shafeek", 2)
weighted_graph.add_edge("farzana", "thoufeek", 2)
weighted_graph.add_edge("shafeek", "thoufeek", 4)
weighted_graph.add_edge("farzana", "rahmathali", 2)
weighted_graph.add_edge("farzana", "kareema", 2)
weighted_graph.add_edge("rahmathali", "kareema", 1)
weighted_graph.add_edge("minnathullah", "nasira", 1)
weighted_graph.add_edge("wasif", "sajidha", 4)
weighted_graph.add_edge("wasif", "minnathullah", 2)
weighted_graph.add_edge("wasif", "nasira", 2)
weighted_graph.add_edge("sajidha", "nasira", 2)
weighted_graph.add_edge("sajidha", "minnathullah", 2)
weighted_graph.add_edge("rahmathali", "minnathullah", 2)
weighted_graph.add_edge("kareema", "minnathullah", 2)
weighted_graph.add_edge("riyaz", "lathifa", 1)
weighted_graph.add_edge("riyaz", "asim", 2)
weighted_graph.add_edge("asim", "lathifa", 2)
weighted_graph.add_edge("riyaz", "rahmathali", 2)
weighted_graph.add_edge("riyaz", "kareema", 2)
weighted_graph.add_edge("noor", "fazlina", 1)
weighted_graph.add_edge("noor", "sharief", 2)
weighted_graph.add_edge("noor", "saliha", 2)
weighted_graph.add_edge("sharief", "fazlina", 2)
weighted_graph.add_edge("saliha", "fazlina", 2)
weighted_graph.add_edge("sharief", "saliha", 4)
weighted_graph.add_edge("rahmathali", "fazlina", 2)
weighted_graph.add_edge("kareema", "fazlina", 2)
weighted_graph.add_edge("farzana", "fazlina", 4)
weighted_graph.add_edge("riyaz", "fazlina", 4)
weighted_graph.add_edge("minnathullah", "fazlina", 4)
weighted_graph.add_edge("riyaz", "farzana", 4)
weighted_graph.add_edge("minnathullah", "farzana", 4)
weighted_graph.add_edge("riyaz", "minnathullah", 4)





m = ["ali", "shafeek", "thoufeek", "rahmathali", "minnathullah", "wasif","riyaz","asim", "noor", "sharief"]
f = ["farzana", "kareema", "nasira", "sajidha", "lathifa", "fazlina", "saliha"]


a = ["rahmathali", "kareema"]
b = ["ali", "farzana", "minnathullah", "nasira", "riyaz","lathifa", "noor", "fazlina"]
c = ["shafeek", "thoufeek","wasif", "sajidha", "asim" , "sharief", "saliha"]


print("********** RELATIONSHIP FINDER **********")
start_node = input("Person 1 : ")
end_node = input("Person 2 : ")

print(start_node)

if (start_node in m or end_node in m) or (start_node in f or end_node in f) or (start_node in b or end_node in b) or (start_node in c or end_node in c):
    min_distances = weighted_graph.find_min_distances(start_node)
    if end_node in min_distances:
        min_distance = min_distances[end_node]
        if min_distance == 1:
            if start_node in m:
                print(f"{end_node} is the wife of {start_node}.")
            elif start_node in f:
                print(f"{end_node} is the husband of {start_node}.")
        elif min_distance == 2:
            if end_node in m:
                if (start_node in c and end_node in b) or (start_node in b and end_node in a):
                    print(f"{end_node} is the father of {start_node}.")
                elif (start_node in b and end_node in c) or (start_node in a and end_node in b):
                    print(f"{end_node} is the son of {start_node}.")
            elif end_node in f:
                if (start_node in c and end_node in b) or (start_node in b and end_node in a):
                    print(f"{end_node} is the mother of {start_node}.")
                elif (start_node in b and end_node in c) or (start_node in a and end_node in b):
                    print(f"{end_node} is the daughter of {start_node}.")
        elif min_distance == 3:
            if end_node in m:
                if (start_node in b and end_node in a):
                    print(f"{end_node} is the father-in-law of {start_node}.")
                elif (start_node in a and end_node in b):
                        print(f"{end_node} is the son-in-law of {start_node}.")
            elif end_node in f:
                if (start_node in b and end_node in a):
                    print(f"{end_node} is the mother-in-law of {start_node}.")
                elif (start_node in a and end_node in b):
                    print(f"{end_node} is the daughter-in-law of {start_node}.")
        elif min_distance == 4:
            if end_node in m :
                if (start_node in c and end_node in c) or (start_node in b and end_node in b):
                    print(f"{end_node} is the brother of {start_node}.")
                elif (start_node in a and end_node in c):
                    print(f"{end_node} is the grandson of {start_node}.")
                elif (start_node in c and end_node in a):
                    print(f"{end_node} is the grandfather of {start_node}.")
            elif end_node in f:
                if (start_node in c and end_node in c) or (start_node in b and end_node in b):
                    print(f"{end_node} is the sister of {start_node}.")
                elif (start_node in a and end_node in c):
                    print(f"{end_node} is the granddaughter of {start_node}.")
                elif (start_node in c and end_node in a):
                    print(f"{end_node} is the grandmother of {start_node}.")
        elif min_distance == 6:
            if end_node in m:
                if (start_node in c and end_node in b):
                    print(f"{end_node} is the uncle of {start_node}.")
                elif (start_node in b and end_node in c):
                    print(f"{end_node} is the nephew of {start_node}.")
                elif (start_node in b and end_node in b):
                    print(f"{end_node} is the brother of {start_node}.")
            elif end_node in f:
                if (start_node in c and end_node in b):
                    print(f"{end_node} is the aunt of {start_node}.")
                elif (start_node in b and end_node in c):
                    print(f"{end_node} is the niece of {start_node}.")
                elif (start_node in b and end_node in b):
                    print(f"{end_node} is the sister of {start_node}.")
        elif min_distance == 7:
            if end_node in m:
                if(start_node in c and end_node in b):
                    print(f"{end_node} is the uncle of {start_node}.")
                elif (start_node in b and end_node in c):
                    print(f"{end_node} is the nephew of {start_node}.")
            if end_node in f:
                if (start_node in c and end_node in b):
                    print(f"{end_node} is the aunt of {start_node}.")
                elif (start_node in b and end_node in c):
                    print(f"{end_node} is the niece of {start_node}.")
        elif min_distance == 8:
            print(f"{end_node} is the cousin of {start_node}.")
    else:
        print(f"End node {end_node} not reachable from the start node {start_node}.")
else:
    print("Start and end nodes should belong to either list 'm', 'f', 'b', or 'c'.")