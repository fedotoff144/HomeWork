package model;

import java.util.List;

public interface Repository {
    String addToy(Toy toy);
    void saveToy(String toys);
    List<Toy> getListToys();

    void getHelp();
}
