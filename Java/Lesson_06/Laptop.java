package Lesson_06;

public class Laptop {
    String brand;
    int RAM;
    int HDD;
    String OS;
    String color;
    int price;

    // CONSTRUCTORS
    
    public Laptop(String brand, int RAM, int HDD, String OS, String color, int price) {
        this.brand = brand;
        this.RAM = RAM;
        this.HDD = HDD;
        this.OS = OS;
        this.color = color;
        this.price = price;
    }

    public Laptop() {
        this.brand = "";
        this.RAM = 0;
        this.HDD = 0;
        this.OS = "";
        this.color = "";
        this.price = 0;
    }

    @Override
    public String toString() {
        return "notebook: %s, RAM: %d, HDD: %d, OS: %s, color: %s, price: %d".formatted(brand, RAM, HDD, OS, color,
                price);
    }

    // GET METHODS

    public String getBrand() {
        return brand;
    }

    public Integer getRAM() {
        return RAM;
    }

    public Integer getHDD() {
        return HDD;
    }

    public String getOS() {
        return OS;
    }

    public String getColor() {
        return color;
    }

    public Integer getPrice() {
        return price;
    }

    // SET METHODS

    public void setBrand(String brand) {
        this.brand = brand;
        return;
    }

    public void setRAM(Integer RAM) {
        this.RAM = RAM;
        return;
    }

    public void setHDD(Integer HDD) {
        this.HDD = HDD;
        return;
    }

    public void setOS(String OS) {
        this.OS = OS;
        return;
    }

    public void setColor(String color) {
        this.color = color;
        return;
    }

    public void setBrand(Integer price) {
        this.price = price;
        return;
    }

}
