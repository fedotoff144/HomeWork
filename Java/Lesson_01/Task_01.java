import java.util.Scanner;

public class Task_01 {
    public static void main(String[] args) {
        // Заполните массив случайным числами и выведите максимальное, минимальное и
        // среднее значение.
        // Для генерации случайного числа используйте метод Math.random(), который
        // возвращает значение в промежутке [0, 300].


        // Запрашиваем размер массива у пользователя
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int size = scn.nextInt();
        scn.close();

        // Задаем массив указанного размера
        int[] arr = new int[size];

        // В промежутке от 0 до 300 заполняем рандомно массив и выводим в консоль
        System.out.print("Primery array: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) (Math.random() * 301);
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        // Ищем среднее значение массива и выводим в консоль
        double average;
        double sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        average = sum / arr.length;
        System.out.println("Array mean: " + average);

        // Ищем максимальное и минимальное значени массива
        int max = arr[0];
        int min = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        System.out.println("Maximal value of array: " + max);
        System.out.println("Minimal value of array: " + min);
    }
}