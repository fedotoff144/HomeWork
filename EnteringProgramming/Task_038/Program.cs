// Task 38
/*
Задайте массив вещественных чисел. Найдите разницу между 
максимальным и минимальным элементов массива.
[3 7 22 2 78] -> 76
*/

void FindMaxMin(int[] array)
{
    int max = 0;
    int min = 100;
    for(int i = 0; i < array.Length; i++)
    {
        if(array[i] > max)
        max = array[i];
        if(array[i] < min)
        min = array[i];
    }
    int diff = max - min;
    Console.WriteLine("Max = " + max);
    Console.WriteLine("Min = " + min);
    Console.WriteLine("Difference = " + diff);
}

int[] array = new int[] {5, 11, 33, 1, 87};
FindMaxMin(array);