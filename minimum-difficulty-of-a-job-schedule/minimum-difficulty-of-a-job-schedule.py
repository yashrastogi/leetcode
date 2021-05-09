class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        m = [[-1 for j in range(len(jobDifficulty))] for i in range(0, d + 1)]
        return self.dp(m, jobDifficulty, d, 0) # 0 is starting job
    
    def dp(self, memo, jobDifficulty, d, jobId) -> int:
        numJobs = len(jobDifficulty)
        # if there is only one day left, get the max difficulty value of rest of the job
        if d == 1:
            return max(jobDifficulty[jobId:])
        # if it is memoized, return value
        if memo[d][jobId] != -1:
            return memo[d][jobId]
        
        # for jobs starting from current id until the last feasible job, (feasible means if splitting job here will result in later jobs not being able to break into necessary days. For example, cutting [4, 3, 2, 1] d = 4 firstly into [4, 3, 2][1] will resulting in not [1] not being able to be splitted)
        curMax = 0
        res = float("+inf")
        for i in range(jobId, numJobs - d + 1):
            # get the current most difficult job value
            curMax = max(curMax, jobDifficulty[i])
            # get the min of the jobs so far 
            res = min(res, curMax + self.dp(memo, jobDifficulty, d - 1, i + 1))
        # store it in memo
        memo[d][jobId] = res
        return res