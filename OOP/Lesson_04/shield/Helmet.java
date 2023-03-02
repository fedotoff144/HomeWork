package Lesson_04.shield;

public class Helmet implements Shield {
    @Override
    public int Protection() {
        return 50;
    }

    @Override
    public String toString() {
        return " Helmet protection= " + Protection();
    }
    
}
