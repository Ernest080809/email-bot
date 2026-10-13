# Time Travel — сайт с дверью

Один файл `index.html`: пиксельное пшеничное поле, избушка, закрытая дверь, отсчёт до дропа
(22.04.2027, 19:00 по Берлину) и предрегистрация. Без внешних запросов: шрифты встроены (по DSGVO
Google Fonts нельзя подключать напрямую), картинок нет, всё рисуется кодом.

## Посмотреть локально
Открой `index.html` в браузере. Полезные параметры:
- `?open` — показать, как выглядит открытая дверь (после дропа)
- `?reset` — сбросить «ты уже зарегистрирован» в этом браузере

## Запуск на Shopify (рекомендуется — регистрации сразу попадают в клиентов)
1. Shopify Admin → Online Store → Themes → `…` → **Edit code**.
2. Templates → **Add a new template** → тип `page`, формат `liquid`, имя `time-travel`.
3. Вставь первой строкой `{% layout none %}`, под ней — всё содержимое `index.html`. Сохрани.
4. Online Store → Pages → **Add page** «Time Travel», справа выбери шаблон `page.time-travel`.
5. Проверь страницу `novalife.store/pages/time-travel`: введи свой email → в Customers появится клиент
   с тегом `time-travel-waitlist` и согласием на рассылку.
6. **Settings → Customer privacy / Marketing → Double opt-in включить** (в Германии обязательно).
7. Проверь, что есть Privacy Policy и Impressum (Settings → Policies → Legal notice) — ссылки ведут туда.

В день дропа: в Shopify Email отправляешь сегмент `customer_tags CONTAINS 'time-travel-waitlist'`
письмо в 18:00 со ссылкой на коллекцию. В 19:00 дверь на сайте открывается сама и кнопка ведёт на
`CONFIG.dropUrl` (по умолчанию `/collections/time-travel`).

## Настройки
Всё в блоке `CONFIG` в начале `<script>`: даты, режим сохранения, ссылки.
Вне Shopify можно поставить `endpoint` (например Formspree) — тогда email уходит туда POST-запросом.
