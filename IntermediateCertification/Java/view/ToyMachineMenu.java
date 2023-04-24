package view;

import controller.ToyMachineController;
import model.Toy;

import java.util.Scanner;

public class ToyMachineMenu {
    ToyMachineController toyMachineController;

    public ToyMachineMenu(ToyMachineController toyMachineController) {
        this.toyMachineController = toyMachineController;
    }

    public void menu() {
        Commands com;
        while (true) {
            System.out.println("\n<<<<<< Автомат игрушек >>>>>>\nКоманды для выбора: ADD_TOYS, WIN_TOY, VIEW_TOYS, HELP, EXIT");
            System.out.println("-------------------------------------------------------------");
            String command = prompt("Введите вашу команду пожалуйста: ");
            try {
                com = Commands.valueOf((command.toUpperCase()));
                if (com == Commands.EXIT)
                    return;
                switch (com) {
                    case ADD_TOYS -> toyMachineController.addToy();
                    case WIN_TOY -> System.out.println("WIN_TOY");
                    case VIEW_TOYS -> toyMachineController.viewAllToys();
                    case HELP -> toyMachineController.help();
                }
            } catch (Exception e) {
                System.out.println("Данная команда не найдена! Повторите ввод.");
            }
        }

    }


    public static String prompt(String massage) {
        Scanner scn = new Scanner(System.in);
        System.out.println(massage);
        return scn.nextLine();
    }
}
