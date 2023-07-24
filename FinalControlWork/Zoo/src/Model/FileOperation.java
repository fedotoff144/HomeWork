package Model;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FileOperation {
    private String filename;

    public FileOperation(String fileName) {
        this.filename = filename;
        try (FileWriter writer = new FileWriter(filename, true)) {
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public List<String> ReadAllLines() {
        List<String> lines = new ArrayList<>();
        try {
            File file = new File(filename);
            //создаем объект FileReader для объекта File
            FileReader fr = new FileReader(file);
            //создаем BufferedReader с существующего FileReader для построчного считывания
            BufferedReader reader = new BufferedReader(fr);
            // считаем сначала первую строку
            String line = reader.readLine();
            if (line != null) {
                lines.add(line);
            }
            while (line != null) {
                // считываем остальные строки в цикле
                line = reader.readLine();
                if (line != null) {
                    lines.add(line);
                }
            }
            fr.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lines;
    }

    public void SaveAllLines(List<String> lines) {
        try (FileWriter writer = new FileWriter(filename, false)) {
            for (String line : lines) {
                // запись всей строки
                writer.write(line);
                // запись по символам
                writer.append('\n');
            }
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }
}
