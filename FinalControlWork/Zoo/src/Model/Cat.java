package Model;

public class Cat extends PetAnimal{
    private int weight;

    public Cat(String name, int age, String color, int weight){
        super(name, age, color);
        this.weight = weight;
    }
}
