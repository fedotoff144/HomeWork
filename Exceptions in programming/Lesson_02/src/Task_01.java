import java.util.InputMismatchException;
import java.util.Scanner;

public class Task_01 {

    public static float prompt() {
        float num = 0F;
        while (true) {
            Scanner scn = new Scanner(System.in);
            System.out.print("Enter double number please: ");
            try {
                num = scn.nextFloat();
                return num;
            } catch (InputMismatchException e) {
                System.out.println("You're wrong, try again please");
            } finally {
                System.out.println("Accepted");
            }
        }
    }

    public static void main(String[] args) {

        // 1. Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
        //    и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения,
        //    вместо этого, необходимо повторно запросить у пользователя ввод данных.

        System.out.println(prompt());
    }
}
