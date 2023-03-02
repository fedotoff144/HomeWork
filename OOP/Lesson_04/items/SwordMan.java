package Lesson_04.items;

import Lesson_04.shield.Helmet;
import Lesson_04.weapons.Sword;

public class SwordMan extends Warrior<Sword, Helmet>{
    public SwordMan(String name, Sword weapon, Helmet shield) {
        super(name, weapon, shield);
    }


    @Override
    public String toString() {
        return super.toString() + " Type = SwordMan";
    }
}