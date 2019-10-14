#634. Word Squares

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []  # 为了快速找出当前prefix可以组成的词语

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True
        
    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
    
    # 为了以column 为prefix组词组
    def get_words_with_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list    
    
    # 没啥用..
    def contains(self, word):
        node = self.find(word)
        return node if not None else node.is_word
        
class Solution:
    def wordSquares(self, words):
        trie = Trie()
        
        # initilizaiton
        for word in words:
            trie.add(word)
        
        squares = []
        for word in words:
            self.search(trie, [word], squares)
        return squares
    
    def search(self, trie, square, squares):
        n = len(square[0])
        curt_index = len(square)
        
        # termination
        if curt_index == n:
            squares.append(list(square))
            return 
    
        # prune
        for row_index in range(n):     
            prefix = ''.join([square[i][row_index] for i in range(curt_index)]) 
            if trie.find(prefix) is None:
                return 
            
        # backtracking
        prefix = ''.join([square[i][curt_index] for i in range(curt_index)])
        for word in trie.get_words_with_prefix(prefix):
            square.append(word)
            self.search(trie, square, squares)
            square.pop() # remove the last word
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      