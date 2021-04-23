class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_substr = ""
        max_lens = []
        for c in s:
            if c not in max_substr:
                max_substr += c
            else:
                max_lens.append(len(max_substr))
                c_index = max_substr.index(c)
                max_substr = max_substr[c_index+1:]
                max_substr += c
        max_lens.append(len(max_substr))


        if len(max_lens)==0:
            return 0
        else:
            return max(max_lens)