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
    
''''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cleaned = re.sub(r'[!?\',;.]', ' ', paragraph.lower())
    

        words = cleaned.split()
        word_counts = Counter(words)
    

        for banned_word in banned:
            if banned_word in word_counts:
                del word_counts[banned_word]
    
  
        return max(word_counts.items(), key=lambda x: x[1])[0]
        '''