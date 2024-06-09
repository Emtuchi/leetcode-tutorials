import re

class solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in range(len(s)-1, -1, -1):
            string = string + s[i]
        clean_reverse = re.sub(r'[\W_]','',string.lower())

        clean_s = re.sub(r'[\W_]','',s.lower())
        if (clean_reverse == clean_s):
            return True
        else:
            return False
            

