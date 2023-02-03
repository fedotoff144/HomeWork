import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Task_02 {
    public static void main(String[] args) {
        // Даны два Deque представляющие два неотрицательных целых числа. Цифры хранятся
        // в обратном порядке,
        // и каждый из их узлов содержит одну цифру.
        // Сложите два числа и верните сумму в виде связанного списка.

        Deque<Integer> d1 = new ArrayDeque<>(Arrays.asList(1, 2, 3));
        Deque<Integer> d2 = new ArrayDeque<>(Arrays.asList(5, 4, 7));
        // result [6,6,0,1]

        System.out.println(sum(d1, d2));

    }

    public static Deque<Integer> sum(Deque<Integer> d1, Deque<Integer> d2) {
        int len = d1.size() < d2.size() ? d1.size() : d2.size();
        Deque<Integer> d3 = new ArrayDeque<>();
        while (len > 0) {
            int temp = d1.pollFirst() + d2.pollFirst();
            if (temp > 9) {
                d3.addLast(temp % 10);
                d3.addLast(1);
            } else {
                d3.addLast(temp);
            }
            len--;
        }
        return new ArrayDeque<>(d3);
    }
}
