package Lesson_03;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Task_01 {

    // Нужно удалить из него четные числа
    public static List<Integer> removeEvenValue(List<Integer> list) {
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) % 2 == 0) {
                list.remove(i);
                i--;
            }
        }
        return list;
    }

    // Найти минимальное значение
    public static Integer getMin(List<Integer> list) {
        int min = list.get(0);
        for (int i = 0; i < list.size(); i++) {
            int item = list.get(i);
            if (item < min) {
                min = item;
            }
        }
        return min;
    }

    // Найти максимальное значение
    public static Integer getMax(List<Integer> list) {
        int max = 0;
        for (int i = 0; i < list.size(); i++) {
            int item = list.get(i);
            if (item > max) {
                max = item;
            }
        }

        return max;
    }

    // Найти среднее значение
    public static Double getAverage(List<Integer> list) {
        double sum = 0;
        for (int i = 0; i < list.size(); i++) {
            sum += list.get(i);
        }
        return sum / list.size();
    }

    // Пусть дан произвольный список целых чисел [3, 5, 2, 6, 1, 8]
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(Arrays.asList(3, 5, 2, 6, 1, 8));

        System.out.println("Исходный список чисел: " + list);
        System.out.println("Максимальный элемент: " + getMax(list));
        System.out.println("Минимальный элемент: " + getMin(list));
        System.out.printf("Среднее значение: %.2f\n", getAverage(list));
        System.out.println("Список без четных чисел: " + removeEvenValue(list));

    }

}
