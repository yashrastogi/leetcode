class Solution:
    def fourSum(self, n: List[int], target: int) -> List[List[int]]:
        n.sort()
        a = 0
        ret = set()
        while a < len(n):
            b = a+1
            while b < len(n):
                c_sum = n[a]+n[b]
                c = b+1
                d = len(n)-1
                while c < d:
                    c_sum_2 = c_sum + n[c] + n[d]
                    if c_sum_2 == target:
                        ret.add((n[a],n[b],n[c],n[d]))
                        c += 1
                        d -= 1
                    if c_sum_2 < target:
                        c += 1
                    elif c_sum_2 > target:
                        d -= 1
                b += 1
            a += 1
        
        return ret