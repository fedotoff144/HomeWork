package model;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class RepositoryFile implements Repository {
    private ToyMapper mapper = new ToyMapper();
    private FileOperation fileOperation;

    public RepositoryFile(FileOperation fileOperation) {
        this.fileOperation = fileOperation;
    }

    @Override
    public String addToy(Toy toy) {
        String nameToy = view.ToyMachineMenu.prompt("Введите название игрушки: ");
        List<Toy> toys = getListToys();
        int winning = getIntRandom(100);
        int newId = 1;
        for(Toy item : toys){
            int id = item.getId();
            if(newId == id){
                newId++;
            }
        }
        toy.setId(newId);
        toy.setName(nameToy);
        toy.setWinning(winning);

        return mapper.map(toy);
    }

    @Override
    public void saveToy(String toys) {
        List<String> toy = new ArrayList<>();
        toy.add(toys);
        fileOperation.saveInFile(toy);
    }

    @Override
    public List<Toy> getListToys(){
        List<String> toysInMachine = fileOperation.readFromFile();
        List<Toy> toysList = new ArrayList<>();
        for(String item : toysInMachine){
            toysList.add(mapper.map(item));
        }
        return toysList;
    }

    public int getIntRandom(int count){
        Random rnd = new Random();
        int rndNum = rnd.nextInt(count);
        return rndNum;
    }

    public void getHelp() {
        System.out.println("-------------------------------------");
        System.out.println("ADD_TOYS - добавить игрушку в автомат\nWIN_TOY - разыграть игрушку\nVIEW_TOYS - посмотреть все игрушки в автомате\nEXIT - выход");
    }

}
