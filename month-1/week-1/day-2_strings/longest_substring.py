class solution:
    def longest_substring(self, s: str) -> int:
        l,r = 0,1
        count = 0
        max_count = 0
        while l < len(s):
            while r < len(s):
                count += 1
                if ((r == len(s) - 1) and (s[l] != s[r])): # if r is at the last element and that element isn't same as what is in l
                    count = 0
                if s[l] == s[r]:
                    max_count = max(max_count, count)
                    count = 0
                    break
                r += 1
            l += 1
            r = l + 1
        print(max_count)
        return max_count