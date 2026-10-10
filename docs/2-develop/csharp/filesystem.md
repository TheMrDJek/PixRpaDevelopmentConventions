# Классы файловой системы .NET

Справка по классам .NET для работы с файловой системой. Правила работы с файлами в роботах — в разделе [Работа с файлами](../file.md).

## Содержание

- [FILESYSTEM-01. Используйте классы Path, Directory и File](#filesystem-01-используйте-классы-path-directory-и-file) — 🟡 Рекомендуется
- [FILESYSTEM-02. Выбирайте между File/Directory и FileInfo/DirectoryInfo по количеству операций](#filesystem-02-выбирайте-между-filedirectory-и-fileinfodirectoryinfo-по-количеству-операций) — 🟡 Рекомендуется

## FILESYSTEM-01. Используйте классы Path, Directory и File

🟡 **Рекомендуется**

### Класс Path для работы с путями

Класс `Path` предоставляет методы для обработки строк пути к файлам и директориям без обращения к реальной файловой системе. Он обеспечивает кроссплатформенность и безопасность операций.

**Основные методы:**

- `Path.Combine()` - объединяет две или более строки в путь с учетом разделителей для текущей ОС
- `Path.GetExtension()` - возвращает расширение файла (включая точку)
- `Path.GetFileName()` - возвращает имя файла и расширение
- `Path.GetFileNameWithoutExtension()` - возвращает имя файла без расширения
- `Path.GetDirectoryName()` - возвращает директорию из полного пути к файлу
- `Path.GetFullPath()` - возвращает абсолютный путь
- `Path.GetTempPath()` - возвращает путь к временной папке (особенно важно для PIX RPA)
- `Path.GetTempFileName()` - создает уникальный временный файл и возвращает путь к нему
- `Path.GetRandomFileName()` - генерирует случайное имя файла для временных файлов
- `Path.ChangeExtension()` - изменяет расширение в указанном пути
- `Path.HasExtension()` - проверяет наличие расширения в пути
- `Path.IsPathRooted()` - проверяет, является ли путь абсолютным

**Примеры использования в PIX RPA:** _(пример на C#)_

```csharp
// Создание путей к файлам отчетов с текущей датой
string reportFolder = Path.Combine(
    Settings.ReportBasePath, 
    DateTime.Now.ToString("yyyy-MM-dd")
);

// Генерация имени временного файла в системной папке
string tempFile = Path.Combine(
    Path.GetTempPath(), 
    $"pix_temp_{Guid.NewGuid()}.xlsx"
);

// Обработка списка файлов с определенным расширением
var files = Directory.GetFiles(sourceDir)
    .Where(f => Path.GetExtension(f).Equals(".pdf", StringComparison.OrdinalIgnoreCase))
    .Select(f => new { 
        FullPath = f,
        FileName = Path.GetFileNameWithoutExtension(f),
        CreationTime = File.GetCreationTime(f)
    })
    .ToList();
```

### Класс Directory для работы с директориями

Класс `Directory` предоставляет статические методы для создания, перемещения и перечисления директорий.

**Ключевые методы:**

- `Directory.Exists()` - проверяет существование директории
- `Directory.CreateDirectory()` - создает директорию (включая все родительские), если она не существует
- `Directory.Delete()` - удаляет директорию
- `Directory.GetFiles()` - получает список файлов в директории
- `Directory.GetDirectories()` - получает список поддиректорий
- `Directory.Move()` - перемещает директорию и её содержимое
- `Directory.GetCurrentDirectory()` - получает текущую рабочую директорию

**Примеры использования в PIX RPA:** _(пример на C#)_

```csharp
// Создание структуры директорий для хранения результатов
string baseDir = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "PIX_Results");
string dateDir = Path.Combine(baseDir, DateTime.Now.ToString("yyyy-MM-dd"));
Directory.CreateDirectory(dateDir); // Создаст все необходимые директории

// Рекурсивная обработка файлов в директории и поддиректориях
void ProcessFilesRecursively(string directory, string searchPattern)
{
    // Обрабатываем файлы в текущей директории
    foreach (var file in Directory.GetFiles(directory, searchPattern))
    {
        ProcessFile(file);
    }
    
    // Рекурсивно обрабатываем поддиректории
    foreach (var subDir in Directory.GetDirectories(directory))
    {
        ProcessFilesRecursively(subDir, searchPattern);
    }
}
```

### Класс File для работы с файлами

Класс `File` предоставляет статические методы для создания, копирования, удаления, перемещения и открытия файлов.

**Полезные методы:**

- `File.Exists()` - проверяет существование файла
- `File.Copy()` - копирует файл
- `File.Move()` - перемещает файл
- `File.Delete()` - удаляет файл
- `File.ReadAllText()` - читает содержимое текстового файла
- `File.WriteAllText()` - записывает текст в файл
- `File.ReadAllBytes()` - читает файл как массив байтов
- `File.WriteAllBytes()` - записывает данные в файл
- `File.ReadAllLines()` - читает все строки файла
- `File.AppendAllText()` - добавляет текст в конец файла
- `File.GetLastWriteTime()` - получает время последнего изменения файла
- `File.GetCreationTime()` - получает время создания файла

[⬆ К содержанию](#содержание)

## FILESYSTEM-02. Выбирайте между File/Directory и FileInfo/DirectoryInfo по количеству операций

🟡 **Рекомендуется**

В .NET есть две пары классов для работы с файловой системой:

| | Статические классы `File`, `Directory` | Экземплярные классы `FileInfo`, `DirectoryInfo` |
|---|---|---|
| Вызов | `File.Exists(path)` — путь передается в каждый вызов | `var info = new FileInfo(path); info.Exists` — объект хранит путь |
| Проверки безопасности и чтение атрибутов | При каждом вызове | Один раз при первом обращении, затем значения кешируются |
| Когда удобнее | Одна-две операции с файлом | Несколько операций или чтение нескольких свойств одного файла, перебор содержимого папки |

```csharp
// Одна операция — статический класс
if (File.Exists(reportPath))
    File.Delete(reportPath);

// Несколько свойств одного файла — FileInfo
var fileInfo = new FileInfo(attachmentPath);
if (fileInfo.Length > maxAttachmentSizeBytes)
    Log.Warning($"Вложение {fileInfo.Name} ({fileInfo.Length / 1024} КБ) превышает лимит");

// Перебор папки: DirectoryInfo возвращает FileInfo с уже прочитанными свойствами
var oldFiles = new DirectoryInfo(archiveFolder)
    .GetFiles("*.pdf")
    .Where(f => f.LastWriteTime < DateTime.Now.AddDays(-retentionDays));
```

> [!WARNING]
> `FileInfo` и `DirectoryInfo` кешируют свойства. Если файл изменился после создания объекта, вызовите `Refresh()`, прежде чем читать `Exists`, `Length` или `LastWriteTime`.

### Работа с атрибутами: оператор `|=`

Атрибуты файлов и папок (`FileAttributes`) — это битовые флаги: у одной папки может быть одновременно несколько атрибутов. Чтобы добавить атрибут, не сбросив уже установленные, используйте оператор побитового ИЛИ с присваиванием `|=`:

```csharp
var dirInfo = new DirectoryInfo(tempFolder);

// Добавить флаг Hidden к текущим атрибутам, сохранив остальные
dirInfo.Attributes |= FileAttributes.Hidden;

// То же самое в полной записи
dirInfo.Attributes = dirInfo.Attributes | FileAttributes.Hidden;
```

Если у папки был атрибут `ReadOnly`, то после выполнения кода она станет `ReadOnly | Hidden`. Присваивание `dirInfo.Attributes = FileAttributes.Hidden` без `|` сбросило бы `ReadOnly`.

Остальные операции с флагами:

```csharp
// Снять флаг, сохранив остальные
dirInfo.Attributes &= ~FileAttributes.Hidden;

// Проверить наличие флага
bool isHidden = dirInfo.Attributes.HasFlag(FileAttributes.Hidden);
```

[⬆ К содержанию](#содержание)
