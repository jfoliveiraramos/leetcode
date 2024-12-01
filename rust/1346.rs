use std::collections::HashSet;

impl Solution {
    pub fn check_if_exist(arr: Vec<i32>) -> bool {
        let set = arr.iter().cloned().collect::<HashSet<i32>>();
        let mut zero = false;

        for elem in &arr {
            if *elem != 0 {
                if set.contains(&(elem * 2)) {
                    return true;
                }
            } else {
                if zero {
                    return true;
                } else {
                    zero = true
                }
            }
        }
        false
    }
}
