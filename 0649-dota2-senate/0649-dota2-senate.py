class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ret = {"R": "Radiant", "D": "Dire"}

        senators = defaultdict(list)
        for i, ch in enumerate(senate):
            senators[ch].append(i)

        i = 0
        while True:
            if not senators["R"]:
                return ret['D']
            elif not senators["D"]:
                return ret['R']
            if senators["R"][0] == i:
                senators["R"].append(senators["R"].pop(0))
                if senators["D"]:
                    senators["D"].pop(0)
                else:
                    return ret["R"]
            elif senators["D"][0] == i:
                senators["D"].append(senators["D"].pop(0))
                if senators["R"]:
                    senators["R"].pop(0)
                else:
                    return ret["D"]
            i += 1
            if i == len(senate):
                i = 0
