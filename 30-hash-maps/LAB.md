# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 30: Hash Tables

## Hash Tables

**This is a solo assignment**

### Specifications

- In your `data-structures-and-algorithms` repository create a branch called `class-30-hash-tables`
- Create a new directory in `data_structures` called `hash_table.py`
- In `hash_table.py`:
    - Create a `HashTable` class, which when instantiated is aware of the following attributes:
        1. `max_size`: defaults to `1024`
        2. `buckets`: defaults to a Python `list()`
            - This list structure should be instantiated with a size of `max_size`, where each element is a `LinkedList`
    - Define the following methods on your `HashTable` class:
        - `hash_key`: which accepts a `string` argument only, and returns a hashed value representing a single bucket location in your hash table
        - `set`: which accepts a `key` and `value` as arguments. The `key` will be used to as the hashed location for identifying a bucket. The `value` will be the actual data stored in the `LinkedList` as a new `Node` in that location.
            - _Note: This implies that your hash table will handle collisions using separate chaining._
        - `get`:
        - `remove`:


### Testing
- Write at least three unit tests for each function that you define as part of this assignment.

### Submission

1. Create a pull request from your `class-30-hash-tables` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-30-hash-tables` into `master`

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
