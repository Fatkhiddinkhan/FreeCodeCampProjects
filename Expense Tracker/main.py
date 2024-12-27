def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    
def delete_expense(expenses):
    if not expenses:
        print('No expenses to delete.')
        return

    print('\nAll Expenses:')
    print_expenses(expenses)

    choice = input('Select the number of the expense you want to delete (or type "cancel" to exit): ')
    if choice.lower() == 'cancel':
        print('Deletion cancelled.')
        return

    try:
        index = int(choice) - 1
        if 0 <= index < len(expenses):
            expense_to_delete = expenses[index]
            confirm = input(f'Are you sure you want to delete this expense (Amount: {expense_to_delete["amount"]}, Category: {expense_to_delete["category"]})? (yes/no): ').lower()
            if confirm == 'yes':
                del expenses[index]
                print('Expense deleted successfully.')
            else:
                print('Deletion cancelled.')
        else:
            print('Invalid selection.')
    except ValueError:
        print('Invalid input. Please enter a valid number or type "cancel".')

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Delete expense')
        print('5. Exit')
       
        choice = input('Enter your choice: ')
        if choice not in ['1', '2', '3', '4', '5']:
            print("\n\n\nInvalid input, please enter numerical input! \n\n\n")

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        
        elif choice == '5':
            delete_expense(expenses)

        elif choice == '6':
            print('Exiting the program.')
            break


main()