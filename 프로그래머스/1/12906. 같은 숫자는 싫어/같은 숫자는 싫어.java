import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> st = new Stack<>();
        
        for (int a : arr) {
            if (st.isEmpty())
                st.push(a);
            else {
                if (st.peek() != a)
                    st.push(a);
            }
        }
        
        int[] answer = new int[st.size()];
        
        for (int i = 0; i < st.size(); i++)
            answer[i] = st.get(i);
        
        return answer;
    }
}