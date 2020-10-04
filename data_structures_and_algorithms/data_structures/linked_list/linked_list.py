class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

    @staticmethod
    def print_node(node):
        ref = node
        values = []

        while (ref):
            values.append(ref.val)
            ref = ref.next
        
        print('--->'.join([str(i) for i in values]))


def remove_duplicates(node):
    ref = node
    values = set()

    while(ref):
        next_ref = ref.next
        if ref.val not in values:
            values.add(ref.val)
        
        #  check duplicates
        if next_ref and next_ref.val in values:
            ref.next = next_ref.next
        else:
            ref = next_ref

    return node

def main():
    # Test the Linked List
    # test_ll = ListNode(1, ListNode(2, ListNode(3)))
    # ListNode.print_node(test_ll)

    # Test remove duplicates
    # rm_duplicates_list_1 = ListNode(1, ListNode(1, ListNode(1)))
    # rm_duplicates_list_2 = ListNode(1, ListNode(2, ListNode(1)))
    # rm_duplicates_list_3 = ListNode(1, ListNode(2, ListNode(3)))
    # rm_duplicates_list_4 = ListNode(1, ListNode(2, ListNode(3, ListNode(1, ListNode(2, ListNode(3, ListNode(1, ListNode(2, ListNode(3)))))))))

    # ListNode.print_node(remove_duplicates(rm_duplicates_list_1))
    # ListNode.print_node(remove_duplicates(rm_duplicates_list_2))
    # ListNode.print_node(remove_duplicates(rm_duplicates_list_3))
    # ListNode.print_node(remove_duplicates(rm_duplicates_list_4))



if __name__ == '__main__':
    main()