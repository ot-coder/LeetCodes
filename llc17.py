class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtracking(i, strcurr):
            if len(strcurr) == len(digits):
                res.append(strcurr)
                return

            for c in digitToChar[digits[i]]:
                backtracking(i+1, strcurr + c)

        if digits:
            backtracking(0, "")

        return res
