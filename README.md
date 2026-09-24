# PIX RPA Development Conventions & Best Practices

Соглашения и рекомендации для команд, которые разрабатывают и сопровождают роботов на платформе PIX RPA: от оценки процесса и структуры проекта до администрирования PIX Master.

## Зачем это нужно

Робот работает без присмотра, в чужих системах, на реальных данных. Большинство проблем в RPA-проектах повторяются от команды к команде:

- **Робот ломается от любого изменения** — новой кнопки в интерфейсе, переименованного столбца в Excel, смены пароля
- **Ошибка обрабатывается молча** — транзакция помечена успешной, а документ не создан, или создан дважды
- **Поддержка не может разобраться без автора** — непонятно, что делает робот, где его настройки и что означает ошибка в логе
- **Каждый робот устроен по-своему** — новый разработчик тратит дни, чтобы разобраться в чужом проекте, а ревью превращается в спор о вкусах

Соглашения фиксируют решения, которые уже проверены на практике, чтобы не принимать их заново в каждом проекте. В результате роботы устроены одинаково, падают предсказуемо и передаются в поддержку без потери знаний.

## С чего начать

| Кто вы | Что прочитать |
|--------|---------------|
| Новый разработчик | [Глоссарий](docs/glossary.md) → [Структура проекта](docs/01-conventions/project-structure.md) → [Исключения](docs/01-conventions/exceptions.md) → [Чек-лист код-ревью](templates/code-review-checklist.md) |
| Ревьюер / техлид | [Чек-лист код-ревью](templates/code-review-checklist.md), [Реестр правил](docs/rules-index.md), [Код-ревью](docs/03-robot-lifecycle/code-review.md) |
| Аналитик | [Жизненный цикл робота](docs/03-robot-lifecycle/README.md), шаблон [PDD](templates/pdd.md) |
| Администратор PIX Master | [Соглашение об администрировании PIX Master](docs/04-master/README.md) |
| Поддержка | [Сопровождение](docs/03-robot-lifecycle/support.md), шаблон [runbook](templates/runbook.md) |

## Как устроена документация

| Раздел | Для кого | Что внутри |
|--------|----------|------------|
| [Соглашения](#соглашения) | Разработчики, ревьюеры | Правила, которые проверяются на код-ревью. В основном MUST |
| [Рекомендации по написанию скриптов](#рекомендации-по-написанию-скриптов) | Разработчики | Приемы написания качественного кода. В основном SHOULD |
| [Жизненный цикл робота](#жизненный-цикл-робота) | Аналитики, разработчики, поддержка | Как робот проходит путь от идеи до вывода из эксплуатации |
| [PIX Master](#pix-master) | Администраторы, DevOps | Именование и настройка компонентов оркестратора |

Сводный список всех правил — в [реестре правил](docs/rules-index.md), термины — в [глоссарии](docs/glossary.md).

### Уровни обязательности

У каждого правила есть идентификатор (например, `EXC-03`) и уровень:

| Уровень | Значение | Что делать при нарушении |
|---------|----------|--------------------------|
| **MUST** — обязательно | Правило соблюдается всегда | Нарушение блокирует слияние Pull Request. Исключение возможно только с обоснованием в описании PR и согласованием с техлидом |
| **SHOULD** — рекомендуется | Правило соблюдается по умолчанию | Отступление допустимо, если причина понятна и указана в комментарии к коду или в PR |
| **MAY** — допустимо | Прием можно применять по ситуации | Решение принимает разработчик |

На код-ревью ссылайтесь на правило по идентификатору: «нарушено EXC-03», «см. LOOP-02».

## Карта разделов

### Соглашения

- [Структура проекта](docs/01-conventions/project-structure.md) — `PRJ`
- [Конфигурация и конфиденциальные данные](docs/01-conventions/config-and-secrets.md) — `CFG`
- [Git](docs/01-conventions/git.md) — `GIT`
- [Именование](docs/01-conventions/naming.md) — `NAM`
- [Базы данных](docs/01-conventions/database.md) — `DB`
- [Очереди](docs/01-conventions/queues.md) — `QUE`
- [Логирование](docs/01-conventions/logging.md) — `LOG`
- [Исключения](docs/01-conventions/exceptions.md) — `EXC`
- [Надежность и восстановление после сбоев](docs/01-conventions/reliability.md) — `REL`
- [Персональные данные](docs/01-conventions/personal-data.md) — `PD`

### Рекомендации по написанию скриптов

- [Стиль кода и принципы проектирования](docs/02-guidelines/csharp-style.md) — `CS`
- [Строковые литералы](docs/02-guidelines/strings.md) — `STR`
- [LINQ](docs/02-guidelines/linq.md) — `LNQ`
- [Условия и условные операторы](docs/02-guidelines/conditions.md) — `CND`
- [Циклы и goto](docs/02-guidelines/loops-and-goto.md) — `LOOP`
- [Работа с файлами](docs/02-guidelines/files.md) — `FS`
- [Работа с Excel](docs/02-guidelines/excel.md) — `XLS`
- [Работа с почтой](docs/02-guidelines/email.md) — `MAIL`
- [Интеграции с внешними системами](docs/02-guidelines/integrations.md) — `INT`
- [Жесткое кодирование](docs/02-guidelines/hardcoding.md) — `HC`
- [Активности PIX RPA](docs/02-guidelines/pix-activities.md) — `ACT`
- [Работа с UI](docs/02-guidelines/ui-automation.md) — `UI`
- [ИИ и интеллектуальная обработка документов](docs/02-guidelines/ai-and-idp.md) — `AI`

### Жизненный цикл робота

- [Обзор этапов и ролей](docs/03-robot-lifecycle/README.md)
- [Оценка процесса](docs/03-robot-lifecycle/assessment.md) — `ASM`
- [Проектирование](docs/03-robot-lifecycle/design.md) — `DSN`
- [Тестирование](docs/03-robot-lifecycle/testing.md) — `TST`
- [Код-ревью](docs/03-robot-lifecycle/code-review.md) — `REV`
- [Релиз и развертывание](docs/03-robot-lifecycle/release-and-deploy.md) — `DPL`
- [Сопровождение](docs/03-robot-lifecycle/support.md) — `SUP`
- [Документирование роботов](docs/03-robot-lifecycle/documentation.md) — будет перенесено во внутренний Confluence

### PIX Master

- [Обзор и общий формат имен](docs/04-master/README.md)
- [Очереди данных](docs/04-master/queues.md) — `MQ`
- [Хосты](docs/04-master/hosts.md) — `HST`
- [Агенты роботов](docs/04-master/agents.md) — `AGT`
- [Задачи, триггеры и планирование](docs/04-master/tasks-and-triggers.md) — `TSK`
- [Ассеты](docs/04-master/assets.md) — `AST`
- [Мониторинг и оповещения](docs/04-master/monitoring.md) — `MON`
- [Интеграция компонентов](docs/04-master/components.md)

### Шаблоны

- [PDD — описание процесса](templates/pdd.md)
- [SDD — техническое решение](templates/sdd.md)
- [Runbook для поддержки](templates/runbook.md)
- [Чек-лист код-ревью](templates/code-review-checklist.md)
- [.gitignore для проекта робота](templates/robot.gitignore)
- Шаблоны проектов роботов — в репозитории [pix-templates](https://github.com/TheMrDJek/pix-templates)

## Участвуйте в развитии

Репозиторий открыт для предложений: создавайте Issues или Pull Requests. Как оформить правило и проверить изменения перед отправкой — в [CONTRIBUTING](CONTRIBUTING.md). История изменений — в [CHANGELOG](CHANGELOG.md).
