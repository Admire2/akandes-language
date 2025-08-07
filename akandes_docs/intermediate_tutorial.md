# Intermediate Tutorial

Level up your AkandeChips skills with functions, modules, and more.

## Defining Functions
```akandechips
def add(x, y):
    return x + y

result = add(2, 3)
print(result)
```

## Using Modules
```akandechips
import math
print(math.sqrt(16))
```

## Working with Lists
```akandechips
nums = [1, 2, 3, 4]
for n in nums:
    print(n)
```

See [Functions & Built-ins](./functions.md) for more details.

pandoc -s akandes_docs/README.md akandes_docs/introduction.md akandes_docs/getting_started.md akandes_docs/syntax.md akandes_docs/functions.md akandes_docs/advanced.md akandes_docs/examples.md akandes_docs/best_practices.md akandes_docs/faq.md akandes_docs/cheatsheet.md -o akandechips_docs.html
