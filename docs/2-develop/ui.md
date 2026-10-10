# Работа с UI

> [!NOTE]
> 🚧 **Раздел в работе.**

Эффективная работа с элементами пользовательского интерфейса — критически важный аспект разработки надежных роботов. Неправильные подходы к поиску и взаимодействию с UI элементами могут привести к хрупким, нестабильным решениям.

## Содержание

- [UI-01. Не используйте абсолютные XPath-пути](#ui-01-не-используйте-абсолютные-xpath-пути) — 🟡 Рекомендуется
- [UI-02. Ищите элементы Desktop UI по уникальным свойствам](#ui-02-ищите-элементы-desktop-ui-по-уникальным-свойствам) — 🟡 Рекомендуется
- [UI-03. Используйте ожидания вместо фиксированных пауз](#ui-03-используйте-ожидания-вместо-фиксированных-пауз) — 🔴 Обязательно
- [UI-04. Создавайте абстракции для часто используемых элементов](#ui-04-создавайте-абстракции-для-часто-используемых-элементов) — 🟡 Рекомендуется
- [UI-05. Проверяйте доступность элемента перед действием](#ui-05-проверяйте-доступность-элемента-перед-действием) — 🟡 Рекомендуется
- [Общие рекомендации для PIX RPA](#общие-рекомендации-для-pix-rpa)

## UI-01. Не используйте абсолютные XPath-пути

🟡 **Рекомендуется**

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

[⬆ К содержанию](#содержание)

## UI-02. Ищите элементы Desktop UI по уникальным свойствам

🟡 **Рекомендуется**

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

[⬆ К содержанию](#содержание)

## UI-03. Используйте ожидания вместо фиксированных пауз

🔴 **Обязательно**

Вместо жестких пауз используйте ожидания с таймаутом: активности PIX RPA для ожидания элемента или собственный цикл ожидания (см. [LOOP-02](loop.md#loop-02-используйте-активность-цикл-с--по-для-ожидания-ui-с-ограниченным-числом-попыток)).

```csharp
// ❌ Плохо: жесткая пауза
Thread.Sleep(5000);

// ✅ Хорошо: ожидание с таймаутом
bool WaitForElement(string xpath, int timeoutSeconds = 10)
{
    DateTime endTime = DateTime.Now.AddSeconds(timeoutSeconds);
    while (DateTime.Now < endTime)
    {
        // FindElements не выбрасывает исключение, если элемент не найден
        var element = driver.FindElements(By.XPath(xpath)).FirstOrDefault();
        if (element != null && element.Displayed && element.Enabled)
            return true;

        Thread.Sleep(500);
    }
    return false;
}
```

[⬆ К содержанию](#содержание)

## UI-04. Создавайте абстракции для часто используемых элементов

🟡 **Рекомендуется**

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

[⬆ К содержанию](#содержание)

## UI-05. Проверяйте доступность элемента перед действием

🟡 **Рекомендуется**

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

[⬆ К содержанию](#содержание)

## Общие рекомендации для PIX RPA

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

[⬆ К содержанию](#содержание)
