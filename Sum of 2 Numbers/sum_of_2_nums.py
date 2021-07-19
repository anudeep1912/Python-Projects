def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that
    they add up to target. You may assume that each input would have exactly one solution, and you may
    not use the same element twice. You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    #Solution 1
    for i in range(len(nums)):
        for j in range(i+1, len(nums));
             if nums[i] + nums[j] == target:
               return [i,j]

    #Solution 2
    for i in range(len(nums)):
        first_digit = nums[i]
        value = target - first_digit
        if value in nums:
            return [i, nums.index(value)]
        else: continue

list_1 = [3,2,4]
sum_1 = 6
two_sum(list_1,sum_1)
