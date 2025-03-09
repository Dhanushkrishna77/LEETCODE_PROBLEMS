class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevLeft = dummy;
        ListNode current = head;

        for (int i = 0; i < left - 1; i++) {
            prevLeft = prevLeft.next;
            current = current.next;
        }

        ListNode sublistTail = current;
        ListNode prev = null;

        for (int i = 0; i < right - left + 1; i++) {
            ListNode nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }

        prevLeft.next = prev;
        sublistTail.next = current;

        return dummy.next;
    }
}