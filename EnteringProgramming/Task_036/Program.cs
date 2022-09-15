// Task 36
/*
Задайте одномерный массив, заполненный случайными числами. 
Найдите сумму элементов, стоящих на нечётных позициях.
[3, 7, 23, 12] -> 19
[-4, -6, 89, 6] -> 0
*/
void InputArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    array[i] = new Random().Next(-99, 100);
}

void PositionNumber(int[] array)
{
    int num_pos = 0;
    for (int i = 0; i < array.Length; i = i + 2)
    {
        num_pos += array[i];
    }
    Console.WriteLine("Сумма элементов нечетных позиций равна: " + num_pos);
}

int[] matrix = new int[12];
InputArray(matrix);
Console.WriteLine("[" + string.Join(", ", matrix) + "]");
PositionNumber(matrix);