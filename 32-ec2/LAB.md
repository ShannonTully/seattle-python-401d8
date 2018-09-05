# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 32: Deploy a WSGI app to AWS

## Deploy a WSGI app to AWS

**This is a paired assignment with your Django partner**

There are a number of moving parts in a full-stack web application. In order to get accustomed to them, deploy a simple WSGI application to AWS.

### Specifications

  1. Create and configure an AWS EC2 Instance for a web server
     1. ensure that the server accepts incoming connections over SSH and HTTP
     2. use a t2.micro instance to avoid incurring costs
  2. Clone the [sample application](https://github.com/cewing/simple-bookapp).

  3. Install and configure nginx as the HTTP front-end proxy
     1. ensure that you use the appropriate server name, given the public DNS of your EC2 instance
     2. set up a proxy pass for the root location

  4. Install [gunicorn](http://docs.gunicorn.org/en/stable/index.html) as your WSGI server
  5. Configure [systemd](http://docs.gunicorn.org/en/stable/deploy.html#systemd) to start your WSGI server.
    - _note that the linked configuration for systemd is for gunicorn, and over-engineered for our purposes. Refer to the lecture videos for more detailed instructions_
  6. Once properly configured, navigate to your public DNS location in a web browser to confirm that your application is running

### Submission

Take a couple of screen shots showing a web browser viewing the application on your EC2 instance. Ensure that the URL of the instance is visible in the images. Upload these screenshots and submit, along with the URL of your instance so I can verify that it is still running.

 **DO NOT stop or terminate your ec2 instance until this assignment is graded.** Having the app stay up even after you have logged out is a vital part of the assignment.

---

## Learning Journal
Refer to the daily learning journal assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas
