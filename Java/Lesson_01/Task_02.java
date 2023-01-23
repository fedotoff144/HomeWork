import java.util.Scanner;

public class Task_02 {
    public static void main(String[] args) {
        // Реализуйте алгоритм сортировки пузырьком для сортировки массива

        // Запрашиваем размер массива у пользователя
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter size of array: ");
        int size = scn.nextInt();
        scn.close();

        // Создаем массив опеределенного размера заполняя его рандомно от 0 до 100 и
        // выводим в консоль
        System.out.print("Primary array: ");
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = (int) (Math.random() * 101);
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        // Сортируем созданный массив
        int temp;
        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        // Выводим отсортированный массив
        System.out.print("Sorted array: ");
        for (int item : arr) {
            System.out.print(item + " ");
        }
        System.out.println();

    }
}
