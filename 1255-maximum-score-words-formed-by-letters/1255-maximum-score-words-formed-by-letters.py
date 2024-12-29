class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        getScore = lambda c: score[ord(c) - ord('a')]
        defaultCounter = Counter(letters)
        def recurse(wordIndex, currentCounter):
            if wordIndex >= len(words): return 0
            # print(words[wordIndex], currentCounter)
            notinclude = 0 + recurse(wordIndex + 1, currentCounter.copy())
            tempScore = 0
            for c in words[wordIndex]:
                tempScore += getScore(c)
                currentCounter[c] += 1
            for key in currentCounter:
                if key not in defaultCounter: return notinclude
                if currentCounter[key] > defaultCounter[key]: return notinclude            
            include = tempScore + recurse(wordIndex + 1, currentCounter.copy())
            return max(notinclude, include)
        temp = defaultdict(int)
        return recurse(0, temp)