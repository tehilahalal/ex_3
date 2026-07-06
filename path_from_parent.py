def path_from_parent(parent, target):
    path = []

    while target is not None:
        path.append(target)
        target = parent[target]

    path.reverse()
    return path


def main():
    parents = {
        0: None,
        1: 0,
        2: 0,
        3: 1,
        4: 3
    }

    path = path_from_parent(parents, 4)
    print(path)


if __name__ == "__main__":
    main()
