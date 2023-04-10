package model;

public class Toy {

    private int id;
    private String name;
    private int quantity;
    private int winning;

    public Toy(int id, String name, int quantity, int winning){
        this.id = id;
        this.name = name;
        this.quantity = quantity;
        this.winning = winning;
    }

    public int getId() {
        return id;
    }

    public String getName(){
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public int getWinning(){
        return winning;
    }


    public void setName(String name){
        this.name = name;
    }

    public void setQuantity(int quantity){
        this.quantity = quantity;
    }


    @Override
    public String toString() {
        return "model.Toy{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", quantity=" + quantity +
                ", winning=" + winning +
                '}';
    }
}

