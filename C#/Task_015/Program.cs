// Task 15
/*
Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является ли этот день выходным.
6 -> да
7 -> да
1 -> нет
*/

Console.WriteLine("Введите число: ");
int n = Convert.ToInt32(Console.ReadLine());

if (n > 7 || n <= 0)
{
    Console.WriteLine("Попробуйте снова...");
}
else if (n == 6 || n == 7)
{
    Console.WriteLine("Ура! Сегодня выходной!");
}
else
{
    Console.WriteLine("Будни...");
}