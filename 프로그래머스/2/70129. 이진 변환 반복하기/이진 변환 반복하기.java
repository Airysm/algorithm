class Solution {
    public int[] solution(String s) {
        int zero = 0;
        int num = 0;
        
        while (!s.equals("1")) {
            int one = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0')         zero++;
                else if (s.charAt(i) == '1')    one++;
            }
            s = Integer.toBinaryString(one);
            num++;
        }
        return new int[] {num, zero};
    }
}