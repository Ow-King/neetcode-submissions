class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = {i: [] for i in range(n)}
        for parent, child in edges:
            edgeMap[parent].append(child)
            edgeMap[child].append(parent)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return

            visited.add(node)
            
            children = edgeMap[node]

            if children == []:
                return
            
            for child in children:
                if child is not parent:
                    dfs(child, node)
            
            return

        components = 0

        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i, -1)
        
        return components
