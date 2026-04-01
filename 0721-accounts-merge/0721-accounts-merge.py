class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}
        m = {} # Maps email to account name

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            p_u = find(u)
            p_v = find(v)
            if p_u == p_v:
                return False 
            if rank[p_u] < rank[p_v]:
                parent[p_u] = p_v
            elif rank[p_u] > rank[p_v]:
                parent[p_v] = p_u
            else:
                parent[p_v] = p_u
                rank[p_u] += 1
            return True

        # 1. Initialize nodes and union them in one O(N * K) pass
        for ac in accounts:
            name = ac[0]
            first_email = ac[1] if len(ac) > 1 else None
            
            for i in range(1, len(ac)):
                email = ac[i]
                # Initialize in DSU if not seen before
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0
                
                m[email] = name
                
                # Union every email to the FIRST email in this specific account list
                if i > 1:
                    union(first_email, email)

        # 2. Gather emails by their absolute root
        ret = defaultdict(list)
        for em in m:
            ret[find(em)].append(em)

        # 3. Format and sort the final output
        ret_list = []
        for root in ret:
            obj = [m[root]] + sorted(ret[root])
            ret_list.append(obj)
            
        return ret_list