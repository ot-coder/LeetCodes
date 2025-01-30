class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_lower = paragraph.lower()
        
        words = re.findall(r"[a-z']+", paragraph_lower)

        valid_words = [word for word in words if any(c.isalpha() for c in word)]

        banned_set = set(banned)
        
        freq = defaultdict(int)
        for word in valid_words:
            if word not in banned_set:
                freq[word] += 1

        max_count = -1
        result = ''
        for word, count in freq.items():
            if count > max_count:
                max_count = count
                result = word
        
        return result
        