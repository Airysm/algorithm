import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer num1, Integer num2) {
                return num1 - num2;
            }
        });
        
        for (int s : scoville)
            pq.offer(s);
        
        int count = 0;
        while (pq.size() > 1) {
            if (pq.peek() < K) {
                pq.offer(pq.poll() + pq.poll()*2);
                count++;
            }
            else
                break;
        }
        
        if (pq.size() == 1 && pq.peek() < K)
            return -1;
        return count;
    }
}