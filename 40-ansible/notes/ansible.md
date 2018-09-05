# Automated Deployment with Ansible

Prior to today we’ve been able to deploy simple web apps to Amazon Web
Services. However, every time we do, it’s a process. Any step that we miss can
be detrimental and break our deployment. We may not even always remember which
steps to take.

It’s easier while it’s fresh in our minds, but what about 6 weeks from now?
How about in 6 months? Let’s take that responsibility off of our mental load
and automate the process.

## A Note about Continuous Delivery and Dev Ops

**Continuous Delivery** or **CD** is the concept of being able to immediately
deliver changes to production. This separates the developer from the direct
handling of the deployment process, allowing them to push a button and “make
it so”. It’s oftentimes used as a synonym for **continuous deployment** ,
which ensures that changes have passed quality assurance tests.

These two, along with **continuous integration** ( **CI** ), start to push
developers into the realm of **Developer Operations** , or **DevOps**. DevOps
engineers spend time focusing on the process for product delivery. They are
the bridge between the software developers who write the production code, and
other IT professionals that make sure the code can actually run in production.
Amongst other tools, DevOps engineers use resources like **Ansible** and
**Docker** to package and deliver software for the production environment.

## Introduction to Ansible

**Ansible** is a configuration management tool written in Python that, in
short, executes a given series of commands on remote machines over
[SSH](http://searchsecurity.techtarget.com/definition/Secure-Shell). While
actual usage can get more fancy than that, it is at base a package that runs
through a command list, executing those commands wherever it is pointed. We’ll
be using Ansible to make deployment easier for us, so that we Developers can
focus less on the needs of AWS (or wherever we deploy), and more on the code
we write.

### Installation

As with most publicly-available Python packages, you can install Ansible with
`pip`. However, **unlike most packages it is only currently available for
Python 2.6 and 2.7**. It also does not like virtual environments (yet).

So, **outside of any environment** , use your system-level `pip` to install
ansible.

    
```sh
$ pip install ansible
```

Upon install, ansible will provide you with _several_ new console scripts:

  * ` ansible`
  * `ansible-console`
  * `ansible-doc`
  * `ansible-galaxy`
  * `ansible-playbook`
  * `ansible-pull`
  * `ansible-vault`

We’ll be chiefly concerned with `ansible`, `ansible-playbook`, and slightly
with `ansible-galaxy`. While ansible itself doesn’t like to be installed
within a Python 3 virtual environment, once it’s installed at the system level
you can use the console scripts anywhere.

Ansible can also be installed and run from a remote server, but we’ll only
need to work with it on our local machines.

Now that we have ansible installed, let’s create a new working directory and
environment for experimenting with it.

    
```sh
$ mkdir ansible-test
$ cd ansible-test
$ python3 -m venv ENV
$ source ENV/bin/activate
(ENV) $
```

### The Simplest Runs

Whenever you run ansible, you run it against a series of servers. At this
point, because we haven’t created a `hosts` file, ansible will look in
`/etc/ansible/hosts` for a list of servers to run commands against.

Chances are you don’t have a file there yet, so let’s make one. To start,
let’s have ansible talk to and execute commands on your local machine.

    
```sh
(ENV) $ echo 127.0.0.1 ansible_connection=local > hosts
(ENV) $ mv hosts /etc/ansible/
```

And now you can run your first ansible command.

`ping` will attempt to contact every host listed, and return a “success”
message when it’s successful. We can use `ping` by typing the following:

    
```sh
(ENV) $ ansible all -m ping
127.0.0.1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

We can use the `-a` flag to run a live command on each server

    
```
(ENV) $ ansible all -a "pwd"
127.0.0.1 | SUCCESS | rc=0 >>
/Users/Nick
```

### Local Host (not “localhost”) Inventory List

You may not want to use the host list at `/etc/ansible/hosts`. You may instead
have a local list of servers you want to run commands against. For this you
create an **inventory** file called ` hosts`, and within that list the servers
you want to run commands against. It’ll end up looking exactly like what we
put into `/etc/ansible/hosts`

    
```ini
# inside hosts
127.0.0.1
```

We can run ansible using this inventory file with the `-i` flag.

    
```sh
(ENV) $ ansible -i hosts all -a "pwd"
127.0.0.1 | SUCCESS | rc=0 >>
/Users/Nick
```

Now we haven’t come all this way just to run commands against `localhost`.
We’ve each provisioned our own AWS EC2 Ubuntu instances, complete with private
keys that we’ve saved to the `~/.ssh/` directory. Let’s put those to use.

Log into your AWS EC2 console and get the Public IP for your instance. The
examples that follow will use one of my own.

In the `hosts` file we just made, put the public IP for your instance.

    
```ini
# inside hosts
127.0.0.1
35.165.212.243
```

If we try to run ansible as is, it will fail.

    
```sh
(ENV) $ ansible -i hosts all -a "pwd"
35.165.212.243 | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh.",
    "unreachable": true
}
127.0.0.1 | SUCCESS | rc=0 >>
/Users/Nick
```

Why did it fail? Remember that ansible tries to reach different servers over
SSH. For our AWS EC2 instances, we need two things in order to reach that
remote address:

  * The remote user
  * The AWS private key

We haven’t yet provided these, and so we fail to connect over ssh. We can add
these in by specifying the `ansible_ssh_user` and
`ansible_ssh_private_key_file` **host variables** in the ` hosts` file.
Because the “user” that we use to ssh into AWS is `ubuntu`, we set that as our
`ansible_ssh_user`. Our private key file was provided to us once (and only
once) by AWS and should have been saved somewhere consistent like the
`~/.ssh/` directory. Let’s use this knowledge to properly set up our `hosts`
file.

    
```ini
# inside hosts
127.0.0.1 ansible_connection=local
35.165.212.243 ansible_ssh_user=ubuntu ansible_ssh_private_key_file=~/.ssh/pk-aws.pem
```

Now when we run that same ansible command, it’ll run `pwd` on our local
machine as well as on our remote AWS server.

    
```sh
(ENV) $ ansible -i hosts all -a "pwd"
127.0.0.1 | SUCCESS | rc=0 >>
/Users/Nick

