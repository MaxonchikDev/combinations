class found_error(Exception):
    pass

def find_combinations(numbers, target):
    results = []
    # Сортируем для оптимизации и исключения дубликатов
    numbers.sort()

    def backtrack(start, current_sum, path):
        # Если нашли нужную сумму, сохраняем копию пути
        if current_sum == target:
            results.append(list(path))
            return
        # Если перешагнули лимит, останавливаем ветку
        if current_sum > target:
            return

        for i in range(start, len(numbers)):
            # Пропускаем одинаковые числа на одном уровне рекурсии, чтобы избежать дубликатов в ответе
            if i > start and numbers[i] == numbers[i - 1]:
                continue

            # Шаг вперед
            path.append(numbers[i])
            # Рекурсивный запуск со следующего элемента
            backtrack(i + 1, current_sum + numbers[i], path)
            # Откат назад (backtrack)
            path.pop()

    backtrack(0, 0, [])
    return results

def search_for_nearest_number(numbers, target):
    "Wait for version 1.0"
