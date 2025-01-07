class Solution {
    public String solution(String s) {
        String[] temp = s.split(" ");
        int maxNum, minNum;
        maxNum = minNum = Integer.parseInt(temp[0]);
        int n = 0;
        
        for (String num : temp) {
            n = Integer.parseInt(num);
            if (maxNum < n) maxNum = n;
            if (minNum > n) minNum = n;
        }
        
        return minNum + " " + maxNum;
    }
}