35.165.212.243 | SUCCESS | rc=0 >>
/home/ubuntu
```

If we have multiple hosts that all use the same variables, or have multiple
hosts that we want to run a given set of commands against, we can create
**host groups**. You can name these groups more-or-less whatever you want, as
long as you encase the name in square brackets (INI style).

    
```ini
# inside hosts
[us-west-2]
35.165.212.243

[us-west-2:vars]
ansible_ssh_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/pk-aws.pem
```

## Ansible Playbooks

Being able to run individual commands like `pwd` or `ping` is all well and
good, but not very useful in the long run. We use the “ansible” tool to
automate a whole series of actions. That’s it’s purpose. To get a series of
commands to run, we use a **playbook**.

Every playbook that you write will be in [YAML
style](http://docs.ansible.com/ansible/YAMLSyntax.html), with the `.yml` file
format. It ends up just being a bunch of key-value pairs, specifying the
various parameters you need to run ansible. Dashes set up a list-like object,
and indentation levels dictate structure.

Start by creating a `playbooks` directory. Adding to it your first playbook
`sample_playbook.yml`, with a list of one element.

    
```yml
# inside sample_playbook.yml
---
- hosts: us-west-2
  remote_user: ubuntu
```

We specify which hosts we want to run commands against. We can use individual
hosts, or we can use host group names. Either way, we can have one or many.
Above I’m using the `us-west-2` group name. I also specify the `remote_user`
that we will be logged in as.

What we’ve begun above is the first item in a list of **plays**. Each **play**
targets a set of hosts, and runs commands on that host. This we’ll use just
one play, which will consist of multiple **tasks**. Let’s hear about these
next.

### Tasks

Tasks are as they sound–actions for ansible to perform on the remote host.
Previously we used the `ansible` command-line script to just do one thing. Now
we’ll use a playbook to do multiple things.

Tasks come as a list in order from top to bottom, and are always run in order.
If for any reason a task is unsuccessful, ansible will throw an error and stop
the play.

Tasks should start with a `name`. This `name` can be just about whatever you
want, but should be descriptive of the task being executed.

**Modules** actually execute the tasks. There are [a wide array of
modules](http://docs.ansible.com/ansible/modules_by_category.html) baked in to
ansible. However if you don’t see one or know of one that’s useful for your
specific task, you can use the ` command` module. It’ll run the `bash` command
as you write it.

Let’s write our first task. In `playbooks/sample_playbook.yml`, have the
following code.

    
```yml
# inside sample_playbook.yml
---
- hosts: us-west-2
  remote_user: ubuntu
  tasks:
    - name: Run the "ls -a" command to see what's in the home directory
      command: ls -a
