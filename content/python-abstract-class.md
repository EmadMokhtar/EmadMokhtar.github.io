Title: Python Abstract Class
Date: 2018-08-22 12:00
Category: python
Tags: Python
Authors: Emad Mokhtar
Status: draft

If you are coming from static type language word, like C# or Java, I'm sure you've created an abstract class and wondering how to do that in Python. First, let's now what is the abstract class.

> In programming languages, an abstract type is a type in a nominative type system that cannot be instantiated directly; a type that is not abstract – which can be instantiated – is called a concrete type. Every instance of an abstract type is an instance of some concrete subtype. Abstract types are also known as existential types. - [Wikipedia](https://en.wikipedia.org/wiki/Abstract_type)

To be simple, an abstract class is a class that can be instantiated, it's created to be a superclass. In Python, a class can be instantiated no restrictions and no `abstract` keyword.

``` python
class AbstractCollectionMerger:
     def merge(self):
         pass

# Abstract class can ve instantiated
abstract_obj = AbstractClass()


abstract_obj.__class__.__name__  # AbstractClass

```

**How can I  create an abstract class in Python?**

Python has a module to do that, the module called [`abc`](https://docs.python.org/3/library/abc.html), this module created {Read the PEP 3119 and get the overview of it and link to it.} https://www.python.org/dev/peps/pep-3119/

``` python
 class AbstractCollectionMerger(abc.ABC):
     @abc.abstractmethod
     def merge(self):
         pass


abstract_obj = AbstractClass()
>>> Traceback (most recent call last):
  File "<input>", line 1, in <module>
    obj = AbstractCollectionMerger()
TypeError: Can't instantiate abstract class AbstractCollectionMerger with abstract methods merge
```