package Lesson_04.shield;

public class Raincoat implements Shield {
    @Override
    public int Protection() {
        return 70;
    }
    @Override
    public String toString() {
        return " Raincoat protection= " + Protection();
    }
}
