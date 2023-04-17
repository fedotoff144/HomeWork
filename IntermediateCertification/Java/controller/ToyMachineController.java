package controller;

import model.Repository;

public class ToyMachineController {
    private final Repository repository;

    public ToyMachineController(Repository repository){
        this.repository = repository;
    }

    public void help(){
        repository.getHelp();
    }
}
