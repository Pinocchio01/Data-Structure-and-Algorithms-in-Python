# -*- coding: UTF-8 -*-

# 链表移除元素：删除链表的倒数第二个元素，返回删除后的链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_second_last(head):
    # 创建哑节点，用于处理删除头节点的情况
    dummy = ListNode(0)
    dummy.next = head

    # 初始化快慢指针
    slow = dummy
    fast = dummy.next

    # 快指针先走n步
    n = 1
    while n > 0 and fast:
        fast = fast.next
        n -= 1

    # 快慢指针一起走，直到快指针走到链表末尾
    while fast and fast.next: # 先判断fast是否为空，为空则False结束循环，不会判断fast.next而抛出异常
        slow = slow.next
        fast = fast.next

    # 删除倒数第二个节点
    slow.next = slow.next.next

    # 返回头节点
    return dummy.next

if __name__ == '__main__':

    # 创建一个示例链表
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # 打印原始链表
    print("原始链表：")
    cur = node1
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

    # 删除倒数第二个节点
    remove_second_last(node1)

    # 打印删除后的链表
    print("删除倒数第二个节点后的链表：")
    cur = node1
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
