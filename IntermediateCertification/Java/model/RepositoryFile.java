package model;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class RepositoryFile implements Repository {
    private final ToyMapper mapper = new ToyMapper();
    private final FileOperation fileOperation;

    public RepositoryFile(FileOperation fileOperation) {
        this.fileOperation = fileOperation;
    }

    @Override
    public void addToy(Toy toy, String nameToy, int count) {
        for (int i = 0; i < count; i++) {
            int winning = getIntRandom(100);
            int newId = findId();
            toy.setId(newId);
            toy.setName(nameToy);
            toy.setWinning(winning);
            saveToy(mapper.map(toy));
        }
    }

    @Override
    public void winToy() {
        List<Toy> toys = getListToys();
        int maxChance = 0;
        int tempId = 1;
        for (Toy item : toys) {
            if (maxChance < item.getWinning()) {
                maxChance = item.getWinning();
                tempId = item.getId();
            }
        }
        for (Toy toy : toys) {
            if (tempId == toy.getId()) {
                System.out.print("\nПоздравляем! Вы выиграли: " + toy + '\n');
                continue;
            }
            saveToy(mapper.map(toy));

        }
    }


    private int findId() {
        List<Toy> toys = getListToys();
        int newId = 1;
        for (Toy item : toys) {
            int id = item.getId();
            if (newId == id) {
                newId++;
            }
        }
        return newId;
    }

    public void saveToy(String toys) {
        List<String> toy = new ArrayList<>();
        toy.add(toys);
        fileOperation.saveInFile(toy);
    }

    @Override
    public List<Toy> getListToys() {
        List<String> toysInMachine = fileOperation.readFromFile();
        List<Toy> toysList = new ArrayList<>();
        for (String item : toysInMachine) {
            toysList.add(mapper.map(item));
        }
        return toysList;
    }

    public int getIntRandom(int count) {
        Random rnd = new Random();
        int rndNum = rnd.nextInt(count);
        return rndNum;
    }

    public void getHelp() {
        System.out.println("-------------------------------------");
        System.out.println("ADD_TOYS - добавить игрушку в автомат\nWIN_TOY - разыграть игрушку\nVIEW_TOYS - посмотреть все игрушки в автомате\nEXIT - выход");
    }

}
