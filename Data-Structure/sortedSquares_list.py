# -*- coding: UTF-8 -*-

''' 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1： 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]

示例 2： 输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121] '''

from typing import List

# 双指针法，充分利用平方两边大中间小的特性，先平方再比较后移动指针

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        i, j, k = 0, length-1, length-1
        ans = [-1] * length
        while k >= 0:
            if nums[i] ** 2 > nums[j] ** 2:
                ans[k] = nums[i] ** 2
                i += 1
            else:
                ans[k] = nums[j] ** 2
                j -= 1
            k -= 1
        return ans
    
if __name__ == '__main__':
    solution = Solution()
    nums = [-4, -1, 0, 3, 10]
    nums1 = [-7,-3,2,3,11]
    print(solution.sortedSquares(nums))
    print(solution.sortedSquares(nums1))