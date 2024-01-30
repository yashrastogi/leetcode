class Solution:
    def decodeString(self, s: str) -> str:
        def repeatRecursion(string, i):
            ret = ""
            reps = 0
            while i < len(s):
                if string[i].isnumeric():
                    reps = reps * 10 + int(string[i])
                elif string[i] == "[":
                    substr, i = repeatRecursion(string, i + 1)
                    ret += substr * reps
                    reps = 0
                elif string[i] == "]":
                    return ret, i
                else:
                    ret += string[i]
                i += 1
            return ret, i

        def repeatStack(string):
            i = 0
            ret = ""
            reps = 0
            stack = []
            while i < len(string):
                if string[i].isnumeric():
                    reps = reps * 10 + int(string[i])
                elif string[i] == "[":
                    stack.append((ret, reps))
                    reps = 0
                    ret = ""
                elif string[i] == "]":
                    popped = stack.pop()
                    ret = popped[0] + ret * popped[1]
                else:
                    ret += string[i]
                i += 1
            return ret

        return repeatRecursion(s)
