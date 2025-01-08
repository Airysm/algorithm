class Solution {
    public int solution(int n) {
        int answer = 0;
        int sum;
        for (int i = 1; i <= n; i++) {
            sum = 0;
            for (int j = i; sum < n; j++)
                sum += j;
            if (sum == n)
                    answer++;
        }
        
        return answer;
    }
}