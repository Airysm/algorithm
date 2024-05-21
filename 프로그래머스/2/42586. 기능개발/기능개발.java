import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer_list = new ArrayList<>();
        int[] progress_days = new int[progresses.length];
        
        for (int i = 0; i < progresses.length; i++) {
            if ((100-progresses[i]) % speeds[i] == 0)
                progress_days[i] = (100-progresses[i]) / speeds[i];
            else
                progress_days[i] = (100-progresses[i]) / speeds[i] + 1;
        }
        
        int max_day = progress_days[0];
        int count = 1;
        for (int i = 1; i < progress_days.length; i++) {
            if (progress_days[i] > max_day) {
                answer_list.add(count);
                max_day = progress_days[i];
                count = 1;
            } else
                count++;
        }
        if (count > 0)
            answer_list.add(count);
        
        int[] answer = new int[answer_list.size()];
        for (int i = 0; i < answer_list.size(); i++)
            answer[i] = answer_list.get(i);
        
        return answer;
    }
}