impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i = 1;
        let mut count = 1;

        while i < nums.len() {
            if (nums[i] == nums[i - 1]) {
                nums.remove(i);
            } else {
                i += 1;
                count += 1;
            }
        }
        count
    }
}
