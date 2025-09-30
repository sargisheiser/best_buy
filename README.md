# BestBuy Store CLI 🛒

A simple Python project that simulates a tech store (like Best Buy).  
Users can browse available products, check total stock, and place orders through a terminal-based menu.

---

## 🚀 Features
- Product management  
  - Each product has a name, price, quantity, and active status  
  - Buying products updates stock automatically  
- Store management  
  - Store holds multiple products (composition pattern)  
  - Add/remove products from inventory  
  - Calculate total stock quantity  
- Interactive CLI menu  
  - List all products in store  
  - Show total amount in stock  
  - Make an order (with validation)  
  - Quit the program  

---

## 🛠️ Project Structure
bestbuy/
├── main.py # CLI menu (user interface)
├── products.py # Product class (manages individual products)
├── store.py # Store class (manages collection of products)
└── README.md # Project documentation

yaml
Copy code

---

## 📦 Installation
Clone the repository:
```bash

git clone https://github.com/<your-username>/bestbuy.git
cd bestbuy

▶️ Usage
Run the program:
python3 main.py

You will see the following menu:

   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number:
📚 Example

Available Products:
1. MacBook Air M2, Price: 1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: 250, Quantity: 500
3. Google Pixel 7, Price: 500, Quantity: 250

Total quantity in store: 850

Order placed successfully! Total cost: 1950 dollars
🧑‍💻 Technologies
Python 3

Git & GitHub for version control

✅ Learning Goals
Practice with OOP in Python (classes, methods, composition)

Implementing an interactive command-line interface

Using Git and GitHub for version control and portfolio building

📄 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it.