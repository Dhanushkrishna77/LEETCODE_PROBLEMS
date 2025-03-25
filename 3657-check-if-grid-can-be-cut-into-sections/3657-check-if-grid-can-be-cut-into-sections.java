class Solution {
    public boolean checkValidCuts(int n, int[][] rec) {
        int cnt=0,ind=0;
        ArrayList<int[]> ar1=new ArrayList<>();
        ArrayList<int[]> ar2=new ArrayList<>();
        for(int i=0;i<rec.length;i++){
            ar1.add(new int[]{rec[i][1],rec[i][3]});
            ar2.add(new int[]{rec[i][0],rec[i][2]});
        }
        Collections.sort(ar1, (a, b) -> Integer.compare(a[0], b[0]));
        Collections.sort(ar2, (a, b) -> Integer.compare(a[0], b[0]));
       

        if(check(ar1))return true;
        return check(ar2);
    }
    boolean check(ArrayList<int[]> ar){
        int max=ar.get(0)[1];
        int cnt=0;
        for(int i=1;i<ar.size();i++){
            if(ar.get(i)[0]>=max){
                cnt++;
            }
            max=Math.max(max,ar.get(i)[1]);
        }
        return (cnt>=2);
    }
}