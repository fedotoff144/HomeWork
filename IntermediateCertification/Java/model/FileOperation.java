package model;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FileOperation implements Operation {
    private String filename;

    public FileOperation(String filename) {
        this.filename = filename;
        try (FileWriter writer = new FileWriter(filename, true)) {
            writer.flush();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    @Override
    public List<String> readFromFile() {
        List<String> lines = new ArrayList<>();
        try {
            File file = new File(filename);
            FileReader fr = new FileReader(file);
            BufferedReader reader = new BufferedReader(fr);
            String line = reader.readLine();
            if (line != null)
                lines.add(line);
            while (line != null) {
                line = reader.readLine();
                if (line != null) {
                    lines.add(line);
                }
            }
            fr.close();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
        return lines;
    }

    @Override
    public void saveInFile(List<String> lines) {
        try (FileWriter writer = new FileWriter(filename, true)) {
            for (String line : lines) {
                writer.write(line);
                writer.append('\n');
            }
            writer.flush();

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }


    }

}
