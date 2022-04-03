import java.util.*;


class Main{
    static class Node{
        int val;
        Node next;
        public Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }
    static class LinkedList{
        Node head;
        Node tail;
        static int length = 0;

        public void append(int val){
            if(tail == null){
                insertAtBegining(val);
            }
            else{
                Node newNode = new Node(val, null);
                tail.next = newNode;
                tail = tail.next;
                length++;
            }
        }

        public void insertAtBegining(int val){
            Node newNode = new Node(val, null);
            if(head == null){
                head = newNode;
                tail = newNode;
            }
            else{
                newNode.next = head;
                head = newNode;
            }
            length++;
        }

        public void printList(){
            if(head == null){
                System.out.println("No node available");
            }
            Node itr = head;
            while(itr != null){
                System.out.println(itr.val);
                itr = itr.next;
            }
            System.out.println("*******************");
        }

        public void insertAtPos(int val, int k){
            if(k > length){
                System.out.println("Index out of bound");
                return;
            }
            if(k == 0){
                insertAtBegining(val);
            }
            else{
                Node itr = head;
                while(k--> 1){
                    itr = itr.next;
                }
                Node nxt = itr.next;
                itr.next = new Node(val, nxt);
                length++;
            }
        }

        public int popBack(){
           if(head == null){
               System.out.println("List is empty. Kya kr rha hai tu..");
               return -1;
           }
           else if(head.next == null){
              return popFront();
           }
           else{
               Node itr = head;
               while(itr.next != null && itr.next.next != null){
                   itr = itr.next;
               }
               int value = itr.next.val;
               itr.next = null;
               tail = itr;
               length--;
               return value;
           }
        }

        public int popFront(){
            if(head == null) {
                System.out.println("No node available");
                return -1;
            }
            else{
                int value = head.val;
                head = head.next;
                length--;
                return value;
            }
        }

        public int deleteAtPos(int k){
            if(k >= length){
                System.out.println("Index out of bound");
                return -1;
            }
            if(head == null) {
                System.out.println("No node available");
                return -1;
            }
            if(k == 0){
                return popFront();
            }
            Node itr = head;
            while(itr.next != null && k --> 1){
                itr = itr.next;
            }
            
            if(itr.next == null){
                return popBack();
            }
            int value = itr.next.val;
            itr.next = itr.next.next;
            length--;
            return value;
        }

        static int getLength(){
            return length;
        }
    }

    public static void main(String[] args){
        LinkedList lst = new LinkedList();
        for(int i = 0; i < 5; i++){
            lst.append(i);
        }
        lst.printList();

        lst.insertAtBegining(500);
        lst.printList();

        lst.deleteAtPos(1);
        lst.printList();

        System.out.println("Length : " + LinkedList.getLength());

        lst.insertAtPos(53, 2);
        lst.printList();

        lst.popBack();
        lst.printList();

        lst.popFront();
        lst.printList();

        lst.deleteAtPos(100);

        for(int i = 0; i < 5; i++){
            lst.popBack();
        }
        System.out.println("Length : " + LinkedList.getLength());
        
        lst.insertAtPos(4,1);
        lst.printList();
        
        lst.insertAtPos(88, 0);
        lst.printList();

        System.out.println("Length : " + LinkedList.getLength());

    }
}