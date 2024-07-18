"""
Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""
import json


class Factorial:
    def __init__(self, k: int = 1):
        self.k = k
        self.memory = []

    def __call__(self, num: int = 1):
        if num <= 0:
            raise ValueError('Num less or equal 0.')
        else:
            if len(self.memory) == self.k:
                self.memory.pop(0)
            temp = 1
            for i in range(2, num + 1):
                temp *= i
            self.memory.append({num: temp})

    def get_memory(self):
        return self.memory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('task_02.json', 'w', encoding='utf-8') as f:
            json.dump(self.memory, f, ensure_ascii=True)


if __name__ == '__main__':
    f1 = Factorial(3)
    f1(5)
    f1(6)
    f1(3)
    f1(10)
    f1(6)
    print(f1.get_memory())
    with f1 as f1_mngr:
        print('OK')
