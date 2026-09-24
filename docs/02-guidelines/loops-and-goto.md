# Циклы и goto

<details>
    <summary><b>Избегайте использования goto (В работе)</b></summary>

Оператор `goto` в большинстве случаев создает запутанный и сложный для поддержки код, известный как "спагетти-код". В современном программировании существуют более эффективные и читаемые альтернативы.

### Проблемы использования goto

1. **Нарушение структуры кода**
   - Затрудняет понимание потока выполнения
   - Усложняет отладку и тестирование
   - Делает рефакторинг кода сложнее

2. **Снижение поддерживаемости**
   - Сложно проследить все возможные пути выполнения
   - Повышает вероятность появления ошибок при модификации
   - Затрудняет анализ кода другими разработчиками

3. **Риск создания бесконечных циклов**
   - Легко создать ситуацию, когда программа не сможет выйти из цикла переходов
   - Сложнее контролировать условия выхода

### Пример неправильного использования goto

```csharp
// ❌ Плохо: использование goto для организации цикла
public void ProcessOrders(List<Order> orders)
{
    int i = 0;

start:
    if (i >= orders.Count)
        goto end;
        
    var order = orders[i];
    
    if (!order.IsValid)
    {
        i++;
        goto start;
    }
    
    ProcessOrder(order);
    
    i++;
    goto start;
    
end:
    Console.WriteLine("Все заказы обработаны");
}
```

### Альтернативы использованию goto

#### 1. Используйте стандартные управляющие конструкции

```csharp
// ✅ Хорошо: использование foreach вместо goto
public void ProcessOrders(List<Order> orders)
{
    foreach (var order in orders)
    {
        if (order.IsValid)
        {
            ProcessOrder(order);
        }
    }
    
    Console.WriteLine("Все заказы обработаны");
}
```

#### 2. Применяйте методы раннего возврата

```csharp
// ✅ Хорошо: использование return вместо goto
public void ProcessOrder(Order order)
{
    // Ранние проверки и возврат
    if (order == null)
        return;
        
    if (!order.IsValid)
        return;
        
    // Основная логика обработки
    // ...
}
```

#### 3. Используйте конструкции обработки исключений

```csharp
// ✅ Хорошо: использование try-catch вместо goto для обработки ошибок
public void ProcessOrder(Order order)
{
    try
    {
        ValidateOrder(order);
        // Обработка заказа...
    }
    catch (InvalidOrderException ex)
    {
        Log.Error($"Ошибка обработки заказа: {ex.Message}");
        // Обработка ошибки
    }
}
```

### Допустимые случаи использования goto

Хотя в целом следует избегать использования `goto`, существуют редкие ситуации, когда он может быть оправдан:

#### 1. Реализация паттерна State Machine

```csharp
// Допустимое использование goto для конечного автомата
public void ProcessWorkflow()
{
    string state = "Start";
    
Start:
    if (state == "Start")
    {
        // Обработка начального состояния
        state = DetermineNextState();
        goto HandleState;
    }
    
HandleState:
    switch (state)
    {
        case "Processing":
            // Обработка
            state = "Validation";
            goto HandleState;
            
        case "Validation":
            // Валидация
            state = "Completion";
            goto HandleState;
            
        case "Completion":
            // Завершение
            return;
            
        default:
            state = "Error";
            goto HandleError;
    }
    
HandleError:
    // Обработка ошибок
    Log.Error($"Ошибка в состоянии {state}");
}
```

#### 2. Выход из вложенных циклов

```csharp
// Допустимое использование goto для выхода из вложенных циклов
public void ProcessMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (matrix[i, j] < 0)
            {
                // Нашли отрицательный элемент
                Console.WriteLine($"Найден отрицательный элемент в позиции [{i},{j}]");
                goto MatrixProcessed;
            }
        }
    }
    
MatrixProcessed:
    Console.WriteLine("Обработка матрицы завершена");
}
```

### Лучшие альтернативы даже для допустимых случаев

Даже в случаях, когда использование `goto` кажется оправданным, обычно существуют более чистые альтернативы:

