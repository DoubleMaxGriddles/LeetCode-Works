class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
       
        # Initialize pointers for s and p
        sptr, pptr = 0, 0
        # Initialize the last match position for '*' in p to -1
        last_star_match = -1
        # Initialize pointers for s and p when a '*' is encountered in p
        star_sptr, star_pptr = 0, -1
        
        # Iterate over each character in s
        while sptr < len(s):
            # Case 1: If p has a '?' or the character in p matches the character in s,
            #         move both pointers to the next character in s and p
            if pptr < len(p) and (p[pptr] == '?' or p[pptr] == s[sptr]):
                sptr += 1
                pptr += 1
            # Case 2: If p has a '*', update the pointers for s and p when a '*' is
            #         encountered in p and move the pointer for p to the next character
            elif pptr < len(p) and p[pptr] == '*':
                last_star_match = sptr
                star_sptr = sptr
                star_pptr = pptr
                pptr += 1
            # Case 3: If p has a '*', but the last match was not successful, update
            #         the pointers for s and p to the next character in s and the
            #         character after the '*' in p
            elif star_pptr != -1:
                star_sptr += 1
                sptr = star_sptr
                pptr = star_pptr + 1
            # Case 4: If none of the above cases apply, return False
            else:
                return False
        
        # Iterate over the remaining characters in p
        while pptr < len(p) and p[pptr] == '*':
            pptr += 1
        
        # If p has been completely processed, return True
        return pptr == len(p)
