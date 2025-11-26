// Print N to 1 without loop
// https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1?page=1&category=Recursion&sortBy=submissions

class Solution {

    void printNos(int N) {
        // code here
        if(N==0){
            return;
        }
        System.out.print(N+" ");
        printNos(N-1);
        
    }
}