class solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            dict_s = {}
            for index, value in enumerate(s):
                dict_s[value] = index
            
            for index, value in enumerate(t):
                if value not in dict_s:
                    return (False)
            
            return (True)