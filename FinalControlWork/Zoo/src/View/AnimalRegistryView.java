package View;

import java.util.ArrayList;
import java.util.Scanner;

public class AnimalRegistryView {
    private Scanner scanner;

    public AnimalRegistryView(){
        scanner = new Scanner(System.in);
    }

    public int showMenu(){
        System.out.println("Выберите действие:\n" +
                "1. Завести новое животное\n" +
                "2. Показать всех животных\n" +
                "3. Показать животное\n" +
                "4. Обучить животное новым командам\n" +
                "0. Выйти из программы");
        return scanner.nextInt();
    }

    public void addAnimal(){
        while (true){
            System.out.println("Выберите животное: 1. Собака\n2. Кошка\n3. Хомяк\n4. Лошадь\n5. Верблюд\n6. Осел");
            int choiseAnimal = scanner.nextInt();
            if (choiseAnimal == 1){

            }
        }
    }

    public String setName(){
        System.out.println("Введите имя животного: ");
        return scanner.next();
    }
    public int setAge(){
        System.out.println("Введите возраст животного: ");
        return validateInputNum();
    }
    public ArrayList<String> setCommands(ArrayList<String> listOfCommands){
        System.out.println("Введите команду для животного: ");
        String command = scanner.next();
        listOfCommands.add(command);
        return listOfCommands;
    }
    public boolean setPredator(){
        System.out.println("Является ли вьючное животное хищником?\n1. да\n2. нет");
        boolean predator = true;
        int answer = validateInputNum();
        if (answer != 1){
            predator = false;
        }
        return predator;
    }
    public String setColor(){
        System.out.println("Введите цвет домашнего животного: ");
        return scanner.next();
    }
    public String setBreed(){
    System.out.println("Введите породу собаки: ");
    return scanner.next();
    }
    public int setWeight(){
        System.out.println("Введите вес кота: ");
        return validateInputNum();
    }

    public boolean setHasTail(){
        System.out.println("Есть ли у хомяка хвост?\n1. да\n2. нет");
        boolean hasTail = true;
        int answer = validateInputNum();
        if (answer != 1){
            hasTail = false;
        }
        return hasTail;
    }
    public int setSpeed(){
    System.out.println("Введите скорость лошади: ");
        return validateInputNum();
    }

    public int setDistance(){
    System.out.println("Введите максимальное расстояние для верблюда: ");
        return validateInputNum();
    }

    public int setLiftingCapacity(){
        System.out.println("Введите вес, который может перевозить осел: ");
        return validateInputNum();
    }

    public int validateInputNum(){
        int input;
        while (true){
            try{
                input = scanner.nextInt();
                break;
            }catch (Exception e){
                System.out.println("Ошибка! " + e + " Повторите ввод");
            }
        }
        return input;
    }

}
