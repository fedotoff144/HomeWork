package Lesson_06;

/*
 * 1) Подумать над структурой класса Ноутбук для магазина техники - выделить поля и методы. Реализовать в java.
 * 2) Создать коллекцию ноутбуков.
 * 3) Написать мапу, которая будет содержать критерий (или критерии) фильтрации и выведет
 *    ноутбуки, отвечающие фильтру.
 *    Пример: ОЗУ - Значение, Объем ЖД - Значение, Операционная система - Значение, Цвет - Значение
 * 4) Отфильтровать ноутбуки их первоначального множества и вывести проходящие по условиям.
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Homwork {
    public static void main(String[] args) {
        Laptop notebook1 = new Laptop("HP", 8, 128, "Windows", "black", 100);
        Laptop notebook2 = new Laptop("Gigabyte", 16, 256, "Linux", "red", 200);
        Laptop notebook3 = new Laptop("Samsung", 16, 512, "Linux", "balck", 400);
        Laptop notebook4 = new Laptop("Asus", 64, 1024, "Linux", "white", 400);
        Laptop notebook5 = new Laptop("Lenovo", 32, 512, "Windows", "balck", 500);
        Laptop notebook6 = new Laptop("Dell", 32, 1024, "Windows", "blue", 400);

        List<Laptop> list = new ArrayList<>(
                Arrays.asList(notebook1, notebook2, notebook3, notebook4, notebook5, notebook6));

        Map<String, Integer> parameter = new HashMap<>();
        parameter.put("price", 400);
        parameter.put("RAM", 32);

        for (Laptop item : list) {
            if ((item.getPrice() == parameter.get("price").intValue()) && (item.getRAM() == parameter.get("RAM").intValue())) {
                System.out.println(item);
            }
        }
    }
}
