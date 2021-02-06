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

    def get_kth_node_from_last(self, k):
        # while k is not None:          -> 내가 생각했던 거: 끝 애를 헤드로 잡자
        #     linked_list[-1] = self.head
        #     node = self.head
        #     count = 1
        #     while count < k:
        #         node = node.next
        #         count += 1

        # length = 1                    -> 전체 길이를 구해서 k를 빼면 k번 째 노드!
        # cur = self.head
        # while cur.next is not None:
        #     cur = cur.next
        #     length += 1
        #
        # last_length = length - k
        # cur = self.head
        # for i in range(last_length):
        #     cur = cur.next
        #     return cur

        fast = self.head
        slow = self.head
        for i in range(k):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)