// Task 13
/*Напишите программу, которая выводит третью цифру заданного числа или сообщает, 
что третьей цифры нет.
645 -> 5
78 -> третьей цифры нет
32679 -> 6
*/

Console.WriteLine("Введите число: ");
int n = Convert.ToInt32(Console.ReadLine());

if (n < 100)
{
    Console.WriteLine("Третьей цифры нет...");
}
else Console.WriteLine(n.ToString()[2]);


//Решение через математический расчет
/*else for (int i = 0; i < 2; i++)
    {
        n = n / 10;
    }
Console.WriteLine($"третья цифра: {n}");
*/