```csharp
// ✅ Лучше: Использование метода вместо goto для выхода из вложенных циклов
public void ProcessMatrix(int[,] matrix)
{
    try
    {
        SearchNegativeInMatrix(matrix);
        Console.WriteLine("Отрицательных элементов не найдено");
    }
    catch (NegativeElementFoundException ex)
    {
        Console.WriteLine(ex.Message);
    }
    finally
    {
        Console.WriteLine("Обработка матрицы завершена");
    }
}

private void SearchNegativeInMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (matrix[i, j] < 0)
            {
                throw new NegativeElementFoundException(
                    $"Найден отрицательный элемент в позиции [{i},{j}]");
            }
        }
    }
}
```

## Рекомендации для PIX RPA

1. **Используйте структурированные блоки вместо goto**
   - Применяйте конструкции `if`, `switch`, `foreach`, `while`
   - Разбивайте сложную логику на отдельные методы
   
2. **Для организации рабочего процесса используйте процессы и диаграммы**
   - PIX RPA предоставляет визуальные средства для построения процессов
   - Используйте стандартные элементы процессов вместо `goto`
   
3. **При необходимости реализации конечного автомата**
   - Используйте паттерн "Состояние" (State)
   - Создавайте явные классы для каждого состояния

4. **В случае необходимости выхода из сложных циклов**
   - Используйте флаги для контроля выхода
   - Разбивайте сложные циклы на методы

