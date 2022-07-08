class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def topo_sort(ch, topo_order, visited, visited_curr):
            visited.add(ch)
            visited_curr.add(ch)
            for nbr in graph[ch]:
                if nbr in visited_curr:
                    return False
                elif nbr not in visited:
                    if not topo_sort(nbr, topo_order, visited, visited_curr):
                        return False
            topo_order.append(ch)
            visited_curr.remove(ch)
            return True
        
        graph = { ch: set() for word in words for ch in word }
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        topo_order, visited, visited_curr = [], set(), set()
        for ch in graph:
            if ch not in visited:
                if not topo_sort(ch, topo_order, visited, visited_curr):
                    return ''
        return ''.join(reversed(topo_order))