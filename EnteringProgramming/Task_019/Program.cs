// A Task - 19

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
