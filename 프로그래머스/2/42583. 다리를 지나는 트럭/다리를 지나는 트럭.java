import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> q = new LinkedList<>();
        int time = 0;
        int weight_now = 0;
        
        for (int truck : truck_weights) {
            while (true) {
                if (q.isEmpty()) {
                    q.offer(truck);
                    weight_now += truck;
                    time++;
                    break;
                }
                else if (bridge_length == q.size()) {
                    weight_now -= q.poll();
                }
                else {
                    if (weight_now + truck <= weight) {
                        q.offer(truck);
                        weight_now += truck;
                        time++;
                        break;
                    }
                    else {
                        q.offer(0);
                        time++;
                    }
                }
            }
        }
        
        return time + bridge_length;
    }
}