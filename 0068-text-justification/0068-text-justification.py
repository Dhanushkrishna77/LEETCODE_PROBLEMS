class Solution(object):
    def fullJustify(self, words, maxWidth):
        out = []
        def write(j, i, t):
           if i-j==1:
             out.append(words[j]+(" "*(maxWidth-len(words[j]) )) )
             return 
           n = maxWidth - t
           if n>=0:
              n +=1
              r = n%(i-j-1)
              spaces = " "*((n//(i-j-1))+1)
              line = words[j]
              for k in range(j+1, i):
                 if r:
                    line +=" "
                    r-=1
                 line += spaces+ words[k]
              out.append(line)
           else:
              out.append(" ".join(words[j:i]))
        t = 0
        j = 0
        for i, w in enumerate(words):
            if t+len(w)<=maxWidth:
                t+=len(w)+1
            else:
                write(j, i, t)
                j =i 
                t = len(w)+1
        line = words[j]
        for k in range(j+1, len(words)):
              line+=" "+words[k]
        line += " "*(maxWidth- len(line))
        out.append(line)
        return out