package Controller;

import Model.Animal;
import Model.PetAnimal;
import Model.WildAnimal;
import View.AnimalRegistryView;

public class AnimalRegistryController {
    private AnimalRegistryView view;

        public void start() {
        while (true) {
            int choice = view.showMenu();

            switch (choice) {
                case 1:
                    int choiceAnimal = view.choiceAnimal();
                    addAnimal(choiceAnimal);
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
//                    break;
            }
        }
    }

    public void addAnimal(int choice){
        if (1 <= choice && choice <= 3){
            Animal animal = view.addAnimal();
            PetAnimal petAnimal = view.addPetAnimal(animal);
            if (choice == 1){
                view.addDog(petAnimal);
            } else if (choice == 2) {
                view.addCat(petAnimal);
            }
            view.addHamster(petAnimal);
        }else if (4 <= choice && choice <= 6){
            Animal animal = view.addAnimal();
            WildAnimal wildAnimal = view.addWildAnimal(animal);
            if (choice == 4){
                view.addHorse(wildAnimal);
            } else if (choice == 5) {
                view.addCamel(wildAnimal);
            }
            view.addDonkey(wildAnimal);
        }
        start();
    }

}