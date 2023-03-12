# -*- coding: UTF-8 -*-

# Breadth first search: directed graph

# 散列表（字典）实现广度优先搜索（用于非加权图），不适合带权重的路径搜索问题（cost仅为路段数）

graph = {} # create empty dict
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

graph["a"] = ["b"]
graph["b"] = ["a"]

from collections import deque # 创建python队列

def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] # put searched name in a list, in case of unlimited cycling like a <-> b

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
        
def person_is_seller(name):
    return name[-1] == 'm'

if __name__ == '__main__':
    breadth_first_search("you")
    print(breadth_first_search("a")) # 返回的布尔值不会输出，除非print