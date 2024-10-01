class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()


    def say_info(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age}")


    def birthday(self):
        self.age += 1
        print(f"У меня день рождения, мне теперь {self.age}")


    def __len__(self):
        return self.age


    def __lt__(self, other):
        return self.age < other.age


    def __gt__(self, other):
        return self.age > other.age


    def __del__(self):
        print(f"{self.name} ушел")


    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


    def __bool__(self):
        return bool(self.age)


    def __str__(self):
        return self.name


den = Human("Денис", 22)
max = Human("Макс", 22)

#del den

if den:
    den.say_info()

a = 6
print(a)
print(den)  # def __str__
print(max)  # def __str__

print(bool(den == max)) # def __bool__

print(len(den))  # def __len__
print(len(max))  # def __len__

print(den < max) # def __lt__ - Lower than (то есть меньше чем)
print(den > max) # def __gt__ - Greater than (больше чем)

max.birthday()   # def birthday(self):

print(len(den))  # def __len__
print(len(max))  # def __len__

print(den < max) # def __lt__ - Lower than (то есть меньше чем)
print(den > max) # def __gt__ - Greater than (больше чем)

print(den == max) # def __eq__ - Сравнение (Переопределяет метод в объекте)
max.name = "Денис"
den.birthday()
print(den == max)