from avl import BinTree


def main():
    binary = BinTree()

    for _ in range(int(input())):
        command = input().split()
        if command[0] == "add":
            binary.add(int(command[1]))
        elif command[0] == "del":
            binary.delete(int(command[1]))
        elif command[0] == "exists":
            print(binary.exists(int(command[1])))
        elif command[0] == "next":
            print(binary.next_key(int(command[1])))
        elif command[0] == "prev":
            print(binary.prev_key(int(command[1])))
        elif command[0] == "root":
            print(binary.get_root_key())
        elif command[0] == "height":
            print(binary.get_height_from_root())
        elif command[0] == "print":
            print(*binary.print_from_root())

main()
