package View;

import Model.*;
import Model.Animals.*;

import java.util.ArrayList;
import java.util.Scanner;

public class AnimalRegistryView {
    private Scanner scanner;

    public AnimalRegistryView() {
        scanner = new Scanner(System.in);
    }

    public int showMenu() {
        System.out.println("Выберите действие:\n" +
                "1. Завести новое животное\n" +
                "2. Показать всех животных\n" +
                "3. Показать животное\n" +
                "4. Обучить животное новым командам\n" +
                "0. <-- Выход");
        return scanner.nextInt();
    }

    public int choiceAnimal(){
        System.out.println("Выберите животное: \n" +
                "1. Собака\n" +
                "2. Кошка\n" +
                "3. Хомяк\n" +
                "4. Лошадь\n" +
                "5. Верблюд\n" +
                "6. Осел\n" +
                "0. <-- Назад");
        int choice = validateInputNum();
        if(choice < 0 || 7 <= choice){
            System.out.println("Ошибка! Повторите ввод");
            choiceAnimal();
        }
        return choice;
    }
    public Animal addAnimal() {
        int id = 0;
        System.out.println("Введите имя животного: ");
        String name = setString();
        System.out.println("Введите возраст животного: ");
        int age = validateInputNum();
        return new Animal(id, name, age);

    }


    //    add methods for pet animals
    public PetAnimal addPetAnimal(Animal animal) {
        System.out.println("Введите цвет домашнего животного: ");
        String color = setString();
        return new PetAnimal(animal.getId(), animal.getName(), animal.getAge(), color);
    }

    public Dog addDog(PetAnimal animal) {
        System.out.println("Введите породу собаки: ");
        String breed = setString();
        return new Dog(animal.getId(),animal.getName(), animal.getAge(), animal.getColor(), breed);
    }

    public Cat addCat(PetAnimal animal) {
        System.out.println("Введите вес кота: ");
        int weight = validateInputNum();
        return new Cat(animal.getId(), animal.getName(), animal.getAge(), animal.getColor(), weight);
    }

    public Hamster addHamster(PetAnimal animal) {
        System.out.println("Есть ли у хомяка хвост?\n1. да\n2. нет");
        boolean hasTail = setBoolChoice();
        return new Hamster(animal.getId(), animal.getName(), animal.getAge(), animal.getColor(), hasTail);
    }

    //    add methods for wild animals
    public WildAnimal addWildAnimal(Animal animal) {
        System.out.println("Является ли вьючное животное хищником?\n1. да\n2. нет");
        boolean predator = setBoolChoice();
        return new WildAnimal(animal.getId(), animal.getName(), animal.getAge(), predator);
    }

    public Horse addHorse(WildAnimal animal) {
        System.out.println("Введите скорость лошади: ");
        int speed = validateInputNum();
        Horse horse = new Horse(animal.getId(), animal.getName(), animal.getAge(), animal.getPredator(), speed);
        System.out.println(horse);
        return horse;
    }

    public Camel addCamel(WildAnimal animal) {
        System.out.println("Введите максимальное расстояние для верблюда: ");
        int distance = validateInputNum();
        return new Camel(animal.getId(), animal.getName(), animal.getAge(), animal.getPredator(), distance);
    }

    public Donkey addDonkey(WildAnimal animal) {
        System.out.println("Введите вес, который может перевозить осел: ");
        int weight = validateInputNum();
        return new Donkey(animal.getId(), animal.getName(), animal.getAge(), animal.getPredator(), weight);
    }


    //    methods for validate data
    public String setString() {
        String str = scanner.next();
        if (str.isEmpty() || !str.matches("^[а-яА-Я ]+$")) {
            System.out.println("Ошибка! Повторите ввод");
            setString();
        }
        return str;
    }

    public boolean setBoolChoice() {
        boolean boolChoice = true;
        int answer = validateInputNum();
        if (answer != 1) {
            boolChoice = false;
        }
        return boolChoice;
    }

    public int validateInputNum() {
        int input;
        while (true) {
            try {
                input = scanner.nextInt();
                break;
            } catch (Exception e) {
                System.out.println("Ошибка! " + e + " Повторите ввод");
            }
        }
        return input;
    }

    public int addId(){
        int id = 0;
        return id;
    }

    public ArrayList<String> setCommands(ArrayList<String> listOfCommands) {
        System.out.println("Введите команду для животного: ");
        String command = scanner.next();
        listOfCommands.add(command);
        return listOfCommands;
    }
}
