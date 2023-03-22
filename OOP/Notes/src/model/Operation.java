package model;

import java.util.List;

public interface Operation {
    void SaveAllLines(List<String> lines);

    List<String> ReadAllLines();
}
