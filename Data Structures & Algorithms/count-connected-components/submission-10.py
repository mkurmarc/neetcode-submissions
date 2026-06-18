class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = [ i for i in range(n) ]  # [0,0,2,3,4]
        # sizes = [ 0 for i in range(len(n))]  # [0,0,0,0,0]

        for node_a, node_b in edges: # 0,1
            self.union(node_a, node_b, roots)

        count = 0
        for i in range(len(roots)):
            if roots[i] == i:
                count += 1
        return count

    def union(self, node_a, node_b, roots):
        root_a = self.find(node_b, roots)
        root_b = self.find(node_a, roots)
        roots[root_b] = root_a


    def find(self, node, roots):
        if node == roots[node]:
            return node
        
        return self.find(roots[node], roots)

