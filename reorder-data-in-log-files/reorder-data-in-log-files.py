class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        list_num = []
        list_text = []
        for log in logs:
            log_s = log.split(' ')
            log_s_1 =' '.join(log_s[1:])
            if ord(log_s_1[0]) in range(48, 58):
                list_num.append(log)
            else:
                list_text.append(log)
            
        list_text.sort()
        list_text.sort(key=lambda x: " ".join(x.split(' ')[1:]))
        
        return list_text + list_num 