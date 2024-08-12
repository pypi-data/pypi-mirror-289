# How to use the library ?

You can import the @interface method and use it as a decorator
in your classes

```python
@interface
class Animal:
    def walk(): pass
    def eat(): pass
```

And then inherit from your interface class

```python
@interface
class Dog(Animal):
    def walk(): pass
    def eat(): pass
```
