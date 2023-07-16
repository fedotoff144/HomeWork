package Model;

public class Dog extends PetAnimal{
    private String breed;

    public Dog(String name, int age, String color, String breed){
        super(name, age, color);
        this.breed = breed;
    }

}
