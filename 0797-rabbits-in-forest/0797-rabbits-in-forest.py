class Solution(object):
    def numRabbits(self, answers):
      
        d=dict()
        for  i in answers:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=0
        for x in d:
            g=x+1
            ans=math.ceil(d[x]/float(g))
            gp=int(ans*g)
            c+=gp
        return c