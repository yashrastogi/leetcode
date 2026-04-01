from pprint import pprint


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        m = {}
        adj = defaultdict(list)
        for ac in accounts:
            for i in range(1, len(ac)):
                if ac[i] not in adj:
                    adj[ac[i]] = []
                for j in range(i + 1, len(ac)):
                    adj[ac[i]].append(ac[j])
                m[ac[i]] = ac[0]

        parent = {p: p for p in adj}
        rank = {p: 0 for p in adj}

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            p_u = find(u)
            p_v = find(v)
            if p_u == p_v:
                return False  # already connected
            if rank[p_u] < rank[p_v]:
                parent[p_u] = p_v
            elif rank[p_u] > rank[p_v]:
                parent[p_v] = p_u
            else:
                parent[p_v] = p_u
                rank[p_u] += 1
            return True

        for e1 in adj:
            for e2 in adj[e1]:
                union(e1, e2)

        ret = defaultdict(list)
        for em in m:
            ret[find(em)].append(em)
        ret_list = []
        for em in ret:
            obj = [m[em], *sorted(ret[em])]
            ret_list.append(obj)
        return ret_list
