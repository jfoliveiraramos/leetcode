from typing import List

class Solution:

    def subfolder(self, folder: str, dirs: set) -> bool:

        i = 0
        while True:
            i = folder.find('/', i + 1)
            if i == -1:
                return False

            if folder[0: i] in dirs:
                return True

    def removeSubfolders(self, folder: List[str]) -> List[str]:

        dirs = set(folder)

        for f in folder:
            if self.subfolder(f, dirs):
                dirs.remove(f)

        return list(dirs)
