import java.io.File;

public class Main {

    public static Integer methodOne(int[] arr, int n) {
        return arr[n];
    }

    public static Integer methodTwo(int m, int n) {
        return m / n;
    }

    public static Integer methodThree() {
        return Integer.parseInt("1a");
    }

    public static void methodFour(int[] arrFirst, int[] arrSecond) {
        int[] result = new int[arrFirst.length];
        if (arrFirst.length == arrSecond.length) {
            for (int i = 0; i < arrFirst.length; i++) {
                result[i] = arrFirst[i] - arrSecond[i];
            }
            for (int i = 0; i < result.length; i++) {
                System.out.print(result[i] + "  ");
            }
        } else {
            System.out.println("Массивы не равны!");
        }
    }

    public static void main(String[] args) {

// Реализуйте 3 метода, чтобы в каждом из них получить разные исключения
// Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?

        // method 1 ArrayIndexOutOfBoundsException
        int[] arr = {1, 2, 3, 4, 5};
//        methodOne(arr, 6);

        // method 2 -> ArithmeticException
//        methodTwo(10, 0);

        // method 3 -> NumberFormatException
//        methodThree();


// Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
// и возвращающий новый массив, каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке.
// Если длины массивов не равны, необходимо как-то оповестить пользователя.
        int[] arrFirst = {1, 7, 3, 9};
        int[] arrSecond = {6, 2, 8, 4, 10};
        methodFour(arrFirst, arrSecond);

// * Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив, каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке. Если длины массивов не равны, необходимо как-то оповестить пользователя. Важно: При выполнении метода единственное исключение, которое пользователь может увидеть - RuntimeException, т.е. ваше.
    }
}
