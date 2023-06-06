public class List {
    public static class sList {
        Node head;

        private static class Node {
            int value;
            Node next;
            Node prev;
        }

        public void add(int value) {
            Node newNode = new Node();
            newNode.value = value;
            newNode.next = head;
            head = newNode;
        }

        public void reverse() {
            Node currentNode=head;
            currentNode.prev = null;

            while (currentNode != null){
                Node temp = currentNode.next;
                currentNode.next=currentNode.prev;
                currentNode.prev=currentNode;
                currentNode=temp;
            }
        }

        public void print() {
            Node currentNode = head;
            if (head != null) {
                System.out.println(head.value);
                while (currentNode.next != null) {
                    currentNode = currentNode.next;
                    System.out.println(currentNode.value);
                }
            }
        }


        public static void main(String[] args) {
            sList list = new sList();

            list.add(1);
            list.add(2);
            list.add(3);

            list.print();

            list.reverse();
            System.out.println("----------------------------------");

            list.print();
        }

    }

}
