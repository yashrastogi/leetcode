class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first]
        for i, num in enumerate(encoded):
            ret += [ret[i] ^ num]
        return ret
            