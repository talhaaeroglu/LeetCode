/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL) return false;
        ListNode *trav1 = head;
        ListNode *trav2 = head->next;
        
        while(trav1 != trav2){
            if(trav2 == NULL || trav2->next == NULL){
                return false;
            }
            trav1 = trav1->next;
            trav2 = trav2->next->next;
        }
        return true;
    }
};