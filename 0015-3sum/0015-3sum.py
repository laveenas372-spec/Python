class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []

        nums.sort()

        for indx,val in enumerate(nums):

            if indx > 0 and val == nums[indx-1]:
                continue
            left = indx + 1
            right = len(nums) - 1

            while left < right:

                currentSum = val + nums[left] + nums[right]

                if currentSum > 0:
                    right -= 1
                elif currentSum < 0:
                    left  +=1
                else:
                    triplets.append([val,nums[left],nums[right]])

                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                        

        return triplets
