from typing import List
class Solution:
    def solution(self,nums,ans,cur,index):
        if(index>len(nums)):
            return
        ans.append(cur[:])
        print("ANS == ", ans)
        for i in range(index,len(nums)):
            print(" I === ", i)
            x = nums[i]
            if(x not in cur):
                cur.append(nums[i])
                self.solution(nums,ans,cur,i)
                cur.pop()
        return
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(nums,ans,cur,0)
        return ans

soln = Solution()
print(soln.subsets([1,2,3]))

