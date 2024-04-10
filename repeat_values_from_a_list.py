import collections
class Solution:
    def duplicates(self, arr, n): 
    	self.arr = arr
    	self.n = n
    def out(self):
        length = len(self.arr)
        cont = []
        cont_2 = []
        if self.n == length:
            for j in self.arr:
                if collections.Counter(self.arr)[j] > 1:
                    cont_2.append(j)
                else:
                    cont.append(j)
        if len(cont_2) == 0:
            return -1
        else:
            return sorted(cont_2)
        
