impl Solution {
    pub fn compressed_string(word: String) -> String {
        let mut marker = 0;
        let mut previous: Option<char> = None;
        let mut res = String::new();

        for (i, c) in word.char_indices() {
            if Some(c) != previous || i - marker == 9 {
                if let Some(prev_char) = previous {
                    res += &format!("{}{}", i - marker, prev_char);
                }
                previous = Some(c);
                marker = i;
            }
        }

        if let Some(last_char) = previous {
            res += &format!("{}{}", word.len() - marker, last_char);
        }

        res
    }
}
