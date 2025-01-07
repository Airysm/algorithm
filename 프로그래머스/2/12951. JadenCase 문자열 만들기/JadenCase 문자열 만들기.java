class Solution {
    public String solution(String s) {
        String answer = "";
        String[] s_split = s.split(" ");
        
        for(String str : s_split) {
            if (str.length() > 0) {
                answer += str.substring(0, 1).toUpperCase();
                answer += str.substring(1, str.length()).toLowerCase();
            }
            answer += " ";
        }
        
        if (s.charAt(s.length()-1) != ' ')
            answer = answer.substring(0, answer.length()-1);
        
        return answer;
    }
}