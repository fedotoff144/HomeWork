package model;

import java.util.List;

public interface Repository {
    void addToy(Toy toy, String nameToy, int count);

    void winToy();

    List<Toy> getListToys();

    void getHelp();
}
