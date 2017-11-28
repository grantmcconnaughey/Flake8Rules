# Flake8 Rules

Documentation and examples for the rules in [Flake8](http://flake8.pycqa.org/en/latest/index.html) ([pyflakes](https://github.com/PyCQA/pyflakes), [pycodestyle](http://pycodestyle.pycqa.org/en/latest/), and [mccabe](https://github.com/pycqa/mccabe)).

## API

Flake8 Rules includes an API that returns individual rules. You can access the API at `https://lintlyci.github.io/Flake8Rules/rules/{rule code}.json`.

```
$ curl https://lintlyci.github.io/Flake8Rules/rules/E101.json
{
    "code": "E101",
    "content": "The unrendered Markdown content",
    "links": [
        "https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces"
    ],
    "message": "Indentation contains mixed spaces and tabs"
}
```

* `code` - The 4 character Flake8 issue code.
* `message` - A short message describing the issue.
* `content` - The unrendered Markdown content describing the issue and how to fix it.
* `links` - A list of additional links to visit for more information.

## Contributing

All rules go in the `_rules` directory. They should be named with their 4 character code, like `E301.md`.

To run the jekyll development server, run the following:

```
$ bundle exec jekyll serve
```
