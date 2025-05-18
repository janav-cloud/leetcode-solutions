
class Solution:
    

  def cloneGraph(self, node):
      if not node:
          return None

      visited = {}
      queue = deque([node])

      # Create a copy of the starting node and add it to visited
      visited[node] = Node(node.val)

      while queue:
          # Get the next node from the queue
          curr_node = queue.popleft()

          # Loop through the current node's neighbors
          for neighbor in curr_node.neighbors:
              if neighbor not in visited:
                  # Create a copy of the neighbor and add it to visited
                  visited[neighbor] = Node(neighbor.val)
                  queue.append(neighbor)

              # Add the copy of the neighbor to the copy of the current node's neighbors
              visited[curr_node].neighbors.append(visited[neighbor])

      return visited[node]