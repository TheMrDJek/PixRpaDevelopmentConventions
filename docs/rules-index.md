# Реестр правил

Сводный список всех правил с идентификаторами и уровнями обязательности. Уровни описаны в [README](../README.md#уровни-обязательности).

Ссылайтесь на правило по идентификатору, например в комментарии к Pull Request: «нарушено EXC-03».

## Соглашения

| ID | Уровень | Правило | Раздел |
|----|---------|---------|--------|
| PRJ-01 | MUST | [Разделяйте проект на слои](01-conventions/project-structure.md#prj-01-разделяйте-проект-на-слои) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-02 | MUST | [Используйте шаблон на основе State Machine](01-conventions/project-structure.md#prj-02-используйте-шаблон-на-основе-state-machine) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-03 | MUST | [Используйте состояния по назначению](01-conventions/project-structure.md#prj-03-используйте-состояния-по-назначению) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-04 | MUST | [Храните шаблоны и прочие файлы в самом проекте робота](01-conventions/project-structure.md#prj-04-храните-шаблоны-и-прочие-файлы-в-самом-проекте-робота) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-05 | SHOULD | [Подключайте общие компоненты только как версионированную библиотеку](01-conventions/project-structure.md#prj-05-подключайте-общие-компоненты-только-как-версионированную-библиотеку) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| CFG-01 | MUST | [Используйте ассеты мастера для хранения конфигурации](01-conventions/config-and-secrets.md#cfg-01-используйте-ассеты-мастера-для-хранения-конфигурации) | [Конфигурация и конфиденциальные данные](01-conventions/config-and-secrets.md) |
| CFG-02 | MUST | [Используйте зашифрованные ассеты для хранения конфиденциальных данных](01-conventions/config-and-secrets.md#cfg-02-используйте-зашифрованные-ассеты-для-хранения-конфиденциальных-данных) | [Конфигурация и конфиденциальные данные](01-conventions/config-and-secrets.md) |
| GIT-01 | SHOULD | [Используйте осмысленные названия коммитов](01-conventions/git.md#git-01-используйте-осмысленные-названия-коммитов) | [Соглашения о Git](01-conventions/git.md) |
| GIT-02 | SHOULD | [Следуйте стратегии ветвления](01-conventions/git.md#git-02-следуйте-стратегии-ветвления) | [Соглашения о Git](01-conventions/git.md) |
| GIT-03 | MUST | [Используйте Pull/Merge Request для изменений](01-conventions/git.md#git-03-используйте-pullmerge-request-для-изменений) | [Соглашения о Git](01-conventions/git.md) |
| GIT-04 | SHOULD | [Настройте .gitignore для PIX-проектов](01-conventions/git.md#git-04-настройте-gitignore-для-pix-проектов) | [Соглашения о Git](01-conventions/git.md) |
| GIT-05 | MUST | [Не коммитьте конфиденциальные данные](01-conventions/git.md#git-05-не-коммитьте-конфиденциальные-данные) | [Соглашения о Git](01-conventions/git.md) |
| GIT-06 | SHOULD | [Ведите CHANGELOG для релизов](01-conventions/git.md#git-06-ведите-changelog-для-релизов) | [Соглашения о Git](01-conventions/git.md) |
| GIT-07 | SHOULD | [Используйте тегирование для версий](01-conventions/git.md#git-07-используйте-тегирование-для-версий) | [Соглашения о Git](01-conventions/git.md) |
| GIT-08 | MAY | [Используйте вкладку "Проекты" в PIX Master для контроля версий](01-conventions/git.md#git-08-используйте-вкладку-проекты-в-pix-master-для-контроля-версий) | [Соглашения о Git](01-conventions/git.md) |
| NAM-01 | MUST | [Используйте PascalCasing для параметров скриптов](01-conventions/naming.md#nam-01-используйте-pascalcasing-для-параметров-скриптов) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-02 | MUST | [Используйте camelCasing для локальных переменных](01-conventions/naming.md#nam-02-используйте-camelcasing-для-локальных-переменных) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-03 | MUST | [Используйте осмысленные и информативные имена](01-conventions/naming.md#nam-03-используйте-осмысленные-и-информативные-имена) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-04 | MUST | [Соблюдайте конвенции нейминга языка и компании](01-conventions/naming.md#nam-04-соблюдайте-конвенции-нейминга-языка-и-компании) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-05 | SHOULD | [Используйте устоявшиеся термины для общих понятий](01-conventions/naming.md#nam-05-используйте-устоявшиеся-термины-для-общих-понятий) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-06 | MUST | [Не используйте кириллицу в именах](01-conventions/naming.md#nam-06-не-используйте-кириллицу-в-именах) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-07 | SHOULD | [Избегайте венгерской нотации](01-conventions/naming.md#nam-07-избегайте-венгерской-нотации) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-08 | SHOULD | [Избегайте избыточных названий](01-conventions/naming.md#nam-08-избегайте-избыточных-названий) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-09 | SHOULD | [Используйте контекстуально понятные имена](01-conventions/naming.md#nam-09-используйте-контекстуально-понятные-имена) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-10 | SHOULD | [Избегайте абстрактных названий](01-conventions/naming.md#nam-10-избегайте-абстрактных-названий) | [Соглашение об именовании](01-conventions/naming.md) |
| NAM-11 | SHOULD | [Избегайте отрицательных переменных](01-conventions/naming.md#nam-11-избегайте-отрицательных-переменных) | [Соглашение об именовании](01-conventions/naming.md) |
| DB-01 | SHOULD | [Используйте Bulk запросы](01-conventions/database.md#db-01-используйте-bulk-запросы) | [Соглашение о БД](01-conventions/database.md) |
| DB-02 | SHOULD | [Выполняйте фильтрацию в SQL-запросах, а не в коде](01-conventions/database.md#db-02-выполняйте-фильтрацию-в-sql-запросах-а-не-в-коде) | [Соглашение о БД](01-conventions/database.md) |
| DB-03 | SHOULD | [Избегайте создания хранимых процедур в БД](01-conventions/database.md#db-03-избегайте-создания-хранимых-процедур-в-бд) | [Соглашение о БД](01-conventions/database.md) |
| DB-04 | MUST | [Корректно работайте с NULL и пустыми строками](01-conventions/database.md#db-04-корректно-работайте-с-null-и-пустыми-строками) | [Соглашение о БД](01-conventions/database.md) |
| QUE-01 | SHOULD | [Выбирайте оптимальный формат данных для элементов очереди](01-conventions/queues.md#que-01-выбирайте-оптимальный-формат-данных-для-элементов-очереди) | [Соглашение об очередях](01-conventions/queues.md) |
| QUE-02 | MUST | [Обрабатывайте элемент очереди как транзакцию](01-conventions/queues.md#que-02-обрабатывайте-элемент-очереди-как-транзакцию) | [Соглашение об очередях](01-conventions/queues.md) |
| QUE-03 | MUST | [Используйте информативные сообщения в статусах очередей](01-conventions/queues.md#que-03-используйте-информативные-сообщения-в-статусах-очередей) | [Соглашение об очередях](01-conventions/queues.md) |
| QUE-04 | MUST | [Правильно обрабатывайте повторные попытки (retry)](01-conventions/queues.md#que-04-правильно-обрабатывайте-повторные-попытки-retry) | [Соглашение об очередях](01-conventions/queues.md) |
| LOG-01 | SHOULD | [Логируйте прогресс обработки](01-conventions/logging.md#log-01-логируйте-прогресс-обработки) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-02 | SHOULD | [Правильно логируйте исключения](01-conventions/logging.md#log-02-правильно-логируйте-исключения) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-03 | MUST | [Используйте подходящие уровни логирования](01-conventions/logging.md#log-03-используйте-подходящие-уровни-логирования) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-04 | SHOULD | [Избегайте избыточного логирования](01-conventions/logging.md#log-04-избегайте-избыточного-логирования) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-05 | MAY | [Логируйте метрики производительности](01-conventions/logging.md#log-05-логируйте-метрики-производительности) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-06 | MUST | [Не логируйте конфиденциальные данные](01-conventions/logging.md#log-06-не-логируйте-конфиденциальные-данные) | [Соглашение о логировании](01-conventions/logging.md) |
| EXC-01 | MUST | [Избегайте появления 'Exception has been thrown by the target of an invocation.'](01-conventions/exceptions.md#exc-01-избегайте-появления-exception-has-been-thrown-by-the-target-of-an-invocation) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-02 | SHOULD | [Не генерируйте исключения повторно](01-conventions/exceptions.md#exc-02-не-генерируйте-исключения-повторно) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-03 | MUST | [Не оставляйте Catch пустым и не используйте Try/Catch/Finally в бизнес-логике](01-conventions/exceptions.md#exc-03-не-оставляйте-catch-пустым-и-не-используйте-trycatchfinally-в-бизнес-логике) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-04 | MAY | [Используйте свойство Data для хранения дополнительной информации в исключениях](01-conventions/exceptions.md#exc-04-используйте-свойство-data-для-хранения-дополнительной-информации-в-исключениях) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-05 | SHOULD | [Обрабатывайте исключения на правильном уровне абстракции](01-conventions/exceptions.md#exc-05-обрабатывайте-исключения-на-правильном-уровне-абстракции) | [Соглашение об исключениях](01-conventions/exceptions.md) |

## Рекомендации по написанию скриптов

| ID | Уровень | Правило | Раздел |
|----|---------|---------|--------|
| CS-01 | SHOULD | [Соблюдайте соглашение о коде C#](02-guidelines/csharp-style.md#cs-01-соблюдайте-соглашение-о-коде-c) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-02 | SHOULD | [Соблюдайте ключевые принципы проектирования](02-guidelines/csharp-style.md#cs-02-соблюдайте-ключевые-принципы-проектирования) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-03 | SHOULD | [Используйте минимальное количество аргументов](02-guidelines/csharp-style.md#cs-03-используйте-минимальное-количество-аргументов) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-04 | SHOULD | [Избегайте булевых флагов в аргументах методов](02-guidelines/csharp-style.md#cs-04-избегайте-булевых-флагов-в-аргументах-методов) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| STR-01 | SHOULD | [Используйте подходящие строковые литералы](02-guidelines/strings.md#str-01-используйте-подходящие-строковые-литералы) | [Строковые литералы](02-guidelines/strings.md) |
| LNQ-01 | SHOULD | [Форматируйте LINQ-запросы](02-guidelines/linq.md#lnq-01-форматируйте-linq-запросы) | [LINQ](02-guidelines/linq.md) |
| LNQ-02 | SHOULD | [Используйте LINQ эффективно](02-guidelines/linq.md#lnq-02-используйте-linq-эффективно) | [LINQ](02-guidelines/linq.md) |
| CND-01 | SHOULD | [Используйте современные условные операторы C#](02-guidelines/conditions.md#cnd-01-используйте-современные-условные-операторы-c) | [Условия и условные операторы](02-guidelines/conditions.md) |
| CND-02 | SHOULD | [Избегайте глубоких вложений в скриптах](02-guidelines/conditions.md#cnd-02-избегайте-глубоких-вложений-в-скриптах) | [Условия и условные операторы](02-guidelines/conditions.md) |
| CND-03 | SHOULD | [Избегайте отрицательных условий](02-guidelines/conditions.md#cnd-03-избегайте-отрицательных-условий) | [Условия и условные операторы](02-guidelines/conditions.md) |
| CND-04 | SHOULD | [Избегайте громоздких if-else конструкций](02-guidelines/conditions.md#cnd-04-избегайте-громоздких-if-else-конструкций) | [Условия и условные операторы](02-guidelines/conditions.md) |
| FS-01 | SHOULD | [Используйте классы Path, Directory и File](02-guidelines/files.md#fs-01-используйте-классы-path-directory-и-file) | [Работа с файлами](02-guidelines/files.md) |
| FS-02 | MUST | [Не используйте жестко заданные пути и конкатенацию строк для путей](02-guidelines/files.md#fs-02-не-используйте-жестко-заданные-пути-и-конкатенацию-строк-для-путей) | [Работа с файлами](02-guidelines/files.md) |
| FS-03 | MUST | [Управляйте временными файлами](02-guidelines/files.md#fs-03-управляйте-временными-файлами) | [Работа с файлами](02-guidelines/files.md) |
| FS-04 | SHOULD | [Копируйте файлы перед обработкой](02-guidelines/files.md#fs-04-копируйте-файлы-перед-обработкой) | [Работа с файлами](02-guidelines/files.md) |
| HC-01 | MUST | [Не используйте жесткое кодирование](02-guidelines/hardcoding.md#hc-01-не-используйте-жесткое-кодирование) | [Жесткое кодирование](02-guidelines/hardcoding.md) |
| ACT-01 | SHOULD | [Не размещайте большой код в активности «Выполнить»](02-guidelines/pix-activities.md#act-01-не-размещайте-большой-код-в-активности-выполнить) | [Активности PIX RPA](02-guidelines/pix-activities.md) |
| ACT-02 | SHOULD | [Используйте активность «Комментарий» только для неочевидного](02-guidelines/pix-activities.md#act-02-используйте-активность-комментарий-только-для-неочевидного) | [Активности PIX RPA](02-guidelines/pix-activities.md) |
| ACT-03 | MAY | [Заменяйте часто вызываемые скрипты контейнерами (временное решение)](02-guidelines/pix-activities.md#act-03-заменяйте-часто-вызываемые-скрипты-контейнерами-временное-решение) | [Активности PIX RPA](02-guidelines/pix-activities.md) |
| UI-01 | SHOULD | [Используйте надежные селекторы и явные ожидания](02-guidelines/ui-automation.md#ui-01-используйте-надежные-селекторы-и-явные-ожидания) | [Работа с UI](02-guidelines/ui-automation.md) |
| LOOP-01 | SHOULD | [Избегайте использования goto](02-guidelines/loops-and-goto.md#loop-01-избегайте-использования-goto) | [Циклы и goto](02-guidelines/loops-and-goto.md) |
| LOOP-02 | MUST | [Ограничивайте каждый цикл таймаутом или числом итераций](02-guidelines/loops-and-goto.md#loop-02-ограничивайте-каждый-цикл-таймаутом-или-числом-итераций) | [Циклы и goto](02-guidelines/loops-and-goto.md) |
