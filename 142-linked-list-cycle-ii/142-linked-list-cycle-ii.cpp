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
    ListNode *detectCycle(ListNode *head) {
        if(!head || head->next == NULL){
            return NULL;
        }
        ListNode* rabbit = head->next->next;
        ListNode* turtle = head->next;
        while(rabbit && rabbit->next && turtle != rabbit){
            rabbit = rabbit->next->next;
            turtle = turtle ->next;
        }
        if(turtle != rabbit){
            return NULL;
        }
        turtle = head;
        while(turtle != rabbit){
            rabbit = rabbit->next;
            turtle = turtle->next;
        }
        return rabbit;


    }
};