package Model.Animals;

import Model.PetAnimal;

public class Cat extends PetAnimal {
    private int weight;

    public Cat(int id, String name, int age, String color, int weight) {
        super(id, name, age, color);
        this.weight = weight;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "Cat {" +
                "id=" + getId() +
                ", name= " + getName() +
                ", age= " + getAge() +
                ", commands= " + getCommands() +
                ", color= " + getColor() +
                ", weight= " + weight +
                "}";
    }
}
