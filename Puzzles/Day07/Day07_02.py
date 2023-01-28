from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
"""


def get_combinations(array, n):

    if n == 0:
        return [[]]
    combinations = []
    for i in range(0, len(array)):
        anchor = array[i]
        rest = array[i+1:]
        rest_combo = get_combinations(rest, n - 1)
        for p in rest_combo:
            combinations.append([anchor, *p])
    return combinations


def answer(s):
    command_responses = [i.strip() for i in s.split("$") if len(i.strip()) != 0]
    directory_stack = ["/"]
    folders = {}
    for cr in command_responses:
        command = cr.split("\n")[0]
        responses = cr.split("\n")[1:]

        if command[:2] == "cd":
            destination = command.split()[1].strip()
            if destination == "..":
                directory_stack.pop()
            elif destination == "/":
                directory_stack = ["/"]
            else:
                directory_stack.append(destination)
        if command[:2] == "ls":
            folders["".join(directory_stack)] = responses

    folder_sizes = {}
    # this is brute force - is there a more efficient way to do this?
    while True:
        if len(folder_sizes) == len(folders):
            break
        for k, v in folders.items():
            if k in folder_sizes.keys():
                continue
            completable = True
            size = 0
            for i in v:
                if i[:3] == "dir":
                    inner_dir = k+i.split()[1].strip()
                    if folder_sizes.get(inner_dir) is None:
                        completable = False
                        break
                    else:
                        size += folder_sizes.get(inner_dir)
                elif completable:
                    size += int(i.split()[0].strip())
            if completable:
                folder_sizes[k] = size
    space_required = 30000000 - (70000000 - folder_sizes["/"])
    return sorted([v for v in folder_sizes.values() if v >= space_required])[0]


if __name__ == "__main__":
    test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    expected_output = "24933642"

    answer_checker = AnswerChecker()
    answer_checker.check(expected_output, answer(test_input))
    answer_checker.generate_puzzle_output(__file__, answer)

    # answer_checker.generate_next_day_files(__file__)

