class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        edgeMap = {i: [] for i in range(n)}

        for parent, child in edges:
            edgeMap[parent].append(child)
            edgeMap[child].append(parent)

        visited = set()

        def dfs(edge, parent):
            if edge in visited:
                return False
            visited.add(edge)

            if edgeMap[edge] == []:
                return True

            for node in edgeMap[edge]:
                if node != parent:
                    if not dfs(node, edge):
                        return False
                    
            return True
        
        if dfs(0, -1):
            return len(visited) == n
        return False
