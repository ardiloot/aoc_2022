import re

class Folder:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = {}
        self.files = {}

    def add_dir(self, dir_name):
        if dir_name not in self.dirs:
            self.dirs[dir_name] = Folder(dir_name, self)

    def get_dir(self, dir_name):
        return self.dirs[dir_name]

    def add_file(self, filename, size):
        self.files[filename] = size

    def get_size(self, path=[]):
        osize = 0
        size = sum(self.files.values())
        for dir_name, folder in self.dirs.items():
            dir_size, dir_osize = folder.get_size(path + [dir_name])
            size += dir_size
            osize += dir_osize

        if size <= 100000:
            osize += size
        return size, osize
    

root = Folder("")
cwd = root
lines = list(map(str.strip, open("input.txt").readlines()))
index = 0

while index < len(lines):
    line = lines[index]
    if line == "$ cd /":
        cwd = root
    elif line == "$ cd ..":
        cwd = cwd.parent
    elif line.startswith("$ cd "):
        cwd = cwd.get_dir(line[5:])
    elif line == "$ ls":
        while index + 1 < len(lines) and not lines[index + 1].startswith("$"):
            ls_line = lines[index + 1]
            if ls_line.startswith("dir "):
                cwd.add_dir(ls_line[4:])
            else:
                filesize, filename = re.match("(\d*) (.*)", ls_line).groups()
                cwd.add_file(filename, int(filesize))
            index += 1
    else:
        raise NotImplementedError()
    index += 1

print(root.get_size()[1])
