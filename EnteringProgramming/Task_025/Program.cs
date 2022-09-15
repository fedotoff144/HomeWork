// Task 25
/*
Напишите цикл, который принимает на вход два числа (A и B) и возводит 
число A в натуральную степень B.
3, 5 -> 243 (3⁵)
2, 4 -> 16
*/

Console.WriteLine("Введите число: ");
int n = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Введите степень числа: ");
int s = Convert.ToInt32(Console.ReadLine());
int res = 1;

for (int i = 0; i < s; i++)
{
    res *= n;
}
Console.WriteLine(res);
