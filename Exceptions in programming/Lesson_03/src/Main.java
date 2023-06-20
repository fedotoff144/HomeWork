import java.util.Scanner;


public class Main {

    static String[] splitData(String data) {

        return data.trim().split("\\s+");
    }

    static boolean isValidateDate(String date) {
        String regex = "\\d{2}\\.\\d{2}\\.\\d{4}";
        return date.matches(regex);
    }

    static boolean isValidName(String data) {
        return data.matches("[a-zA-Z]+");
    }

    static String[] dataInput() {

        while (true) {
            System.out.println("Введите свои Фамилию, Имя, Отчество, дату рождения в формате dd.mm.yyyy, номер телефона и пол в формате f/m");
            String[] data = splitData(prompt());
            if (data.length < 6) {
                System.out.println("Количество данных меньше, чем нужно. Повторите ввод!");
            } else if (data.length > 6) {
                System.out.println("Количество данных больше, чем нужно. Повторите ввод!");
            } else
                return data;
        }

    }


    public static void main(String[] args) {
//        Fedotov Artem Gennadievich 06.01.1987 9607253166 m


    }
}