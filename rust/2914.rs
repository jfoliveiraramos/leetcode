impl Solution {
    pub fn min_changes(s: String) -> i32 {
        let mut changes = 0;
        let mut chars = s.chars();

        while let Some(c1) = chars.next() {
            if let Some(c2) = chars.next() {
                if c1 != c2 {
                    changes += 1;
                }
            }
        }

        changes
    }
}
