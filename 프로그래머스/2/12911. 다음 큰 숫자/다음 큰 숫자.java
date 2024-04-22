class Solution {
    public int solution(int n) {
        int count = count1(n);
        
        for (int i = n+1; i <= 1000000; i++)
            if (count1(i) == count)
                return i;
                
        return 0;
    }
    
    public int count1(int num) {
        int count = 0;
        
        String binary = Integer.toBinaryString(num);
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1')
                count++;
        }
        
        return count;
    }
}