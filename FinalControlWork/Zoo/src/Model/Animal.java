package Model;

import java.util.ArrayList;

public class Animal {
    private int id;
    private String name;
    private int age;
    private ArrayList<String> commands;

    public Animal(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.commands = commands;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public ArrayList<String> getCommands() {
        return commands;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setCommands(ArrayList<String> commands) {
        this.commands = commands;
    }

//    @Override
//    public String toString() {
//        return "Animal{" +
//                "id=" + id +
//                ", name=" + name +
//                ", age=" + age +
//                ", commands=" + commands +
//                '}';
//    }
}
