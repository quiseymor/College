import csv
from datetime import datetime
import matplotlib.pyplot as plt

def datas(file_path):
    dates = []
    open_prices = []
    high_prices = []
    low_prices = []
    close_prices = []
    volumes = []

    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        
        for row in reader:
            date = datetime.strptime(row[0], '%Y%m%d').date() 
            open_price = float(row[1])
            high_price = float(row[2])
            low_price = float(row[3])
            close_price = float(row[4])
            volume = float(row[5]) / 1_000_000  # пересчет объема в млн. руб.
            
            dates.append(date)
            open_prices.append(open_price)
            high_prices.append(high_price)
            low_prices.append(low_price)
            close_prices.append(close_price)
            volumes.append(volume)

    return dates, open_prices, high_prices, low_prices, close_prices, volumes

def plot_prices(dates, open_prices, high_prices, low_prices, close_prices):
   # plt.figure(figsize=(12, 6))
    plt.subplot(2,2,1)
    plt.plot(dates, open_prices, color='blue', label='Цена открытия', marker='o', markersize=5)
    plt.plot(dates, high_prices, color='green', label='Максимальная цена', marker='o', markersize=5)
    plt.plot(dates, low_prices, color='red', label='Минимальная цена', marker='o', markersize=5)
    plt.plot(dates, close_prices, color='purple', label='Цена закрытия', marker='o', markersize=5)
    
    plt.fill_between(dates, low_prices, high_prices, color='yellow', alpha=0.3) # заливка области между минимальной и максимальной ценой
    
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.title('Изменение цены золота')
    plt.legend()
    plt.grid(True)

def plot_volumes(dates, volumes):
    #plt.figure(figsize=(12, 6))
    plt.subplot(2,2,2)
    plt.bar(dates, volumes, color='orange')
    
    plt.xlabel('Дата')
    plt.ylabel('Объем сделок, млн. руб.')
    plt.title('Динамика объемов сделок')
    plt.grid(True)

def main():
    file_path = 'G_30112023_01122023.csv'
    dates, open_prices, high_prices, low_prices, close_prices, volumes = datas(file_path)

    plot_prices(dates, open_prices, high_prices, low_prices, close_prices)
    plot_volumes(dates, volumes)
    
    plt.show()

if __name__ == "__main__":
    main()