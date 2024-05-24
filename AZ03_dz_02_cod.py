# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные,
# найти среднюю цену и вывести ее, а также
# сделать гистограмму цен на диваны

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# Шаг 1: Парсинг цен на диваны с сайта divan.ru
def fetch_data():
    url = 'https://www.divan.ru/divany'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    sofas = soup.find_all('div', {'class': 'catalog-product'})
    data = []

    for sofa in sofas:
        try:
            name = sofa.find('div', {'class': 'catalog-product__name'}).text.strip()
            price = sofa.find('div', {'class': 'catalog-product__price'}).text.strip().replace('₽', '').replace(' ', '')
            data.append([name, int(price)])
        except:
            continue

    return data


# Шаг 2: Запись данных в CSV файл
def save_to_csv(data, filename='sofas.csv'):
    df = pd.DataFrame(data, columns=['Name', 'Price'])
    df.to_csv(filename, index=False)


# Шаг 3: Обработка данных и нахождение средней цены
def calculate_average_price(filename='sofas.csv'):
    df = pd.read_csv(filename)
    average_price = df['Price'].mean()
    return average_price


# Шаг 4: Построение гистограммы цен на диваны
def plot_histogram(filename='sofas.csv'):
    df = pd.read_csv(filename)
    plt.figure(figsize=(10, 5))
    plt.hist(df['Price'], bins=30, edgecolor='black', alpha=0.7)
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()


# Основная программа
if __name__ == '__main__':
    data = fetch_data()
    save_to_csv(data)
    average_price = calculate_average_price()
    print(f'Средняя цена на диваны: {average_price} ₽')
    plot_histogram()