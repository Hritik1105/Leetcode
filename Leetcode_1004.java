// Max Consecutive Ones III

class Solution {
    public int longestOnes(int[] nums, int k) {
        int zero=0,maxi=0,left=0,right=0;
        int n=nums.length;
        while(right<n){
            if(nums[right]==0) zero++;
            while(zero>k){
                if(nums[left]==0) zero--;
                left++;
            }
            maxi=Math.max(maxi,right-left+1);
            right++;
        }
        return maxi;
    }
}