#!/usr/bin/env python
"""
A little script to generate our rules from a JSON dump of the Lintly issues table.
"""
import json
import os
import shutil

RULES_DIRECTORY = '_rules'

FILE_TEMPLATE = """---
layout: rule
code: {code}
message: "{message}"
title: "{message} ({code})"{links_section}
---

{explanation}
"""

rules = None
with open('issues.json') as f:
    rules = json.load(f)

if os.path.exists(RULES_DIRECTORY):
    shutil.rmtree(RULES_DIRECTORY)
os.mkdir(RULES_DIRECTORY)

for rule_obj in rules:
    rule = rule_obj['fields']

    links_section = ''
    if rule['documentation']:
        links_section = """
links:
  - {documentation}""".format(documentation=rule['documentation'])

    file_contents = FILE_TEMPLATE.format(
        message=rule['message'].capitalize(),
        code=rule['code'],
        explanation=rule['explanation'],
        links_section=links_section
    )

    with open(RULES_DIRECTORY + '/{}.md'.format(rule['code']), 'w') as f:
        f.write(file_contents)
