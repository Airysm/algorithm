class Solution {
    public String solution(String s) {
        String[] temp = s.split(" ");
        int max, min, n;
        max = min = Integer.parseInt(temp[0]);
        for(int i = 0; i < temp.length; i++) {
            n = Integer.parseInt(temp[i]);
            if(min > n) min = n;
            if(max < n) max = n;
        }
        
        return min+" "+max;
    }
}