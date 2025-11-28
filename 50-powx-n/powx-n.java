class Solution {
    public double myPowHelp(double x, long n) {
        if(n==0) return 1;
        double faith=myPowHelp(x,n/2);
        if(n%2==0) return faith*faith;
        else return faith*faith*x;
    }
    public double myPow(double x, int n) {
        if(n<0){
            return (1.0/myPowHelp(x,n*-1l));
        }
        else{
            return myPowHelp(x,n);
        }
    }
}