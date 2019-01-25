def search_array(array_list, item):
    for i in range(len(array_list)):
        if array_list[i] == item:
            return True
    return False


def search_singly_linked_list(linked_list, item):
    cur = linked_list.head
    while cur:
        if cur.value == item:
            return True
        cur = cur.next
    return False


def search_doubly_linked_list(linked_list, item):
    cur = linked_list.header.next
    trailer = linked_list.trailer
    while cur != trailer:
        if cur.value == item:
            return True
        cur = cur.next
    return False
