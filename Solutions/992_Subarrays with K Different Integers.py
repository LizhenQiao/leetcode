"""
Keys:
- Point for this question is that we should notice at once that subarraysWithAtMostKDistinct is a typical sliding window unit
  question which is easy to solve. Then we would realize that we could convert `subarraysWithKDistinct(k)` to
  `subarraysWithAtMostKDistinct(k) - subarraysWithAtMostKDistinct(k-1)`.
- Actually, this sub-question is almost the same with "Leetcode340. Longest Substring with At Most K Distinct Characters",
  except that we are counting all possible #subarray instead of the longest one. Thus we use `result += right - left + 1`
  instead of `maxl = max(maxl, right - left + 1)`. But eventaully, thinking of them in a sliding window format, we would
  notice that they are the same problem. But this one is definitely more abstract.
"""


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def subarraysWithAtMostKDistinct(nums, k):
            dct = collections.defaultdict(int)
            left = 0
            result = 0

            for right in range(len(nums)):
                dct[nums[right]] += 1
                while len(dct) > k:
                    dct[nums[left]] -= 1
                    if dct[nums[left]] == 0:
                        del dct[nums[left]]
                    left += 1
                result += right - left + 1

            return result

        return subarraysWithAtMostKDistinct(nums, k) - subarraysWithAtMostKDistinct(nums, k-1)
