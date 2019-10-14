#526. Load Balancer
# like Leetcode #380. Insert Delete GetRandom O(1)

import random
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.dataMap = {}
        self.dataList = []
        
    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id in self.dataMap:
            return 
        self.dataMap[server_id] = len(self.dataList)
        self.dataList.append(server_id)
        
    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.dataMap:
            return 
        idx = self.dataMap[server_id]
        tail = self.dataList.pop()
        if idx < len(self.dataList):
            self.dataList[idx] = tail
            self.dataMap[tail] = idx
        del self.dataMap[server_id]
        

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        return random.choice(self.dataList)