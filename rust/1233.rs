// 1233. Remove Sub-Folders from the Filesystem

use std::collections::HashSet;

impl Solution {
    pub fn is_subfolder(folder: &str, dirs: &HashSet<&str>) -> bool {
        let mut i = 0;

        loop {
            i = match folder[i + 1..].find('/') {
                Some(index) => index + i + 1,
                None => return false,
            };

            if dirs.contains(&folder[0..i]) {
                return true;
            }
        }
    }

    pub fn remove_subfolders(folder: Vec<String>) -> Vec<String> {
        let mut dirs: HashSet<&str> = folder.iter().map(|f| f.as_str()).collect();

        for f in &folder {
            if Self::is_subfolder(f, &dirs) {
                dirs.remove(f.as_str());
            }
        }

        dirs.into_iter().map(|f| f.to_string()).collect()
    }
}
