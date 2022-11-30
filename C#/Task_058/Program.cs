// Task 58
/*
Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
Например, даны 2 матрицы:
2 4 | 3 4
3 2 | 3 3
Результирующая матрица будет:
18 20
15 18
*/

Console.Clear();

void InputMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            matrix[i, j] = new Random().Next(1, 10);
    }
}

void PrintMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            Console.Write(matrix[i, j] + " \t");

        Console.WriteLine();
    }
}
void MultiplyMatrix(int[,] firstMartrix, int[,] secomdMartrix, int[,] resultMatrix)
{
    for (int i = 0; i < resultMatrix.GetLength(0); i++)
    {
        for (int j = 0; j < resultMatrix.GetLength(1); j++)
        {
            int sum = 0;
            for (int k = 0; k < firstMartrix.GetLength(1); k++)
            {
                sum = firstMartrix[i, j] * secomdMartrix[i, j];
            }
            resultMatrix[i, j] = sum;
        }
    }
}


int[,] matrix = new int[3, 3];

int[,] firstMartrix = new int[3, 3];
InputMatrix(firstMartrix);
Console.WriteLine("Первый двумерный массив: ");
PrintMatrix(firstMartrix);

int[,] secomdMartrix = new int[3, 3];
InputMatrix(secomdMartrix);
Console.WriteLine("Второй двумерный массив: ");
PrintMatrix(secomdMartrix);

Console.WriteLine();
int[,] resultMatrix = new int[3, 3];
MultiplyMatrix(firstMartrix, secomdMartrix, resultMatrix);
Console.WriteLine("Произведение двумерных массивов: ");
PrintMatrix(resultMatrix);
