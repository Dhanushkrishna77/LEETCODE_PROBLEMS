class Solution(object):
    def maxEvents(self, events):
        def find(day):
            if li[day]!=day:
                li[day]=find(li[day])
            return li[day]

        events.sort(key=lambda events:events[1]) #sorting based on end_day
        
        mx=max(e[1] for e in events)
        li=list(range(mx+2))
        ans=0

        for start_day,end_day in events:
            x=find(start_day)
            if x<=end_day:
                ans+=1
                li[x]+=1

        return ans


        