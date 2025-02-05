class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if(s1.length()!=s2.length()) return false;
        if(s1.equals(s2)) return true;
        int cnt=0;
        int ptr=-1;
        for(int i=0;i<s1.length();++i){
            if(s1.charAt(i)!=s2.charAt(i)){
                cnt++;
                if(ptr==-1){
                    ptr=i;
                }
                else if(s1.charAt(i)!=s2.charAt(ptr) || cnt>2 || (s1.charAt(ptr)!=s2.charAt(i))) return false;
            }
            
            
        }
        return(cnt==2);
    }
}