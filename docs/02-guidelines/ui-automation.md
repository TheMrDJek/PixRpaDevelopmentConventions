# Работа с UI

<details>
    <summary><b>Рекомендации по работе с UI (В работе)</b></summary>

Эффективная работа с элементами пользовательского интерфейса — критически важный аспект разработки надежных роботов. Неправильные подходы к поиску и взаимодействию с UI элементами могут привести к хрупким, нестабильным решениям.

## 1. Работа с Web UI (Selenium)

### Проблемы использования абсолютных XPath-путей

```xml
<!-- ❌ Плохо: абсолютный XPath путь -->
/html/body/div[1]/div/div/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[2]/div[4]/div/div/span[2]
```

Такие пути:
- Хрупкие: ломаются при малейшем изменении структуры страницы
- Нечитаемые: невозможно понять, к какому элементу ведет путь
- Сложные в поддержке: при изменении UI требуют полного переписывания

### Рекомендуемые подходы к поиску элементов

#### 1. Используйте идентификаторы и уникальные атрибуты

```xml
<!-- ✅ Хорошо: использование ID -->
//button[@id="submit-button"]

<!-- ✅ Хорошо: использование уникальных атрибутов -->
//input[@name="username"]
//button[@data-testid="login-btn"]
```

#### 2. Применяйте относительные пути с контекстом

```xml
<!-- ✅ Хорошо: использование класса и текста -->
//div[contains(@class, "user-profile")]//button[text()="Настройки"]

<!-- ✅ Хорошо: использование родительского контекста -->
//label[text()="Имя пользователя"]/following-sibling::input
```

#### 3. Используйте CSS-селекторы для простых случаев

```csharp
// CSS-селекторы часто короче и читабельнее XPath
string cssSelector = ".login-form button.submit";
```

#### 4. Создавайте надежные составные локаторы

```csharp
// Пример для PIX RPA (Selenium)
public IWebElement FindUserMenuItem()
{
    // Сначала находим меню пользователя
    var userMenu = driver.FindElement(By.Id("user-menu"));
    
    // Затем ищем конкретный пункт в контексте меню
    return userMenu.FindElement(By.XPath(".//li[contains(text(), 'Настройки')]"));
}
```

## 2. Работа с Desktop UI (UIAutomation)

### Проблемы при поиске элементов

Проблемы с Desktop UI аналогичны проблемам web UI, но имеют свою специфику:
- Нестабильность идентификаторов элементов
- Зависимость от разрешения экрана
- Изменение структуры окон при обновлениях приложения

### Рекомендуемые подходы

#### 1. Используйте уникальные свойства элементов

```csharp
// ✅ Хорошо: поиск по автоматизационному ID
element = windowElement.FindFirst(TreeScope.Descendants, new PropertyCondition(
    AutomationElement.AutomationIdProperty, "txtUsername"));

// ✅ Хорошо: поиск по имени
element = windowElement.FindFirst(TreeScope.Descendants, new PropertyCondition(
    AutomationElement.NameProperty, "Войти в систему"));
```

#### 2. Применяйте последовательное построение пути

```csharp
// ✅ Хорошо: пошаговый поиск элементов
var mainWindow = GetMainWindow("Название приложения");
var panel = FindElementByAutomationId(mainWindow, "mainPanel");
var button = FindElementByName(panel, "Сохранить");
```

#### 3. Добавляйте проверки доступности элементов

```csharp
// ✅ Хорошо: проверка существования и видимости элемента
public void ClickIfExists(AutomationElement parent, string elementName, int timeoutSeconds = 5)
{
    DateTime endTime = DateTime.Now.AddSeconds(timeoutSeconds);
    
    while (DateTime.Now < endTime)
    {
        var element = FindElementByName(parent, elementName);
        if (element != null && element.Current.IsEnabled)
        {
            InvokePattern invokePattern = element.GetCurrentPattern(InvokePattern.Pattern) as InvokePattern;
            invokePattern.Invoke();
            return;
        }
        Thread.Sleep(500);
    }
    
    throw new TimeoutException($"Элемент '{elementName}' не найден или недоступен");
}
```

## 3. Общие принципы работы с UI

### Используйте ожидания и таймауты

Вместо жестких пауз используйте явные и неявные ожидания:

```csharp
// ❌ Плохо: жесткая пауза
Thread.Sleep(5000);

// ✅ Хорошо: ожидание с таймаутом
bool WaitForElement(string xpath, int timeoutSeconds = 10)
{
    DateTime endTime = DateTime.Now.AddSeconds(timeoutSeconds);
    while (DateTime.Now < endTime)
    {
        try
        {
            var element = driver.FindElement(By.XPath(xpath));
            if (element.Displayed && element.Enabled)
                return true;
        }
        catch (NoSuchElementException) { }
        
        Thread.Sleep(500);
    }
    return false;
}
```

### Создавайте абстракции для часто используемых элементов

```csharp
// Пример для PIX RPA (Page Object Pattern)
public class LoginPage
{
    private readonly IWebDriver _driver;
    
    // Локаторы как свойства класса
    private By UsernameField => By.Id("username");
    private By PasswordField => By.Id("password");
    private By LoginButton => By.XPath("//button[text()='Войти']");
    
    public LoginPage(IWebDriver driver)
    {
        _driver = driver;
    }
    
    public void Login(string username, string password)
    {
        _driver.FindElement(UsernameField).SendKeys(username);
        _driver.FindElement(PasswordField).SendKeys(password);
        _driver.FindElement(LoginButton).Click();
    }
}
```

### Используйте проверки перед действиями

```csharp
// ✅ Хорошо: проверка перед кликом
public void SafeClick(string xpath)
{
    if (WaitForElement(xpath))
    {
        driver.FindElement(By.XPath(xpath)).Click();
    }
    else
    {
        Log.Warning($"Элемент '{xpath}' не найден для клика");
        // Обработка ситуации отсутствия элемента
    }
}
```

## 4. Рекомендации для PIX RPA

1. **Структурируйте локаторы**
   - Храните локаторы в отдельных переменных или константах
   - Группируйте локаторы по функциональным областям
   - Используйте говорящие имена для локаторов

2. **Создавайте обертки для стандартных операций с UI**
   - Разработайте набор утилитных методов для типовых операций
   - Инкапсулируйте логику ожидания и обработки ошибок

3. **Работайте с элементами по бизнес-логике**
   - Вместо механического клика на координаты, ищите элементы по их назначению
   - Используйте поиск "от общего к частному" (сначала контейнер, затем элементы внутри)

4. **Оптимизируйте скорость работы**
   - Используйте оптимальные селекторы (ID и name обычно быстрее, чем XPath)
   - Применяйте кэширование найденных элементов, когда это возможно
   - Используйте динамические ожидания вместо статических пауз

5. **Документируйте локаторы**
   - Добавляйте комментарии, объясняющие назначение локатора
   - При использовании сложных XPath объясняйте логику их построения

**[⬆ К карте разделов](../../README.md#карта-разделов)**

</details>
