# A Python Miscellany: Iterators & Generators

In this lesson we will discuss a few more features of programming in Python.
We’ll be exploring the idea and implementation of iterators and generators.
Understanding these topics will allow you to make your own classes and
functions operate more Pythonically.

## Iterators

Iterators are one of the main reasons Python code is so readable:


```python
for x in just_about_anything:
    do_stuff(x)
```

What’s fun is that `just_about_anything` does not have to be a “sequence”. Rather, you can loop through anything that satisfies the [iterator protocol](http://docs.python.org/2/library/stdtypes.html#typeiter "\(in Pythonv2.7\)") ([py3](http://docs.python.org/3/library/stdtypes.html#typeiter "\(inPython v3.6\)")).

### The Iterator Protocol

An iterator must have the following methods:


```python
an_iterator.__iter__()
```

The [`__iter__`](http://docs.python.org/2/library/stdtypes.html#iterator.__iter__ "\(in Python v2.7\)") special method ([`py3`](http://docs.python.org/3/library/stdtypes.html#iterator.__iter__ "\(in Python v3.6\)")) returns the iterator object itself. The return value might be `self`, or it might be an object constructed that can be iterated over. This is required to allow both containers and iterators to be used with the `for` and `in` statements.


```python
# python 2
an_iterator.next()

# python 3
an_iterator.__next__()
```

The [`next`](http://docs.python.org/2/library/stdtypes.html#iterator.next "\(in Python v2.7\)") method (in python 3 it is [`__next__`](http://docs.python.org/3/library/stdtypes.html#iterator.__next__ "\(in Python v3.6\)")) returns the next item from the container. If there are no further items, this method must raise a `StopIteration` exception.

This change in interface leads to some compatibility problems. In order to write iterators that are compatible with both Python 2 and Python 3, use one of the [compatible idioms](http://python-future.org/compatible_idioms.html#custom-iterators) from python-future.

In Python, data types like lists, tuples, sets, an dicts are sometimes referred to as “iterables”. They too implement the iterator interface, and you can get at the “iterator” directly if you like:


```
In [1]: a_list = [1, 2, 3]

In [2]: list_iter = a_list.__iter__()

In [3]: next(list_iter)
Out[3]: 1

In [4]: next(list_iter)
Out[4]: 2

In [5]: next(list_iter)
Out[5]: 3

In [6]: next(list_iter)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-6-9bc6d561c69b> in <module>()
----> 1 next(list_iter)

StopIteration:
```

It’s not really polite (or proper) to access _special methods_ of objects directly like that, though. Instead, you should use the Python function that utilizes those methods. In this case, that is the [`iter()`](http://docs.python.org/2/library/functions.html#iter "\(in Python v2.7\)") function ([`py3`](http://docs.python.org/3/library/functions.html#iter "\(in Python v3.6\)")).


```
In [7]: iter([2, 3, 4])
Out[7]: <list_iterator at 0x1053d9828>

In [8]: iter(u"a string")
Out[8]: <str_iterator at 0x1053d9f60>

In [9]: iter((u'a', u'tuple'))
Out[9]: <tuple_iterator at 0x1053e70f0>
```

For arbitrary objects, `iter()` calls the `__iter__` special method. But it can also handle objects (`str`, for instance) that don’t have a `__iter__` method (note: strings in Python 3 _DO_ have an ` __iter__` method.

### Making an Iterator

Understanding the iterator protocol allows us to build iterators of our own. Let’s try this out by building a simple iterator that will operate a bit like the Python 2 `xrange`:


```python
class IterateMe_1(object):
    def __init__(self, stop=5):
        self.current = 0
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        if self.current < self.stop:
            self.current += 1
            return self.current
        else:
            raise StopIteration
```

We can even use the protocol to build a function that emulates the Python `for` loop:


```python
def my_for(an_iterable, func):
    """Emulation of a for loop.

    func() will be called with each item in an_iterable
    """
    # equiv of "for i in l:"
    iterator = iter(an_iterable)
    while True:
        try:
            i = iterator.next()
        except StopIteration:
            break
        func(i)
```

[`itertools`](http://docs.python.org/2/library/itertools.html#module-itertools "\(in Python v2.7\)") ([`py3`](http://docs.python.org/3/library/itertools.html#module-itertools "\(in Python v3.6\)")) is a collection of utilities that make it easy to build an iterator that iterates over sequences in various common ways. The utilities it contains work with any object that supports the iterator protocol. And the iterators they return can be used with any Python functions that expect iterators as arguments. Things like `sum`, `tuple`, `sorted`, and `list`, for example.

## Generators

A generator object is a bit like an iterator, except that it is itself the iterator. Another difference is that with a generator you have no access to the data that is being returned, if it even exists.

Conceptually, an iterator allows you to loop over data that exists. Generators, on the other hand, _generate_ their data on the fly. Practically speaking, you can use them interchangeably, and generators are in fact a special case of iterators. Generators just handle some of the internal book- keeping for you.

### ` yield`


```python
def a_generator_function(params):
    some_stuff
    yield something
```

The [`yield`](http://docs.python.org/2/reference/simple_stmts.html#yield "\(in Python v2.7\)") statement ([`py3`](http://docs.python.org/3/reference/simple_stmts.html#yield "\(in Python v3.6\)")) can be used to create generators. Using the `yield` statement in a function causes the function to become a `generator function`. The function can then `yield` values instead of returning them. And the state of the names and values inside the function is preserved between `yield` statements.

When you write a function with `yield` in it, it becomes a “factory” for a `generator object`. Calling the function returns a `generator object`. And every time you call it, a _new_ and _independent_ generator object is returned. Each independent instance keeps track of its own internal state.


```python
gen_a = a_generator_function()
gen_b = a_generator_function()
```

One possible example of a simple generator function might be again to emulate the `xrange` object from Python 2:


```python
def y_xrange(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step
```

It is most common to write generator functions to return a series of values like this. And as we have noted, generators are in fact just a special case of iterators. But notice that we do not use `StopIteration` to signal when a generator function is complete. In fact, calling `return` inside a generator function (or simply allowing an implicit return to happen _at the end_ ) causes `StopIteration` to be raised. You don’t need to do it explicitly.

A final note on writing generator functions. Any callable can be a generator if it uses `yield` instead of `return`. This means, of course, that methods on classes can also be generators. And even classes themselves, if they have a `__call__` method that uses yield, can be generators.

### Generator Comprehensions

There is one last way to create a generator. It turns out that if you use `()` instead of `[]` when writing a comprehension, the result is a generator. It behaves exactly like the equivalent _list comprehension_ , except that it only generates the values one at a time. This can be especially powerful if the item the comprehension is iterating over is itself a generator. The result can be extremely efficient processing of massive amounts of data.


```
In [10]: [x * 2 for x in [1, 2, 3]]
Out[10]: [2, 4, 6]

In [11]: (x * 2 for x in [1, 2, 3])
Out[11]: <generator object <genexpr> at 0x105281200>

In [12]: for n in (x * 2 for x in [1, 2, 3]):
    ...:     print(n)
    ...:
2
4
6
```

## Wrap Up

In this lecture, we’ve learned a bit about two powerful concepts in Python. Using the _iterator protocol_ , we learned to create iterators. We can thus create classes that can work natively with Python’s looping structures and the `itertools` library. Generators, as we learned, are objects that `yield` values one-at-a-time, preserving their internal state. We learned that we can create them using `yield` inside functions or methods. And we learned that there are also _generator comprehensions_. That’s enough to be going on.

