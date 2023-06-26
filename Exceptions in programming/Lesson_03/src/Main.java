import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Main {
        public static String[] inputData() {
        String[] data;
        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Введите данные в следующем порядке: Фамилия Имя Отчество Дата рождения Номер телефона Пол");
            String input = scanner.nextLine();

            data = input.split(" ");
            if (data.length != 6) {
                System.out.println("Ошибка: неверное количество данных");
            }else {
                break;
            }
        }
        return data;
        }

        public static void validateData(String[] data){

        }
    public static void main(String[] args) {

        String[] data = inputData();


        String lastName = data[0];
        String firstName = data[1];
        String middleName = data[2];
        String dateOfBirth = data[3];
        String phoneNumber = data[4];
        String gender = data[5];

        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(lastName + ".txt", true));
            writer.write(lastName + " " + firstName + " " + middleName + " " + dateOfBirth + " " + phoneNumber + " " + gender);
            writer.newLine();
            writer.close();
            System.out.println("Данные успешно записаны в файл " + lastName + ".txt");
        } catch (IOException e) {
            System.out.println("Ошибка при записи в файл:");
            e.printStackTrace();
        }
    }

}