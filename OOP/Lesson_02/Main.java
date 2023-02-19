package OOP.Lesson_02;

import java.util.List;

import OOP.Lesson_02.zoo.Animal;
import OOP.Lesson_02.zoo.Flyable;
import OOP.Lesson_02.zoo.Runable;
import OOP.Lesson_02.zoo.Swimable;
import OOP.Lesson_02.zoo.Zoo;
import OOP.Lesson_02.zoo.Herbivores.Cow;
import OOP.Lesson_02.zoo.Herbivores.Duck;
import OOP.Lesson_02.zoo.Herbivores.Goat;
import OOP.Lesson_02.zoo.Herbivores.Hipopotam;
import OOP.Lesson_02.zoo.Predator.Crocodile;
import OOP.Lesson_02.zoo.Predator.Leo;
import OOP.Lesson_02.zoo.radio.Radio;
import OOP.Lesson_02.zoo.radio.Sayable;

public class Main {
    public static void main(String[] args) {

        List<Animal> animalsList = List.of(
                new Cow("Мурка"),
                new Crocodile("Гена"),
                new Leo("Симба - Леопольд"),
                new Goat("Маруська"),
                new Duck("Дональд Дак"),
                new Hipopotam("Hipo"));
        Zoo zoo = new Zoo(animalsList, new Radio());

        for (Sayable animal : zoo.getSayable()) {
            // System.out.print(((Animal) animal).getName() + ": ");
            System.out.println(animal.say());
        }
        System.out.println("______________________");
        for (Runable animal : zoo.getRunableList()) {
            System.out.println(((Animal) animal).getName());
            System.out.println(((Animal) animal).say());
            System.out.println(animal.getSpeedRun() + "\n");
        }
        System.out.println("______________________");
        for (Flyable animal : zoo.getFlyableList()) {
            System.out.println(((Animal) animal).getName());
            System.out.println(((Animal) animal).say());
            System.out.println(animal.getSpeedFlyable());
            System.out.println(animal.getHigh() + "\n");
        }
        System.out.println("______________________");
        for (Swimable animal : zoo.getSwimableList()) {
            System.out.println(((Animal) animal).getName());
            System.out.println(((Animal) animal).say());
            System.out.println(animal.getSpeedRun());
            System.out.println(animal.getSwimSpeed() + "\n");
        }
        System.out.println("____Определяем чемпиона по бегу_____");
        System.out.println(zoo.getRunChampion());
        System.out.println("____Определяем чемпиона по полётам_______");
        System.out.println(zoo.getFlightChampion());

    }
}