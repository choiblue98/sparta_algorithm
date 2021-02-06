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

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        new_node = Node(value) # 추가할 새 노드 생성
        node = self.get_node(index-1)  # '인덱스번 째' 노드를 가져와
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        #index_node = node.next
        #new_node = index_node.next

    def delete_node(self,index):
        if index == 0:
            self.head = self.head.next
        else:
            node = self.get_node(index-1)
            next_node = node.next
            node.next = node.next.next
        return

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.add_node(1, 6)
linked_list.delete_node(0)
linked_list.print_all()
