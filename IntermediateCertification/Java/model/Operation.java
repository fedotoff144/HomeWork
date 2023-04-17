package model;
import java.util.List;

public interface Operation {
    void putAllToys(List<String> toyList);
    List<String> getAllToys();
}
