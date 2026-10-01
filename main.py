file_name ='sales_log.txt'
def display_menu():
    print('========================================')
    print('SALES RECORD MANAGEMENT SYSTEM')
    print('========================================')
    print('1. Add Sale Record')
    print('2. View All Records & Summary Statistics')
    print('3. Clear All Sales Data')
    print('4. Exit System')
    print('========================================')



def sale_record():
    try:
        item_name = input("Enter Item Name:").strip()
        quantity = int(input("Enter Quantity:"))
        price = float (input("Enter price:"))


    if quantity < 0 or price < 0:
        print('Quantity and price should be above 0 and not negative.')
        return

    total_amount = quantity * price

    with open(file_name, "a", encoding='utf-8') as file:
        file.write(
            f"{item_name}, {quantity}, {price:.2f}, "
            f"{total_amount:.2f}\n"

        )
    print("Sale record saved successfully")


    except ValueError:
        print('Enter a numerical value')

    except OSError:
        print('File save error')






def view_records():
    print('---SALES RECORD---')
    total_units = 0
    total_revenue = 0
    records = False

    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()

            if line == '':
                continue



