class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        sp = s.split(' ')
        ret = []
        for string in reversed(sp):
            if string == '': continue
            ret.append(string)
        return ' '.join(ret)
