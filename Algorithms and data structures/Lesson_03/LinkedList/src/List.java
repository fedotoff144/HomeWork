public class List {
    public static class sList {
        Node head;

        private static class Node {
            int value;
            Node next;
            Node prev;
        }

        public void addToTop(int value) {
            Node newNode = new Node();
            newNode.value = value;
            newNode.next = head;
            head = newNode;
        }

        public void addToEnd(int value) {
            Node newNode = new Node();
            newNode.value = value;
            Node currentNode = head;

            if (currentNode != null) {
                while (currentNode.next != null) {
                    currentNode = currentNode.next;
                }
                currentNode.next = newNode;
            } else {
                head = newNode;
            }
        }

        public void reverseList() {
            Node currentNode = head;
            currentNode.prev = null;

            while (currentNode.next != null) {
                Node temp = currentNode.next;
                currentNode.next = currentNode.prev;
                currentNode.prev = currentNode;
                currentNode = temp;

            }
        }

        public void print() {
            Node currentNode = head;
            if (head != null) {
                System.out.print(head.value + " ");
                while (currentNode.next != null) {
                    currentNode = currentNode.next;
                    System.out.print(currentNode.value + " ");
                }
            }
        }


        public static void main(String[] args) {
            sList list = new sList();

            list.addToTop(1);
            list.addToTop(2);
            list.addToTop(3);
            list.addToTop(4);            list.print();

            System.out.println("\n------");

            list.reverseList();
            list.print();

        }

    }

}
