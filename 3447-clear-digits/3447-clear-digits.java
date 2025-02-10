import java.util.*;
class Solution {
    public String clearDigits(String s) {
        StringBuilder s1=new StringBuilder();
        Stack<Character> st=new Stack<>();
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(!Character.isDigit(ch)){
                st.push(ch);
            }else if(!st.isEmpty()){
                st.pop();
            }
        }
       while(!st.isEmpty()){
        s1.append(st.pop());
       }
       return s1.reverse().toString();
       
    }
}