package Model;

public class Hamster extends PetAnimal{
    private boolean hasTail;

    public Hamster(String name, int age, String color, boolean hasTail){
        super(name, age, color);
        this.hasTail = hasTail;
    }

    public boolean getHasTail(){
        return hasTail;
    }

    public void setHasTail(boolean hasTail){
        this.hasTail = hasTail;
    }
}
