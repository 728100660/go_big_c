"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        new_head = None
        node=head
        old_node_id_map = {}       # 旧的每个节点的内存地址列表    key: 老对象的id， val: 老对象
        new_node_id_map = {}       # 新节点的内存地址和对象映射列表 key: 老对象的id， val: 新对象
        while node is not None:
            # 创建新的，如果已经创建过，就用创建过的
            if id(node) in new_node_id_map:
                new_node = new_node_id_map.get(id(node))
            else:
                new_node = Node(node.val)
            if new_head is None:
                new_head = new_node

            if id(node.next) in new_node_id_map:
                new_nex_node = new_node_id_map.get(id(node))
            else:
                new_nex_node = Node(node.val)
            new_node.next = new_nex_node

            if id(node) in new_node_id_map:
                new_rand_node = new_node_id_map.get(id(node))
            else:
                new_rand_node = Node(node.val)
            new_node.random = new_rand_node

            new_node_id_map[id(node)] = new_node
            new_node_id_map[id(node.next)] = new_nex_node
            new_node_id_map[id(node.random)] = new_rand_node

            node = node.next

        return new_head
