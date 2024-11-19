# class device():
#     def __init__(self, height, width, name):
#         self.name = name
#         self.height = height
#         self.width = width
#     def power_on():
#         print("POWERING ON")

# class computer(device):
#     def power_on(self):
#         print("TOTALLY NOT POWERING ON")
#     def power_off(self):
#         print("TOTALLY NOT POWERING OFF")
#     def sass(self):
#         print("ughghajfh 💁‍♀️💅🏼👑")   

# dell = computer(203, 102, "Deli")

# dell.sass()

# class vehicle():
#     def __init__(self, name, speed, size):
#         self.name = name
#         self.speed = speed
#         self.size = size
#     def switch_on(self):
#         print("Switching on")
#     def drive(self):
#         print("Im driving, whoop, whoop")
#         if self.speed > 10:
#             print("AAAAAAAH")
#     def fix(self):
#         self.speed += 10
#         print("FIXINGBASHBSDAH")

# class car(vehicle):
#     def switch_on(self):
#         print("Switching off")
#     def drive(self):
#         print("Im driving, no, no")
#         if self.speed > 10:
#             print("YAAAAAAAAAAAAY")
#     def fix(self):
#         self.speed -= 10
#         print("MESSING ABOUT")
#     def spoiler(self):
#         speed += 10
#         print("PUTTING UP SPOILER")

# class motorbike(vehicle):
#     def switch_on(self):
#         print("Switching off")
#     def drive(self):
#         print("Im driving, no, no")
#         if self.speed > 10:
#             print("YAAAAAAAAAAAAY")
#     def fix(self):
#         self.speed -= 10
#         print("MESSING ABOUT")
#     def spoiler(self):
#         speed -= 10
#         print("PUTTING down SPOILER")

from pprint import pprint

class employee():
    def __init__(self, name, job_title, salary, years_of_exp):
        self.name = name
        self.job_title = job_title
        self.salary = int(salary)
        self.years_of_exp = int(years_of_exp)
    
    def change_job_title(self, new_job_title):
        self.job_title = new_job_title
    
    def increase_salary(self, perc_increase):
        self.salary *= (1 + perc_increase/100)
    
    def increase_years_of_exp(self, new_years_of_exp):
        self.years_of_exp = new_years_of_exp
    
    def calculate_hourly_rate(self):
        return int(self.salary / 2000)

class manager(employee):
    def __init__(self, name, job_title, salary, years_of_exp):
        super().__init__(name, job_title, salary, years_of_exp)
        self.bonus = 0

    def calculate_bonus(self):
        self.bonus = self.salary/100 * self.years_of_exp

doug = manager("doug", "manager", "10000", "10")

doug.change_job_title("Janitor")

pprint(vars(doug))