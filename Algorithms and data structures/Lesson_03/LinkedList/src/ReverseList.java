class Node {
    int value;
    Node next;

    Node(int value) {
        this.value = value;
    }
}

class Main {
    public static void printList(Node head) {
        Node currentNode = head;
        while (currentNode != null) {
            System.out.print(currentNode.value + " —> ");
            currentNode = currentNode.next;
        }
        System.out.println("null");
    }

    public static Node push(Node head, int value) {
        Node newNode = new Node(value);
        newNode.next = head;
        return newNode;
    }

    public static Node reverse(Node head) {
        Node prev = null;
        Node curr = head;
        while (curr != null) {
            Node temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }

    public static void main(String[] args) {
        int[] values = {1, 2, 3, 4, 5, 6};

        Node head = null;
        for (int i = values.length - 1; i >= 0; i--) {
            head = push(head, values[i]);
        }

        printList(head);
        System.out.println("----------------------------------");
        head = reverse(head);
        printList(head);
    }
}