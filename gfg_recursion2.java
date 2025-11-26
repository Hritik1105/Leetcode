// Print 1 to n without using loops
// GeeksforGeeks
// hhttps://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

class Solution {
    static void printTillN(int N) {
        // code here
        if(N==0){
            return;
        }
        printTillN(N-1);
        System.out.print(N+" ");
    }
}