class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int: 
        n = len(questions) 

        @cache
        def test(i) :  
            if i >= n : 
                return 0 
            else : 
                return max(test(i + 1), questions[i][0] + test(i + questions[i][1] + 1)) 
        return test(0) 


        