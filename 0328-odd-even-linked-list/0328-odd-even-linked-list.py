class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        values = []

        # Odd positions
        temp = head
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        # Even positions
        temp = head.next
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        # Put values back
        temp = head
        index = 0

        while temp:
            temp.val = values[index]
            index += 1
            temp = temp.next

        return head