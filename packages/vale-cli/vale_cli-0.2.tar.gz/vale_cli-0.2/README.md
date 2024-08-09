# Vale CLI Python Wrapper

[Vale](https://vale.sh/) is an open-source, command-line tool for validating
content based on editorial style rules. This package acts as a basic wrapper to
pass text to Vale and return styles rules that you can use in your Python
projects.

## Installation

**NOTE: This package only acts as a wrapper for using Vale and does not install
Vale. Make sure you install and configure Vale before using this package.**

Add `vale-cli` package as a dependency in your `requirements.txt` file:

```shell
vale-cli
```

## Usage

Example usage:

```python
import vale_cli.vale_config as vale_config

release_note = "An error with the WhizBang API caused incorrect processing of data, which stopped you from using certain routes in the API. This fix corrects the logic around data processing. You can now process data without errors."
vale = vale_config.ValeConfig("/path/to/.vale.ini")
output = vale.check_text(release_note, ext='.adoc')
print(output)
```

Output:

```shell
[{'Action': {'Name': '', 'Params': None}, 'Span': [19, 26], 'Check': 'RedHat.PascalCamelCase', 'Description': '', 'Link': 'https://redhat-documentation.github.io/asciidoc-markup-conventions', 'Message': "Consider wrapping this Pascal or Camel case term ('WhizBang') in backticks.", 'Severity': 'suggestion', 'Match': 'WhizBang', 'Line': 1}, {'Action': {'Name': 'replace', 'Params': ['wrong']}, 'Span': [39, 47], 'Check': 'RedHat.SimpleWords', 'Description': '', 'Link': 'https://redhat-documentation.github.io/vale-at-red-hat/docs/main/reference-guide/simplewords/', 'Message': "Use simple language. Consider using 'wrong' rather than 'incorrect'.", 'Severity': 'suggestion', 'Match': 'incorrect', 'Line': 1}]
```
