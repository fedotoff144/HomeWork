package Model;

public class PetAnimal extends Animal{
    private String color;

    public PetAnimal(String name, int age, String color) {
        super(name, age);
        this.color = color;
    }

    public String getColor(){
        return color;
    }

    public void setColor(String color){
        this.color = color;
    }
}
