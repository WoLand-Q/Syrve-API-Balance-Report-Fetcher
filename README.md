# 🛒 Syrve-API-Balance-Report-Fetcher

Этот скрипт предназначен для работы с **API Syrve/iiko**, получения отчёта по остаткам товаров на складах и их анализа.

---

## 🚀 Функциональность

- 🔑 **Авторизация в API Syrve** с использованием API-ключа
- 🏬 **Получение остатков товаров для нескольких точек**
- 📊 **Форматирование и анализ данных в pandas**
- 💾 **Сохранение отчёта в CSV**
- 📊 **Вывод данных в читаемом формате в консоли**

---
2️⃣ Настройте параметры подключения
```bash
API_KEY = "ВАШ_ТОКЕН"
BASE_URL = "https://ВАШ_СЕРВЕР.syrve.online/resto/api/v2"
```

⚙️ Как работает скрипт?
- Запрос отчёта по остаткам товаров
- Выполняется GET-запрос /reports/balance/stores
- В запросе передаётся список складов (store_ids) и временная метка (timestamp)
- Обработка данных
- Данные конвертируются в pandas.DataFrame
- Выводится список доступных колонок
- Данные сохраняются в CSV
- Вывод отчёта в консоль
- Показывается структура отчёта и список колонок


📝 Примечания
- 📌 API позволяет получать данные по нескольким точкам сразу – указывайте store_ids.
- 📌 Дата и время в запросе (timestamp) указываются в формате ISO 8601 (YYYY-MM-DDTHH:MM:SS).
- 📌 Файл balance_report.csv сохраняется в кодировке utf-8-sig для корректного отображения в Excel.
- 📌 Логирование включено – в случае ошибки скрипт покажет HTTP-код и тело ответа.