**[⬆ К карте разделов](../../README.md#карта-разделов)**

</details>

<details>
    <summary><b>Избегайте бесконечных циклов (В работе)</b></summary>

Бесконечные циклы представляют серьезную проблему в роботизированной автоматизации, особенно при работе с пользовательским интерфейсом. Они могут привести к зависанию робота, потере ресурсов и прерыванию бизнес-процессов.

### Распространенные причины бесконечных циклов

1. **Отсутствие условия выхода**
   - Цикл без проверки условия завершения
   - Условие, которое никогда не становится ложным
   - Ошибки в логике обновления счетчиков

2. **Проблемы при работе с UI**
   - Ожидание элемента, который никогда не появляется
   - Попытки взаимодействия с недоступным интерфейсом
   - Неправильная обработка состояний загрузки

3. **Логические ошибки**
   - Ошибки в условиях продолжения цикла
   - Неправильное обновление переменных внутри цикла
   - Бесконечная рекурсия без условия выхода

### Примеры опасных циклов

```csharp
// ❌ Плохо: Бесконечный цикл без условия выхода
while (true)
{
    // Действия без механизма выхода
    ProcessItem();
}

// ❌ Плохо: Цикл с ошибкой в условии
int counter = 0;
while (counter >= 0)
{
    counter++;
    // counter никогда не станет отрицательным
}

// ❌ Плохо: Бесконечное ожидание UI элемента
while (!IsElementVisible("btnSubmit"))
{
    // Если элемент никогда не появится, робот зависнет
    Thread.Sleep(1000);
}
```

### Решения для избежания бесконечных циклов

#### 1. Всегда добавляйте таймауты и ограничения

```csharp
// ✅ Хорошо: Цикл с ограничением по времени
DateTime timeout = DateTime.Now.AddMinutes(5);
while (!IsElementVisible("btnSubmit") && DateTime.Now < timeout)
{
    Thread.Sleep(1000);
}

if (!IsElementVisible("btnSubmit"))
{
    Log.Warning("Кнопка не появилась в течение 5 минут");
    // Альтернативное действие или обработка ошибки
}
```

#### 2. Используйте максимальное количество итераций

```csharp
// ✅ Хорошо: Цикл с ограничением по числу попыток
int maxAttempts = 30;
int attempts = 0;

while (!IsElementVisible("btnSubmit") && attempts < maxAttempts)
{
    Thread.Sleep(1000);
    attempts++;
}

if (attempts >= maxAttempts)
{
    Log.Warning($"Превышено максимальное количество попыток ({maxAttempts})");
    // Обработка ситуации
}
```

#### 3. Комбинируйте таймаут и счетчик

```csharp
// ✅ Хорошо: Комбинированный подход
public bool WaitForElement(string elementId, int maxSeconds = 30, int checkIntervalMs = 500)
{
    DateTime timeout = DateTime.Now.AddSeconds(maxSeconds);
    int attempts = 0;
    
    while (DateTime.Now < timeout)
    {
        attempts++;
        
        if (IsElementVisible(elementId))
            return true;
            
        if (attempts % 10 == 0)
            Log.Debug($"Ожидание элемента {elementId}, попытка {attempts}");
            
        Thread.Sleep(checkIntervalMs);
    }
    
    Log.Warning($"Элемент {elementId} не появился за {maxSeconds} секунд ({attempts} попыток)");
    return false;
}
```

#### 4. Добавляйте защитный код для циклов с неизвестным числом итераций

```csharp
// ✅ Хорошо: Защита от бесконечного цикла при обработке данных
public void ProcessItems(IEnumerable<Item> items)
{
    int processedCount = 0;
    int maxItems = 10000; // Разумное ограничение
    
    foreach (var item in items)
    {
        ProcessItem(item);
        processedCount++;
        
        if (processedCount > maxItems)
        {
            Log.Warning($"Превышено максимальное количество обрабатываемых элементов ({maxItems})");
            break;
        }
    }
}
```

### Особенности при работе с UI

#### 1. Ожидание элементов интерфейса

```csharp
// ✅ Хорошо: Безопасное ожидание с обработкой исключений
public bool WaitForElementSafely(string elementId, int timeoutSeconds)
{
    try
    {
        DateTime endTime = DateTime.Now.AddSeconds(timeoutSeconds);
        
        while (DateTime.Now < endTime)
        {
            try
            {
                if (IsElementVisible(elementId))
                    return true;
            }
            catch (Exception ex)
            {
                Log.Debug($"Ошибка при проверке элемента: {ex.Message}");
                // Продолжаем попытки до истечения времени
            }
            
            Thread.Sleep(500);
        }
        
        return false;
    }
    catch (Exception ex)
    {
        Log.Error($"Критическая ошибка при ожидании элемента: {ex.Message}");
        return false;
    }
}
```

#### 2. Обработка динамических списков

```csharp
// ✅ Хорошо: Обработка динамически изменяющихся списков элементов
public void ProcessDynamicList(string listContainerId)
{
    int maxIterations = 1000;
    int itemsProcessed = 0;
    bool hasMoreItems = true;
    
    while (hasMoreItems && itemsProcessed < maxIterations)
    {
        var visibleItems = GetVisibleItems(listContainerId);
        
        if (visibleItems.Count == 0)
        {
            hasMoreItems = false;
            continue;
        }
        
        foreach (var item in visibleItems)
        {
            ProcessItem(item);
            itemsProcessed++;
            
            if (itemsProcessed >= maxIterations)
            {
                Log.Warning("Достигнуто максимальное количество обрабатываемых элементов");
                return;
            }
        }
        
        // Проверяем, есть ли кнопка "Загрузить еще" и кликаем если есть
        hasMoreItems = TryLoadMoreItems();
    }
    
    Log.Info($"Обработано элементов: {itemsProcessed}");
}
```

### Рекомендации для PIX RPA

1. **Всегда задавайте условия выхода из циклов**
   - Используйте конструкции с предусловием (`while`) или ограниченным числом итераций (`for`)
   - Добавляйте проверки таймаутов во все циклы ожидания
   
2. **Применяйте логирование внутри циклов**
   - Логируйте прогресс выполнения через определенные интервалы
   - Добавляйте информацию о текущем состоянии цикла
   
3. **Используйте защитные механизмы**
   - Обрабатывайте исключения внутри циклов
   - Добавляйте вложенные таймауты для разных уровней ожидания
   
4. **При работе с UI**
   - Не полагайтесь только на визуальную проверку элементов
   - Комбинируйте разные методы проверки доступности элементов
   - Используйте явные ожидания вместо циклов с паузами

5. **Мониторинг и диагностика**
   - Добавляйте метрики выполнения длительных циклов
   - Предусматривайте механизмы аварийного прерывания зависших операций

**[⬆ К карте разделов](../../README.md#карта-разделов)**

</details>
