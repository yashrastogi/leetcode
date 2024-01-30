class Solution:
    def decodeString(self, s: str) -> str:
        def repeat(string, i):
            ret = ''
            reps = 0
            while i < len(s):
                if string[i].isnumeric():
                    reps = reps * 10 + int(string[i])
                elif string[i] == '[':
                    substr, i = repeat(string, i + 1)
                    ret += substr * reps
                    reps = 0
                elif string[i] == ']':
                    return ret, i
                else:
                    ret += string[i]
                i += 1
            return ret, i
        
        return repeat(s, 0)[0]