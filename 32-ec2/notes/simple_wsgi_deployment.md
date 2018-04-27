# Deploying a Simple WSGI Application on AWS

Let’s walk through manually deploying a simple WSGI application to an AWS EC2
instance we’ve created.

## Setup


```bash
$ mkdir wsgiapp
$ cd wsgiapp
$ python3 -m venv ENV
$ . ENV/bin/activate
(ENV)$
```

In the new `wsgiapp` directory, create a very simple WSGI application. Start
by creating a new file `myapp.py` and opening it in your editor. In the file,
type the following Python code:


```python
# -*- coding: utf-8 -*-
"""A simple WSGI app for deployment."""
from sys import version_info


def app(environ, start_response):
    """A simple WSGI app."""
    data = "Hello, World!\n"

    if version_info.major > 2:
        data = data.encode("utf-8")

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, app)
    srv.serve_forever()
```

Test your application to be sure it works by running it from the command line:


```bash
(ENV)$ python myapp.py
```

Point your web browser at _`http://localhost:8080/`_ and verify that you can
see “Hello World!” printed.

Next, provision a new EC2 instance on AWS using the through-the-web
provisioner.

  * Make sure you are using an Ubuntu image, either version 14.04 or 16.04.
  * Make sure that your security group allows inbound SSH, HTTP, and HTTPS
  * Download and save a private key for the EC2 instance to your filesystem
  * Change permissions on the private key file (`chmod 400`)
  * Move the private key to the `~/.ssh/` directory.

Next, use the shell command `scp` to securely copy your wsgi application to
the new server instance. You’ll need to update the path to your **private key
file** and the **public DNS name** of your EC2 instance from the values shown
here.


```bash
(ENV)$ scp -i ~/.ssh/pk-cpe.pem myapp.py ubuntu@ec2-54-184-162-20.us-west-2.compute.amazonaws.com:~/
...
Are you sure you want to continue connecting (yes/no)? yes
...
myapp.py                                      100%  381     0.4KB/s   00:00
(ENV)$
```

`-i ~/.ssh/pk-cpe.pem` provides a file that gives you credentials for copying
data from your computer to some other one. In our case, these credentials come
in the form of the private key provided by AWS.

## Manual Configuration

We are going to do this manually once together. Later on in the week, you’ll
have a chance to repeat the process using the configuration management tool
Ansible.

### Configure Nginx

The first step is to configure `nginx` to proxy HTTP requests to our simple
application.

If you know, or are more comfortable with the `Apache` webserver, you can also
use that. However, the trend I’ve seen over the last few years is toward the
use of `nginx` over the old stand-by.

Nginx stores site configuration on Ubuntu in the `/etc/nginx/sites-available`
directory. This is in fact a pattern you’ll get used to. On most Linux
machines, configuration of individual applications can be found in some
subdirectory of the `/etc` directory.

Let’s SSH into our new instance and look at what’s there:


```bash
(ENV)$ ssh -i ~/.ssh/pk-cpe.pem ubuntu@ec2-54-184-162-20.us-west-2.compute.amazonaws.com
Welcome to Ubuntu 12.04.4 LTS (GNU/Linux 3.2.0-58-virtual x86_64)
...
Last login: Wed Feb 26 19:10:01 2014 from 199.231.242.170
ubuntu@ip-10-254-159-140:~$
```

The first time you enter your EC2 instance, there is literally the barest-
minimum installed on it. You will have to install `Nginx` yourself, with `sudo apt-get install nginx`.

You may also need to run `sudo apt-get update` if nginx does not install correctly.

The `sites-available` directory will hold individual site configuration for
**all** sites that **might** be available on a server.


```bash
ubuntu@ip-10-254-159-140:~$ ls /etc/nginx/sites-available/
default
ubuntu@ip-10-254-159-140:~$ more /etc/nginx/sites-available/default
# You may add here your
# server {
#   ...
# }
# statements for each of your virtual hosts to this file
...

ubuntu@ip-10-254-159-140:~$
```

**Active** site configuration is listed in the ` /etc/nginx/sites-enabled`:


```bash
ubuntu@ip-10-254-159-140:~$ ls /etc/nginx/sites-enabled/
default
ubuntu@ip-10-254-159-140:~$ ls -l /etc/nginx/sites-enabled/
total 0
lrwxrwxrwx 1 root root 34 Feb 26 19:09 default -> /etc/nginx/sites-available/default
ubuntu@ip-10-254-159-140:~$
```

Notice that in fact, although `default` is in that directory too, it’s
actually a soft link to the file in `sites-available`.

Let’s move aside the existing `default` config by renaming it and replace it
with a simple one of our own.

On your local machine, in the `wsgiapp` directory, make a new file
`simple_nginx_config`. No file format extension is necessary.

Open that file in your editor and add the following:


```
# in simple_nginx_config

server {
    listen 80;
    server_name ec2-54-184-162-20.us-west-2.compute.amazonaws.com; # replace with the DNS of your instance
    access_log  /var/log/nginx/test.log;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Now, copy that file up to your server too with `scp`:


```bash
(ENV)$ scp -i ~/.ssh/pk-cpe.pem simple_nginx_config ubuntu@ec2-54-184-162-20.us-west-2.compute.amazonaws.com:~/
simple_nginx_config                           100%  363     0.4KB/s   00:00
(ENV)$
```

Next, on the server, move the original default configuration file aside and
put your new one in its place:


```bash
ubuntu@ip-10-254-159-140:~$ ls
myapp.py  simple_nginx_config
ubuntu@ip-10-254-159-140:~$ sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.orig
ubuntu@ip-10-254-159-140:~$ sudo mv simple_nginx_config /etc/nginx/sites-available/default
ubuntu@ip-10-254-159-140:~$ ls -l /etc/nginx/sites-enabled/
total 0
lrwxrwxrwx 1 root root 34 Feb 26 19:09 default -> /etc/nginx/sites-available/default
ubuntu@ip-10-254-159-140:~$
```

Once that’s complete, you can restart nginx to have it pick up your changes.
Note, if you alter the nginx configuration file `default`, you _must_ restart
the nginx service in order to see any changes:


```bash
ubuntu@ip-10-254-159-140:~$ sudo service nginx restart
...
ubuntu@ip-10-254-159-140:~$
```

If you now try to load the public DNS name for your EC2 instance, you’ll see
that nginx has updated and is now throwing an error: **502 Bad Gateway**

The `502 Bad Gateway` error means “I am a proxy set up to receive requests at
this URL, but the thing I’m proxying to is either not running at all, or not
running at the URL/port I was told!”

### Running a WSGI Server

Let’s make our wsgi app run, so we can fix that.

On your server, run the wsgi app:


```bash
ubuntu@ip-10-254-159-140:~$ python myapp.py
```

And now reload your web browser and verify that you can see “Hello, World!”

## Automation

The steps we took above allowed us to upload an application and some
configuration to our server, apply the configuration to the `nginx` web server
we installed, and then run our WSGI application in a terminal to get a
response via public DNS.

Your task is to repeat this process for homework with a different WSGI
application. Later, we’ll learn how to automate this task using configuration
management tools.

