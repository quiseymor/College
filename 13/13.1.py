import xml.etree.ElementTree as ET

tree = ET.parse('orders.xml')
root = tree.getroot()

# Визуализация структуры файла
def visualize_element(elem, level=0):
    print('\t' * level + elem.tag)
    for child in elem:
        visualize_element(child, level + 1)

# Вывод содержимого отдельных частей
print("Структура файла:")
visualize_element(root)

# Вывод содержимого каждого заказчика
for customer in root.findall('./Customers/Customer'):
    print("\n---")
    print(f"Customer ID: {customer.get('CustomerID')}")
    print(f"Company Name: {customer.find('CompanyName').text}")
    print(f"Contact Name: {customer.find('ContactName').text}")
    print(f"Contact Title: {customer.find('ContactTitle').text}")
    print(f"Phone: {customer.find('Phone').text}")
    full_address = customer.find('FullAddress')
    print("Full Address:")
    print(f"\tAddress: {full_address.find('Address').text}")
    print(f"\tCity: {full_address.find('City').text}")
    print(f"\tRegion: {full_address.find('Region').text}")
    print(f"\tPostal Code: {full_address.find('PostalCode').text}")
    print(f"\tCountry: {full_address.find('Country').text}")