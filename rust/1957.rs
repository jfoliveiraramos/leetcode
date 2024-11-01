impl Solution {
    pub fn make_fancy_string(s: String) -> String {
        let mut res = String::new();
        let mut c1: Option<char> = None;
        let mut c2: Option<char> = None;

        for c in s.chars() {
            if Some(c) != c1 || Some(c) != c2 {
                res.push(c);
                c2 = c1;
                c1 = Some(c);
            }
        }
        res
    }
}
