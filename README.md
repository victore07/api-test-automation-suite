# API Test Automation Suite

This is a small API testing project I built to practice writing automated tests for REST endpoints using Python.

The goal was to keep the project simple, but still include the kinds of things I would expect to use in a real QA, support, or engineering workflow: reusable test code, positive and negative test cases, basic response validation, and CI through GitHub Actions.

## What this project does

This project tests a public REST API using pytest and requests.

The API used is JSONPlaceholder:

https://jsonplaceholder.typicode.com

I chose this API because it is simple, public, and easy to test without needing authentication or setup.

## Tools used

- Python
- pytest
- requests
- GitHub Actions
- REST API testing

## Project structure

```text
api-test-automation-suite/
    .github/
        workflows/
            tests.yml
    tests/
        test_negative_cases.py
        test_posts.py
        test_users.py
    utils/
        api_client.py
    requirements.txt
    README.md
```

## What I tested

The test suite covers a few basic API testing scenarios:

- getting a single user
- getting all users
- getting a single post
- getting all posts
- checking that expected fields exist in the response
- checking behavior for missing users and posts

This is not meant to be a huge test framework. It is meant to show that I can structure API tests clearly and automate them.

## How to run the tests locally

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
pytest -v
```

## Continuous integration

I added a GitHub Actions workflow so the tests run automatically on push and pull requests.

The workflow file is here:

```text
.github/workflows/tests.yml
```

## What I learned

This project helped me practice:

- organizing automated tests in a simple Python project
- writing positive and negative API tests
- validating status codes and response data
- setting up GitHub Actions for automated test runs