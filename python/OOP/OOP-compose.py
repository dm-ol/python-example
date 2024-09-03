# Композиція — це відношення, при якому об'єкти одного класу пов'язані з об'єктами іншого.
# Такий спосіб організації взаємодії між класами називається асоціацією.
# Зазвичай, тоді об'єкт одного з класів (у прикладі — Salary) є полем іншого (Employee).
# Асоційовані об'єкти можуть циклічно посилатися один на одного, що ламає стандартний механізм збирання сміття.

class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus):
        self.salary = Salary(pay)
        self.bonus = bonus

    def get_salary(self):
        return self.salary.get_total() + self.bonus


employee = Employee(5000, 10000)
print(employee.get_salary())  # 70000
