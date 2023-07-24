package Model.Animals;

import Model.PetAnimal;

public class Hamster extends PetAnimal {
    private boolean hasTail;

    public Hamster(int id, String name, int age, String color, boolean hasTail) {
        super(id, name, age, color);
        this.hasTail = hasTail;
    }

    public boolean getHasTail() {
        return hasTail;
    }

    public void setHasTail(boolean hasTail) {
        this.hasTail = hasTail;
    }

    @Override
    public String toString() {
        return "Hamster {" +
                "id=" + getId() +
                ", name= " + getName() +
                ", age= " + getAge() +
                ", commands= " + getCommands() +
                ", color= " + getColor() +
                ", tail= " + hasTail +
                "}";
    }
}
