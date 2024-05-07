import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> list = new ArrayList<>();
        int[] remain_days = new int[progresses.length];
        
        for (int i = 0; i < progresses.length; i++) {
            int remain = 100 - progresses[i];
            remain_days[i] = remain / speeds[i];
            if (remain % speeds[i] != 0)
                remain_days[i] += 1;
        }
        
        int max_days = remain_days[0];
        int count = 1;
        
        for (int i = 1; i < remain_days.length; i++) {
            if (max_days < remain_days[i]) {
                list.add(count);
                count = 1;
                max_days = remain_days[i];
            }
            else
                count += 1;
        }
        list.add(count);
        
        int[] answer = new int[list.size()];
        
        for (int i = 0; i < list.size(); i++)
            answer[i] = list.get(i);
        
        return answer;
    }
}