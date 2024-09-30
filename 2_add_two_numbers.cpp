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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

    //ListNode l3temp=ListNode();
    //ListNode* l3=&l3temp;
        int temp=0;
        ListNode* l3=new ListNode;
        *l3=ListNode(l1->val+l2->val);
        
        if(l1->val+l2->val > 9) {
            temp=1;
            l3->val=(l3->val % 10);
        }
        
        
        ListNode* l3head=l3;
        int i=0,j=0;
        ListNode* l1head=l1;
        ListNode* l2head=l2;

        while(l1head!=nullptr){
             i++;
             l1head=l1head->next;
         }
        while(l2head!=nullptr){
            j++;
            l2head=l2head->next;
        }
        int length=(i>j)? i:j;
    
        
        l1head=l1;l2head=l2;
        for (i=1;i<length;i++){
            if(l1->next!=nullptr){
                l1=l1->next;
            }
            else{
                l1->val=0;
            }
            if(l2->next!=nullptr){
                l2=l2->next;
            }
            else{
                l2->val=0;
            }            
         
            l3head->next=new ListNode(l1->val+l2->val+temp);
            if ((l1->val+l2->val+temp) >9){
                l3head->next=new ListNode((l1->val+l2->val+temp)%10);
                temp=1;
            }
            else{
                temp=0;
            }
            
            l3head=l3head->next;
        }
        
        if (temp==1){
            l3head->next=new ListNode(1);
        }
        
        
 
    return l3;
    }
};