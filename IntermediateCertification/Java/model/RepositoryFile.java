package model;

import java.util.ArrayList;
import java.util.List;

public class RepositoryFile implements Repository {
    private ToyMapper mapper = new ToyMapper();
    private FileOperation fileOperation;

    @Override
    public String addToy(Toy toy) {
        List<Toy> toys = new ArrayList<>();

        return null;
    }

    @Override
    public void saveToy(List<Toy> toys) {

    }

    public void getHelp() {
        System.out.println("-------------------------------------");
        System.out.println("ADD_TOYS - добавить игрушку в автомат\nWIN_TOY - разыграть игрушку\nVIEW_TOYS - посмотреть все игрушки в автомате\nEXIT - выход");
    }

}
