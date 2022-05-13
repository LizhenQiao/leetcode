# Sliding Window related questions

The first 7 questions are the most basic and classic type of questions of `Sliding Window`, which is to find largest subarray / substring.

- Basic idea is that for each time we tend to move right cursor of the window, we need to firstly interatively check the limit and move left cursor. Then we will get all valid cases. therefore, pick out the largest one.

76 and 727 are examples of finding smallest subarray.

- the basic idea for these questions is to first find a valid right boundary, then move left boundary as much as possible with the limit valid. This should be relatively intuitive.

---

- [3 | Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

  - [solution](../../Solutions/3_Longest%20Substring%20Without%20Repeating%20Characters.py)

- [159 | Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)

  - [solution](../../Solutions/159_Longest%20Substring%20with%20At%20Most%20Two%20Distinct%20Characters.py)

- [340 | Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

  - [solution](../../Solutions/340_Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters.py)

**From the first three questions of sliding window, we could already conclude common pattern of the most basic version of sliding window questions.**

- [1695 | Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/)

  - [solution](../../Solutions/1695_Maximum%20Erasure%20Value.py)

- [438 | Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

  - [solution](../../Solutions/438_Find%20All%20Anagrams%20in%20a%20String.py)

- [424 | Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

  - [solution](../../Solutions/424_Longest%20Repeating%20Character%20Replacement.py)

- [2024 | Maximize the Confusion of an Exam](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/)

  - [solution](../../Solutions/2024_Maximize%20the%20Confusion%20of%20an%20Exam.py)

- [992 | Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

  - [solution](../../Solutions/992_Subarrays%20with%20K%20Different%20Integers.py)

- [2107 | Number of Unique Flavors After Sharing K Candies](https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/)

  - [solution](..)

---

- [76 | Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

  - [solution](../../Solutions/76_Minimum%20Window%20Substring.py)

- [727 | Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/)

  - [solution](../../Solutions/727_Minimum%20Window%20Subsequence.py)

**727 and 76 share similar thought which is intuitive for sliding window. Firstly find end index, then get start index.**

---

[https://www.notion.so/fa46bae02e5f49fbaee96d22a40a7554?v=4257c12d1b7e4cd694719235561a261c](https://www.notion.so/fa46bae02e5f49fbaee96d22a40a7554?v=4257c12d1b7e4cd694719235561a261c)
