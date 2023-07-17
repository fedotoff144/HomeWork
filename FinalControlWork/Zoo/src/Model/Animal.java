package Model;

import java.util.ArrayList;

public class Animal {
    private String name;
    private int age;
    private ArrayList<String> commands;

    public Animal(String name, int age){
        this.name = this.name;
        this.age = age;
        this.commands = commands;
    }

    public String getName(){
        return name;
    }

    public int getAge(){
        return age;
    }
    public ArrayList<String> getCommands(){ return commands;}

    public void setName(String name){
        this.name = name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public void setCommands(ArrayList<String> commands){
        this.commands = commands;
    }

}
