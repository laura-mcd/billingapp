def read_products(filename):
    products = []
    with open(filename , 'r') as file:
        for line in file:
            product_id, name, price =line.strip().split(',')
            products.append({
                'id': product_id,
                'name': name,
                'price': float(price)
            })
    return products

def display_products(products):
    print('Available Products:')
    print('{:<10} {:<20} {:<10}'.format('ProductID', 'ProductName', 'Price'))
    for product in products:
        print('{:<10} {:<20} {:<10.2f}'.format(product['id'], product['name'], product['price']))

def select_products(products):
    selected_products = []
    while True:
        product_id = input('Enter product id to add to cart (or type "done" to finish): ')
        if product_id.lower() == 'done':
            break
        try:
            quantity = int(input('Enter the quantity: '))
        except ValueError:
            print('Invalid quantity. Please enter a number.')
            continue
        for product in products:
            if product['id'] == product_id:
                selected_products.append({
                    'id': product['id'],
                    'name': product['name'],
                    'price': product['price'],
                    'quantity': quantity
                })
                break 
        else:
            print('Invalid Product ID')
    return selected_products

def calculate_total(selected_products):
    total = 0
    for product in selected_products:
        total += product['price'] * product['quantity']
    return total

def write_transaction(filename, selected_products, total):
    with open(filename, 'a') as file:
        for product in selected_products:
            file.write(f"{product['id']},{product['name']},{product['price']},{product['quantity']}\n")
        file.write(f'Total: {total}\n')
        file.write('\n')

def main():
    products = read_products(r'C:\Users\laura\Documents\BillingApp\products.txt')
    display_products(products)
    selected_products = select_products(products) 
    total = calculate_total(selected_products)
    print('Total: ${:.2f}'.format(total))
    write_transaction(r'C:\Users\laura\Documents\BillingApp\transactions.txt', selected_products, total)
    print('Transaction details have been saved to "transactions.txt".')

if __name__ == '__main__':
    main()