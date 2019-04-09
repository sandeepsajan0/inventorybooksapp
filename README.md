# BookStore

It is a public web portal implemented using Python/Django(MVT structure).

It contains the list of book and also have information about its copies and book info link provided by Google Book Api. Anybody can access it, there is no need to login or authenticate(for now).
  


## Features

1. User can add a book or also copy of a existing book to the bookstore.

2. User can also remove or delete the book from the bookstore.

3. User can also get the information about the book on clicking on its title.

4. There is also a search box which shows the books with the help of Google Book Api for the given query.

5. Searched books have indication on their bottom, weather it is already exist in bookstore or not.

6. For existing books, user can add or remove a copy from bookstore and for non-existing books, user can add this book to the bookstore. 

7. User also able to see the copies of a book and ID of book provided by Google Book Api.

### Assumption

In start bookstore have no book. User can add books to the bookstore via search box.

Book will not be shown if there is no copy(0) of that book(out of stock).

Using Python3.

### Installation

Create a virtual environment.

Clone the repo:

`git clone https://github.com/sandeepsajan0/inventorybooksapp.git`

Install all requirements:

`pip3 install -r requirements.txt`

You have to configure database for run server locally:

In `bookstore/settings.py`
uncomment

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}`

and comment
`DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)`

Now you need to migrate the database:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

Now you can run the sever:

`python3 manage.py runserver`

hurray! you app is running on: http://127.0.0.1:8000/

**Live Demo**

It is live on heroku. https://inventorybooksapp.herokuapp.com/
