# Flake8 Rules

Documentation for the rules in Flake8, pyflakes, pycodestyle, and mccabe.e

## API

Flake8 Rules includes an API with a single endpoint. The endpoint returns a list of all Flake8 rules.

```
$ curl http://127.0.0.1:4000/rules.json
[
    {
        "code": "F812",
        "message": "List comprehension redefines name from line n",
        "content": "The rendered and escaped HTML content",
        "links": ["https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions"]
    }
]
```

* `code` - The 4 character Flake8 issue code.
* `message` - A short message describing the issue.
* `content` - The fully rendered HTML content describing the issue and how to fix it. The HTML is escaped.
* `links` - A list of additional links to visit for more information.
