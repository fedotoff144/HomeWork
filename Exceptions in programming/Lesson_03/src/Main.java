import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static String prompt() {
        Scanner scn = new Scanner(System.in);
        String dataLine = scn.nextLine();
        return dataLine;
    }

    static String[] splitData(String data) {
        return data.trim().split("\\s+");
    }

    static boolean isCellEmpty(ArrayList<Object> list, int index) {
        if (list.get(index) != null) {
            return false;
        }
        return true;
    }

    static boolean isValidGender(String gender) {
        if (gender.length() == 1) {
            if (gender.contains("f") || gender.contains("m")) {
                return true;
            }
        }
        return false;
    }

    static boolean isPhoneNumber(String data) {
        try {
            Integer.parseInt(data);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    static boolean isValidateDate(String date) {
        String regex = "\\d{2}\\.\\d{2}\\.\\d{4}";
        return date.matches(regex);
    }

    static String[] dataInput() {
        String[] data;

        while (true) {
            System.out.println("Введите свои Фамилию, Имя, Отчество, дату рождения в формате dd.mm.yyyy, номер телефона и пол в формате f/m");
            data = splitData(prompt());
            if (data.length < 6) {
                System.out.println("Количество данных меньше, чем нужно. Повторите ввод!");
            } else if (data.length > 6) {
                System.out.println("Количество данных больше, чем нужно. Повторите ввод!");
            } else
                return data;
        }

    }


    public static void main(String[] args) {

        String[] data = dataInput();
        ArrayList<Object> fullLine = new ArrayList<>(6);

        for (String item : data) {
            if (isValidGender(item)) {
                fullLine.add(5, item);
            } else if (isValidateDate(item)) {
                fullLine.add(3, item);
            } else if (isPhoneNumber(item)) {
                fullLine.add(4, item);
            }
        }

        System.out.println("Stage 2");

        for (Object item : fullLine) {
            System.out.println(item);
        }

        System.out.println(fullLine.get(5));

    }
}