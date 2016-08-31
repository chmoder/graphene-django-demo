Graphene Django Traffic Violaitons Demo
===============================

This simple demo explores how to build, import, and query data using graphene
and Django.

Data is a subset of https://catalog.data.gov/dataset/traffic-violations-56dda

Getting started
---------------

First you'll need to get the source of the project. Do this by cloning the
 repository:

```bash
# Get the example project code
git clone https://github.com/chmoder/graphene-django-demo.git
cd graphene-django-demo
```

It is good idea (but not required) to create a virtual environment
for this project. We'll do this using
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
to keep things simple,
but you may also find something like
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
to be useful:

```bash
# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate
```

```bash
# uncompress our JSON data
virtualenv env
source env/bin/activate
tar -xvvf traffic_violations.json.tar.gz
```

Now we can install our dependencies:

```bash
pip install -r requirements.txt
```

Now setup our database:

```bash
# Setup the database
./manage.py migrate

# Load some example data
./manage.py loaddata traffic_violations.json

# Create an admin user (useful for logging into the admin UI
# at http://127.0.0.1:8000/admin)
./manage.py createsuperuser
```

Now you should be ready to start the server:

```bash
./manage.py runserver
```

Now head on over to
[http://127.0.0.1:8000/graphiql](http://127.0.0.1:8000/graphiql)
and run some queries!
```
query{
  allViolations(description_Icontains:"identification"){
    edges {
      node {
        date,
        time,
        description
      }
    }
  }
}

```
