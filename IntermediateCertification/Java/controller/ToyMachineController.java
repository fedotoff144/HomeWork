package controller;

import model.Repository;
import model.Toy;

import java.util.List;

public class ToyMachineController {
    private final Repository repository;

    public ToyMachineController(Repository repository){
        this.repository = repository;
    }

    public void addToy(){
        repository.saveToy(repository.addToy(new Toy()));
    }

    public void viewAllToys(){
        for(Toy item : repository.getListToys()){
            System.out.println(item);
        }
    }
    public void help(){
        repository.getHelp();
    }
}
