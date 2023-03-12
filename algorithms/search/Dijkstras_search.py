# 狄克斯特拉算法：三个散列表（字典）———— graph, costs, parents
# 狄克斯特拉算法用于在加权图中查找最短路径，仅当权重为正时狄克斯特拉算法才管用
# 若图中含负权边，使用贝尔曼-福德算法

# graph

graph = {} # initialize

graph["start"] = {}
graph["start"]["a"] = 6 # store costs
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["finish"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5

graph["finish"] = {} # finish node has no neighbours

# print(graph)

# costs
# 节点的开销表示从起点出发到该节点需要多少时间

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity

# parents
# 存储父节点的散列表

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

# 记录处理过的节点，避免重复

processed = []

# 开始程序

def find_lowest_cost_node(costs): # 同一程序中函数定义必须在执行之前
    lowest_cost = float("inf") # numpy, math等库有不同的表示
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 避免重复，加入已处理列表
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # node为未处理节点中代价最小的
while node is not None:
    cost = costs[node]
    neighbours = graph[node] # 取出node节点的所有相邻节点
    for n in neighbours.keys():
        new_cost = cost + neighbours[n] # 新代价为到达node节点当前的最小代价 + node到n的代价
        if costs[n] > new_cost: # 若经其他节点到n节点的新代价比原cost低，则:
            costs[n] = new_cost # 更新n节点cost
            parents[n] = node # 并将n节点的父节点更新为node节点
    processed.append(node) # 处理完所有node相邻节点后将node放入已处理的列表，下一步寻找不再包括node
    node = find_lowest_cost_node(costs)

print(costs["finish"])


