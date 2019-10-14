#120. Word Ladder

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, beginWord, endWord, wordList):
        # write your code here
        wordList = set(wordList) 
        wordList.add(endWord) 			# 和leetcode唯一不同，endWord might not in the WordList
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':

                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordList:
                        wordList.remove(newWord)
                        queue.append([newWord, length+1])
        return 0