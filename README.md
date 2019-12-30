# Flake8 Rules

Documentation and examples for the rules in [Flake8](http://flake8.pycqa.org/en/latest/index.html) ([pyflakes](https://github.com/PyCQA/pyflakes), [pycodestyle](http://pycodestyle.pycqa.org/en/latest/), and [mccabe](https://github.com/pycqa/mccabe)).

## API

Flake8 Rules includes simple API with two endpoints.

### Retrieve a single rule

This endpoints returns a single Flake8 rule.

**Heads up:** This endpoint returns JSON content but the Content-Type is set to `text/html`. This is due to Jekyll's inability to generate files with permalinks that end in `.json`.

```
$ curl https://flake8rules.com/api/rules/E111/
{
    "code": "E111",
    "message": "Indentation is not a multiple of four",
    "content": "The rendered HTML content",
    "links": ["https://www.python.org/dev/peps/pep-0008/#indentation"]
}
```

* `code` - The 4 character Flake8 issue code.
* `message` - A short message describing the issue.
* `content` - The fully rendered HTML content describing the issue and how to fix it.
* `links` - A list of additional links to visit for more information.

### Retrieve a list of all rules

This endpoint returns a list of all Flake8 rules.

```
$ curl https://flake8rules.com/api/rules.json
[
    {
        "code": "F812",
        "message": "List comprehension redefines name from line n",
        "content": "The rendered HTML content",
        "links": ["https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions"]
    }
]
```

## Contributing

All rules go in the `_rules` directory. They should be named with their 4 character code, like `E301.md`.

To run the jekyll development server first [install Jekyll](https://jekyllrb.com/docs/installation/). Then run the following:

```
$ bundle exec jekyll serve
```
