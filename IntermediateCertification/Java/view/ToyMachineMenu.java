package view;

import controller.ToyMachineController;
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
            String command = prompt("Введите вашу команду: ");
            try {
                com = Commands.valueOf(command.toUpperCase());
                if (com == Commands.EXIT)
                    return;
                switch (com) {
                    case ADD_TOYS: {
                        String nameToy = prompt("Введите название игрушки: ");
                        int count = Integer.parseInt(prompt("Введите количество: "));
                        toyMachineController.addToy(nameToy, count);
                        break;
                    }
                    case WIN_TOY: {
                        System.out.println("ok");
                        toyMachineController.winToy();
                        break;
                    }
                    case VIEW_TOYS: {
                        System.out.println("no");
                        toyMachineController.viewAllToys();
                        break;
                    }
                    case HELP: {
                        toyMachineController.help();
                        break;
                    }
                }
            } catch (Exception e) {
                System.out.println("Данная команда не найдена! Повторите ввод.");
            }
        }

    }


    public static String prompt(String massage) {
        Scanner scn = new Scanner(System.in);
        System.out.print(massage);
        return scn.nextLine();
    }
}
