# Работа с файлами

Пути, временные файлы и файлы, которые могут быть открыты другими пользователями. Справка по классам `Path`, `File`, `FileInfo` и работе с атрибутами — в [pix-csharp-guide](https://github.com/TheMrDJek/pix-csharp-guide/blob/main/docs/filesystem.md).

## Содержание

- [FILE-01. Не используйте жестко заданные пути и конкатенацию строк для путей](#file-01-не-используйте-жестко-заданные-пути-и-конкатенацию-строк-для-путей) — 🔴 Обязательно
- [FILE-02. Управляйте временными файлами](#file-02-управляйте-временными-файлами) — 🔴 Обязательно
- [FILE-03. Копируйте файлы перед обработкой](#file-03-копируйте-файлы-перед-обработкой) — 🟡 Рекомендуется

## FILE-01. Не используйте жестко заданные пути и конкатенацию строк для путей

🔴 **Обязательно**

Примеры приведены на C#. Общие правила вынесения настроек из кода описаны в разделе [Жесткое кодирование](../1-project/config.md).

**Не используйте жестко заданные пути**
```csharp
// Плохо
string badPath = "C:\\Users\\Username\\Documents\\file.txt";

// Хорошо
string goodPath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments),
    "file.txt"
);
```

**Не конкатенируйте пути как строки**
```csharp
// Плохо - проблемы с разделителями
string badPath = baseDir + "\\" + subDir + "\\" + fileName;

// Хорошо - кроссплатформенно и надежно
string goodPath = Path.Combine(baseDir, subDir, fileName);
```

**Не создавайте файлы без проверки существования директории**
```csharp
// Плохо - может вызвать исключение
File.WriteAllText(Path.Combine(newDir, "file.txt"), content);

// Хорошо - создает директорию, если она не существует
Directory.CreateDirectory(newDir);
File.WriteAllText(Path.Combine(newDir, "file.txt"), content);
```

[⬆ К содержанию](#содержание)

## FILE-02. Управляйте временными файлами

🔴 **Обязательно**

При работе с файлами в процессе выполнения роботов важно соблюдать правила хранения временных файлов для обеспечения стабильности и безопасности системы.

**Используйте системную временную директорию:**
- Всегда используйте системную папку Temp для временных файлов вместо жестко заданных путей
- Получайте путь к системной временной директории с помощью класса [Path](https://learn.microsoft.com/ru-ru/dotnet/api/system.io.path)
- Никогда не храните временные файлы внутри проекта робота или в корневых директориях дисков

**Рекомендации по работе с временными файлами:**
- Создавайте уникальные имена для временных файлов (используйте Guid)
- Обязательно удаляйте временные файлы после использования, после исключения или очищайте временные папки перед использованием
- Логируйте операции создания и удаления временных файлов **для отладки**

**Запрещенные практики:**
- Хранение временных файлов в проекте робота: `@"C:\Projects\MyBot\temp\file.xlsx"`
- Хардкодинг путей: `@"C:\Temp\file.xlsx"` или `@"D:\WorkFiles\temp.csv"`
- Использование локальных папок без проверки доступности: `@".\temp\file.xlsx"`
- Создание временных файлов без механизма их гарантированного удаления

**Удаляйте временные файлы через общий вспомогательный метод.** Ошибка удаления временного файла не должна прерывать обработку транзакции, но и молча игнорировать ее нельзя:

```csharp
void SafeDeleteFile(string path)
{
    if (!File.Exists(path))
        return;

    try
    {
        File.Delete(path);
    }
    catch (IOException ex)
    {
        Log.Warning($"Не удалось удалить временный файл {path}: {ex.Message}");
    }
}
```

Этот метод используется в примерах ниже.

[⬆ К содержанию](#содержание)

## FILE-03. Копируйте файлы перед обработкой

🟡 **Рекомендуется**

> [!NOTE]
> 🚧 **Раздел в работе.**

При работе с файлами, особенно с форматами, которые могут быть открыты другими пользователями (Excel, Word, PDF), важно использовать копирование для предотвращения конфликтов доступа и обеспечения стабильности работы роботов.

### Проблемы при работе с файлами напрямую

1. **Блокировка файлов**
   - Файл может быть открыт другим пользователем
   - Excel и другие приложения блокируют файлы при открытии
   - Возникают исключения доступа, прерывающие работу робота

2. **Риск повреждения данных**
   - Одновременный доступ может привести к потере данных
   - Изменения, вносимые роботом, могут конфликтовать с действиями пользователя
   - Возможна потеря данных при сбоях

3. **Нестабильность выполнения**
   - Робот не может предсказать, когда файл будет освобожден
   - Прерывание операций чтения/записи влияет на весь процесс

### Рекомендации по работе с файлами

#### 1. Копирование файлов перед чтением

```csharp
// ✅ Хорошо: копирование файла перед чтением
public DataTable ReadExcelData(string sourceFilePath)
{
    // Создаем временное имя файла
    string tempFile = Path.Combine(
        Path.GetTempPath(),
        $"{Guid.NewGuid()}_{Path.GetFileName(sourceFilePath)}");
        
    try
    {
        // Копируем файл во временную локацию
        File.Copy(sourceFilePath, tempFile, true);
        
        // Работаем с копией файла
        using (var excel = new ExcelPackage(new FileInfo(tempFile)))
        {
            // Чтение данных из Excel...
            var worksheet = excel.Workbook.Worksheets[0];
            // Преобразование в DataTable...
            return ConvertToDataTable(worksheet);
        }
    }
    finally
    {
        // Обязательно удаляем временный файл
        SafeDeleteFile(tempFile);
    }
}
```

#### 2. Использование режима "только для чтения" там, где возможно

```csharp
// ✅ Хорошо: открытие файла только для чтения
using (var stream = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.ReadWrite))
using (var reader = new StreamReader(stream))
{
    // Чтение данных из файла
    string content = reader.ReadToEnd();
    // Обработка содержимого...
}
```

#### 3. Обработка занятых файлов

```csharp
// ✅ Хорошо: попытка доступа к файлу с повторами
public DataTable TryReadExcelWithRetries(string filePath, int maxAttempts = 3)
{
    int attempt = 0;
    while (attempt < maxAttempts)
    {
        try
        {
            attempt++;
            return ReadExcelData(filePath);
        }
        catch (IOException ex) when (IsFileLockException(ex))
        {
            Log.Warning($"Файл занят, попытка {attempt} из {maxAttempts}");
            
            if (attempt >= maxAttempts)
                throw new FileAccessException($"Не удалось получить доступ к файлу после {maxAttempts} попыток", ex);
                
            // Пауза перед следующей попыткой
            Thread.Sleep(2000);
        }
    }
    
    // Этот код не должен выполняться (из-за throw выше)
    throw new InvalidOperationException("Unexpected execution path");
}

private bool IsFileLockException(IOException ex)
{
    int errorCode = Marshal.GetHRForException(ex) & 0xFFFF;
    return errorCode == 32 || errorCode == 33; // 32: file being used by another process, 33: lock violation
}
```

### Рекомендации для различных типов файлов

#### Excel-файлы

```csharp
// ✅ Хорошо: безопасное чтение Excel-файла
public DataTable ReadExcelSafely(string excelPath)
{
    // Создаем временную копию
    string tempFile = Path.Combine(
        Path.GetTempPath(),
        $"temp_{Guid.NewGuid()}.xlsx");
    
    try
    {
        File.Copy(excelPath, tempFile, true);
        
        // Используем библиотеку для работы с Excel (EPPlus, NPOI, и т.д.)
        using (var package = new ExcelPackage(new FileInfo(tempFile)))
        {
            var worksheet = package.Workbook.Worksheets[0];
            // Чтение и конвертация данных...
            return ConvertWorksheetToDataTable(worksheet);
        }
    }
    finally
    {
        // Гарантированная очистка
        SafeDeleteFile(tempFile);
    }
}
```

#### Файлы CSV и текстовые файлы

```csharp
// ✅ Хорошо: безопасное чтение текстовых файлов
public List<string> ReadTextFileSafely(string filePath)
{
    string tempFile = Path.Combine(
        Path.GetTempPath(),
        $"temp_{Guid.NewGuid()}.txt");
    
    try
    {
        File.Copy(filePath, tempFile, true);
        return File.ReadAllLines(tempFile).ToList();
    }
    finally
    {
        SafeDeleteFile(tempFile);
    }
}
```

### Когда НЕ нужно копировать файлы

При некоторых сценариях копирование файлов не требуется или может быть нежелательным:

1. **При редактировании файлов**
   - Если цель - изменить оригинальный файл, лучше обрабатывать ошибки доступа
   - Вместо копирования используйте блокировки и информативные сообщения об ошибках

```csharp
// Для сценариев редактирования: обработка ошибок доступа
try
{
    using (var excel = new ExcelPackage(new FileInfo(filePath)))
    {
        // Редактирование...
        excel.Save();
    }
}
catch (IOException ex) when (IsFileLockException(ex))
{
    Log.Error("Невозможно отредактировать файл, так как он открыт другим пользователем");
    throw new BusinessException("Пожалуйста, закройте файл и повторите операцию", ex);
}
```

2. **Для очень больших файлов**
   - При работе с большими файлами копирование может быть неэффективным
   - Используйте потоковую обработку и блокировки

```csharp
// Потоковая обработка большого файла
using (var stream = new FileStream(
    largeFilePath, FileMode.Open, FileAccess.Read, FileShare.ReadWrite))
using (var reader = new StreamReader(stream))
{
    string line;
    while ((line = reader.ReadLine()) != null)
    {
        // Построчная обработка без полного копирования
        ProcessLine(line);
    }
}
```

### Рекомендации для PIX RPA

1. **Создавайте утилитные методы для работы с файлами**
   - Разработайте стандартные функции для копирования и чтения файлов
   - Инкапсулируйте логику работы с временными файлами

2. **Применяйте шаблон для обработки разных типов файлов**
   - Выделите общую логику копирования и очистки
   - Создайте специализированные обработчики для различных форматов

```csharp
public T ProcessFileWithCopy<T>(string filePath, Func<string, T> processFunc)
{
    string tempFile = Path.Combine(
        Path.GetTempPath(),
        $"temp_{Guid.NewGuid()}_{Path.GetFileName(filePath)}");
    
    try
    {
        File.Copy(filePath, tempFile, true);
        return processFunc(tempFile);
    }
    finally
    {
        SafeDeleteFile(tempFile);
    }
}

// Использование
var excelData = ProcessFileWithCopy(excelPath, path => ReadExcelFile(path));
var csvData = ProcessFileWithCopy(csvPath, path => ReadCsvFile(path));
```

3. **Логируйте операции с файлами**
   - Добавляйте информативные сообщения о копировании и обработке
   - Логируйте успешное удаление временных файлов

4. **Обрабатывайте исключения специфично для каждого типа файлов**
   - Создавайте специализированные обработчики ошибок для Excel, PDF и других форматов
   - Предоставляйте понятные бизнес-сообщения при сбоях

[⬆ К содержанию](#содержание)
