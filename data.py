class DataLoader(object):

    def __init__(self, txt_file):
        self.special_markers = ["/a", "/b", "/c", "/o"]
        self.txt_file = txt_file
        self.lines = []
        self._read_file()

    def _read_file(self):
        with open(self.txt_file, "r") as f:
            for line in f.readlines():
                self.lines.append(line.strip())

    def information_count(self):
        res = []
        for line in self.lines:
            cnt = 0
            for marker in self.special_markers:
                if marker in line:
                    cnt += 1
            res.append(cnt)
        return res

    def one_line_operation(self, line):
        data = []
        labels = []

        no_space_line = "".join(line.split("  "))
        characters = no_space_line.split("_")
        cursor = 0
        cut = 0

        while cursor < len(characters):
            marker_index = [characters[cursor].find(
                x) for x in self.special_markers]
            has_marker = [m for m in marker_index if m >= 0]
            if len(has_marker) > 0:
                first_marker = [
                    i for i, j in enumerate(marker_index) if j == min(has_marker)]
                marker = self.special_markers[first_marker[0]]
                try:
                    head, tail = characters[cursor].split(marker)
                except ValueError:
                    head = characters[cursor].split(marker)[0]
                    tail = marker.join(characters[cursor].split(marker)[1:])
                # Before the cursor
                for i in range(cut, cursor):
                    data.append(characters[i])
                    labels.append(marker)
                data.append(head)
                labels.append(marker)
                if tail != "":
                    characters.insert(cursor+1, tail)
                # FIXME
                cut = cursor + 1
                cursor += 1
            else:
                cursor += 1
        if len(characters[cut:cursor-1]) != 0:
            data.append(characters[cut:cursor-1])
        labels += ["/o"] * len(characters[cut:cursor])
        assert len(data) == len(labels), "data:{} and labels: {}Must be the same length".format(
            len(data), len(labels)
        )

        return data, labels

    def multi_operation(self):
        x = []
        y = []
        for i, line in enumerate(self.lines):
            d, l = self.one_line_operation(line)
            x += d
            y += l

        return x, y


def main():
    dl = DataLoader("./datagrand/train.txt")
    # print(len(dl.lines))
    # print(dl.information_count())
    # print(dl.lines[27])
    # data, label = dl.one_line_operation(dl.lines[27])
    # print(data)
    # print(label)
    x, y = dl.multi_operation()
    print(x[:10])
    print(y[:10])
    print(len(x), len(y))
    keywords = []
    for w, l in zip(x, y):
        if l not in dl.special_markers:
            continue

    w2l = {a: b for a, b in zip(x, y)}


if __name__ == '__main__':
    main()