```

To run playbooks we use the `ansible-playbook` console script. Just like the
bare `ansible` command, we use our local list of hosts with the `-i` flag. We
point the `ansible-playbook` script at the `sample_playbook.yml` file we just
edited. When we run `ansible-playbook`, it should look something like this
(but with color).

    
```sh
(ENV) $ ansible-playbook -i hosts playbooks/sample_playbook.yml

PLAY [us-west-2] ***************************************************************

TASK [setup] *******************************************************************
ok: [35.165.212.243]

TASK [Run the ls command] ******************************************************
changed: [35.165.212.243]

PLAY RECAP *********************************************************************
35.165.212.243             : ok=2    changed=1    unreachable=0    failed=0
```

When a playbook is run, ansible first checks to see that it can contact the
host. After setting up a connection to the host, it runs the tasks that we’ve
set out. Here it ran the `ls` command, though as we’ve run the script above we
don’t see the output. When the playbook is finished, it gives you a summary of
what was done. Every time something was changed on the remote host, the status
after the command was run is `changed`, etc.

If we want the actual output from the `ls -a` command we ran on our remote
host, we need to change how verbose our output is with the `-v` flag. This
flag is entirely optional. `-v` is the first level of verbosity, `-vv` is a
little more verbose, and `-vvv` is very verbose, telling you everything that
ansible is doing (whether you want that info or not).

Run the `ansible-playbook` command with `-v` and check the output.

    
```sh
(ENV) $ ansible-playbook -i hosts playbooks/sample_playbook.yml -v
No config file found; using defaults

PLAY [us-west-2] ***************************************************************

TASK [setup] *******************************************************************
ok: [35.165.212.243]

TASK [Run the ls command] ******************************************************
changed: [35.165.212.243] => {"changed": true, "cmd": ["ls", "-a"], "delta": "0:00:00.001853", "end": "2016-12-28 06:51:35.633423", "rc": 0, "start": "2016-12-28 06:51:35.631570", "stderr": "", "stdout": ".\n..\n.ansible\n.bash_history\n.bash_logout\n.bashrc\nbookapp\n.cache\nmyapp.py\n.pip\n.profile\n.python_history\n.ssh", "stdout_lines": [".", "..", ".ansible", ".bash_history", ".bash_logout", ".bashrc", "bookapp", ".cache", "myapp.py", ".pip", ".profile", ".python_history", ".ssh"], "warnings": []}

PLAY RECAP *********************************************************************
35.165.212.243             : ok=2    changed=1    unreachable=0    failed=0
```

Here, ansible ran the `ls -a` command and the output is captured in
`stdout_lines` as a list. Your output will look different than mine above, but
we’ll fix that in a bit.

#### apt Module and Looping

During the manual deployment, one of the first things needing to be done was
an update of the Ubuntu system. This was accomplished with `sudo apt-get
update`. We don’t need to run the bare bash command to use `apt-get` though,
we can use ansible’s own `apt` module.

The [apt module](http://docs.ansible.com/ansible/apt_module.html) accesses the
`apt` package manager on the Ubuntu system. To update the system, we can pass
in the `update_cache=yes` parameter. Finally, because we need to do this as
the “superuser”, we need ansible to become the superuser and execute the
command.

    
```yml
# inside sample_playbook.yml
---
- hosts: us-west-2
  remote_user: ubuntu
  tasks:
    - name: Update the Ubuntu system and services
      apt: update_cache=yes
      become: yes
      become_method: sudo
```
    
```sh
(ENV) $ ansible-playbook -i hosts playbooks/sample_playbook.yml -v
No config file found; using defaults

PLAY [us-west-2] ***************************************************************

TASK [setup] *******************************************************************
ok: [35.165.212.243]

TASK [Update the Ubuntu system and services] ***********************************
ok: [35.165.212.243] => {"cache_update_time": 1482908590, "cache_updated": true, "changed": false}

