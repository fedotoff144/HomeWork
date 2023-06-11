import java.io.IOException;

public class Task_02 {
    public static void main(String[] args) {
        // 2. Если необходимо, исправьте данный код (задание 2 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)
        int[] Array = new int[] {};

        try {
            int d = 0;
            double catchedRes1 = Array[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        }catch (IndexOutOfBoundsException e){
            System.out.println("Index out of bounds: " + e);
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic exception: " + e);
        }catch (Exception e){
            System.out.println("Something wrong");
        }

    }
}
