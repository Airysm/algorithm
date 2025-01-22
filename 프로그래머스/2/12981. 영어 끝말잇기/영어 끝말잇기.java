import java.util.HashMap;

class Solution {
    public int[] solution(int n, String[] words) {
        HashMap<Integer, String> map = new HashMap<Integer, String>();
        int[] answer = new int[2];
        int i;
        
        map.put(0, words[0]);
        for (i = 1; i < words.length; i++) {
            String w = words[i];
            if (map.containsValue(w) || (w.charAt(0) != words[i-1].charAt(words[i-1].length()-1)))
                break;
            map.put(i, w);
        }
        
        if (map.size() == words.length) {
            answer[0] = 0;
            answer[1] = 0;
        } else {
            answer[0] = i%n+1;
            answer[1] = i/n+1;
        }
        
        return answer;
    }
}