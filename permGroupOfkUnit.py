import math
class perGroup(object):
    def __init__(self, k) -> None:
        self.k = k
        self.iGroup = self.getInvertibleSet()
    
    #Get all elements in the invertible group of Z/(k)
    def getInvertibleSet(self):
        iGroup = set()
        for i in range(1,self.k):
            if math.gcd(i,self.k) == 1:
                iGroup.add(i)
        return iGroup

    #Given an element in invertible group, give its permutation group in dictionary
    def getPermutationGroup(self, n):
        perm = {}
        perm[self.k] = self.k

        for i in range(1,self.k):
            perm[i] = (i * n) % self.k

        return perm
    
    #Given a permutation group, print it in latex form
    def permToCycle(self,dict):
        keySet = set()
        String = "\\item $"

        #For each key value in dictionary
        for i in dict.keys():
            
            #If we have not visited it
            if i not in keySet:
                keySet.add(i)
                k = dict[i]

                if k != i:
                    String += '('
                    String += str(i)
                    String += ','

                #We loop through this set
                while k != i:
                    # print("i:", i)
                    # print("k:", k)
                    keySet.add(k)
                    String += str(k)
                    String += ','
                    k = dict[k]
                
                if dict[i] != i:
                    String = String[0:-1]
                    String += ')'
        
        if String == "\\item $": return "\\item $e$"
        return (String +"$")
    
    #A function that returns all permutation groups of the invertible group of Z/n
    def allPermGroupToSet(self):
        string = "\\{"
        for i in self.iGroup:
            string += self.permToCycle(self.getPermutationGroup(i))
        return string+"\\}"
    
    def printAllPermGroup(self):
        # print(self.iGroup)
        for i in self.iGroup:
            print(self.permToCycle(self.getPermutationGroup(i)))

pg = perGroup(12)

print(pg.iGroup)

# for i in pg.iGroup:
#     print(pg.getPermutationGroup(i))

pg.printAllPermGroup()
print(pg.allPermGroupToSet())
