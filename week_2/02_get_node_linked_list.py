class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head # ->  "인덱스번 째" 를 찾아야된다는 건 헤드노드로부터 '인덱스번' 이동해야 됨.
        count = 0 # 숫자를 세기 위한 변수
        while count < index:
            node = node.next
            count += 1
        return node

        return cur

linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!