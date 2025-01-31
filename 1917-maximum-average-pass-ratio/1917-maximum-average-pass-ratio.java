class Gain{
    double gain;
    double ratio;
    int pass;
    int total;

    Gain(){}

    Gain(double gain, double ratio, int pass, int total){
        this.gain = gain;
        this.ratio = ratio;
        this.pass = pass;
        this.total = total;
    }
}
class Solution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<Gain> pq = new PriorityQueue<>((a, b) -> Double.compare(b.gain, a.gain));
        double sum = 0.0;
        int n = classes.length;

        for(int i=0; i<classes.length; i++){
            int pass = classes[i][0];
            int total = classes[i][1];
            double currRatio = (double) pass/total;
            double incRatio = ((double) (pass+1) / (total+1));
            double gain = incRatio - currRatio;
            sum += currRatio;
            pq.add(new Gain(gain, currRatio, pass, total));
        }

        for(int i=0; i<extraStudents; i++){
            Gain g = pq.poll();
            double gain = g.gain;
            double prevRatio = g.ratio;
            int pass = g.pass;
            int total = g.total;

            sum -= prevRatio;
            pass += 1;
            total += 1;
            double currRatio = (double) pass/total;
            sum += currRatio;

            double newGain = ((double) (pass+1) / (total+1)) - currRatio;
            pq.add(new Gain(newGain, currRatio, pass, total));
        }

        return sum/n;
    }
}