# Item Catalog Project

## Introduction
This project is meant to teach students the basics of CRUD operations with Flask, SQLAlchemy, Python etc. [Udacity Full Stack Nanodegree's](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) 

## Summary:
This project contains a web app called Item catalog which lets you add, edit and delete items that belong to certain Mario Kart Item categories. Google login is required in order to add, edit or delete items. 

## How to install:
- Download [Vagrant](https://www.vagrantup.com/), [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [extra files](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and download or clone this repository on you machine.
- Move the current directory to the shared vagrant directory.
- Start the virtual machine using `vagrant up` command.
- Run `vagrant ssh` to log in to your VM.
- To load the data, use the command `psql -d news -f newsdata.sql`.
- Once you have the data loaded into your database, connect to your database using `psql -d news`.

## How to run:
- Go to vagrant directory that contains project.py
- Run project.py file to start the web-app on port 5000.
- visit http://localhost:5000/categories/*/, with  * is equal to 1, 2 or 3.