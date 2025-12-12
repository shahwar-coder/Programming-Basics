'''
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        sorted_c = sorted(c.items(), key=lambda x : (-x[1], x[0])) #1st sort by descending, then sort by ascending # sorted func always retuns a list
        return ''.join([k*v for k,v in sorted_c])
