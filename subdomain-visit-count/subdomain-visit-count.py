class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        di = {}
        for el in cpdomains:
            count, domain = el.split(' ')
            d_s = domain.split('.')
            for i in range(len(d_s)):
                t = ".".join(d_s[i:])
                di.setdefault(t, 0)
                di[t] += int(count)
        ret = []
        for k, v in di.items():
            ret.append(str(v) + " " + k)
        return ret