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
    /*

    Метод reverse разворачивает связный список. Он принимает два аргумента:
    головной узел списка и ссылку на головной узел, которая используется для возврата развернутого списка.
    Первым делом создается переменная currentNode, которая указывает на головной узел списка.
    Затем проверяется, является ли головной узел null. Если это так, то возвращается ссылка на головной узел headRef.
    Если следующий узел currentNode.next равен null, то головной узел становится последним узлом,
    и ссылка на него сохраняется в headRef. Затем метод возвращает headRef.
    Если следующий узел currentNode.next не равен null, то метод вызывает сам себя
    для следующего узла currentNode.next и сохраняет возвращаемую ссылку в headRef.
    Это происходит рекурсивно, пока не будет достигнут конец списка.
    После того, как рекурсивный вызов завершен, метод меняет ссылки между
    текущим узлом currentNode и следующим узлом currentNode.next, чтобы развернуть список.
    Сначала устанавливается ссылка на следующий узел currentNode.next.next равной текущему узлу currentNode.
    Затем ссылка на следующий узел currentNode.next устанавливается равной null,
    чтобы разорвать связь между текущим и следующим узлами.
    Наконец, метод возвращает ссылку на головной узел headRef, который теперь указывает на последний узел списка,
    а все узлы списка развернуты в обратном порядке.
    Machinet AI
     */

    public static Node reverse(Node head) {
        return reverse(head, head);
    }

    public static void main(String[] args) {
        int[] values = {1, 2, 3, 4};

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