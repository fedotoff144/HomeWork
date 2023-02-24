package OOP.Lesson_03;

public class Main {

    public static void printList(Node head) {
        Node ptr = head;
        while (ptr != null) {
            System.out.print(ptr.data + " —> ");
            ptr = ptr.next;
        }

        System.out.println("null");
    }

    public static Node constructList() {

        Node first = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);
        Node fourth = new Node(4);

        Node head = first;
        first.next = second;
        second.next = third;
        third.next = fourth;

        return head;
    }

    public static void main(String[] args) {
        Node head = constructList();

        printList(head);
    }
}