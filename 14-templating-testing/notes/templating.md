# Pyramid Views & Templates
We got started with a Pyramid app with the intention to display some content online. Toward this end, we created a basic view that read raw a HTML file and provided its content to the browser as an HTTP response. That worked, but it’s a really crappy way to use Pyramid and doesn’t even begin to take advantage of its capabilities. Today we’ll learn about better ways to connect views to the HTML they serve, and how to use templates to display our information.

## The MVC View
We return again to the Model-View-Controller pattern. We’ve built our controller using Pyramid’s view callables that take HTTP requests as arguments. We’ve also created the beginnings of our MVC view using our HTTP files. Let’s dig into both of these some more.

## Presenting Data
The job of the view in the MVC pattern is to present data in a format that is readable to the users of the system. There are many ways to present data. Some are readable by humans (e.g. tables, charts, graphs, HTML pages, text files), while others are more for machines (e.g. xml files, csv, json).
