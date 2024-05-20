/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *temp, *prev, *it;

        if (!head)    return NULL;
        if (!head->next)    return head;

        prev = head;
        it = head->next;
        temp = head->next;
        head->next = NULL;

        while (it->next != NULL) {
            temp = it->next;
            it->next = prev;
            prev = it;
            it = temp;
        }
        it->next = prev;
        return it;
    }
};

