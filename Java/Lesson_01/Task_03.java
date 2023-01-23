public class Task_03 {
    public static void main(String[] args) {
        // Напишите программу, которая выводит на консоль простые числа в промежутке от
        // [2, 100].
        // Используйте для решения этой задачи оператор "%" (остаток от деления) и
        // циклы.


        // Создаем массив от 0 до 100
        int[] arr = new int[100];
        for (int i = 0; i <= arr.length - 1; i++) {
            arr[i] = i + 1;
            // System.out.print(arr[i] + " ");
        }

        // Выводим простые числа
        System.out.println("Prime numbers from 0 to 100 are: ");
        for (int i = 1; i < arr.length; i++) {
            if ((arr[i] == 2) || (arr[i] == 3) || (arr[i] == 5)
                    || (arr[i] % 2 != 0) && (arr[i] % 3 != 0) && (arr[i] % 5 != 0)) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }
}
