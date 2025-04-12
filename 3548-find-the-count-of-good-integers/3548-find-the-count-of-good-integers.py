class Solution(object):
    def factorial(self, number): #calculate factorial
        res = 1
        for i in range(1, number+1):
            res*=i
        return res
    
    def gen(self, num, index, res, k): #backtrack calc every palindrome
        if index >= (len(num)+1)//2: # if we've gone over the halfway point
            if int(num)%k==0: #if the number is divisible by k
                res.append(num) # add to the list
            return 
        if index!=0: #if it's nto the first index we can consider 0
            temp = num
            temp = temp[0:index] + '0' +temp[index+1:]
            temp = temp[0:len(temp) - index - 1] + '0' +temp[len(temp) - index :]
            self.gen(temp, index+1, res, k)
        for i in range(1, 10): # loop 1-9 and replace the index 
#and it's symmetrical counterpart on the other side of the string with the same char
            temp = num
            temp = temp[0:index] + str(i) +temp[index+1:]
            temp = temp[0:len(temp) - index - 1] + str(i) +temp[len(temp) - index :]
            self.gen(temp, index+1, res, k)

    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        palis = []
        begin = "0" * n
        self.gen(begin, 0, palis, k)
        freq_set = set() #create set to remove duplicates

        for i in palis: 
            temp_list = ['0'] * 10 #frequency list
            for j in i:
                if(temp_list[int(j)] == '9'):
                    temp_list[int(j)] = 'A' # if we go above 9, this only works because 10 is the max n
                else: # add to freq list
                    temp_list[int(j)] = str(int(temp_list[int(j)]) + 1)
            freq_set.add(''.join(temp_list))
        
    
        base_line = self.factorial(n)
        result = 0 

        for i in freq_set: # iterate for every value in the freq_set
            permutations = base_line  #n! 
            for freq in i: #for every char frequency
                
                if(freq=='A'):
                    div = 10
                else:
                    div = int(freq)
                div = self.factorial(div)
                permutations/=div #divide by factorial of freq of char

            if(i[0] !='0'): # if the palindrome contains zero
                #set first value in permutation to 0
                zeros = int(i[0])-1 # one less value in zero freq
                zero_perms = self.factorial(n-1)  # (n-1) ! remaining spots
                for j in range(1,len(i)): 
                    
                    if(i[j]=='A'):
                        div = 10
                    else:
                        div = int(i[j])
                    div = self.factorial(div) #divide by freqs
                    zero_perms/=div
                zero_perms/=self.factorial(zeros)
                permutations-=zero_perms 
# subtract from permtuations the number that begin with zero
            result+=permutations
        
        return result 
        