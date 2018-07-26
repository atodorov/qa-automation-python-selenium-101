# Module 04: Object Oriented Programming

## Preparation

* Read Chapter 5 from Dive into Python;
* Read [Chapter 9. Classes](https://docs.python.org/3/tutorial/classes.html)
from the Python tutorial;
* Read this file!


Object Oriented Programming is a programming paradigm, that's all about representing concepts with
objects, classes, methods and members.

Popular object oriented languages are C++, Java, Python and Ruby.


## The four principles of OOP

- Abstraction - wrapping common characteristics, states and functionality in abstract structures
- Encapsulation - hiding implementation details and accessing functionality through public interfaces
- Inheritance - reusing code while creating superstructures, also known as being DRY*
- Polymorphism - the provision of a single interface to entities of different types


## Glossary

The fancy words we're going to use.

* Class - an abstraction (ex. Person, Vehicle..)
* Object - an instance of class
* Member/field/attribute - a class variable
* Method - a class function
* DRY - Don't Repeat Yourself
* WET - We Enjoy Typing (opposite of DRY)


# Python OOP by example

## Creating a class (abstraction)

```python
class Panda:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def _get_buff(self):
        if self.weight < 1000:
            self.weight += 1

    def eat_bamboo(self):
        self._get_buff()
        return "Nomm nomm nomm!"


dimcho = Panda("Dimcho", 10, 1500)
print(dimcho.age) # 10
print(dimcho.eat_bamboo()) # "Nomm nomm nomm!"
```

The key concepts here are:

* The initialiser (aka constructor) method for each class is called `__init__`
* Each method takes `self` as the first argument - this is a reference to the current instance of the class.
* **Everything is public!** Private and protected are only a notation - something that we all agree on.
More on private and public later.

## How to check if object is an instance of a class?

We can also check if an object is the instance of a class.

For example, let's say we have an object of the class Human and we want to check
if it's instance (also subclass) of class Object.

```python
class Human:

    def __init__(self, name, age, weight):
        self.name = name

gosho = Human('Gosho', 20, 70)

print(isinstance(gosho, Human))  # True
print(isinstance(gosho, object)) # True
print(isinstance(gosho, Panda))  # False
```


## Magic methods

In Python, there are special merhods, called **dunders** - short for double underscore.

They give us flexibility and can be very powerful! They also implement some standard
behavior.

For example, if you want the `str()` function to work with your class, you should implement the `__str__(self)` method.


```python
class Panda:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def _get_buff(self):
        if self.weight < 1000:
            self.weight += 1

    def eat_bamboo(self):
        self._get_buff()
        return "Nomm nomm nomm!"

    def __str__(self):
        return "I am a panda - {}".format(self.name)


dimcho = Panda("Dimchou", 10, 1500)
print(str(dimcho)) # "I am a panda - Dimchou"
```

We are going to use the following:

* If we want to compare two instances of our class - `__eq__(self, other)`
* If we want to turn our instance into a string - `__str__(self)`
* If we want to print a string representation of our instance - `__repr__(self)`
* If we want to turn our instance to a `int()` - `__int__(self)`
* If we want to make our class hashable - `__hash__(self)`

You can find more in the [Python data model](https://docs.python.org/3.4/reference/datamodel.html)

## Static methods and fields

* Static fields are shared between all classes of that type. (class `Panda` in our case).
* Static methods are neither obligated to have `self` as a first parameter, nor use objects from the same class as the static method's.
But it's good to have Panda classes do only panda stuff! :panda_face:


Static fields in action:

```python
class Panda:
    all_pandas = []
    total_pandas_mass = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Panda.total_pandas_mass += weight
        Panda.all_pandas.append(self)

    def __repr_(self):
        return self.name


dimcho = Panda("Dimcho", 50)
print(Panda.all_pandas()) # ['Dimcho']

boko = Panda("Boko", 70)
print(Panda.total_pandas_mass) # 120
```

Static methods in action:

```python
class Panda:
    all_pandas = []
    pandas_count = 0

    def __init__(self, name):
        self.name = name
        Panda.pandas_count += 1
        Panda.all_pandas.append(name)

    @staticmethod
    def print_all_pandas():
        for panda in Panda.all_pandas:
            print(panda.name)

    # Possible! But don't do so :(
    @staticmethod
    def calculate_difference(a, b):
        return a - b

dimcho = Panda("Dimcho")
Panda.print_all_pandas() # Dimcho
print(Panda.calculate_difference(10 - 5)) # 5
# Again, don't make poor pandas do math please!
```


## Inheritance

Classes in Python can inherit from other classes in order to implementspecific behavior.
To access methods and fields from the parent class use `super()`.

### Extra glossary

* Parent class - also known as a base class (ex. Panda)
* Child class - also known as sub class or inherited class (ex. KungFuPanda)


**Creating a child class:**

```python
class Panda:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def _get_fatter(self):
        if self.weight < 1000:
            self.weight += 1

    def eat(self):
        self._get_fatter()
        print("Nomm nomm nomm! Bamboo.")


class KungFuPanda(Panda):

    def __init__(self, name, age, weight, skill):
        super(KungFuPanda, self).__init__(name, age, weight)
        self.skill = skill

    def fight(self):
        self.weight -= 1
        print("Bam bam!")


po = KungFuPanda("Po", 5, 700, 10)
po.eat() # Nomm nomm nomm! Bamboo.
```

In Python all methods are effectively virtual. This means we can override a parent method by just
defining a method with the same name in a child class.
That means we can make our `KungFuPanda`s eat rice!


```python
class KungFuPanda(Panda):

    def __init__(self, name, age, weight, skill):
        super(KungFuPanda, self).__init__(name, age, weight)
        self.skill = skill

    def fight(self):
        self.weight -= 1
        print("Bam bam!")

    def eat(self):
        self._get_fatter()
        self._get_fatter()
        print("Nomm nomm nomm! Rice.")

po = KungFuPanda("Po", 5, 700, 10)
po.eat() # Nomm nomm nomm! Rice.
```


## Protected and private fields

You don't have an actual protected privacy in Python. This means protected fields can be accessed by everyone,
but developers will know not to do so! (It also makes testing easier)

* Names that starts with _ are protected
* Names that starts with __ are private


```python
class Panda:
    def __init__(self):
        self._dna = 'pandish'
        self.__power = 42

jorko = Panda()
print(jorko._dna) # pandish
print(jorko.__power) # AttributeError: 'Panda' object has no attribute '__power'
```

## Polymorphism

At last, let's show how we can manage all Pandas.

```python
class Panda:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        return "nomnom nom"


class PandaCareTaker():

    .....

    def feed_panda(panda):
        panda.eat()
        print("I fed {}".format(panda.name))


boko = Panda('Boko', 5, 200)
jacky_chan = PandaCareTaker('Jacky', 60, 67)

jacky_chan.feed_panda(boko) # I fed Boko
```


## Tasks & homework

* Checkout the 3 tasks in this directory;
* Use the `test.py` file in each directory to validate your implementation!
