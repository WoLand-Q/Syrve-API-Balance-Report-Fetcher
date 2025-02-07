import requests
import pandas as pd
import json

# Настройки
API_KEY = ''  # Ваш ТОКЕН
BASE_URL = '/resto/api/v2'  # Ваш базовый URL

def get_balance_report(store_ids, timestamp):
    url = f"{BASE_URL}/reports/balance/stores"
    params = {
        'key': API_KEY,
        'timestamp': timestamp,
        'store': store_ids  # Указываем несколько магазинов через параметр store
    }
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка при получении отчета по остаткам: {response.status_code}")
        print(response.text)
        return None

def main():
    # Точки для получения отчета
    store_ids = [
        "6b55f377-322d-499e-a3cc-4275f9d639f2",
        "14ca2cf5-a44b-418b-bc3a-3255f7f9d850",
        "e8b3dbce-cdd0-436f-8b23-b7fac9fea76d"
    ]

    # Timestamp для запроса (можешь указать нужную дату)
    timestamp = "2024-10-16T14:23:57"

    # Получение данных по остаткам
    print("Получение отчета по остаткам товаров для указанных точек...")
    report = get_balance_report(store_ids, timestamp)

    if report and isinstance(report, list):  # Если report - это список
        df = pd.DataFrame(report)

        # Вывести все данные для проверки структуры
        print("\n===== Данные отчета =====")
        print(df.to_string(index=False))  # Вывод всех колонок для анализа структуры

        # Вывести доступные колонки
        print("\n===== Доступные колонки =====")
        print(df.columns.tolist())

        # Сохранение данных в CSV (опционально)
        df.to_csv('balance_report.csv', index=False, encoding='utf-8-sig')
        print("\nОтчет по остаткам сохранен в 'balance_report.csv'.")
    else:
        print("Не удалось получить отчет по остаткам.")

if __name__ == "__main__":
    main()
