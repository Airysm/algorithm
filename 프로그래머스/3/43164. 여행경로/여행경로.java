import java.util.ArrayList;
import java.util.Collections;

class Solution {
    
    ArrayList<String> list = new ArrayList<>();
    Boolean[] useTickets;
    
    public String[] solution(String[][] tickets) {
        useTickets = new Boolean[tickets.length];
        for (int i = 0; i < useTickets.length; i++)
            useTickets[i] = false;
        
        dfs(0, "ICN", "ICN", tickets);
        Collections.sort(list);
        
        return list.get(0).split(" ");
    }
    
    public void dfs(int depth, String now, String path, String[][] tickets) {
        if (depth == tickets.length) {
            list.add(path);
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            if (!useTickets[i] && now.equals(tickets[i][0])) {
                useTickets[i] = true;
                dfs(depth+1, tickets[i][1], path + " " + tickets[i][1], tickets);
                useTickets[i] = false;
            }
        }
    }
}