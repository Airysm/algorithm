class Solution {
    public int[] solution(String s) {
        int count = 0;
        int count0 = 0;
        
        while (!s.equals("1")) {
            int count1 = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '1') count1 += 1;
                else                    count0 += 1;
            }
            s = Integer.toBinaryString(count1);
            count += 1;
        }
        
        return new int[] {count, count0};
    }
}