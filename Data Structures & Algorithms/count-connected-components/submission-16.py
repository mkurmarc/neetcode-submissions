class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = [ i for i in range(n) ]  # [0,0,2,3,4]
        sizes = [ 1 for i in range(n) ]  # [1,1,1,1,1]

        for node_a, node_b in edges: # 0,1
            self.union(node_a, node_b, roots, sizes)

        count = 0
        for i in range(len(roots)):
            if roots[i] == i:
                count += 1
        return count

    def union(self, node_a, node_b, roots, sizes):
        root_a = self.find(node_b, roots)
        root_b = self.find(node_a, roots)

        if root_a == root_b:
            return

        if sizes[root_a] >= sizes[root_b]:
            roots[root_b] = root_a
            sizes[root_a] += sizes[root_b]
        else:
            roots[root_a] = root_b
            sizes[root_b] += sizes[root_a]


    def find(self, node, roots):
        if node == roots[node]:
            return node

        found = self.find(roots[node], roots)
        roots[node] = found
        return found

