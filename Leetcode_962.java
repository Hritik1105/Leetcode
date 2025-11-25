// Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

class Solution {
    public int maxWidthRamp(int[] nums) {
        int n=nums.length;
        int[] rampmax=new int[n];
        
        rampmax[n-1]=nums[n-1];
        
        for(int i=n-2;i>=0;i--){
            rampmax[i]=Math.max(nums[i],rampmax[i+1]);
        }
        int i=0,j=0,ramp=0;
        while(j<n){
            while(nums[i]>rampmax[j]){
                i++;
            }
            ramp=Math.max(ramp,j-i);
            j++;
        }
        return ramp;
    }
}