PLAY RECAP *********************************************************************
35.165.212.243             : ok=2    changed=0    unreachable=0    failed=0
```

If `sudo apt-get update` has already been run, then nothing will change. The
system above was already updated, so even though the command was run there was
nothing to change. In general, ansible commands are **idempotent** , where
**they won’t change the state of the system if the intended state has already
been reached**.

If we’re working with a fresh system, we need to install a number of other
services in order to get our site up and running:

  * nginx
  * python3
  * python3-pip
  * python3.4-venv
  * git
  * gunicorn

We could get each individual one with a series of tasks that run `sudo apt-get install <service>`.

    
```yml
# inside sample_playbook.yml
---
- hosts: us-west-2
  remote_user: ubuntu
  tasks:
    - name: Update the Ubuntu system and services
      apt: update_cache=yes
      become: yes
      become_method: sudo

    - name: Install Nginx
      apt: name=nginx state=latest
      become: yes
      become_method: sudo

    - name: Install Python 3
      apt: name=python3 state=latest
      become: yes
      become_method: sudo

    - name: Install pip for Python 3
      apt: name=python3-pip state=latest
      become: yes
      become_method: sudo

    ... and on and on
```

However, we could be better programmers and keep even this playbook DRY.
First, since we know we’re going to become the superuser a lot, we could just
run every command as the superuser.

    
```yml
# inside sample_playbook.yml
---
- hosts: us-west-2
  remote_user: ubuntu
  become: yes
  become_method: sudo
  tasks: # and now list the tasks out as before
```

I tend to not do the above, as I only like using `sudo` when I absolutely need
it. However it’s justifiable here, as we’re managing packages, editing config
files, etc.

Second, we can use a variable whose value will be the name of each package. We
can then list out the packages we want to install within that task.

    
```yml
# inside sample_playbook.yml
---
- hosts: us-west-2
  remote_user: ubuntu
  tasks:
    - name: Update the Ubuntu system and services
      apt: update_cache=yes
      become: yes
      become_method: sudo

    - name: Install Basic Unix-level Services
      apt: name={{ item }} state=latest
      become: yes
      become_method: sudo
      with_items:
        - nginx
        - python3
        - python3-pip
        - python3.4-venv
        - git
        - gunicorn
```

The above task will loop through the given items and put each in the place of
“item”. Ansible uses Jinja2-style templating for declaring variables. We’ll
see more of this later.

If each item was a list of values, then we’d use `{{ item[0] }}`, `{{ item[1]
}}`, etc. to get every element. If instead every item was a dictionary, then
we’d use `{{ item.key1 }}`, `{{ item.key2 }}`, etc. to get the value of every
key-value pair.

When the playbook is run in the command line with the “verbose” flag we get a
bunch of output. Like...a ton, so be careful.

    
```sh
(ENV) $ ansible-playbook -i hosts playbooks/sample_playbook.yml

PLAY [us-west-2] ***************************************************************

TASK [setup] *******************************************************************
ok: [35.165.212.243]

TASK [Update the Ubuntu system and services] ***********************************
ok: [35.165.212.243]

TASK [Install Basic Unix-level Services] ***************************************
changed: [35.165.212.243] => (item=[u'nginx', u'python3', u'python3-pip', u'python3.4-venv', u'git', u'gunicorn'])

PLAY RECAP *********************************************************************
35.165.212.243             : ok=3    changed=1    unreachable=0    failed=0
```

#### The git Module

We can use the [git module](http://docs.ansible.com/ansible/git_module.html)
to clone an app onto our remote system like we would any other computer. We
provide `git` with the repo url as well as the path to where this repository
should be cloned.

We’re going to use [this simple book app](https://github.com/cewing/simple-
bookapp) as our example application. We’ll clone it into our “home” directory
and just call it “bookapp”. To do this, we’ll add the following task

    
```yml
# at the bottom of sample_playbook.yml
- name: Clone the Book App to the Home Directory
  git: clone=yes repo=https://github.com/cewing/simple-bookapp.git dest=/home/ubuntu/bookapp
