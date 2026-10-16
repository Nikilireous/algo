class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None
        self.height: int = 1


class BinTree:
    def __init__(self):
        self.root: Node | None = None

    # Высота и балансировка

    def get_height(self, cur_root: Node | None) -> int:
        if cur_root is None:
            return 0
        return cur_root.height

    def get_height_from_root(self) -> int:
        return self.get_height(self.root)

    def update_height(self, cur_root: Node) -> None:
        cur_root.height = 1 + max(self.get_height(cur_root.left), self.get_height(cur_root.right))

    def get_balance(self, cur_root: Node) -> int:
        return self.get_height(cur_root.left) - self.get_height(cur_root.right)

    def to_balance(self, node: Node) -> None:
        cur_root = node

        while cur_root is not None:
            self.update_height(cur_root)
            balance = self.get_balance(cur_root)

            if balance > 1:
                child = cur_root.left
                if child is not None and self.get_balance(child) < 0:
                    self.rotate_left(child)
                self.rotate_right(cur_root)
            elif balance < -1:
                child = cur_root.right
                if child is not None and self.get_balance(child) > 0:
                    self.rotate_right(child)
                self.rotate_left(cur_root)

            cur_root = cur_root.parent

    # Добавление

    def add(self, new: int) -> None:
        if self.root is None:
            self.root = Node(new)
            return

        cur_root = self.root

        while cur_root is not None:
            if cur_root.key > new:
                if cur_root.left is None:
                    cur_root.left = Node(new)
                    cur_root.left.parent = cur_root
                    self.to_balance(cur_root.left)
                    return
                cur_root = cur_root.left
            elif cur_root.key < new:
                if cur_root.right is None:
                    cur_root.right = Node(new)
                    cur_root.right.parent = cur_root
                    self.to_balance(cur_root.right)
                    return
                cur_root = cur_root.right
            else:
                return

    # Удаление

    def delete(self, key: int) -> None:
        to_delete = self.find(key)
        if to_delete is None:
            return

        path = []
        cur_root = self.root
        while cur_root is not to_delete:
            path.append(cur_root)
            if cur_root.key > key:
                cur_root = cur_root.left
            else:
                cur_root = cur_root.right

        if to_delete.left is not None and to_delete.right is not None:
            successor = self.minimum(to_delete.right)
            to_delete.key = successor.key
            to_delete = successor

        child = to_delete.left if to_delete.left is not None else to_delete.right
        parent = to_delete.parent

        if child is not None:
            child.parent = parent

        if parent is None:
            self.root = child
        elif parent.left == to_delete:
            parent.left = child
        else:
            parent.right = child

        if parent is not None:
            self.to_balance(parent)
        elif self.root is not None:
            self.to_balance(self.root)

    # Доп функции

    def get_root_key(self) -> int | str:
        if self.root is None:
            return "Empty"
        return self.root.key

    def next_key(self, key: int) -> int | None:
        cur_root = self.root
        result = None

        while cur_root is not None:
            if cur_root.key >= key:
                result = cur_root.key
                cur_root = cur_root.left
            else:
                cur_root = cur_root.right
        return result

    def prev_key(self, key: int) -> int | None:
        cur_root = self.root
        result = None

        while cur_root is not None:
            if cur_root.key <= key:
                result = cur_root.key
                cur_root = cur_root.right
            else:
                cur_root = cur_root.left
        return result

    def minimum(self, cur_root: Node | None):
        if cur_root.left is None:
            return cur_root
        return self.minimum(cur_root.left)

    def exists(self, key: int) -> str:
        cur_root = self.root
        while cur_root is not None:
            if cur_root.key == key:
                return "YES"
            if cur_root.key > key:
                cur_root = cur_root.left
            else:
                cur_root = cur_root.right
        return "NO"

    def print(self, cur_root: Node | None, to_print: list) -> None:
        if cur_root is not None:
            to_print.append(cur_root.key)
            self.print(cur_root.left, to_print)
            self.print(cur_root.right, to_print)

    def print_from_root(self) -> list:
        to_print = list()
        self.print(self.root, to_print)

        if len(to_print) == 0:
            return ["Empty"]
        return to_print

    def find(self, key: int) -> Node | None:
        cur_root = self.root
        while cur_root is not None:
            if cur_root.key == key:
                return cur_root
            if cur_root.key > key:
                cur_root = cur_root.left
            else:
                cur_root = cur_root.right
        return None

    # Вращение

    def rotate_left(self, to_rotate: Node) -> None:
        child = to_rotate.right
        if to_rotate is None or child is None:
            return

        parent = to_rotate.parent
        child.parent = parent

        if parent is None:
            self.root = child
        elif parent.left == to_rotate:
            parent.left = child
        else:
            parent.right = child

        to_rotate.parent = child

        subtree = child.left
        to_rotate.right = subtree
        if subtree is not None:
            subtree.parent = to_rotate

        child.left = to_rotate

        self.update_height(to_rotate)
        self.update_height(child)

    def rotate_right(self, to_rotate: Node) -> None:
        child = to_rotate.left
        if to_rotate is None or child is None:
            return

        parent = to_rotate.parent
        child.parent = parent
        if parent is None:
            self.root = child
        elif parent.left == to_rotate:
            parent.left = child
        else:
            parent.right = child

        to_rotate.parent = child

        subtree = child.right
        to_rotate.left = subtree
        if subtree is not None:
            subtree.parent = to_rotate

        child.right = to_rotate

        self.update_height(to_rotate)
        self.update_height(child)
