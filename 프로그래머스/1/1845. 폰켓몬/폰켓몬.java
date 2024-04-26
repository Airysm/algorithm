import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int take = nums.length / 2;
        HashSet<Integer> poketmon = new HashSet<>();
        
        for (int num : nums)
            poketmon.add(num);

        return (poketmon.size() > take) ? take : poketmon.size();
    }
}