```

Be aware that when ansible sees `~`, it uses it to mean `/root`. We shouldn’t
be working in the `/root` directory, so make sure to provide the path to the
home directory on your instance.

Note

“git” is entirely independent of the “GitHub” company. It is just the
commonly-used version control system, and exists in multiple forms. As long as
you have the URL to a remote repository, whether it’s on GitHub, BitBucket,
GitLab, etc., you can clone a remote repository.

Now we rerun our playbook.

    
```sh
(ENV) $ ansible-playbook -i hosts playbooks/sample_playbook.yml -v

# all the old output

TASK [Clone the Book App to the Home Directory] ********************************
changed: [35.165.212.243] => {"after": "79bda0988147d88d25217a46b361742e29ea6a92", "before": null, "changed": true, "warnings": []}

PLAY RECAP *********************************************************************
35.165.212.243             : ok=4    changed=1    unreachable=0    failed=0
```

#### Virtual Environments and The pip Module

As we do on our local machines we can do our Python work in a virtual
environment. We have to, of course, make one first.

We can use the `command` module to run our classic virtual environment
creation.

    
```yml
# at the bottom of sample_playbook.yml
- name: Create a virtual environment in the book app repo
  command: python3 -m venv /home/ubuntu/bookapp
  become: yes
  become_method: sudo
```

Then we can use `pip` to install the `gunicorn` Python package, as well as
this individual `bookapp` package. Instead of using pip from the command line,
we can use ansible’s `pip` module.

`pip` will at the very least take the `name` parameter. The value attached to
this parameter needs to be the name of an installable package from the Python
Package Index, or the path to a local distribution.

As an option you can provide the path to an existing virtual environment. What
qualifies is a directory containing the `bin` and `lib` directories. Above we
created a virtual environment in our `bookapp` repo so we can use that one.

    
```yml
# at the bottom of sample_playbook.yml
- name: Install gunicorn to the virtualenv
  pip: virtualenv=/home/ubuntu/bookapp name=gunicorn
  become: yes
  become_method: sudo

- name: Install bookapp to the virtualenv
  pip: virtualenv=/home/ubuntu/bookapp name=/home/ubuntu/bookapp/ extra_args="-e"
  become: yes
  become_method: sudo
```

Rerun the playbook using the verbose flag and see that these tasks ran
successfully.

## Templates and Configuring Nginx

During our manual deployment we had to perform several steps to get Nginx up
and running. Let’s do that with ansible.

Recall that on a fresh system, there’s a file called `default` within the
`/etc/nginx/sites-available` directory. This file is what the `nginx` service
uses to set up a proxy server to stand between your web app and the internet.

We can use ansible to change that file’s name so that we can use the `default`
name for our own Nginx configuration.

    
```yml
- name: Rename old default file
  command: mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.old
  become: yes
  become_method: sudo
```

However, this comes with a problem. This task is not idempotent. This means
that if we try to run our playbook again, we’ll get the following failure
message

    
```sh
TASK [Rename old default file] ***************************************************
fatal: [35.165.212.243]: FAILED! => {"changed": true, "cmd": ["mv", "/etc/nginx/sites-available/default", "/etc/nginx/sites-available/default.old"], "delta": "0:00:00.002064", "end": "2016-12-28 21:52:38.818380", "failed": true, "rc": 1, "start": "2016-12-28 21:52:38.816316", "stderr": "mv: cannot stat ‘/etc/nginx/sites-available/default’: No such file or directory", "stdout": "", "stdout_lines": [], "warnings": []}
```

We need to be able to make different decisions about what to do based on the
existence or nonexistence of a file.

### File Status

Ansible allows us to create tasks that simply look for files and register
their statuses. These tasks use the [stat
module](http://docs.ansible.com/ansible/stat_module.html), and we can register
that status as an in-playbook variable.

The `stat` module will tell you whether or not a file exists, how large that
file is, whether or not it’s executable, readable, writeable, whether or not
it’s a directory, and a host of other information.

We can use that information as the basis for our decision-making.

Write this next task above the previous task that changes the `default` file’s
name.

    
```yml
- name: Register the old default file
  stat: path=/etc/nginx/sites-available/default.old
  register: default_stat
