# Реестр правил

Сводный список всех правил с идентификаторами и уровнями обязательности. Уровни описаны в [README](../README.md#уровни-обязательности).

Ссылайтесь на правило по идентификатору, например в комментарии к Pull Request: «нарушено EXC-03».

> Файл генерируется командой `python tools/build_docs.py`. Не редактируйте его вручную.

## Соглашения

| ID | Уровень | Правило | Раздел |
|----|---------|---------|--------|
| CFG-01 | MUST | [Используйте ассеты мастера для хранения конфигурации](01-conventions/config-and-secrets.md#cfg-01-используйте-ассеты-мастера-для-хранения-конфигурации) | [Конфигурация и конфиденциальные данные](01-conventions/config-and-secrets.md) |
| CFG-02 | MUST | [Используйте зашифрованные ассеты для хранения конфиденциальных данных](01-conventions/config-and-secrets.md#cfg-02-используйте-зашифрованные-ассеты-для-хранения-конфиденциальных-данных) | [Конфигурация и конфиденциальные данные](01-conventions/config-and-secrets.md) |
| CFG-03 | MUST | [Используйте входные параметры робота только для значений запуска](01-conventions/config-and-secrets.md#cfg-03-используйте-входные-параметры-робота-только-для-значений-запуска) | [Конфигурация и конфиденциальные данные](01-conventions/config-and-secrets.md) |
| DB-01 | SHOULD | [Используйте Bulk запросы](01-conventions/database.md#db-01-используйте-bulk-запросы) | [Соглашение о БД](01-conventions/database.md) |
| DB-02 | SHOULD | [Выполняйте фильтрацию в SQL-запросах, а не в коде](01-conventions/database.md#db-02-выполняйте-фильтрацию-в-sql-запросах-а-не-в-коде) | [Соглашение о БД](01-conventions/database.md) |
| DB-03 | SHOULD | [Избегайте создания хранимых процедур в БД](01-conventions/database.md#db-03-избегайте-создания-хранимых-процедур-в-бд) | [Соглашение о БД](01-conventions/database.md) |
| DB-04 | MUST | [Корректно работайте с NULL и пустыми строками](01-conventions/database.md#db-04-корректно-работайте-с-null-и-пустыми-строками) | [Соглашение о БД](01-conventions/database.md) |
| DB-05 | MUST | [Передавайте значения в запросы только через параметры](01-conventions/database.md#db-05-передавайте-значения-в-запросы-только-через-параметры) | [Соглашение о БД](01-conventions/database.md) |
| EXC-01 | MUST | [Избегайте появления 'Exception has been thrown by the target of an invocation.'](01-conventions/exceptions.md#exc-01-избегайте-появления-exception-has-been-thrown-by-the-target-of-an-invocation) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-02 | SHOULD | [Не генерируйте исключения повторно](01-conventions/exceptions.md#exc-02-не-генерируйте-исключения-повторно) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-03 | MUST | [Не оставляйте Catch пустым и не используйте Try/Catch/Finally в бизнес-логике](01-conventions/exceptions.md#exc-03-не-оставляйте-catch-пустым-и-не-используйте-trycatchfinally-в-бизнес-логике) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-04 | MAY | [Используйте свойство Data для хранения дополнительной информации в исключениях](01-conventions/exceptions.md#exc-04-используйте-свойство-data-для-хранения-дополнительной-информации-в-исключениях) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-05 | SHOULD | [Обрабатывайте исключения на правильном уровне абстракции](01-conventions/exceptions.md#exc-05-обрабатывайте-исключения-на-правильном-уровне-абстракции) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-06 | MUST | [Разделяйте бизнес-исключения и системные исключения](01-conventions/exceptions.md#exc-06-разделяйте-бизнес-исключения-и-системные-исключения) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| EXC-07 | MUST | [Указывайте источник исключения](01-conventions/exceptions.md#exc-07-указывайте-источник-исключения) | [Соглашение об исключениях](01-conventions/exceptions.md) |
| GIT-01 | SHOULD | [Используйте осмысленные названия коммитов](01-conventions/git.md#git-01-используйте-осмысленные-названия-коммитов) | [Соглашения о Git](01-conventions/git.md) |
| GIT-02 | SHOULD | [Следуйте стратегии ветвления](01-conventions/git.md#git-02-следуйте-стратегии-ветвления) | [Соглашения о Git](01-conventions/git.md) |
| GIT-03 | MUST | [Используйте Pull/Merge Request для изменений](01-conventions/git.md#git-03-используйте-pullmerge-request-для-изменений) | [Соглашения о Git](01-conventions/git.md) |
| GIT-04 | SHOULD | [Настройте .gitignore для PIX-проектов](01-conventions/git.md#git-04-настройте-gitignore-для-pix-проектов) | [Соглашения о Git](01-conventions/git.md) |
| GIT-05 | MUST | [Не коммитьте конфиденциальные данные](01-conventions/git.md#git-05-не-коммитьте-конфиденциальные-данные) | [Соглашения о Git](01-conventions/git.md) |
| GIT-06 | SHOULD | [Ведите CHANGELOG для релизов](01-conventions/git.md#git-06-ведите-changelog-для-релизов) | [Соглашения о Git](01-conventions/git.md) |
| GIT-07 | SHOULD | [Используйте тегирование для версий](01-conventions/git.md#git-07-используйте-тегирование-для-версий) | [Соглашения о Git](01-conventions/git.md) |
| GIT-08 | MAY | [Используйте вкладку "Проекты" в PIX Master для контроля версий](01-conventions/git.md#git-08-используйте-вкладку-проекты-в-pix-master-для-контроля-версий) | [Соглашения о Git](01-conventions/git.md) |
| LOG-01 | SHOULD | [Логируйте прогресс обработки](01-conventions/logging.md#log-01-логируйте-прогресс-обработки) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-02 | SHOULD | [Правильно логируйте исключения](01-conventions/logging.md#log-02-правильно-логируйте-исключения) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-03 | MUST | [Используйте подходящие уровни логирования](01-conventions/logging.md#log-03-используйте-подходящие-уровни-логирования) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-04 | SHOULD | [Избегайте избыточного логирования](01-conventions/logging.md#log-04-избегайте-избыточного-логирования) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-05 | MAY | [Логируйте метрики производительности](01-conventions/logging.md#log-05-логируйте-метрики-производительности) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-06 | MUST | [Не логируйте конфиденциальные данные](01-conventions/logging.md#log-06-не-логируйте-конфиденциальные-данные) | [Соглашение о логировании](01-conventions/logging.md) |
| LOG-07 | MUST | [Указывайте идентификатор транзакции в каждой записи лога](01-conventions/logging.md#log-07-указывайте-идентификатор-транзакции-в-каждой-записи-лога) | [Соглашение о логировании](01-conventions/logging.md) |
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
| PD-01 | MUST | [Обрабатывайте только необходимые персональные данные](01-conventions/personal-data.md#pd-01-обрабатывайте-только-необходимые-персональные-данные) | [Персональные данные](01-conventions/personal-data.md) |
| PD-02 | MUST | [Не допускайте персональные данные в логи, статусы и имена файлов](01-conventions/personal-data.md#pd-02-не-допускайте-персональные-данные-в-логи-статусы-и-имена-файлов) | [Персональные данные](01-conventions/personal-data.md) |
| PD-03 | MUST | [Ограничивайте доступ к скриншотам и артефактам с персональными данными](01-conventions/personal-data.md#pd-03-ограничивайте-доступ-к-скриншотам-и-артефактам-с-персональными-данными) | [Персональные данные](01-conventions/personal-data.md) |
| PD-04 | MUST | [Используйте обезличенные данные для разработки и тестирования](01-conventions/personal-data.md#pd-04-используйте-обезличенные-данные-для-разработки-и-тестирования) | [Персональные данные](01-conventions/personal-data.md) |
| PD-05 | MUST | [Не передавайте персональные данные во внешние сервисы без согласования](01-conventions/personal-data.md#pd-05-не-передавайте-персональные-данные-во-внешние-сервисы-без-согласования) | [Персональные данные](01-conventions/personal-data.md) |
| PRJ-01 | MUST | [Разделяйте проект на слои](01-conventions/project-structure.md#prj-01-разделяйте-проект-на-слои) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-02 | MUST | [Используйте шаблон на основе State Machine](01-conventions/project-structure.md#prj-02-используйте-шаблон-на-основе-state-machine) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-03 | MUST | [Используйте состояния по назначению](01-conventions/project-structure.md#prj-03-используйте-состояния-по-назначению) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-04 | MUST | [Храните шаблоны и прочие файлы в самом проекте робота](01-conventions/project-structure.md#prj-04-храните-шаблоны-и-прочие-файлы-в-самом-проекте-робота) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-05 | SHOULD | [Подключайте общие компоненты только как версионированную библиотеку](01-conventions/project-structure.md#prj-05-подключайте-общие-компоненты-только-как-версионированную-библиотеку) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-06 | SHOULD | [Разделяйте загрузку и обработку транзакций (Dispatcher / Performer)](01-conventions/project-structure.md#prj-06-разделяйте-загрузку-и-обработку-транзакций-dispatcher--performer) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| PRJ-07 | SHOULD | [Организуйте бизнес-логику транзакции по паттерну Transaction Script](01-conventions/project-structure.md#prj-07-организуйте-бизнес-логику-транзакции-по-паттерну-transaction-script) | [Соглашение о структуре проекта](01-conventions/project-structure.md) |
| QUE-01 | SHOULD | [Выбирайте оптимальный формат данных для элементов очереди](01-conventions/queues.md#que-01-выбирайте-оптимальный-формат-данных-для-элементов-очереди) | [Соглашение об очередях](01-conventions/queues.md) |
| QUE-02 | MUST | [Обрабатывайте элемент очереди как транзакцию](01-conventions/queues.md#que-02-обрабатывайте-элемент-очереди-как-транзакцию) | [Соглашение об очередях](01-conventions/queues.md) |
| QUE-03 | MUST | [Используйте информативные сообщения в статусах очередей](01-conventions/queues.md#que-03-используйте-информативные-сообщения-в-статусах-очередей) | [Соглашение об очередях](01-conventions/queues.md) |
| QUE-04 | MUST | [Правильно обрабатывайте повторные попытки (retry)](01-conventions/queues.md#que-04-правильно-обрабатывайте-повторные-попытки-retry) | [Соглашение об очередях](01-conventions/queues.md) |
| REL-01 | MUST | [Делайте обработку транзакции идемпотентной](01-conventions/reliability.md#rel-01-делайте-обработку-транзакции-идемпотентной) | [Надежность и восстановление после сбоев](01-conventions/reliability.md) |
| REL-02 | SHOULD | [Сохраняйте прогресс многошаговых транзакций](01-conventions/reliability.md#rel-02-сохраняйте-прогресс-многошаговых-транзакций) | [Надежность и восстановление после сбоев](01-conventions/reliability.md) |
| REL-03 | SHOULD | [Восстанавливайте приложения после системного исключения](01-conventions/reliability.md#rel-03-восстанавливайте-приложения-после-системного-исключения) | [Надежность и восстановление после сбоев](01-conventions/reliability.md) |
| REL-04 | SHOULD | [Сохраняйте диагностику при системном исключении](01-conventions/reliability.md#rel-04-сохраняйте-диагностику-при-системном-исключении) | [Надежность и восстановление после сбоев](01-conventions/reliability.md) |
| REL-05 | MUST | [Останавливайте робота после серии системных исключений подряд](01-conventions/reliability.md#rel-05-останавливайте-робота-после-серии-системных-исключений-подряд) | [Надежность и восстановление после сбоев](01-conventions/reliability.md) |
| REL-06 | MUST | [Проверяйте сигнал остановки от мастера](01-conventions/reliability.md#rel-06-проверяйте-сигнал-остановки-от-мастера) | [Надежность и восстановление после сбоев](01-conventions/reliability.md) |

## Рекомендации по написанию скриптов

| ID | Уровень | Правило | Раздел |
|----|---------|---------|--------|
| AI-01 | MUST | [Не передавайте конфиденциальные данные во внешние модели без согласования](02-guidelines/ai-and-idp.md#ai-01-не-передавайте-конфиденциальные-данные-во-внешние-модели-без-согласования) | [ИИ и интеллектуальная обработка документов](02-guidelines/ai-and-idp.md) |
| AI-02 | MUST | [Проверяйте результат модели перед использованием](02-guidelines/ai-and-idp.md#ai-02-проверяйте-результат-модели-перед-использованием) | [ИИ и интеллектуальная обработка документов](02-guidelines/ai-and-idp.md) |
| AI-03 | MUST | [Направляйте неуверенные результаты на проверку человеку](02-guidelines/ai-and-idp.md#ai-03-направляйте-неуверенные-результаты-на-проверку-человеку) | [ИИ и интеллектуальная обработка документов](02-guidelines/ai-and-idp.md) |
| AI-04 | MUST | [Не позволяйте модели самостоятельно выполнять необратимые действия](02-guidelines/ai-and-idp.md#ai-04-не-позволяйте-модели-самостоятельно-выполнять-необратимые-действия) | [ИИ и интеллектуальная обработка документов](02-guidelines/ai-and-idp.md) |
| AI-05 | SHOULD | [Храните промпты и настройки модели в репозитории робота](02-guidelines/ai-and-idp.md#ai-05-храните-промпты-и-настройки-модели-в-репозитории-робота) | [ИИ и интеллектуальная обработка документов](02-guidelines/ai-and-idp.md) |
| AI-06 | SHOULD | [Логируйте вызовы модели без содержимого](02-guidelines/ai-and-idp.md#ai-06-логируйте-вызовы-модели-без-содержимого) | [ИИ и интеллектуальная обработка документов](02-guidelines/ai-and-idp.md) |
| CND-01 | SHOULD | [Используйте современные условные операторы C#](02-guidelines/conditions.md#cnd-01-используйте-современные-условные-операторы-c) | [Условия и условные операторы](02-guidelines/conditions.md) |
| CND-02 | SHOULD | [Избегайте глубоких вложений в скриптах](02-guidelines/conditions.md#cnd-02-избегайте-глубоких-вложений-в-скриптах) | [Условия и условные операторы](02-guidelines/conditions.md) |
| CND-03 | SHOULD | [Избегайте отрицательных условий](02-guidelines/conditions.md#cnd-03-избегайте-отрицательных-условий) | [Условия и условные операторы](02-guidelines/conditions.md) |
| CND-04 | SHOULD | [Избегайте громоздких if-else конструкций](02-guidelines/conditions.md#cnd-04-избегайте-громоздких-if-else-конструкций) | [Условия и условные операторы](02-guidelines/conditions.md) |
| CS-01 | SHOULD | [Соблюдайте соглашение о коде C#](02-guidelines/csharp-style.md#cs-01-соблюдайте-соглашение-о-коде-c) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-02 | SHOULD | [Не повторяйтесь (DRY)](02-guidelines/csharp-style.md#cs-02-не-повторяйтесь-dry) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-03 | SHOULD | [Оставляйте скрипту одну ответственность (SRP)](02-guidelines/csharp-style.md#cs-03-оставляйте-скрипту-одну-ответственность-srp) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-04 | SHOULD | [Делайте проще (KISS)](02-guidelines/csharp-style.md#cs-04-делайте-проще-kiss) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-05 | SHOULD | [Не добавляйте функциональность впрок (YAGNI)](02-guidelines/csharp-style.md#cs-05-не-добавляйте-функциональность-впрок-yagni) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-06 | SHOULD | [Программируйте защитно](02-guidelines/csharp-style.md#cs-06-программируйте-защитно) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-07 | SHOULD | [Используйте минимальное количество аргументов](02-guidelines/csharp-style.md#cs-07-используйте-минимальное-количество-аргументов) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-08 | SHOULD | [Избегайте булевых флагов в аргументах методов](02-guidelines/csharp-style.md#cs-08-избегайте-булевых-флагов-в-аргументах-методов) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| CS-09 | SHOULD | [Записывайте инициализацию коллекций в столбик](02-guidelines/csharp-style.md#cs-09-записывайте-инициализацию-коллекций-в-столбик) | [Стиль кода и принципы проектирования](02-guidelines/csharp-style.md) |
| MAIL-01 | MUST | [Работайте с почтой по протоколам, а не через Outlook](02-guidelines/email.md#mail-01-работайте-с-почтой-по-протоколам-а-не-через-outlook) | [Работа с почтой](02-guidelines/email.md) |
| MAIL-02 | MUST | [Используйте отдельный почтовый ящик робота](02-guidelines/email.md#mail-02-используйте-отдельный-почтовый-ящик-робота) | [Работа с почтой](02-guidelines/email.md) |
| MAIL-03 | MUST | [Отмечайте обработанные письма явно](02-guidelines/email.md#mail-03-отмечайте-обработанные-письма-явно) | [Работа с почтой](02-guidelines/email.md) |
| MAIL-04 | SHOULD | [Проверяйте входящие письма и вложения](02-guidelines/email.md#mail-04-проверяйте-входящие-письма-и-вложения) | [Работа с почтой](02-guidelines/email.md) |
| XLS-01 | MUST | [Не используйте Excel Interop и COM](02-guidelines/excel.md#xls-01-не-используйте-excel-interop-и-com) | [Работа с Excel](02-guidelines/excel.md) |
| XLS-02 | MAY | [Используйте приложение Excel только там, где без него нельзя](02-guidelines/excel.md#xls-02-используйте-приложение-excel-только-там-где-без-него-нельзя) | [Работа с Excel](02-guidelines/excel.md) |
| XLS-03 | SHOULD | [Читайте лист целиком, а не по ячейкам](02-guidelines/excel.md#xls-03-читайте-лист-целиком-а-не-по-ячейкам) | [Работа с Excel](02-guidelines/excel.md) |
| XLS-04 | SHOULD | [Обращайтесь к столбцам по заголовкам](02-guidelines/excel.md#xls-04-обращайтесь-к-столбцам-по-заголовкам) | [Работа с Excel](02-guidelines/excel.md) |
| FS-01 | SHOULD | [Используйте классы Path, Directory и File](02-guidelines/files.md#fs-01-используйте-классы-path-directory-и-file) | [Работа с файлами](02-guidelines/files.md) |
| FS-05 | SHOULD | [Выбирайте между File/Directory и FileInfo/DirectoryInfo по количеству операций](02-guidelines/files.md#fs-05-выбирайте-между-filedirectory-и-fileinfodirectoryinfo-по-количеству-операций) | [Работа с файлами](02-guidelines/files.md) |
| FS-02 | MUST | [Не используйте жестко заданные пути и конкатенацию строк для путей](02-guidelines/files.md#fs-02-не-используйте-жестко-заданные-пути-и-конкатенацию-строк-для-путей) | [Работа с файлами](02-guidelines/files.md) |
| FS-03 | MUST | [Управляйте временными файлами](02-guidelines/files.md#fs-03-управляйте-временными-файлами) | [Работа с файлами](02-guidelines/files.md) |
| FS-04 | SHOULD | [Копируйте файлы перед обработкой](02-guidelines/files.md#fs-04-копируйте-файлы-перед-обработкой) | [Работа с файлами](02-guidelines/files.md) |
| HC-01 | MUST | [Не используйте жесткое кодирование](02-guidelines/hardcoding.md#hc-01-не-используйте-жесткое-кодирование) | [Жесткое кодирование](02-guidelines/hardcoding.md) |
| INT-01 | SHOULD | [Выбирайте канал интеграции по надежности: API → БД → файлы → UI](02-guidelines/integrations.md#int-01-выбирайте-канал-интеграции-по-надежности-api--бд--файлы--ui) | [Интеграции с внешними системами](02-guidelines/integrations.md) |
| INT-02 | MUST | [Задавайте таймауты для всех внешних вызовов](02-guidelines/integrations.md#int-02-задавайте-таймауты-для-всех-внешних-вызовов) | [Интеграции с внешними системами](02-guidelines/integrations.md) |
| INT-03 | MUST | [Используйте отдельные учетные записи робота для каждой системы](02-guidelines/integrations.md#int-03-используйте-отдельные-учетные-записи-робота-для-каждой-системы) | [Интеграции с внешними системами](02-guidelines/integrations.md) |
| INT-04 | SHOULD | [Выполняйте HTTP-запросы через HttpClient](02-guidelines/integrations.md#int-04-выполняйте-http-запросы-через-httpclient) | [Интеграции с внешними системами](02-guidelines/integrations.md) |
| LNQ-01 | SHOULD | [Форматируйте LINQ-запросы](02-guidelines/linq.md#lnq-01-форматируйте-linq-запросы) | [LINQ](02-guidelines/linq.md) |
| LNQ-02 | SHOULD | [Фильтруйте и проецируйте данные как можно раньше](02-guidelines/linq.md#lnq-02-фильтруйте-и-проецируйте-данные-как-можно-раньше) | [LINQ](02-guidelines/linq.md) |
| LNQ-03 | SHOULD | [Используйте оптимальные методы LINQ](02-guidelines/linq.md#lnq-03-используйте-оптимальные-методы-linq) | [LINQ](02-guidelines/linq.md) |
| LNQ-04 | SHOULD | [Материализуйте результат, если он нужен несколько раз](02-guidelines/linq.md#lnq-04-материализуйте-результат-если-он-нужен-несколько-раз) | [LINQ](02-guidelines/linq.md) |
| LNQ-05 | MAY | [Применяйте PLINQ только для тяжелых вычислений в памяти](02-guidelines/linq.md#lnq-05-применяйте-plinq-только-для-тяжелых-вычислений-в-памяти) | [LINQ](02-guidelines/linq.md) |
| LNQ-06 | SHOULD | [Используйте цикл вместо LINQ, где он понятнее](02-guidelines/linq.md#lnq-06-используйте-цикл-вместо-linq-где-он-понятнее) | [LINQ](02-guidelines/linq.md) |
| LOOP-01 | SHOULD | [Избегайте использования goto](02-guidelines/loops-and-goto.md#loop-01-избегайте-использования-goto) | [Циклы и goto](02-guidelines/loops-and-goto.md) |
| LOOP-02 | MUST | [Ограничивайте каждый цикл таймаутом или числом итераций](02-guidelines/loops-and-goto.md#loop-02-ограничивайте-каждый-цикл-таймаутом-или-числом-итераций) | [Циклы и goto](02-guidelines/loops-and-goto.md) |
| LOOP-03 | SHOULD | [Используйте активность «Цикл с … по» для ожидания UI с ограниченным числом попыток](02-guidelines/loops-and-goto.md#loop-03-используйте-активность-цикл-с--по-для-ожидания-ui-с-ограниченным-числом-попыток) | [Циклы и goto](02-guidelines/loops-and-goto.md) |
| LOOP-04 | SHOULD | [Используйте «Цикл для каждого» для перебора коллекций](02-guidelines/loops-and-goto.md#loop-04-используйте-цикл-для-каждого-для-перебора-коллекций) | [Циклы и goto](02-guidelines/loops-and-goto.md) |
| ACT-01 | SHOULD | [Не размещайте большой код в активности «Выполнить»](02-guidelines/pix-activities.md#act-01-не-размещайте-большой-код-в-активности-выполнить) | [Активности PIX RPA](02-guidelines/pix-activities.md) |
| ACT-02 | SHOULD | [Используйте активность «Комментарий» только для неочевидного](02-guidelines/pix-activities.md#act-02-используйте-активность-комментарий-только-для-неочевидного) | [Активности PIX RPA](02-guidelines/pix-activities.md) |
| ACT-03 | MAY | [Заменяйте часто вызываемые скрипты контейнерами (временное решение)](02-guidelines/pix-activities.md#act-03-заменяйте-часто-вызываемые-скрипты-контейнерами-временное-решение) | [Активности PIX RPA](02-guidelines/pix-activities.md) |
| STR-01 | SHOULD | [Используйте интерполяцию строк вместо конкатенации](02-guidelines/strings.md#str-01-используйте-интерполяцию-строк-вместо-конкатенации) | [Строковые литералы](02-guidelines/strings.md) |
| STR-02 | SHOULD | [Используйте string.Format для шаблонов из конфигурации](02-guidelines/strings.md#str-02-используйте-stringformat-для-шаблонов-из-конфигурации) | [Строковые литералы](02-guidelines/strings.md) |
| STR-03 | SHOULD | [Используйте дословные строки для путей и многострочного текста](02-guidelines/strings.md#str-03-используйте-дословные-строки-для-путей-и-многострочного-текста) | [Строковые литералы](02-guidelines/strings.md) |
| STR-04 | MAY | [Используйте необработанные строковые литералы для JSON и XML](02-guidelines/strings.md#str-04-используйте-необработанные-строковые-литералы-для-json-и-xml) | [Строковые литералы](02-guidelines/strings.md) |
| STR-05 | SHOULD | [Используйте StringBuilder для сборки строки в цикле](02-guidelines/strings.md#str-05-используйте-stringbuilder-для-сборки-строки-в-цикле) | [Строковые литералы](02-guidelines/strings.md) |
| UI-01 | SHOULD | [Не используйте абсолютные XPath-пути](02-guidelines/ui-automation.md#ui-01-не-используйте-абсолютные-xpath-пути) | [Работа с UI](02-guidelines/ui-automation.md) |
| UI-02 | SHOULD | [Ищите элементы Desktop UI по уникальным свойствам](02-guidelines/ui-automation.md#ui-02-ищите-элементы-desktop-ui-по-уникальным-свойствам) | [Работа с UI](02-guidelines/ui-automation.md) |
| UI-03 | MUST | [Используйте ожидания вместо фиксированных пауз](02-guidelines/ui-automation.md#ui-03-используйте-ожидания-вместо-фиксированных-пауз) | [Работа с UI](02-guidelines/ui-automation.md) |
| UI-04 | SHOULD | [Создавайте абстракции для часто используемых элементов](02-guidelines/ui-automation.md#ui-04-создавайте-абстракции-для-часто-используемых-элементов) | [Работа с UI](02-guidelines/ui-automation.md) |
| UI-05 | SHOULD | [Проверяйте доступность элемента перед действием](02-guidelines/ui-automation.md#ui-05-проверяйте-доступность-элемента-перед-действием) | [Работа с UI](02-guidelines/ui-automation.md) |

## Жизненный цикл робота

| ID | Уровень | Правило | Раздел |
|----|---------|---------|--------|
| ASM-01 | MUST | [Оценивайте пригодность процесса до начала разработки](03-robot-lifecycle/assessment.md#asm-01-оценивайте-пригодность-процесса-до-начала-разработки) | [Оценка процесса](03-robot-lifecycle/assessment.md) |
| ASM-02 | SHOULD | [Оценивайте эффект автоматизации](03-robot-lifecycle/assessment.md#asm-02-оценивайте-эффект-автоматизации) | [Оценка процесса](03-robot-lifecycle/assessment.md) |
| REV-01 | MUST | [Проверяйте изменения по чек-листу](03-robot-lifecycle/code-review.md#rev-01-проверяйте-изменения-по-чек-листу) | [Код-ревью](03-robot-lifecycle/code-review.md) |
| REV-02 | SHOULD | [Ссылайтесь на правила по идентификатору](03-robot-lifecycle/code-review.md#rev-02-ссылайтесь-на-правила-по-идентификатору) | [Код-ревью](03-robot-lifecycle/code-review.md) |
| REV-03 | SHOULD | [Разделяйте блокирующие и неблокирующие замечания](03-robot-lifecycle/code-review.md#rev-03-разделяйте-блокирующие-и-неблокирующие-замечания) | [Код-ревью](03-robot-lifecycle/code-review.md) |
| DSN-01 | MUST | [Описывайте процесс в PDD до начала разработки](03-robot-lifecycle/design.md#dsn-01-описывайте-процесс-в-pdd-до-начала-разработки) | [Проектирование](03-robot-lifecycle/design.md) |
| DSN-02 | MUST | [Описывайте техническое решение в SDD](03-robot-lifecycle/design.md#dsn-02-описывайте-техническое-решение-в-sdd) | [Проектирование](03-robot-lifecycle/design.md) |
| DSN-03 | SHOULD | [Проверяйте готовность задачи к разработке](03-robot-lifecycle/design.md#dsn-03-проверяйте-готовность-задачи-к-разработке) | [Проектирование](03-robot-lifecycle/design.md) |
| DPL-01 | MUST | [Версионируйте роботов по SemVer](03-robot-lifecycle/release-and-deploy.md#dpl-01-версионируйте-роботов-по-semver) | [Релиз и развертывание](03-robot-lifecycle/release-and-deploy.md) |
| DPL-02 | MUST | [Продвигайте одну и ту же сборку по контурам DEV → UAT → PROD](03-robot-lifecycle/release-and-deploy.md#dpl-02-продвигайте-одну-и-ту-же-сборку-по-контурам-dev--uat--prod) | [Релиз и развертывание](03-robot-lifecycle/release-and-deploy.md) |
| DPL-03 | SHOULD | [Готовьте релиз по чек-листу](03-robot-lifecycle/release-and-deploy.md#dpl-03-готовьте-релиз-по-чек-листу) | [Релиз и развертывание](03-robot-lifecycle/release-and-deploy.md) |
| DPL-04 | MUST | [Имейте план отката для каждого релиза](03-robot-lifecycle/release-and-deploy.md#dpl-04-имейте-план-отката-для-каждого-релиза) | [Релиз и развертывание](03-robot-lifecycle/release-and-deploy.md) |
| SUP-01 | SHOULD | [Проводите период hypercare после запуска](03-robot-lifecycle/support.md#sup-01-проводите-период-hypercare-после-запуска) | [Сопровождение](03-robot-lifecycle/support.md) |
| SUP-02 | MUST | [Готовьте runbook для поддержки](03-robot-lifecycle/support.md#sup-02-готовьте-runbook-для-поддержки) | [Сопровождение](03-robot-lifecycle/support.md) |
| SUP-03 | SHOULD | [Разделяйте уровни поддержки](03-robot-lifecycle/support.md#sup-03-разделяйте-уровни-поддержки) | [Сопровождение](03-robot-lifecycle/support.md) |
| SUP-04 | SHOULD | [Отслеживайте показатели работы роботов](03-robot-lifecycle/support.md#sup-04-отслеживайте-показатели-работы-роботов) | [Сопровождение](03-robot-lifecycle/support.md) |
| SUP-05 | SHOULD | [Выводите роботов из эксплуатации по плану](03-robot-lifecycle/support.md#sup-05-выводите-роботов-из-эксплуатации-по-плану) | [Сопровождение](03-robot-lifecycle/support.md) |
| TST-01 | SHOULD | [Покрывайте тестами скрипты с бизнес-логикой и преобразованием данных](03-robot-lifecycle/testing.md#tst-01-покрывайте-тестами-скрипты-с-бизнес-логикой-и-преобразованием-данных) | [Тестирование](03-robot-lifecycle/testing.md) |
| TST-02 | MUST | [Тестируйте все бизнес-исключения из PDD](03-robot-lifecycle/testing.md#tst-02-тестируйте-все-бизнес-исключения-из-pdd) | [Тестирование](03-robot-lifecycle/testing.md) |
| TST-03 | MUST | [Проверяйте поведение робота при сбоях окружения](03-robot-lifecycle/testing.md#tst-03-проверяйте-поведение-робота-при-сбоях-окружения) | [Тестирование](03-robot-lifecycle/testing.md) |
| TST-04 | MUST | [Используйте подготовленные и обезличенные тестовые данные](03-robot-lifecycle/testing.md#tst-04-используйте-подготовленные-и-обезличенные-тестовые-данные) | [Тестирование](03-robot-lifecycle/testing.md) |
| TST-05 | MUST | [Фиксируйте приемку результатом UAT](03-robot-lifecycle/testing.md#tst-05-фиксируйте-приемку-результатом-uat) | [Тестирование](03-robot-lifecycle/testing.md) |
| TST-06 | SHOULD | [Проводите регрессионное тестирование при изменениях в целевых системах](03-robot-lifecycle/testing.md#tst-06-проводите-регрессионное-тестирование-при-изменениях-в-целевых-системах) | [Тестирование](03-robot-lifecycle/testing.md) |
| TST-07 | SHOULD | [Именуйте и структурируйте тесты единообразно](03-robot-lifecycle/testing.md#tst-07-именуйте-и-структурируйте-тесты-единообразно) | [Тестирование](03-robot-lifecycle/testing.md) |

## PIX Master

| ID | Уровень | Правило | Раздел |
|----|---------|---------|--------|
| AGT-01 | MUST | [Именуйте агентов по типу робота](04-master/agents.md#agt-01-именуйте-агентов-по-типу-робота) | [Агенты роботов](04-master/agents.md) |
| AGT-02 | SHOULD | [Учитывайте различия в настройке Unattended и Attended роботов](04-master/agents.md#agt-02-учитывайте-различия-в-настройке-unattended-и-attended-роботов) | [Агенты роботов](04-master/agents.md) |
| AGT-03 | SHOULD | [Группируйте роботов по проектам](04-master/agents.md#agt-03-группируйте-роботов-по-проектам) | [Агенты роботов](04-master/agents.md) |
| AGT-04 | MUST | [Выдавайте роботам отдельные технические учетные записи](04-master/agents.md#agt-04-выдавайте-роботам-отдельные-технические-учетные-записи) | [Агенты роботов](04-master/agents.md) |
| AGT-05 | MUST | [Публикуйте версии роботов с номером SemVer](04-master/agents.md#agt-05-публикуйте-версии-роботов-с-номером-semver) | [Агенты роботов](04-master/agents.md) |
| AGT-06 | SHOULD | [Настраивайте лимиты параллельного выполнения](04-master/agents.md#agt-06-настраивайте-лимиты-параллельного-выполнения) | [Агенты роботов](04-master/agents.md) |
| AST-01 | MUST | [Именуйте ассеты по типу](04-master/assets.md#ast-01-именуйте-ассеты-по-типу) | [Ассеты](04-master/assets.md) |
| AST-02 | SHOULD | [Организуйте ассеты по проектам](04-master/assets.md#ast-02-организуйте-ассеты-по-проектам) | [Ассеты](04-master/assets.md) |
| AST-03 | MUST | [Ограничивайте доступ к учетным данным](04-master/assets.md#ast-03-ограничивайте-доступ-к-учетным-данным) | [Ассеты](04-master/assets.md) |
| AST-04 | SHOULD | [Ведите каталог ассетов](04-master/assets.md#ast-04-ведите-каталог-ассетов) | [Ассеты](04-master/assets.md) |
| HST-01 | MUST | [Именуйте хосты по формату {Контур}-{Расположение}-{Назначение}-{Номер}](04-master/hosts.md#hst-01-именуйте-хосты-по-формату-контур-расположение-назначение-номер) | [Хосты](04-master/hosts.md) |
| HST-02 | SHOULD | [Группируйте хосты по назначению](04-master/hosts.md#hst-02-группируйте-хосты-по-назначению) | [Хосты](04-master/hosts.md) |
| HST-03 | MUST | [Стандартизируйте конфигурацию хостов](04-master/hosts.md#hst-03-стандартизируйте-конфигурацию-хостов) | [Хосты](04-master/hosts.md) |
| MON-01 | MUST | [Настройте оповещения о событиях, требующих реакции](04-master/monitoring.md#mon-01-настройте-оповещения-о-событиях-требующих-реакции) | [Мониторинг и оповещения](04-master/monitoring.md) |
| MON-02 | SHOULD | [Отслеживайте загрузку и состояние инфраструктуры](04-master/monitoring.md#mon-02-отслеживайте-загрузку-и-состояние-инфраструктуры) | [Мониторинг и оповещения](04-master/monitoring.md) |
| MON-03 | SHOULD | [Проверяйте оповещения](04-master/monitoring.md#mon-03-проверяйте-оповещения) | [Мониторинг и оповещения](04-master/monitoring.md) |
| MQ-01 | MUST | [Именуйте очереди по формату {Проект}_{ТипДанных}_{Назначение}](04-master/queues.md#mq-01-именуйте-очереди-по-формату-проект_типданных_назначение) | [Очереди данных](04-master/queues.md) |
| MQ-02 | SHOULD | [Разделяйте очереди по назначению](04-master/queues.md#mq-02-разделяйте-очереди-по-назначению) | [Очереди данных](04-master/queues.md) |
| MQ-03 | SHOULD | [Используйте единую шкалу приоритетов](04-master/queues.md#mq-03-используйте-единую-шкалу-приоритетов) | [Очереди данных](04-master/queues.md) |
| MQ-04 | MUST | [Документируйте структуру данных очереди](04-master/queues.md#mq-04-документируйте-структуру-данных-очереди) | [Очереди данных](04-master/queues.md) |
| TSK-01 | MUST | [Именуйте задачи по формату {Проект}_{Процесс}_{Периодичность}](04-master/tasks-and-triggers.md#tsk-01-именуйте-задачи-по-формату-проект_процесс_периодичность) | [Задачи, триггеры и планирование](04-master/tasks-and-triggers.md) |
| TSK-02 | SHOULD | [Выбирайте тип триггера по характеру процесса](04-master/tasks-and-triggers.md#tsk-02-выбирайте-тип-триггера-по-характеру-процесса) | [Задачи, триггеры и планирование](04-master/tasks-and-triggers.md) |
| TSK-03 | SHOULD | [Планируйте задачи без перекрытий и с учетом зависимостей](04-master/tasks-and-triggers.md#tsk-03-планируйте-задачи-без-перекрытий-и-с-учетом-зависимостей) | [Задачи, триггеры и планирование](04-master/tasks-and-triggers.md) |
| TSK-04 | MUST | [Настраивайте повторы и эскалацию на уровне задач](04-master/tasks-and-triggers.md#tsk-04-настраивайте-повторы-и-эскалацию-на-уровне-задач) | [Задачи, триггеры и планирование](04-master/tasks-and-triggers.md) |
| TSK-05 | SHOULD | [Регулярно пересматривайте расписания](04-master/tasks-and-triggers.md#tsk-05-регулярно-пересматривайте-расписания) | [Задачи, триггеры и планирование](04-master/tasks-and-triggers.md) |
