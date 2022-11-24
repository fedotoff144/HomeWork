// Task 10
/*
Напишите программу, которая принимает на вход трёхзначное число 
и на выходе показывает вторую цифру этого числа.
456 -> 5
782 -> 8
918 -> 1
*/

Console.WriteLine("Введите трехзначное число: ");
int n = Convert.ToInt32(Console.ReadLine());

if (n > 999 || n < 100)
{
    Console.WriteLine("Попробуйте снова...");
}
else
{
    Console.WriteLine(n / 10 % 10);
}