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
            substr = None
            while i < len(string):
                print(stacl)
                if string[i].isnumeric():
                    reps = reps * 10 + int(string[i])
                elif string[i] == "[":
                    stack.append([i + 1, reps])
                    reps = 0
                elif string[i] == "]":
                    popped = stack.pop()
                    stack[-1].append(string[popped[0]:i] * popped[1])

                i += 1
            return ret

        return repeatStack(s)
