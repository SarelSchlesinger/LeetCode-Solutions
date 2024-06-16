// time complexity: O(n)
// space complexity: O(1)

struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:

    ListNode* reversedLinkedList(ListNode* head) {
        ListNode* prevNode = nullptr;
        ListNode* nextNode = nullptr;
        while (head != nullptr) {
            nextNode = head->next;
            head->next = prevNode;
            prevNode = head;
            head = nextNode;
        }
        return prevNode;
    }

    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* tail = reversedLinkedList(slow);
        while (tail != nullptr) {
            if (tail->val != head->val) return false;
            tail = tail->next;
            head = head->next;
        }
        return true;
    }
};