// package Seminars.Lesson_01;

import java.sql.Date;

public class Main {
    public static void main(String[] args) {
        VendingMachine machine = new VendingMachine();
        machine.addProduct(new Product("Lays", 100D));
        machine.addProduct(new Product("Mars", 70D));
        machine.addProduct(new Product("Twix", 70.99D));
        machine.addProduct(new Product("Alenka", 90D));
        machine.addProduct(new Product("Cream-soda", 85D));
        machine.addProduct(new Perishable("Milk", 87D, new Date(2023 - 02 - 10)));
        machine.addProduct(new Drinks("Kola", 55D, 0.5D));
        machine.addProduct(new Drinks("Tarhun", 35D, 0.3D));

        System.out.println(machine);
        System.out.println(machine.findProduct("Alenka"));
        System.out.println(machine.findProduct("beer"));
        System.out.println("----------------------");
        System.out.println(machine.sellProduct(machine.findProduct("Milk").get(0)));
        System.out.println("----------------------");
        System.out.println(machine);
    }
}