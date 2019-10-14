#425. Letter Combinations of a Phone Number

# dfs + backtracking

KEYBOARD = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z'],
}
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
        results = []
        self.dfs(digits, 0, '', results)
        return results
        
    def dfs(self, digits, index, string, results):
        if index == len(digits):
            results.append(string)
            return 
        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, string + letter, results)


--------
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
        results = []
        self.dfs(digits, 0, [], results)
        return results
        
    def dfs(self, digits, index, path, results):
        if len(path) == len(digits):
            results.append(''.join(path[:]))
            return 
        for letter in KEYBOARD[digits[index]]:
            path.append(letter)
            self.dfs(digits, index+1, path, results)
            path.pop()
