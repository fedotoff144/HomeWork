package Model.Animals;

import Model.PetAnimal;

public class Dog extends PetAnimal {
    private String breed;

    public Dog(int id, String name, int age, String color, String breed){
        super(id, name, age, color);
        this.breed = breed;
    }

    @Override
    public String toString() {
        return "Dog {" +
                "id=" + getId() +
                ", name= " + getName() +
                ", age= " + getAge() +
                ", commands= " + getCommands() +
                ", color= " + getColor() +
                ", breed= " + breed +
                "}";
    }
}
