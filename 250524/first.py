class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"멍멍! 나는 {self.name}이야!")

# 사용 예시
dog1 = Dog("초코", 3)
dog1.bark()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("소리를 낸다")

class Cat(Animal):
    def speak(self):
        print("야옹")

# 사용 예시
a = Animal("동물")
a.speak()   # 출력: 소리를 낸다

c = Cat("나비")
c.speak()   # 출력: 야옹
