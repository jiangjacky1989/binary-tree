#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : ${DATE} ${HOUR}:${MINUTE}
# @Author  : Jacky

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums_len = len(nums)
        flag = ''
        for i in range(1, nums_len + 1):
            for j in range(0, nums_len - i + 1):
                if sum(nums[j:j + i]) >= target:
                    flag = True
                    return len(nums[j:j + i])
            if flag:
                break
        return 0
