摩尔投票法（Boyer–Moore majority vote algorithm），
也被称作「多数投票法」，算法解决的问题是：如何在任意多的候选人中（选票无序），选出获得票数最多的那个。要求众数过半

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = None
        vote_cnt = 0
        
        for num in nums:
            if not vote or num == vote:
                vote = num
                vote_cnt += 1
            else:
                vote_cnt -= 1
                if vote_cnt == 0:
                    vote = num
                    vote_cnt = 1
        return vote
