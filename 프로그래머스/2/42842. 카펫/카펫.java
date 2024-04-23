class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int area = brown + yellow;
        int h = 0;
        
        for (int w = 1; w < area; w++) {
            if (area % w == 0) {
                h = area / w;
                if (brown == 2*(w-2)+2*h) {
                    answer[0] = w;
                    answer[1] = h;
                }
            }
        }
        return answer;
    }
}