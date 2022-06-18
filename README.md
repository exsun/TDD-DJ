# Test Driven Development in Django
> Try to Implement
<details>
  <summary>Basics</summary>

## Setup

initilize django virtual environment
```python
pip install pipenv
pipenv shell
```

install django & DRF 
```python
pipenv install django && djangorestframework
```

install DRF and add it to INSTALLED_APPS:
```python
pipenv install coverage
```

</details>

# Type Of Tests

* __Unit Test__ are isolated tests that test one specific function.  
* __Integration Tests__, meanwhile, are larger tests that focus on user behavior and testing entire applications. Put another way, integration testing combines different pieces of code functionality to make sure they behave correctly.

in general, tests result in either a Success (expected results), Failure (unexpected results), or an error. You not only need to test for expected results, but also how well your code handles unexpected results.

# Best practices

1.If it can break, it should be tested. This includes models, views, forms, templates, validators, and so forth.

2.Each test should generally only test one function.

3.Keep it simple. You do not want to have to write tests on top of other tests.

4.Run tests whenever code is PULLed or PUSHed from the repo and in the staging environment before PUSHing to production.

5.When upgrading to a newer version of Django:
  * upgrade locally,
  * run your test suite,
  * fix bugs,
  * PUSH to the repo and staging, and then
  * test again in staging before shipping the code

<details>
  <summary>Testing Models</summary>
## Setup
install coverage and add it to INSTALLED_APPS:
```python
pip install coverage==3.6
```

## Run Coverage  
```python
coverage run manage.py test movies -v 2

```
Build your report to see where testing should begin:
```python
coverage html
```
</details>

