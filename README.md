# LeetCode-Works
Leetcode Submissions that I did in my spare time.
---------------------------------------------------------------------------------------------------------------------------------------------
PWsolution.py


Q420. A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.

---------------------------------------------------------------------------------------------------------------------------------------------
ShipDsolution.py

Q1011. Capacity To Ship Packages Within D Days
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Constraints:

1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500

---------------------------------------------------------------------------------------------------------------------------------------------
Wildcard.py

Q44. Wildcard Matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.

---------------------------------------------------------------------------------------------------------------------------------------------
RE.py

Q10. Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

---------------------------------------------------------------------------------------------------------------------------------------------
SortedArrays.py

Q4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

 

