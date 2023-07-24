package Model;

public class PetAnimal extends Animal {
    private String color;

    public PetAnimal(int id, String name, int age, String color) {
        super(id, name, age);
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
}
