// Task 34
/*
Задайте массив заполненный случайными положительными трёхзначными числами. 
Напишите программу, которая покажет количество чётных чисел в массиве.
[345, 897, 568, 234] -> 2
*/
void InputArray(int[] array) 
{ 
    for (int i = 0; i < array.Length; i++) 
    array[i] = new Random().Next(100, 1000); 
} 
void FindEvenNumber(int[] array)
{
    int count = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] % 2 == 0) 
        count++;
    }
    Console.WriteLine("Кол-во четных чисел в массиве: " + count);
}
    int[] array = new int[10]; 
    InputArray(array); 
    Console.WriteLine("[" + string.Join(", ", array) + "]");
    FindEvenNumber(array);
