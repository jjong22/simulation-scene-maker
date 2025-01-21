https://google.github.io/styleguide/pyguide.html

#### 2-1. `pylint` extension. 
-> find bug and style problems in Python source code.

#### 2-2. Imports
Use `import` statements for packages and modules only, not for individual types, classes, or functions.

#### 2.3 Packages
Import each module using the full pathname location of the module.

#### 2.4 Exceptions
Exceptions are allowed but must be used carefully.

#### 2.5 Mutable Global State
Avoid mutable global state.

#### 2.6 Nested/Local/Inner Classes and Functions
Nested local functions or classes are fine when used to close over a local variable. Inner classes are fine.

#### 2.7 Comprehensions & Generator Expressions
Okay to use for simple cases.

#### 2.8 Default Iterators and Operators
Use default iterators and operators for types that support them, like lists, dictionaries, and files.

#### 2.9 Generators
Use generators as needed.

#### 2.10 Lambda Functions
Okay for one-liners. Prefer generator expressions over map() or filter() with a lambda.

#### 2.11 Conditional Expressions
Okay for simple cases.

#### 2.12 Default Argument Values
Okay in most cases.

#### 2.13 Properties
Properties may be used to control getting or setting attributes that require trivial computations or logic. Property implementations must match the general expectations of regular attribute access: that they are cheap, straightforward, and unsurprising.

#### 2.14 True/False Evaluations
Use the “implicit” false if at all possible (with a few caveats).

`if foo is None` or `if foo is None`
Never use False with `==`. Use `if not x:`

#### 2.16 Lexical Scoping
Okay to use.

#### 2.17 Function and Method Decorators
Use decorators judiciously when there is a clear advantage. Avoid staticmethod and limit use of classmethod.

#### 2.18 Threading
Do not rely on the atomicity of built-in types.

While Python’s built-in data types such as dictionaries appear to have atomic operations, there are corner cases where they aren’t atomic (e.g. if __hash__ or __eq__ are implemented as Python methods) and their atomicity should not be relied upon. Neither should you rely on atomic variable assignment (since this in turn depends on dictionaries).

Use the queue module’s Queue data type as the preferred way to communicate data between threads. Otherwise, use the threading module and its locking primitives. Prefer condition variables and threading.Condition instead of using lower-level locks.

#### 2.19 Power Features
Avoid these features.

#### 2.20 Modern Python: from __future__ imports
New language version semantic changes may be gated behind a special future import to enable them on a per-file basis within earlier runtimes.

#### 2.21 Type Annotated Code
You can annotate Python code with type hints according to PEP-484, and type-check the code at build time with a type checking tool like pytype.

Type annotations can be in the source or in a stub pyi file. Whenever possible, annotations should be in the source. Use pyi files for third-party or extension modules.

https://peps.python.org/pep-0484/

## 3 Python Style Rules

#### 3.1 Semicolons
Do not terminate your lines with semicolons, and do not use semicolons to put two statements on the same line.

#### 3.2 Line length
Maximum line length is 80 characters.

Explicit exceptions to the 80 character limit:

* Long import statements.
* URLs, pathnames, or long flags in comments.
* Long string module-level constants not containing whitespace that would be inconvenient to split across lines such as URLs or pathnames.
    * Pylint disable comments. (e.g.: # pylint: disable=invalid-name)

#### 3.3 Parentheses
Use parentheses sparingly.

It is fine, though not required, to use parentheses around tuples. Do not use them in return statements or conditional statements unless using parentheses for implied line continuation or to indicate a tuple.

#### 3.4 Indentation
Indent your code blocks with 4 spaces.

Never use tabs. Implied line continuation should align wrapped elements vertically (see line length examples), or use a hanging 4-space indent. Closing (round, square or curly) brackets can be placed at the end of the expression, or on separate lines, but then should be indented the same as the line with the corresponding opening bracket.

#### 3.5 Blank Lines
Two blank lines between top-level definitions, be they function or class definitions. One blank line between method definitions and between the docstring of a class and the first method. No blank line following a def line. Use single blank lines as you judge appropriate within functions or methods.

Blank lines need not be anchored to the definition. For example, related comments immediately preceding function, class, and method definitions can make sense. Consider if your comment might be more useful as part of the docstring.

#### 3.6 Whitespace
Follow standard typographic rules for the use of spaces around punctuation.

No whitespace inside parentheses, brackets or braces.

#### 3.7 Shebang Line
Most .py files do not need to start with a #! line. Start the main file of a program with #!/usr/bin/env python3 (to support virtualenvs) or #!/usr/bin/python3 per PEP-394.

This line is used by the kernel to find the Python interpreter, but is ignored by Python when importing modules. It is only necessary on a file intended to be executed directly.

#### 3.8 Comments and Docstrings
Be sure to use the right style for module, function, method docstrings and inline comments.

## Google style comment

Files should start with a docstring describing the contents and usage of the module.

```py
"""
A one-line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```

```py
"""This blaze test uses golden files.

You can update those files by running
`blaze run //foo/bar:foo_test -- --update_golden_files` from the `google3`
directory.
"""
```

```py
"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second parma.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.

"""
```

#### Classes
```py
class SampleClass:
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam: bool = False):
        """Initializes the instance based on spam preference.

        Args:
          likes_spam: Defines if instance exhibits this preference.
        """
        self.likes_spam = likes_spam
        self.eggs = 0

    @property
    def butter_sticks(self) -> int:
        """The number of butter sticks we have."""
```

#### 3.10 Strings
Use an f-string, the % operator, or the format method for formatting strings, even when the parameters are all strings. Use your best judgment to decide between string formatting options. A single join with + is okay but do not format with +.

#### 3.11 Files, Sockets, and similar Stateful Resources
Explicitly close files and sockets when done with them. This rule naturally extends to closeable resources that internally use sockets, such as database connections, and also other resources that need to be closed down in a similar fashion. To name only a few examples, this also includes mmap mappings, h5py File objects, and matplotlib.pyplot figure windows.

#### 3.12 TODO Comments
Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.

#### 3.13 Imports formatting
Imports should be on separate lines; there are exceptions for typing and collections.abc imports.

#### 3.14 Statements
Generally only one statement per line.

However, you may put the result of a test on the same line as the test only if the entire statement fits on one line. In particular, you can never do so with try/except since the try and except can’t both fit on the same line, and you can only do so with an if if there is no else.

#### 3.15 Getters and Setters
Getter and setter functions (also called accessors and mutators) should be used when they provide a meaningful role or behavior for getting or setting a variable’s value.

#### 3.16 Naming
Function names, variable names, and filenames should be descriptive; avoid abbreviation. In particular, do not use abbreviations that are ambiguous or unfamiliar to readers outside your project, and do not abbreviate by deleting letters within a word.

Always use a .py filename extension. Never use dashes.

https://google.github.io/styleguide/pyguide.html#3161-names-to-avoid

#### 3.17 Main
In Python, pydoc as well as unit tests require modules to be importable. If a file is meant to be used as an executable, its main functionality should be in a main() function, and your code should always check if __name__ == '__main__' before executing your main program, so that it is not executed when the module is imported.

When using absl, use app.run:

#### 3.18 Function length
Prefer small and focused functions.

#### 3.19 Type Annotations
...

#### 4 Parting Words
BE CONSISTENT.