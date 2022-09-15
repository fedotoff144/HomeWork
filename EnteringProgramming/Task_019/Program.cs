// A Task - 19
/*
Напишите программу, которая принимает на вход пятизначное число и проверяет, 
является ли оно палиндромом.
14212 -> нет
12821 -> да
23432 -> да
*/
Console.Write("Введите число: ");
string? num = Console.ReadLine();
char[] numArray = num.ToCharArray();
Array.Reverse(numArray);
string reverse = new string(numArray);

if (reverse == num){
    Console.WriteLine("Полиандром!");
} else {
    Console.WriteLine("Не полиандром!");
}
