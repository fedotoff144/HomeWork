// Task 4
/*
Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
2, 3, 7 -> 7
44 5 78 -> 78
22 3 9 -> 22
*/

Console.WriteLine("Введите первое число для сравнения: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите второе число для сравнения: ");
int b = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите третье число для сравнения: ");
int c = Convert.ToInt32(Console.ReadLine());
int max = 0;

if (a >= max)
{
    max = a;
}
if (b >= max)
{
    max = b;
}
if (c >= max)
{
    max = c;
}
Console.WriteLine("max = {0}", max);