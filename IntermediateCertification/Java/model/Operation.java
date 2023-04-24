package model;
import java.util.List;

public interface Operation {
    void saveInFile(List<String> toyList);
    List<String> readFromFile();
}
