class Solution(object):
    def countSymmetricIntegers(self, low, high):
        c=0
        for i in range(low,high+1):
            i=str(i)
            if len(i)%2==0:
                arr=[]
                for j in i:
                    arr.append(int(j))
                if sum(arr[:len(arr)//2])==sum(arr[len(arr)//2:]):
                    c+=1
        return c

                