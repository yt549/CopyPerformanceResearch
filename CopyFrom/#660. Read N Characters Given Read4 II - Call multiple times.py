#660. Read N Characters Given Read4 II - Call multiple times

'''
笔记：

buffer 是一种数据结构, 队列：
 # 队列先进先出 保持顺序不变
 # 队列为空 就进队 Read4
 # 队列不为空 就出队 并且把出队element放进result里
'''
<有点bug，待修改>

class Solution:

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        buffer = [None]*4
        head = 0 # buffer head
        tail = 0 # buffer tail
        
        ptr = 0 # RAM pointer
        while ptr < n:
            # buffer 就是一个队列
            # 如果队列为空，则read4
            if head = tail:
                tail = Reader.read4(buffer)
                bufferPtr = 0 
            # 如果读不进去了，则break
            # 缓冲区没有内容时，向系统要一个缓冲区，
            # 要不到就退出
            if tail == 0:
                break 
            # 如果队列不为空: bufferPtr < bufferCnt
            # ptr 读到RAM的个数 < maximum number of chars to read
            # 出队
            while (ptr < n and head < tail):
                buff[ptr] = buffer[head]
                ptr += 1; head +=1
        return ptr

----
<别人的>

class Solution:

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def __init__(self):
        self.queue = [] # global "buffer"

    def read(self, buf, n):
        idx = 0

    # if queue is large enough, read from queue
    # 先看一下是不是 queue这个buffer还有没读的
        while self.queue and n > 0:
            buf[idx] = self.queue.pop(0)
            idx += 1
            n -= 1
    # 如果读了queue里面的，还需要读更多则，while n > 0 
        while n > 0:
        # read file to buf4
        # read 一波，可多次 in iteration
        
            buf4 = [""]*4
            l = Reader.read4(buf4)

        # if no more char in file, return
            if not l:
                return idx

        # if buf can not contain buf4, save to queue
            if l > n:
                self.queue += buf4[n:l]

        # write buf4 into buf directly
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx