package View;

import Model.Data;

import java.util.Scanner;

public class ViewData {
    static Data dataInput() {
        while (true){
            try {
                String lastName = prompt("Введите фамилию: ");

            }catch (Exception e){
                System.out.println("Что-то пошло не так..." + e);
            }
        }
    }
    static String prompt(String message) {
        System.out.print(message + ": ");
        Scanner scn = new Scanner(System.in);
        return scn.nextLine();
    }
}
