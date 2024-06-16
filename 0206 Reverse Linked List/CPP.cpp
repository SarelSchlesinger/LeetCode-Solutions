struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// first approach - using stack
// time complexity: O(n)
// space complexity: O(n)
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) return nullptr;
        stack<ListNode*> stack;
        while (head != nullptr) {
            stack.push(head);
            head = head->next;
        }
        ListNode *newHead = stack.top();
        stack.pop();
        ListNode *tail = newHead;
        while (!stack.empty()) {
            tail->next = stack.top();
            stack.pop();
            tail = tail->next;
        }
        tail->next = nullptr;
        return newHead;
    }
};

// second approach - using two pointers
// time complexity: O(n)
// space complexity: O(1)
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *prevNode = nullptr, *nextNode = nullptr;
        while (head != nullptr) {
            nextNode = head->next;
            head->next = prevNode;
            prevNode = head;
            head = nextNode;
        }
        return prevNode;
    }
};