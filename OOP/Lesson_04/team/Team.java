package Lesson_04.team;

import Lesson_04.items.DistanceAttacker;
import Lesson_04.items.Warrior;

import java.util.ArrayList;
import java.util.List;

public class Team<T extends Warrior> {
    private List<T> team = new ArrayList<>();
    private String name;

    public Team(String name) {
        this.name = name;
    }

    public Team<T> addWarrior(T warrior) {
        team.add(warrior);
        return this;
    }

    public int getMaxDistance() {
        int distance = 0;
        for (T item : team) {
            if (!(item instanceof DistanceAttacker)) {
                continue;
            }
            DistanceAttacker temp = (DistanceAttacker) item;
            if (temp.getDistance() > distance) {
                distance = temp.getDistance();
            }
        }
        return distance;
    }

    public int getTeamHealth(){
        int sumHealth = 0;
        for (T items : team) {
            sumHealth += items.getHealthPoint();
        }
        return sumHealth;
    }

    public int getTeamDamage() {
        int sumDamage = 0;
        for (T item : team) {
            sumDamage += item.getMaxDamage();
        }
        return sumDamage;
    }

    public int getMinShield(){
        int min = team.get(0).getProtetion();
        for(int i = 1; i<team.size();i++){
            if(team.get(i).getProtetion()< min){
                min = team.get(i).getProtetion();
            }
        }
      return min;
    }

    @Override
    public String toString() {
        StringBuilder teamBuilder = new StringBuilder();
        for (T item : team) {
            teamBuilder.append(item.toString() + "\n");
        }
        return String.format("Team{ team= %s, teamHealth= %d, maxDistance = %d, maxDamage = %d, minShield = %d \n%s}", name, getTeamHealth(), getMaxDistance(), getTeamDamage(), getMinShield(), teamBuilder);
    }
}
