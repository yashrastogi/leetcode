class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        matches = 0
        
        rule_idx = 0
        if ruleKey == 'color':
            rule_idx = 1
        elif ruleKey == 'name':
            rule_idx = 2
        
        for i, item in enumerate(items):
            if item[rule_idx] == ruleValue:
                matches += 1
        
        return matches