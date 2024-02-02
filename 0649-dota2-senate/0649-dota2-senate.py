class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = defaultdict(list)
        for i, ch in enumerate(senate):
            senators[ch].append(i)

        i = 0
        while True:
            if not senators["R"]:
                return "Dire"
            elif not senators["D"]:
                return "Radiant"
            if senators["R"][0] == i:
                senators["R"].append(senators["R"].pop(0))
                senators["D"].pop(0)
            elif senators["D"][0] == i:
                senators["D"].append(senators["D"].pop(0))
                senators["R"].pop(0)
            i = (i + 1) % len(senate)