# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        total = sum(cardPoints[-k:])
        max_score = total

        for i in range(1, k + 1):
            total += cardPoints[i - 1] - cardPoints[-k + i - 1]
            max_score = max(max_score, total)

        return max_score