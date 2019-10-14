#637. Valid Word Abbreviation
class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        i = 0; j = 0
        while i < len(word) and j < len(abbr):
            if '0' <= abbr[j] <= '9':
                if int(abbr[j]) == 0:
                    return False
                val = 0
                while j < len(abbr) and '0' <= abbr[j] <= '9':
                    val = val*10 + int(abbr[j])
                    j += 1
                i += val
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return True if i == len(word) and j == len(abbr) else False

'''
笔记：
'0' <= abbr[j] <= '9'是好的

而 0 <= int(abbr[j]) <= 9 是不行的。 因为
if abbr[i].alpha == True: 则不能用 int 来转换. 
或者用 abbr[j].isdigit() 系统函数来代替
'''