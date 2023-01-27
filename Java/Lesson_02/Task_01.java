import java.util.Scanner;
import java.util.logging.*;
import java.io.IOException;
import java.io.FileWriter;

public class Task_01 {
    /*
     * Напишите программу, которая принимает с консоли число в формате byte и
     * записывает его в файл ”result.txt”.
     * Требуется перехватить все возможные ошибки и вывести их в логгер.
     * После написания, попробуйте подать на вход числа 100 и 200 и проследите
     * разницу в результате
     */

    public static void LogWrite(String errors) throws IOException {

        Logger log = Logger.getLogger(Task_01.class.getName());
        FileHandler fh = new FileHandler("log.xml", true);
        log.addHandler(fh);
        XMLFormatter xmlForm = new XMLFormatter();
        fh.setFormatter(xmlForm);
        log.log(Level.INFO, errors + "\n\n");
        fh.close();
    }

    public static String GetByteNumber() throws IOException {

        System.out.print("Enter number in byte format: ");
        String string_num = "";

        try {
            Scanner scn = new Scanner(System.in);
            byte byte_num = scn.nextByte();
            string_num = Byte.toString(byte_num);
            scn.close();

        } catch (Exception ex) {
            LogWrite(ex.toString());
        } finally {
            System.out.println("Operation ended");
        }
        return string_num;
    }

    public static void resultWrite(String str) throws IOException {
        FileWriter fw = new FileWriter("result.txt", true);
        fw.write(str + "\n");
        fw.flush();
        fw.close();
    }

    public static void main(String[] args) throws IOException {

        resultWrite(GetByteNumber());

    }
}
