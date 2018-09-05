# Queues

![queue](https://netmatze.files.wordpress.com/2014/08/queue.png)

Queues are a data structure that serve as a collection of elements, similar to Stacks. These elements are stacked in a first in, first out sequence **(aka FIFO - First In / First Out)**. It may help to think about a queue as a line at the buffet (assuming you don't have anyone cutting in line!).

Common methods include:
  - `enqueue` adds a new element to the back of the queue
  - `dequeue` removes the front-most element from the queue

Example implementations / use cases for Queues:
  - Modeling real-world scenarios of ordered operations
  - When a resource is shared among multiple consumers. Examples include CPU scheduling, Disk Scheduling.
  - When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes. Examples include IO Buffers, pipes, file IO, etc.
