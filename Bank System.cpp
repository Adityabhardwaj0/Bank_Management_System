#include<iostream>
#include<string>
using namespace std;

class BankAccount {
protected:
    string accountHolderName;
    int accountNumber;
    double balance;
public:
    BankAccount(string name, int number, double initialBalance) {
        accountHolderName = name;
        accountNumber = number;
        balance = initialBalance;
    }
    void deposit(double amount) {
        balance += amount;
        cout << "Deposited: $" << amount << endl;
    }
    void withdraw(double amount) {
        if (balance < amount) {
            cout << "Insufficient balance!" << endl;
        }
        else {
            balance -= amount;
            cout << "Withdrawn: $" << amount << endl;
        }
    }
    void displayBalance() {
        cout << "Account balance: $" << balance << endl;
    }
};

class SavingsAccount : public BankAccount {
private:
    double interestRate;
public:
    SavingsAccount(string name, int number, double initialBalance, double rate) : BankAccount(name, number, initialBalance) {
        interestRate = rate;
    }
    void addInterest() {
        double interest = balance * interestRate / 100;
        balance += interest;
        cout << "Interest added: $" << interest << endl;
    }
};

class CheckingAccount : public BankAccount {
private:
    double transactionFee;
public:
    CheckingAccount(string name, int number, double initialBalance, double fee) : BankAccount(name, number, initialBalance) {
        transactionFee = fee;
    }
    void deductFee() {
        balance -= transactionFee;
        cout << "Transaction fee deducted: $" << transactionFee << endl;
    }
};

int main() {
    SavingsAccount s("Alice", 123456, 1000, 2.5);
    CheckingAccount c("Bob", 654321, 500, 1.0);

    s.displayBalance();
    s.deposit(500);
    s.addInterest();
    s.displayBalance();

    c.displayBalance();
    c.withdraw(200);
    c.deductFee();
    c.displayBalance();

    return 0;
}
