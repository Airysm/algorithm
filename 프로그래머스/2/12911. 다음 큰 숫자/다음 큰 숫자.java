class Solution {
    public int solution(int n) {
        int answer = 0;
        int CountOne = toBinaryCountOne(n);
        for (int i = n + 1;;i++) {
            int temp = toBinaryCountOne(i);
            if (CountOne == temp) {
                answer = i;
                break;
            }
        }
        return answer;
    }
    
    public int toBinaryCountOne(int num) {
        int one = 0;
        while (num > 0) {
            if (num%2 == 1)
                one++;
            num /= 2;
        }
        
        return one;
    }
}