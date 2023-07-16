package Controller;

import View.AnimalRegistryView;

public class AnimalRegistryController {
    private AnimalRegistryView view;

        public void start() {
        while (true) {
            int choice = view.showMenu();

            switch (choice) {
                case 1:
//                    addAnimal();
                    break;
                case 2:
//                    findAnimalClass();
                    break;
                case 3:
//                    printAnimalCommands();
                    break;
                case 4:
//                    addAnimalCommand();
                    break;
                case 0:
                    System.exit(0);
                    break;
                default:
//                    view.printError("Неверный выбор");
                    break;
            }
        }
    }

}
