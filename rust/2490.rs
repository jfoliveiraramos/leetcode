impl Solution {
    pub fn is_circular_sentence(sentence: String) -> bool {
        let words: Vec<&str> = sentence.split_whitespace().collect();

        for i in 0..words.len() {
            let current_word = words[i];
            let prev_word = words[(i + words.len() - 1) % words.len()];

            if current_word.chars().next() != prev_word.chars().last() {
                return false;
            }
        }
        true
    }
}
