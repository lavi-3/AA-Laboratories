import random
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

# Define the number of nodes
num_nodes = random.randint(8, 15)

# Create the balanced tree
balanced_tree = nx.balanced_tree(2, int(num_nodes/2)-1)

# Create the unbalanced tree
unbalanced_tree = nx.DiGraph()
unbalanced_tree.add_node(0)
for i in range(1, num_nodes):
    parent = random.randint(0, i-1)
    unbalanced_tree.add_edge(parent, i)

# Draw the trees side by side
fig, axs = plt.subplots(ncols=2, figsize=(10, 5))
nx.draw(balanced_tree, with_labels=True, ax=axs[0])
axs[0].set_title('Balanced Binary Tree')
nx.draw(unbalanced_tree, with_labels=True, ax=axs[1])
axs[1].set_title('Unbalanced Binary Tree')
plt.show()


# create a bfs function for the balanced tree
def bfs_balanced_tree(balanced_tree, start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(balanced_tree[vertex]) - set(visited))
    return visited


# create a bfs function for the unbalanced tree
def bfs_unbalanced_tree(unbalanced_tree, start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(unbalanced_tree[vertex]) - set(visited))
    return visited


# create a dfs function for the balanced tree
def dfs_balanced_tree(balanced_tree, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(balanced_tree[vertex]) - set(visited))
    return visited


# create a dfs function for the unbalanced tree
def dfs_unbalanced_tree(unbalanced_tree, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(unbalanced_tree[vertex]) - set(visited))
    return visited


# create a function that calculates the time complexity of the bfs function for the balanced tree
def time_complexity_bfs_balanced_tree(balanced_tree, start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(balanced_tree[vertex]) - set(visited))
    return len(visited)


# create a function that calculates the time complexity of the bfs function for the unbalanced tree

def time_complexity_bfs_unbalanced_tree(unbalanced_tree, start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(unbalanced_tree[vertex]) - set(visited))
    return len(visited)


# create a function that calculates the time complexity of the dfs function for the balanced tree
def time_complexity_dfs_balanced_tree(balanced_tree, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(balanced_tree[vertex]) - set(visited))
    return len(visited)


# create a function that calculates the time complexity of the dfs function for the unbalanced tree
def time_complexity_dfs_unbalanced_tree(unbalanced_tree, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(unbalanced_tree[vertex]) - set(visited))
    return len(visited)


# Define the starting node
start_node = 0

# Calculate the time complexities
bfs_balanced_time = time_complexity_bfs_balanced_tree(balanced_tree, start_node)
bfs_unbalanced_time = time_complexity_bfs_unbalanced_tree(unbalanced_tree, start_node)
dfs_balanced_time = time_complexity_dfs_balanced_tree(balanced_tree, start_node)
dfs_unbalanced_time = time_complexity_dfs_unbalanced_tree(unbalanced_tree, start_node)

# Create a bar chart to display the time complexities
x_labels = ['BFS Balanced', 'BFS Unbalanced', 'DFS Balanced', 'DFS Unbalanced']
y_values = [bfs_balanced_time, bfs_unbalanced_time, dfs_balanced_time, dfs_unbalanced_time]
plt.bar(x_labels, y_values)
plt.title('Time Complexities of BFS and DFS Functions')
plt.ylabel('Time Complexity')
plt.show()
