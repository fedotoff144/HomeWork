public class Main {
    public static class LinkedList {
    private Node head;

    public LinkedList() {
        head = null;
    }

    public class Node {
        public int value;
        public Node next;

        public Node(int value) {
            this.value = value;
            next = null;
        }
    }

    public void add(int value) {
        Node newNode = new Node(value);
        Node currentNode = head;

        if (head == null) {
            head = newNode;
        } else {
            while (currentNode.next != null) {
                currentNode = currentNode.next;
            }
        }
    }

    public void remove(int value) {
        Node currentNode = head;
        Node previousNode = null;

        while (currentNode.next != null) {
            if (currentNode.value == value) {
                if (currentNode == head) {
                    head = currentNode.next;
                } else {
                    previousNode.next = currentNode.next;
                }
            }
            previousNode = currentNode;
            currentNode = currentNode.next;
        }
    }

//    public void print() {
//        Node currentNode = head;
//        if (head != null) {
//            System.out.println(head.value);
//        }
//        while (currentNode.next != null) {
//            currentNode = currentNode.next;
//            System.out.println(currentNode.value);
//        }
//    }
        void print() {
        LinkedList.Node current = head;
        while (current != null) {
            System.out.println(current.value);
            current = current.next;
        }
    }
}
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.add(10);
        list.add(8);
        list.add(5);

        list.print();

//        list.remove(10);
//        list.print();
    }
}
