class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        N = len(nums)
        new_nums = []
        for i in range(N):
            new_nums.append([nums[i],i])
        
        new_nums.sort()
        for i in range(N-1):
            for j in range(i+1,N):
                if new_nums[i][0]+new_nums[j][0]==target:
                    if(new_nums[i][1]<=new_nums[j][1]):
                        return [new_nums[i][1],new_nums[j][1]]
                    else:
                        return [new_nums[j][1],new_nums[i][1]]
        