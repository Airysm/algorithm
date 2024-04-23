class Solution {
    
    public int gcd(int a, int b) {
        if (a%b == 0)
            return b;
        return gcd(b, a%b);
    }
    
    public int solution(int[] arr) {
        int answer = 1;
        for (int num : arr) {
            answer = answer * num / gcd(answer, num);
        }
        return answer;
    }
}