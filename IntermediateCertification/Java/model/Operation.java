package model;
import java.util.List;

public interface Operation {
    void saveAllLines(List<String> toyList);
    List<String> readAllLines();
}
