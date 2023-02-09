package Lesson_05;

import java.util.HashMap;
import java.util.Map;

public class Task_05 {
    public static void main(String[] args) {
        /*
         * Реализуйте структуру телефонной книги с помощью HashMap, учитывая, что 1
         * человек может иметь несколько телефонов.
         * Пусть дан список сотрудников:Иван Иванов (и остальные)
         * Написать программу, которая найдет и выведет повторяющиеся имена с
         * количеством повторений.
         * Отсортировать по убыванию популярности.
         * 
         * Иван Иванов 88001122333
         * Иван Курицин 88001662333
         * Иван Курицин 88001112333
         * Иван Незлобин 88001122432
         * Сергей Потапов 88001112453
         * Сергей Потапов 8800163214
         * Сергей Курицин 8800142421
         * Михаил Незлобин 880012343
         * 
         * counterName
         * Иван - 3
         * Сергей - 2
         * Потому как если один сотрудник имеет 2 или более номера , его имя считаем 1
         * раз.
         */

        Map<String, String> phonebook = Map.of("88001122333D", "Иван Иванов",
                "88001662333D", "Иван Курицин",
                "88001112333D", "Иван Курицин",
                "88001122432D", "Иван Незлобин",
                "88001112453D", "Сергей Потапов",
                "8800163214D", "Сергей Потапов",
                "8800142421D", "Сергей Курицин",
                "880012343D", "Михаил Незлобин");

        counterName(sortedMap(phonebook));

    }

    public static Map<String, String> sortedMap(Map<String, String> phonebook) {
        Map<String, String> sortMap = new HashMap<String, String>();
        for (var item : phonebook.entrySet()) {
            if (!sortMap.containsValue(item.getValue())) {
                sortMap.put(item.getKey(), item.getValue());
            }
        }
        return sortMap;
    }

    public static void counterName(Map<String, String> sortMap) {
        HashMap<String, Integer> countName = new HashMap<String, Integer>();
        String tempName;
        for (var item : sortMap.entrySet()) {
            tempName = item.getValue().split(" ")[0];
            if (!countName.containsKey(tempName)) {
                countName.put(tempName, 1);
            } else {
                countName.put(tempName, countName.get(tempName) + 1);
            }
        }
        for (var item : countName.entrySet()) {
            if (item.getValue() == 1) {
                continue;
            } else {
                System.out.printf("%s - %d\n", item.getKey(), item.getValue());
            }
        }
    }
}
