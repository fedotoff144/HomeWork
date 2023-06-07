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

    public static Node reverse(Node head, Node headRef) {
        Node currentNode = head;

        if (head == null) {
            return headRef;
        }

        if (currentNode.next == null) {
            headRef = currentNode;
            return headRef;
        }

        headRef = reverse(currentNode.next, headRef);

        currentNode.next.next = currentNode;
        currentNode.next = null;

        return headRef;
    }

    public static Node reverse(Node head) {
        return reverse(head, head);
    }

    public static void main(String[] args) {
        int[] values = {1, 2, 3, 4, 5, 6};

        Node head = null;
        for (int i = values.length - 1; i >= 0; i--) {
            head = push(head, values[i]);
        }

        printList(head);
        System.out.println("---------------------------");
        head = reverse(head);
        printList(head);
    }
}