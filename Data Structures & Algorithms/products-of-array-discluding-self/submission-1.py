class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        temp = 1
        for i in range(len(nums)):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = pre[i-1] * nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == (len(nums)-1):
                suf[i] = nums[i]
            else:
                suf[i] = suf[i+1] * nums[i]
        

        
        for i in range(len(output)):
            if i == 0:
                output[i] = suf[i+1]
            elif i == len(output)-1:
                output[i] = pre[i-1]
            else:
                output[i] = pre[i-1] * suf[i+1]
        return output

        