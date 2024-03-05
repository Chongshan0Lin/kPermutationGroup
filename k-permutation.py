from collections import deque
from copy import copy

class kPermutaionGroup(object):

    def permk(self,k):
        dictQue1 = deque()
        for i in range(1,k+1):
            dictQue1.append({1:i})

        dictQue2 = deque()

        for j in range(2, k+1):

            while dictQue1:
                perm = dictQue1.popleft()
                for i in range(1, k+1):
                    if i not in perm.values():
                        newPerm = copy(perm)
                        newPerm[j] = i
                        dictQue2.append(newPerm)

            dictQue1 = dictQue2
            dictQue2 = deque()
        
        return dictQue1


    def permToCycle(self,dict):
        keySet = set()
        String = "\item $"

        for i in dict.keys():

            if i not in keySet:
                keySet.add(i)
                k = dict[i]

                if k != i:
                    String += '('
                    String += str(i)
                    String += ','

                while k != i:
                    keySet.add(k)
                    String += str(k)
                    String += ','
                    k = dict[k]
                
                if dict[i] != i:
                    String = String[0:-1]
                    String += ')'
        
        if String == "\item $": return "\item $e$"
        return (String+"$")
    
    def printPermutationGroup(self, k):
        for i in self.permk(k):
            print(self.permToCycle(i))


g = kPermutaionGroup()
g.printPermutationGroup(2)