class Solution {
    public int subtractProductAndSum(int n) {
        int digits=0,digits1=1;
        int m=n;
        while(n>0){
            digits+=n%10;
            n=n/10;
        }
        while(m>0)
        {
            digits1*=m%10;
            m=m/10;
        }
        return digits1-digits;
        
    }
}