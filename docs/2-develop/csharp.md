# Синтаксис C# для скриптов PIX

Справочник показывает синтаксис C# для выражений, строк и коллекций в скриптах PIX. В таблицах указано, в какой версии C# появилась каждая конструкция.

Если проект нацелен на .NET 10, SDK по умолчанию выбирает C# 14. Перед съёмкой скриншота проверьте пример в нужном поле PIX Studio: редактор может обрабатывать выражение иначе, чем компилятор обычного C#-проекта. [Версии языка C#](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning).

## Содержание

- [Как переносить примеры в Studio](#как-переносить-примеры-в-studio) (📘 Справка)
- [Что пригодится в роботах](#что-пригодится-в-роботах) (📘 Справка)
- [Базовые конструкции, появившиеся до C# 10](#базовые-конструкции-появившиеся-до-c-10) (📘 Справка)
- [C# 10: свойства, лямбды и копирование значений](#c-10-свойства-лямбды-и-копирование-значений) (📘 Справка)
- [C# 11: многострочный текст и шаблоны списков](#c-11-многострочный-текст-и-шаблоны-списков) (📘 Справка)
- [C# 12: создание коллекций и параметры лямбд](#c-12-создание-коллекций-и-параметры-лямбд) (📘 Справка)
- [C# 13: изменения для методов и библиотек](#c-13-изменения-для-методов-и-библиотек) (📘 Справка)
- [C# 14: присваивание через null-доступ](#c-14-присваивание-через-null-доступ) (📘 Справка)
- [Возможности для собственных типов](#возможности-для-собственных-типов) (📘 Справка)
- [Остальные изменения и их применимость](#остальные-изменения-и-их-применимость) (📘 Справка)

## Как переносить примеры в Studio

📘 **Справка**

Выражения проверяйте в свойствах активностей PIX. Примеры с объявлениями и выводом можно запустить в консольном проекте с включёнными неявными импортами и проверкой nullable-ссылок. В Studio результат смотрите в переменной при отладке.

- В активности «Присвоить значение» задайте переменную результата и выражение справа от `=`. Объявление типа и завершающая точка с запятой относятся к C#-коду.
- Для нескольких команд используйте активность «Выполнить». Если значения нужны следующим активностям, объявите соответствующие переменные в скрипте и присваивайте им результаты без повторного локального объявления.
- `using` и объявления классов из раздела о библиотеках относятся к C#-файлу. Не переносите их целиком в поле выражения.
- `return` внутри локальной функции завершает эту функцию. Не считайте его способом завершить весь PIX-скрипт.

Проверьте обычный случай и тот, на который рассчитан пример. Для `?.` передайте `null`, для шаблона списка возьмите пустой массив, для `switch` введите неизвестный статус. На скриншоте показывайте одинаковые исходные данные и одну переменную результата для вариантов «до» и «после».

## Что пригодится в роботах

📘 **Справка**

| Платформа | Язык по умолчанию | Полезно в скриптах | Чаще нужно в библиотеках |
|---|---|---|---|
| .NET 6 | C# 10 | Сокращённые проверки вложенных свойств, вывод типа лямбды, `with` для анонимных объектов | `record struct`, `global using`, файловые пространства имён, `CallerArgumentExpression` |
| .NET 7 | C# 11 | Многострочные raw-строки, шаблоны списков | `required`, UTF-8-литералы, обобщённая математика |
| .NET 8 | C# 12 | Выражения коллекций `[]`, включение элементов через `..`, параметры лямбды по умолчанию | Первичные конструкторы, псевдонимы типов, inline-массивы |
| .NET 9 | C# 13 | Новых повседневных сокращений для условий немного | Коллекции в `params`, новый `Lock`, возможности `ref struct` |
| .NET 10 | C# 14 | Присваивание через `?.` и `?[]` | `field`, extension-блоки, преобразования `Span`, новые формы лямбд |

Для первых скриншотов полезнее всего выбор значения, доступ при `null`, `switch`, проверки свойств, шаблоны списков и выражения коллекций. Они встречаются при обработке заявок, результатов API и табличных данных.

## Базовые конструкции, появившиеся до C# 10

📘 **Справка**

| Конструкция | Первая версия | Где пригодится в роботе |
|---|---|---|
| `?:` | C# 1.0, 2002 | Выбрать одну из двух подписей для отчёта в активности «Присвоить значение». |
| Оператор `switch` | C# 1.0, 2002 | Выбрать действие по коду операции. |
| `??` | C# 2.0, 2005 | Выбрать дату по расписанию при отсутствии даты ручного запуска. |
| `?.` и `?[]` | C# 6.0, 2015 | Прочитать поле необязательного объекта или обратиться к элементу коллекции, которая может отсутствовать. |
| `??=` | C# 8.0, 2019 | Заполнить переменную запасным значением, чтобы его использовали следующие активности. |
| `switch`-выражение | C# 8.0, 2019 | Преобразовать код статуса из API в подпись для отчёта. |
| Шаблоны `and`, `or`, `not` и сравнения вроде `>= 0` | C# 9.0, 2020 | Описать допустимые значения, например принять только неотрицательное целое количество товара. |

Версии сверены со спецификациями C# и историей языка. [ECMA-334, 1-е издание](https://www.ecma-international.org/wp-content/uploads/ECMA-334_1st_edition_december_2001.pdf), [ECMA-334, 3-е издание](https://ecma-international.org/wp-content/uploads/ECMA-334_3rd_edition_june_2005.pdf), [история C#](https://github.com/dotnet/csharplang/blob/main/Language-Version-History.md).

### Выбрать одно из двух значений

Для тестового письма добавьте пометку в тему.

**Через `if/else`**

```csharp
string emailSubject;
if (isTestRun)
{
    emailSubject = "[ТЕСТ] Отчёт по заказам";
}
else
{
    emailSubject = "Отчёт по заказам";
}
```

**Через `?:`**

```csharp
string emailSubject = isTestRun
    ? "[ТЕСТ] Отчёт по заказам"
    : "Отчёт по заказам";
```

### Прочитать необязательный комментарий

Уберите пробелы по краям комментария из выгрузки. Если комментарий отсутствует, результатом будет `null`.

**Через проверку на `null`**

```csharp
string? reportComment = null;
if (comment is not null)
{
    reportComment = comment.Trim();
}
```

**Через `?.`**

```csharp
string? reportComment = comment?.Trim();
```

Оператор `?[]` так же проверяет объект слева на `null`. У существующей коллекции индекс должен быть допустимым, а у словаря ключ должен существовать.

### Подставить дату отчёта по умолчанию

При запуске по расписанию робот выгружает данные за предыдущий рабочий период. При ручном перезапуске оператор может передать `in_ReportDate` типа `DateTime?`. Дата по расписанию уже рассчитана в `scheduledReportDate`.

**До.** В ветке «Истина» при `in_ReportDate is null` присвойте `reportDate` значение `scheduledReportDate`. В ветке «Ложь» присвойте `in_ReportDate.Value`.

**После.** Одно «Присвоить значение» для `reportDate`.

```csharp
in_ReportDate ?? scheduledReportDate
```

Параметр `in_ReportDate` сохраняет исходное значение. По нему можно узнать, передал ли оператор дату.

### Заполнить путь к отчёту по умолчанию

При повторном запуске скрипт может получить готовый путь к Excel-отчёту. Если путь отсутствует, робот собирает его из рабочей папки и даты. В обоих случаях сохранение и отправка используют рабочую переменную `reportPath`.

**До.** При `reportPath is null` присвойте `reportPath` результат `Path.Combine(exportDirectory, $"Orders_{reportDate:yyyy-MM-dd}.xlsx")`.

**После.** В активности «Выполнить» запишите присваивание с `??=`.

```csharp
reportPath ??= Path.Combine(exportDirectory, $"Orders_{reportDate:yyyy-MM-dd}.xlsx");
```

При заданном пути правая часть не вычисляется. Пустая строка и пробелы тоже останутся в переменной, поскольку `??=` проверяет только `null`.

### Выбрать значение через `switch`

После проверки заявок робот добавляет в Excel-отчёт исходный код результата и подпись для оператора. Подпись нужна только для отчёта. Если встретится новый код, оператор увидит исходное значение и пометку «Неизвестный результат».

**До.** «Условный оператор» проверяет `resultCode`, а каждая ветка присваивает свою подпись переменной `resultText`.

**После.** Одно «Присвоить значение» для `resultText`.

```csharp
resultCode switch
{
    "IMPORTED" => "Загружено в 1С",
    "DUPLICATE" => "Заказ уже есть",
    "INVALID_DATA" => "Проверьте данные",
    _ => "Неизвестный результат"
}
```

Ветка `_` выбирает текст для любого оставшегося кода, включая `null`.

### Выполнить действие через оператор `switch`

Оператор `switch` выполняет ветку для заданного значения. По параметру `operation` программа копирует или перемещает файл. Ветка `default` отклоняет неизвестную операцию.

```csharp
switch (operation)
{
    case "Copy":
        File.Copy(sourcePath, destinationPath);
        break;

    case "Move":
        File.Move(sourcePath, destinationPath);
        break;

    default:
        throw new ArgumentException("Допустимые операции: Copy и Move.", nameof(operation));
}
```

### Разобрать количество из ячейки через switch и when

Робот читает колонку `Quantity` из `DataTable`. В этом примере источник может вернуть целое число типа `int`, строку с целым числом или `DBNull.Value` для пустой ячейки. Пустая ячейка допустима и даёт `null`.

```csharp
using System.Globalization;

static int? ReadQuantity(object? cellValue) => cellValue switch
{
    null or DBNull => null,
    int quantity and >= 0 => quantity,
    string text when int.TryParse(
        text, NumberStyles.Integer, CultureInfo.InvariantCulture, out var parsedQuantity)
        && parsedQuantity >= 0 => parsedQuantity,
    _ => throw new FormatException("Недопустимое значение в колонке Quantity.")
};

object? cellValue = "42";
int? quantity = ReadQuantity(cellValue);
Console.WriteLine(quantity); // 42
```

Ветка `string text when ...` срабатывает, если строка разбирается в неотрицательное целое число. Для `-1`, пустой строки или `"12.5"` сработает ветка `_` и функция выбросит исключение. Если ваш источник возвращает другие типы, например `double`, учтите их явно при разборе.

Справка Microsoft по синтаксису. [Условный оператор](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/conditional-operator), [null-доступ](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/member-access-operators), [объединение с null](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/null-coalescing-operator), [switch](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/switch-expression).

## C# 10: свойства, лямбды и копирование значений

📘 **Справка**

### Проверить вложенное свойство

Сокращённый шаблон свойства `Customer.Email.Length` объединяет проверку пути и значения. Если объект на пути равен `null`, шаблон не совпадёт. Анонимный объект здесь заменяет небольшой ответ API, чтобы пример не требовал отдельного класса.

```csharp
var request = new
{
    Customer = new { Email = "robot@example.test" }
};

bool hasEmailBefore = request is { Customer: { Email: { Length: > 0 } } };
bool hasEmail = request is { Customer.Email.Length: > 0 };

Console.WriteLine(hasEmailBefore == hasEmail); // True
Console.WriteLine(hasEmail); // True
```

Эта проверка подтверждает только наличие символов. Она не проверяет формат адреса и пропустит строку из пробелов. Для строкового поля часто понятнее `!string.IsNullOrWhiteSpace(value)`. Подробнее о [шаблонах свойств](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/patterns#property-pattern).

### Получить новый анонимный объект через with

Удобно для локального промежуточного результата. Свойства анонимного объекта доступны только для чтения, поэтому для изменения создаётся новый объект.

```csharp
var original = new { OrderNumber = "A-104", RetryCount = 0 };
var retry = original with { RetryCount = original.RetryCount + 1 };

Console.WriteLine(original.RetryCount); // 0
Console.WriteLine(retry.RetryCount);    // 1
```

Если у объекта есть вложенный список, исходный объект и копия ссылаются на тот же список, пока вы явно его не замените. Между скриптами передавайте данные в типе, доступном обоим скриптам. См. [выражение with](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/with-expression).

### Не повторять тип делегата для короткой функции

Компилятор выводит тип делегата из параметров и результата лямбды. В примере функция нужна только внутри одного фрагмента C#.

```csharp
var normalizeCode = (string value) => value.Trim().ToUpperInvariant();
string normalizedCode = normalizeCode(" ab-104 ");

Console.WriteLine(normalizedCode); // AB-104
```

Обычный LINQ вида `items.Where(item => item.IsActive)` не требует этой новой формы. Не переносите большой сценарий робота в лямбду ради сокращения записи. Подробнее о [лямбда-выражениях](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions).

## C# 11: многострочный текст и шаблоны списков

📘 **Справка**

### Записать текст без экранирования кавычек

Raw-строка ограничивается как минимум тремя кавычками. Она удобна для многострочного SQL, XML и постоянных JSON-примеров. Отступ закрывающих кавычек определяет общий отступ, который будет удалён из текста.

```csharp
string query = """
    SELECT "OrderNumber", "Status"
    FROM "Orders"
    WHERE "CustomerId" = @customerId
    """;

Console.WriteLine(query);
```

Значение `customerId` передавайте параметром команды БД. Raw-строка меняет способ записи текста и не делает вставку пользовательских данных в SQL безопасной. Подробнее о [raw-строках](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/raw-string).

### Совместить raw-строку и подстановки

Два знака `$` означают, что подстановка обозначается двойными фигурными скобками. Одиночные фигурные скобки остаются частью текста. В этом примере в JSON подставляется целое число.

```csharp
int retryCount = 2;
string sampleJson = $$"""
    {
      "retryCount": {{retryCount}},
      "status": "pending"
    }
    """;

Console.WriteLine(sampleJson);
```

Для JSON с произвольными строками используйте сериализацию, чтобы кавычки и управляющие символы экранировались по правилам JSON. См. [интерполированные raw-строки](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated#interpolated-raw-string-literals).

### Проверить структуру массива или списка

Шаблон списка проверяет длину и элементы. `..` допускает оставшиеся элементы, `var` сохраняет найденный элемент в переменную. Для `null` или недостаточной длины совпадения не будет.

```csharp
string[] headers = { "OrderNumber", "Amount", "Currency" };

bool hasRequiredPrefix = headers is ["OrderNumber", "Amount", ..];
Console.WriteLine(hasRequiredPrefix); // True

string[]? files = { "orders.csv", "archive.csv" };
if (files is [var firstFile, ..])
{
    Console.WriteLine(firstFile); // orders.csv
}
```

Подходит для массива заголовков с фиксированным порядком. Если порядок столбцов произвольный, ищите их по именам. Шаблон списка не применяется к произвольному `IEnumerable<T>` без доступа по индексу. Не материализуйте большой запрос только ради такого шаблона. См. [шаблоны списков](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/patterns#list-patterns).

### Определить формат выгрузки по первым заголовкам

Робот обрабатывает две выгрузки. В одной после `OrderId` сразу идёт `Amount`, в другой между ними есть `Currency`. Варианты в `switch` описывают начало каждого формата.

```csharp
string[] headers = { "OrderId", "Currency", "Amount", "Comment" };

string layout = headers switch
{
    ["OrderId", "Amount", ..] => "standard",
    ["OrderId", "Currency", "Amount", ..] => "withCurrency",
    _ => throw new FormatException("Неизвестный формат заголовков.")
};

Console.WriteLine(layout); // withCurrency
```

Шаблоны с `..` допускают дополнительные столбцы после указанных. Более короткий массив или заголовки в другом порядке попадут в ветку `_`, если не подходят ни под один из вариантов. Если источник разрешает произвольный порядок, ищите столбцы по именам.

## C# 12: создание коллекций и параметры лямбд

📘 **Справка**

### Создать коллекцию и включить элементы другой

Квадратные скобки создают коллекцию заданного типа. `..` включает элементы существующей последовательности в новую коллекцию.

```csharp
string[] requiredColumns = ["OrderNumber", "Amount"];
List<string> optionalColumns = ["Comment", "Department"];

List<string> allColumns = [.. requiredColumns, .. optionalColumns];
List<string> failedOrderNumbers = [];

Console.WriteLine(string.Join(", ", allColumns));
Console.WriteLine(failedOrderNumbers.Count); // 0
```

Компилятору нужен целевой тип, например `string[]` или `List<string>`. Запись `var columns = ["OrderNumber"]` не компилируется. В Studio проверьте, что редактор выражения использует тип переменной назначения. Для словаря с парами ключ-значение сохраняйте обычный инициализатор `new Dictionary<...> { ... }`.

При создании коллекции `..` сразу перечисляет источник. Для отложенной обработки большого потока используйте LINQ. Ссылочные элементы в обеих коллекциях указывают на те же объекты. См. [выражения коллекций](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/collection-expressions).

### Задать значение параметра лямбды по умолчанию

Подходит для небольшой локальной функции форматирования. Для повторно используемого шага робота предпочтительнее отдельный скрипт с явными параметрами.

```csharp
var formatOrderNumber = (int number, string prefix = "ORD") =>
    $"{prefix}-{number:D6}";

Console.WriteLine(formatOrderNumber(42));        // ORD-000042
Console.WriteLine(formatOrderNumber(42, "RET")); // RET-000042
```

Значение по умолчанию относится к вызову этой лямбды. Оно не задаёт значение параметра в таблице скрипта PIX. См. [параметры лямбд](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions#input-parameters-of-a-lambda-expression).

## C# 13: изменения для методов и библиотек

📘 **Справка**

### Передать несколько аргументов в params-коллекцию

Раньше `params` применялся к массивам. Теперь метод или локальная функция может принимать подходящий тип коллекции. Синтаксис относится к вызовам из C#-кода.

```csharp
static string JoinOrderNumbers(params IEnumerable<string> orderNumbers)
{
    return string.Join(", ", orderNumbers);
}

Console.WriteLine(JoinOrderNumbers("A-101", "A-102")); // A-101, A-102
```

Для обычного робота `params string[]` часто достаточно. Новая форма полезна при проектировании C#-метода, который уже принимает коллекцию. Остальные заметные изменения C# 13 относятся к синхронизации, `ref struct` и генерации кода. См. [нововведения C# 13](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-13).

## C# 14: присваивание через null-доступ

📘 **Справка**

### Записать значение, только если объект существует

В C# 14 операторы `?.` и `?[]` можно использовать слева от присваивания. Оба варианта ниже записывают статус, если словарь отчёта существует. Индексатор добавит ключ или заменит его значение.

```csharp
Dictionary<string, string>? optionalReport = new();

if (optionalReport is not null)
{
    optionalReport["Status"] = "Processed";
}

Console.WriteLine(optionalReport?["Status"]); // Processed

optionalReport = new(); // Те же исходные данные для второго варианта.
optionalReport?["Status"] = "Processed";
Console.WriteLine(optionalReport?["Status"]); // Processed
```

Присваивание пропускается целиком, если объект равен `null`. Робот пропускает и вычисление правой части.

```csharp
Dictionary<string, string>? optionalReport = null;
int buildCount = 0;

string BuildStatus()
{
    buildCount++;
    return "Processed";
}

optionalReport?["Status"] = BuildStatus();
Console.WriteLine(buildCount); // 0
```

Используйте для необязательного результата, который разрешено не формировать. Если объект должен существовать, защитная проверка с исключением лучше покажет ошибку. Оператор не создаёт объект и не защищает от неверного индекса массива. В Studio начните проверку с активности «Выполнить». См. [null-conditional assignment](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-14#null-conditional-assignment).

### Заполнить поле необязательного отчёта через ?[] и ??=

Отчёт может отсутствовать. Если робот его сформировал и поле `source` ещё не заполнено, запишите источник данных.

```csharp
using System.Text.Json.Nodes;

JsonObject? optionalReport = new();
optionalReport?["source"] ??= "Excel";

Console.WriteLine(optionalReport?["source"]); // Excel
```

`?[]` пропускает обращение, если весь отчёт равен `null`. `??=` заполняет отсутствующее или равное `null` поле. Если в отчёте уже указано `"API"`, оно сохранится.

## Возможности для собственных типов

📘 **Справка**

В проектах библиотек эти конструкции пригодятся при объявлении типов для данных и настроек.

### C# 10: readonly record struct

Подходит для небольшого значения, например пары «товар и количество». Компилятор создаёт свойства и сравнение по значениям. `with` возвращает копию с указанными изменениями.

```csharp
var original = new StockPosition("SKU-104", 5);
var updated = original with { Quantity = 7 };

Console.WriteLine(original.Quantity); // 5
Console.WriteLine(updated.Quantity);  // 7

public readonly record struct StockPosition(string ProductCode, int Quantity);
```

`readonly` не делает вложенный список неизменяемым, а `record` не проверяет допустимость количества. При необходимости задавайте ограничения отдельно. Подробнее о [record-типах](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/record).

### C# 11: required для обязательного присваивания свойства

`required` требует указать свойство при создании объекта. Компилятор проверяет, что свойству присвоили значение. Допустимость значения проверяйте отдельно.

```csharp
var request = new OrderRequest { OrderNumber = "A-104" };
Console.WriteLine(request.OrderNumber);

public sealed class OrderRequest
{
    public required string OrderNumber { get; init; }
}
```

Пустую строку присвоить можно. Поведение десериализации зависит от используемого сериализатора и его настроек. См. [модификатор required](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/required).

### C# 12: первичный конструктор

Параметры можно объявить рядом с именем класса. Для обычного класса они не становятся публичными свойствами автоматически.

```csharp
var formatter = new OrderNumberFormatter("ORD");
Console.WriteLine(formatter.Format(42)); // ORD-000042

public sealed class OrderNumberFormatter(string prefix)
{
    public string Format(int number) => $"{prefix}-{number:D6}";
}
```

Применяйте при разработке небольшого класса с зависимостями. Этот синтаксис не заменяет входные параметры PIX-скрипта. См. [первичные конструкторы](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/primary-constructors).

### C# 14: field внутри свойства

`field` обращается к полю, которое компилятор создаёт для свойства. Можно добавить проверку присваивания без отдельного объявления поля.

```csharp
var settings = new RetrySettings { MaxAttempts = 3 };
Console.WriteLine(settings.MaxAttempts); // 3

public sealed class RetrySettings
{
    public int MaxAttempts
    {
        get;
        set => field = value > 0
            ? value
            : throw new ArgumentOutOfRangeException(nameof(value));
    } = 1;
}
```

Проверка выполняется в `set`. Не считайте, что любой способ инициализации автоматически пройдёт через этот код: начальное значение свойства должно быть корректным само по себе. См. [ключевое слово field](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/field).

### C# 14: extension-блок

Можно объявить свойства расширения для существующего типа. В библиотеке такое свойство подходит для проверки, которая повторяется в нескольких местах.

```csharp
string orderNumber = "A-104";
Console.WriteLine(orderNumber.IsBlank); // False

public static class TextExtensions
{
    extension(string? value)
    {
        public bool IsBlank => string.IsNullOrWhiteSpace(value);
    }
}
```

Расширение должно быть доступно через подключённую библиотеку и пространство имён. Оно не добавляет хранимое поле в исходный тип. См. [члены расширения](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-14#extension-members).

## Остальные изменения и их применимость

📘 **Справка**

Ниже перечислены остальные основные возможности периода. Для них отдельные примеры в схеме робота обычно не нужны. Полные списки доступны в [истории версий C#](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history).

| Версия | Возможности | Где применяются |
|---|---|---|
| C# 10 | `global using`, файловое пространство имён | Оформление файлов C#-проекта. Не вставляются внутрь активности. |
| C# 10 | Обработчики интерполированных строк, `CallerArgumentExpression` | Реализация библиотек логирования и проверок. В обычном коде чаще используются через готовый API. |
| C# 10 | Константная интерполяция, смешанная деконструкция, явный возвращаемый тип и атрибуты лямбд | Отдельные локальные сокращения. Не требуют нового правила для роботов. |
| C# 10 | Конструкторы и инициализаторы структур, `with` для структур, `sealed ToString` в record, улучшение анализа присваивания | Проектирование типов и диагностика компилятора. |
| C# 10 | `AsyncMethodBuilder` на методах, привязка `#line` | Специализированные async-библиотеки и генераторы кода. |
| C# 11 | Переносы строк внутри выражения интерполяции | Удобны для короткого многострочного выражения. Сложный расчёт лучше выполнить перед форматированием. |
| C# 11 | UTF-8-литералы `u8` | Возвращают байтовое представление через `ReadOnlySpan<byte>`. Не заменяют `string` в активности отправки письма. |
| C# 11 | Статические абстрактные члены интерфейсов, generic math, беззнаковый сдвиг `>>>`, relaxed shift, checked-операторы | Численные библиотеки и собственные операторы. Для суммы заказа достаточно обычных операций с `decimal`. |
| C# 11 | Обобщённые атрибуты, file-local types, расширенный `nameof`, автоматическая инициализация полей struct | Метаданные, собственные типы и генерация кода. |
| C# 11 | Сопоставление `Span<char>` со строкой, `ref`-поля, `scoped`, aliases `nint`/`nuint`, оптимизация делегатов | Работа с памятью и производительностью. Не повод усложнять обработку обычных строк. |
| C# 12 | Псевдоним любого типа, `ref readonly`, inline-массивы, `ExperimentalAttribute` | Библиотеки и их API. Псевдоним типа не создаёт новый тип данных. |
| C# 12 | Interceptors | Экспериментальная в этой версии возможность генераторов кода. Для скриптов не требуется. |
| C# 13 | `System.Threading.Lock` | Синхронизация потоков C# внутри процесса. Не блокировка очереди или нескольких экземпляров робота. |
| C# 13 | `ref` и `unsafe` в async/итераторах, интерфейсы у `ref struct`, `allows ref struct` | Библиотеки обработки памяти, где важны ограничения времени жизни ссылок. |
| C# 13 | Частичные свойства и индексаторы, приоритет перегрузок, вывод типа группы методов | Библиотеки и сгенерированный код. |
| C# 13 | Escape-последовательность `\e`, индекс `^` в инициализаторе объекта | Терминальный вывод и редкие формы инициализации. Сам индекс `^` появился раньше. |
| C# 14 | Неявные преобразования Span, модификаторы параметров лямбд без явного типа | Вызовы C# API и низкоуровневые делегаты. |
| C# 14 | `nameof(List<>)`, частичные конструкторы и события, пользовательские составные присваивания | Метаданные и реализация типов. `nameof` сам по себе не нововведение C# 14. |
| .NET 10 SDK / C# 14 | Запуск файловых приложений и директивы `#:` | Отдельные утилиты C# вне Studio. Не формат PIX-скрипта. |

Обзоры версий от Microsoft. [C# 10](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-10), [C# 11](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-11), [C# 12](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-12), [C# 13](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-13), [C# 14](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-14).

API платформы, такие как `DateOnly`, `Chunk` и `ArgumentNullException.ThrowIfNull`, ищите в документации библиотек .NET.
