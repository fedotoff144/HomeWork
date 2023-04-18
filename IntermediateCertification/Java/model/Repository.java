package model;

import java.util.List;

public interface Repository {
    String addToy(Toy toy);
    void saveToy(List<Toy> toys);

    void getHelp();
}
