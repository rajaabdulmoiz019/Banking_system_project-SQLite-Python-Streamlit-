<div align="center">
🏦 Bank Management System (Streamlit ,Python ,SQLite)
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Database-SQLite3-green.svg" alt="Database">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status">
</p>
<p align="center">
  A comprehensive command-line banking system built with Python and SQLite3, providing essential banking operations with a user-friendly interface.
</p>
</div>

📋 Overview
The Bank Management System is a robust, console-based application that simulates real-world banking operations. Built entirely in Python with SQLite3 for data persistence, this project demonstrates core banking functionalities including account management, balance inquiries, and secure transactions.
✨ Features
<table>
<tr>
<td width="50%">
🔐 Account Management

Quick Account Creation - Register new customers instantly
Unique Card ID System - Each account gets a unique identifier
Customer Data Storage - Secure storage of customer information
Starting Balance - New accounts initialized with ₹100,000

</td>
<td width="50%">
💰 Banking Operations

Balance Inquiry - Real-time balance checking
Deposit Funds - Add money to accounts securely
Withdraw Funds - Process withdrawal requests
Transaction History - Track all account activities

</td>
</tr>
</table>
🚀 Quick Start
Prerequisites
bashPython 3.8 or higher
SQLite3 (included with Python)
Installation
bash# Clone the repository
git clone https://github.com/yourusername/bank-management-system.git

# Navigate to project directory
cd bank-management-system

# Run the application
python banking_system.py
💻 Usage
The system provides an intuitive menu-driven interface:
-------------------------------------BANK MANAGEMENT SYSTEM------------------------------------
PRESS 1 For Account creation
PRESS 2 For Balance inquiry
PRESS 3 For Transaction
PRESS 4 For Exiting
==================================================
Creating an Account

Select option 1 from the main menu
Enter your unique Card ID
Provide your name and current date
Account is created with initial balance of ₹100,000

Checking Balance

Select option 2 from the main menu
Enter your Card ID
View your account details and current balance

Making Transactions

Select option 3 from the main menu
Authenticate with your Card ID
Choose operation:

1 for Withdrawal
2 for Deposit


Enter the amount and confirm

🗄️ Database Structure
The system uses two main tables:
Customer_data

Card_ID - Unique customer identifier
Name - Customer name
Date - Account creation date

Balance

Card_ID - Foreign key to Customer_data
balance - Current account balance

🛠️ Technical Stack
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

Language: Python 3.8+
Database: SQLite3
Libraries: sqlite3, time

📊 System Architecture
┌─────────────────────────────────────┐
│      User Interface (CLI)           │
├─────────────────────────────────────┤
│    Application Logic Layer          │
│  - Account Management               │
│  - Transaction Processing           │
│  - Balance Operations                │
├─────────────────────────────────────┤
│    Database Layer (SQLite3)         │
│  - Customer_data Table              │
│  - Balance Table                    │
└─────────────────────────────────────┘
🎯 Key Functionalities
FeatureDescriptionStatusAccount CreationRegister new customers with unique IDs✅ ImplementedBalance InquiryCheck account balance anytime✅ ImplementedDepositsAdd funds to accounts✅ ImplementedWithdrawalsWithdraw funds from accounts✅ ImplementedAuthenticationVerify customer before transactions✅ ImplementedData PersistenceSQLite database for permanent storage✅ Implemented
📝 Future Enhancements

 Transaction history viewing
 PIN-based security system
 Interest calculation
 Account statements generation
 Fund transfer between accounts
 GUI interface using Tkinter
 Export data to CSV/PDF
 Multi-user session management

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
👨‍💻 Author
Your Name

GitHub: @yourusername
LinkedIn: Your LinkedIn

🙏 Acknowledgments

Inspired by real-world banking systems
Built as a learning project for Python and database management
Thanks to the Python community for excellent documentation


<div align="center">
⭐ Star this repository if you find it helpful!
Made with ❤️ and Python
</div>
