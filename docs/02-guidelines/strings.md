# Строковые литералы

<details>
    <summary><b>Эффективная работа со строковыми литералами в PIX RPA</b></summary>

C# предлагает несколько специальных синтаксических конструкций для работы со строками, которые значительно упрощают разработку в PIX RPA.

### Основные типы строковых литералов:

#### 1. Интерполяция строк (`$`)

Позволяет встраивать выражения C# непосредственно в строки без конкатенации.

```csharp
// Вместо конкатенации:
string message = "Обработано " + fileCount + " файлов в папке " + folderPath;

// Используйте интерполяцию:
string message = $"Обработано {fileCount} файлов в папке {folderPath}";

// Можно использовать выражения и форматирование:
string report = $"Сумма: {amount:C2} | Дата: {date:dd.MM.yyyy}";
```

**Когда использовать в PIX RPA:**
- Формирование сообщений для логирования
- Построение SQL-запросов с параметрами
- Формирование путей к файлам
- Генерация отчетов

#### 2. Дословные строки (`@`)

Позволяют игнорировать escape-последовательности и записывать многострочный текст.

```csharp
// Вместо экранирования обратных слешей:
string path = "C:\\Program Files\\Application\\Data";

// Используйте дословные строки:
string path = @"C:\Program Files\Application\Data";

// Многострочный текст:
string query = @"
SELECT *
FROM Customers
WHERE City = 'Moscow'
  AND Status = 'Active'";
```

**Когда использовать в PIX RPA:**
- Пути к файлам и директориям
- SQL-запросы
- Регулярные выражения
- XML/HTML-шаблоны

#### 3. Необработанные строковые литералы (`"""`)

Позволяют работать с многострочным текстом, сохраняя форматирование и не требуя экранирования кавычек (доступно в новых версиях C#).

```csharp
// Многострочный текст с сохранением форматирования:
string json = """
{
    "name": "PIX Robot",
    "version": "1.0",
    "settings": {
        "timeout": 30,
        "retryCount": 3
    }
}
""";
```

**Примечание:** Доступна с версий PIX RPA которые работают на .NET 8 и выше

### Комбинирование строковых литералов

Вы можете комбинировать разные типы строковых литералов для максимального удобства:

```csharp
// Интерполяция + дословные строки:
string logEntry = $@"Время: {DateTime.Now:HH:mm:ss}
Пользователь: {userName}
Путь: C:\Users\{userName}\Documents";
```

### Советы для PIX RPA:

- **Используйте интерполяцию** (`$`) для динамического формирования строк вместо конкатенации
- **Применяйте дословные строки** (`@`) для путей к файлам и многострочных запросов
- **Избегайте сложной конкатенации строк** в циклах, используйте `StringBuilder` для большого количества операций
- **Для строк с HTML/XML-кодом** всегда используйте дословные строки (`@`) для улучшения читаемости

```csharp
// Пример в контексте PIX RPA:
string logMessage = $"[{DateTime.Now:yyyy-MM-dd HH:mm:ss}] Обработка файла {fileName}";

// Пример пути к файлу:
string filePath = @$"C:\PIX\Reports\{DateTime.Now:yyyy-MM-dd}\{reportName}.xlsx";

// Пример SQL-запроса:
string query = @$"
SELECT * 
FROM Orders 
WHERE CustomerID = '{customerId}' 
AND OrderDate >= '{startDate:yyyy-MM-dd}'";
```

Дополнительная информация:
- [Строковые литералы verbatim](https://learn.microsoft.com/ru-ru/dotnet/csharp/programming-guide/strings/#verbatim-string-literals)
- [Необработанные строковые литералы](https://learn.microsoft.com/ru-ru/dotnet/csharp/programming-guide/strings/#raw-string-literals)
- [Интерполяция строк](https://learn.microsoft.com/ru-ru/dotnet/csharp/programming-guide/strings/#string-interpolation)


**[⬆ К карте разделов](../../README.md#карта-разделов)**

</details>