```

We register the result of this task as `default_stat`. We can now use this
result in the name-change task.

### Conditionals

Conditional statements in ansible aren’t their own standalone tasks. They come
in as conditions on other tasks. It reads a little like english: “Do <task
name> **when** <condition>”.

We add a condition to our renaming task using the `when` statement.

    
```yml
- name: Rename old default file if a copy doesn't already exist
  command: mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.old
  become: yes
  become_method: sudo
  when: not default_stat.stat.exists # <-- this is the only line that should be added.
```

Our conditionals should all be Python-like. That means you can do comparisons
with `=, <, >` and take negation. You can check if conditions are `True` or
not, etc.

The `.exists` attribute on the `stat` result simply returns a boolean; `True`
if the path given exists and `False` if it doesn’t. The above task then only
runs if the condition is met (`default.old` exists, so there is no `default`
file to move).

We can now run our playbook as many times as we like, safe in the knowledge
that if the system is fresh we make the appropriate change, and if the system
has already been altered then the change isn’t even considered.

Indeed, when our playbook is run, we see the following lines

    
```sh
TASK [Register the old default file] *******************************************
ok: [35.165.212.243]

TASK [Rename old default file if a copy doesn\'t already exist] *****************
skipping: [35.165.212.243]
```

### Ansible Templates

At this step in our process, we need to copy over our new `default` file to
use for Nginx’s configuration. Now, we could always just include this file
with our package and move it to a new location after we clone. However a
problem arises, because certain values will need to change depending upon the
system being used.

Even for our simplest setup, we have to tie the `server_name` attribute to the
name of the actual server we’re using. If we want a different `proxy_pass` for
a given machine, we have to change that too. Maybe we want to serve over HTTP
on some machines and HTTPS on others, meaning we’d have to change the port
that Nginx is listening on.

Instead of constantly conjuring up new variants of an existing file, we can
use a **template** file and fill in the necessary information as-needed.

Ansible’s templating system works off of Jinja2-style templates. Instead of
being tied strictly to HTML, ansible’s templates generate whatever type of
file you want as plain text. When it’s time for action, you can declare the
file type as well as the location for where this file is being placed in the
remote system.

To start, create a directory called `templates` at the same level as your
`playbooks` directory.

From our manual deployment, our `default` file for Nginx looked something like
this:

    
```
server {
    listen 80;
    server_name ec2-35-165-212-243.us-west-2.compute.amazonaws.com;
    access_log /var/log/nginx/test.log;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Here, we want to be able to change the `server_name` attribute to be whatever
we want.

Create a new file in your templates directory called `nginx_config.jinja2`.

Note

Ansible template files don’t necessarily have to have _any_ file format.
Adding one is more for your own comfortability than for the system.

Inside of `nginx_config.jinja2`, paste all of the same code from your
`default` file. On the `server_name` line, remove whatever server DNS you
provided and in its place write `{{ server_dns }}`. Your template should now
look like this:

    
```
server {
    listen 80;
    server_name {{ server_dns }};
    access_log /var/log/nginx/test.log;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

#### Variables

Now that we’ve created a space to be filled with a variable, we need to create
the variable.

Ansible variables can come from a variety of sources. You can set up variables
in your inventory file for each individual host, or for a group of hosts.
We’ve already done that by setting the `ansible_ssh_user` and
`ansible_ssh_private_key_file` variables.

Variables can be defined in the playbook itself at the top of the file, with
the same indentation level as `hosts`, `tasks`, and `remote_user`. The keyword
is `vars` and it might look like this:

    
```yml
- hosts: us-west-2
  remote_user: ubuntu
  vars:
    server_dns: ec2-35-165-212-243.us-west-2.compute.amazonaws.com
  tasks:
    # all the tasks
```

Variables can even be defined in entirely separate files and included in your
playbook. That is, however, a separate discussion and I leave you to [these
docs on playbook
roles](http://docs.ansible.com/ansible/playbooks_roles.html#roles).

I prefer to declare a variable for a simple playbook like ours in the
inventory file. So I declare the `server_dns` variable under the `[us-
west-2:vars]` heading:

    
```ini
[us-west-2]
35.165.212.243

[us-west-2:vars]
ansible_ssh_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/pk-aws.pem
server_dns=ec2-35-165-212-243.us-west-2.compute.amazonaws.com
```

Finally, with my template created and my variable to fill that template
declared, I can write a task that uses it. The [template
module](http://docs.ansible.com/ansible/template_module.html) handles the
filling and placing of templates on remote systems. It takes two required
parameters: `src` and `dest`, though you may decide you want to specify other
parameters depending on the type of file you’re trying to create.

The `src` parameter will take a path, either relative or absolute, to the
template file on our **local** machine. Ours is sitting in our ` templates`
directory at the relative path `../templates/nginx_config.jinja2`.

The `dest` parameter also takes a path, pointing to the spot on the **remote**
machine where we wish to place this new file, including its new file name. Our
` default` file belongs in `/etc/nginx/sites-available/`, so the full path
provided to `dest` will be `/etc/nginx/sites-available/default`.

Because the `/etc/` directory changes system configuration, a `sudo`-enabled
action is required. With all of the above in mind, our task will be

    
```yml
- name: Create a new default file for nginx
  template: src=../templates/nginx_config.jinja2 dest=/etc/nginx/sites-available/default
  become: yes
  become_method: sudo
```

Note that the above task is **not** conditional on whether or not there’s an
old ` default` file. It will overwrite whatever currently sits at that
destination path.

### Services

**Services** are effectively applications that the Unix system runs, and
aren’t necessarily associated with Python. We installed a list of services at
the start of this playbook, which included such useful items as ` git` and
`nginx`.

For many installed services, we often have to start the service up after it’s
been gathered. In order to interact with services that aren’t already built-in
to Ansible like Git, we need to use the [service
module](http://docs.ansible.com/ansible/service_module.html).

For our purposes, we’ll mostly use the `service` module to stop and start
services. During our manual deployment, we restarted Nginx after swapping out
the `default` file. We’ll have ansible do the same, giving it superuser status
so that it may change this service which operates at the system level.

    
```yml
- name: Restart nginx service
  service: name=nginx state=restarted
  become: yes
  become_method: sudo
```

## Getting Moving with Upstart and Gunicorn

After running the playbook to this point, we could ssh into our remote servers
and start our applications manually. But that’s undoubtedly foolish; we
shouldn’t need to maintain a constant connection in order for our app to work.

We tie the startup of our app to the startup of our server with `Upstart`. We
can get it going in a similar way to which we got Nginx going:

  * Create a template for our upstart configuration script
  * Copy the template over to the right location (which creates a service for the Unix system to manage)
  * Start up the new service we’ve created.

Our template `upstart_config` will be simple:

    
```
description "sample bookapp"

start on (filesystem)
stop on runlevel [016]

respawn
setuid nobody
setgid nogroup
chdir /home/ubuntu/bookapp/src/

exec /home/ubuntu/bookapp/bin/gunicorn -b :8080 bookapp:application
```

Notice no spots for variable substitution. There’s no need; nothing we’re
putting into this file is dependent upon the host system.

Our tasks will also be simple. One for copying the code over and naming it
`bookapp.conf`, and one for starting the new `bookapp` service.

**One**

    
```yml
 - name: Copy upstart script into /etc/init
   template: src=../templates/upstart_config dest=/etc/init/bookapp.conf
   become: yes
   become_method: sudo
```

**Two**

    
```yml
 - name: Restart the bookapp upstart job
   service: name=bookapp state=restarted
   become: yes
   become_method: sudo
```

Done.

## Wrapping Up

We now have a playbook that should work on any Ubuntu 14.04 system. We could
provision a new AWS EC2 instance right now and simply change the domain name,
gettin a new application up and running in moments. No need to memorize the
steps, no need to ssh and execute steps manually. One time is all you need.

We’ve gone through the basics of setting up an ansible playbook here, but
there’s so much more to the Ansible ecosystem. You’ll need to dive a bit
deeper for deploying your full Django application, so spend some time getting
cozy with the [Ansible documentation](http://docs.ansible.com/ansible/) and
Google, your bestest friend of all.

Finally, for this and other apps, many folks before you have sought to do the
types of things you want to do. Like with GitHub, there exists a place for
these people to store their playbooks and roles: [Ansible
Galaxy](https://galaxy.ansible.com/). Take time to check that out, especially
one of the roles that handles Nginx for you: [nginx search
results](https://galaxy.ansible.com/list#/roles?page=1&page_size=10&autocomplete=nginx).

