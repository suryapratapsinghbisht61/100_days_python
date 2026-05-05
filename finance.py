import matplotlib.pyplot as plt
import json
import os

class ExpenseTracker:
    def __init__(self):
        self.file = "expenses.json"
        self.expenses = {}
        self.load_data()

    def add_expense(self, month, category, amount):
        if month not in self.expenses:
            self.expenses[month] = {}

        if category in self.expenses[month]:
            self.expenses[month][category] += amount
        else:
            self.expenses[month][category] = amount

        print("✅ Expense added successfully!")


    def show_expenses(self):
        if not self.expenses:
            print("No data found.")
            return

        for month, data in self.expenses.items():
            print(f"\n📅 {month}")
            for category, amount in data.items():
                print(f"  {category}: ₹{amount}")

    def show_bar_graph(self, month):
        if month not in self.expenses:
            print("No data for this month.")
            return

        categories = list(self.expenses[month].keys())
        amounts = list(self.expenses[month].values())

        plt.figure()
        plt.bar(categories, amounts)
        plt.title(f"Expenses for {month}")
        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")
        plt.show()

   
    def show_pie_chart(self, month):
        if month not in self.expenses:
            print("No data for this month.")
            return

        categories = list(self.expenses[month].keys())
        amounts = list(self.expenses[month].values())

        plt.figure()
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title(f"Expense Distribution ({month})")
        plt.show()


    def save_data(self):
        with open(self.file, "w") as f:
            json.dump(self.expenses, f)
        print("💾 Data saved!")

  
    def load_data(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.expenses = json.load(f)
        else:
            self.expenses = {}


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Bar Graph")
        print("4. Show Pie Chart")
        print("5. Save Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            month = input("Enter month (e.g., January): ")
            category = input("Enter category (Food, Travel, etc.): ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(month, category, amount)

        elif choice == "2":
            tracker.show_expenses()

        elif choice == "3":
            month = input("Enter month: ")
            tracker.show_bar_graph(month)

        elif choice == "4":
            month = input("Enter month: ")
            tracker.show_pie_chart(month)

        elif choice == "5":
            tracker.save_data()

        elif choice == "6":
            tracker.save_data()
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()