Title: Difference between `==` and `is` in Python, and when to use each of them
Date: 2019-01-26 17:00
Category: Python
Tags: python
Authors: Emad Mokhtar

<!-- PELICAN_BEGIN_SUMMARY -->
![Difference]({static}/images/will-francis-1071726-unsplash.jpg)

In Python there are many [comparison operators](https://realpython.com/python-operators-expressions/#comparison-operators); you always use them to check something in your code and let your code take decision according to the comparison

In this article, I want to go deep with two operators `==` to check equality, and `is` to check identity.

<!-- PELICAN_END_SUMMARY -->

## The `==` operator
The equality comparison operator. 
``` python
>>> 1 == 1
True
```
In the above code, we are checking whether the value of int **1** is an equal value of int **1**, in other words, we are checking the values equality here. 
``` python
class Number:
    def __init__(self, number):
        self.number = number

>>> Number(1) == Number(1)
False # Wooot
```
In the above code, we are checking if the values of 2 objects are equal. They are not equal. Classes in Python 🐍 have [dunder methods](https://wiki.python.org/moin/DunderAlias) to implement special logic of magic.

<iframe src="https://giphy.com/embed/12NUbkX6p4xOO4" width="480" height="440" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/shia-labeouf-12NUbkX6p4xOO4">via GIPHY</a></p>

For example,  `__init__()` is dunder method to initiate a new object or the class constructor. For our example above, there is a dunder method used to check the equality which is  `__eq__()` , if we implement it correctly, the expression in the code about should work.

```python
class Number:
    def __init__(self, number):
        self.number = number

    def __eq__(self, another_number):
        if isinstance(another_number, Number):
            return self.number == another_number.number
        return self.number == another_number

>>> Number(1) == Number(1)
True 
>>> Number(1) == 1
True
```

All right, now our class has a correct equality logic. The equality logic is implemented in `__eq__` method. It is also implemented in Python built-in types like Integers.

``` python
import inspect
from pprint import pprint

# 1 is object of int class
pprint(inspect.getmembers(1))
pprint(inspect.getmembers(int))
```

## The `is` operator
The identity check operator
``` python
>>> none_obj = None
>>> none_obj is None
True
>>> number_one = 1
>>> number_one is 1
```
In Python, every object created will store a reference to it, like in the above code **none_obj** which is storing a reference to **None** , and **number_one** object is storing a reference to **1**. Let’s examine how this is done by Python.

``` python
>>> none_obj = None
>>> id(none_obj)
4304631824
>>> id(None)
4304631824
>>> id(number_one)
4304948352
>>> id(1)
4304948352
```
When you create a new variable that stores an object or value, this variable name stores a reference to it, so if you create another variable to store the same object, Python stores a pointer to this object instead of creating a new one.

``` python
a = Number(1)
b = a
>>> id(a), id(b)
(4520963656, 4520963656)
>>> a is b
True
```

Technically speaking, when you check the identity, Python checks `id(a) == id(b)`, which means:
Do objects **a** and **b** refer to the same object? So the answer will be **True** if they refer to the same object.


## Conclusion
If you need to check the value equality, use the `==` operator and if you need to check whether 2 objects are the same, use `is`.

Happy Pythoning  😉
