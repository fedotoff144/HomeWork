package model;

import java.util.ArrayList;
import java.util.List;

public class ToyMachine {
    private int toysCounter;
    private List<Toy> toysList;

    public ToyMachine(){
        this.toysCounter = 0;
        this.toysList = new ArrayList<Toy>();
    }


    public List<Toy> setToysList(){
        return toysList;
    }

    public void getToysList(List<Toy> toysList){
        this.toysList = toysList;
    }

    public void getToysCounter(int toysCounter){
        this.toysCounter = toysCounter;
    }

}
