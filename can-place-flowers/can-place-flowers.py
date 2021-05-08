class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(fb) == 1 and n==1:
            return not fb[0]
        if len(fb) == 2:
            if fb[0] | fb[1] == 0 and n==1:
                return True
            
        n_t = 0
        if fb[0] | fb[1] == 0:
            n_t += 1
            fb[0] = 1
        for i in range(1, len(fb)-1):
            if fb[i] == 0:
                if fb[i] | fb[i+1] == 0 and fb[i] | fb[i-1] == 0:
                    n_t += 1
                    fb[i] = 1
        if fb[-1] | fb[-2] == 0:
            n_t += 1
            fb[-1] = 1
        return n <= n_t