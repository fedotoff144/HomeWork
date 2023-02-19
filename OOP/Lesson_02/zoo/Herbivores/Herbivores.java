package OOP.Lesson_02.zoo.Herbivores;

import OOP.Lesson_02.zoo.Animal;

public abstract class Herbivores extends Animal {

    public Herbivores(String name) {
        super(name);
    }

    @Override
    public String feed() {
        return "Grass";
    }


}
