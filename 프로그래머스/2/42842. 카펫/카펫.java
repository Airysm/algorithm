class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        int area = brown + yellow;
        
        for (int i = 1; i < area/2+1; i++) {
            if (area % i == 0) {
                int j = area / i;
                if (i*2 + j*2 - 4 == brown) {
                    answer[0] = j;
                    answer[1] = i;
                    break;
                }
            }
        }
            
        return answer;
    }
}