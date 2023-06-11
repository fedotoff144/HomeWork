import java.util.Scanner;
public class Task_04 {

    public static void emptyInput(){
        Scanner scn = new Scanner(System.in);
        String str = scn.nextLine();

        if(str.isEmpty()){
            System.out.println("Blank strings cannot be entered!");
        }
        System.out.println(str);
    }
    public static void main(String[] args) {
        // 4. Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
        // Пользователю должно показаться сообщение, что пустые строки вводить нельзя.

        emptyInput();
    }
}
