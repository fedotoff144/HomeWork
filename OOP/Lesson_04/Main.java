package Lesson_04;

import Lesson_04.items.Archer;
import Lesson_04.items.SwordMan;
import Lesson_04.items.Warrior;
import Lesson_04.shield.Helmet;
import Lesson_04.shield.Raincoat;
import Lesson_04.team.Team;
import Lesson_04.weapons.Bow;
import Lesson_04.weapons.Sword;

public class Main {
    public static void main(String[] args) {
        Team<Archer> archerTeam = new Team<>("Archers");
        archerTeam.addWarrior(new Archer("Vasya", new Bow(), new Raincoat()))
                .addWarrior(new Archer("Petya", new Bow(), new Raincoat()))
                .addWarrior(new Archer("Misha", new Bow(), new Raincoat()))
                .addWarrior(new Archer("Grisha", new Bow(), new Raincoat()));
        System.out.println(archerTeam);

        Team<Warrior> mixTeam = new Team<>("Mixer");
        mixTeam.addWarrior(new Archer("Vasya", new Bow(), new Raincoat()))
                .addWarrior(new SwordMan("Petya", new Sword(), new Helmet()))
                .addWarrior(new Archer("Misha", new Bow(), new Raincoat()))
                .addWarrior(new SwordMan("Grisha", new Sword(), new Helmet()));
        System.out.println(mixTeam);

    }
}
