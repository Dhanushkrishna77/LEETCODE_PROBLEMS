class Solution(object):
    

    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        list1 = [i for s in grid for i in s]
        list1.sort()

        length = len(list1)
        if length == 1:
            return 0
    
        middleIndex = length//2
        operations = 0
        i = 0
        modvalue1 = list1[i] % x
        middleItem = list1[middleIndex]

        for i in range(length):
            if list1[i] % x != modvalue1:
                return -1
            
            if list1[i] < middleItem:
                difference = middleItem - list1[i]
            elif list1[i] > middleItem:
                difference = list1[i] - middleItem
            else:
                difference = 0
            operations = operations + difference // x

        
        return operations

            
    



    
    