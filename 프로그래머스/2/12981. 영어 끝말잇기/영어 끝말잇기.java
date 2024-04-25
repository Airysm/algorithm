import java.util.HashMap;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        map.put(words[0], 1);
        
        for (int i = 1; i < words.length; i++) {
            if (map.containsKey(words[i]) || words[i-1].charAt(words[i-1].length()-1) != words[i].charAt(0)) {
                answer[0] = i%n+1;
                answer[1] = i/n+1;
                break;
            }
            else
                map.put(words[i], 1);
        }

        return answer;
    }
}