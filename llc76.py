class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        if len(t) > len(s):
            return ""

        need = Counter(t)
        must_chars = len(need)
        made_chars = 0
        window = Counter()
        min_len = float('inf')
        res = 0
        l = 0

        for r, char in enumerate(s):
            window[char] += 1

            if char in need and window[char] == need[char]:
                made_chars += 1

            while made_chars == must_chars:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = l
                
                l_char = s[l]
                window[l_char] -= 1

                if l_char in need and window[l_char] < need[l_char]:
                    made_chars -= 1

                l += 1

        if min_len != float('inf'):
            return s[res:res + min_len]
        
        return ""

        