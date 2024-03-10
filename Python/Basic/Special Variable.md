### Special Variable

### 1- `__file__`
is a built-in constant containing the pathname of the file from which the 
running Python module was loaded. In some instances, such as when code is 
executed in an interactive interpreter rather than from a file, this 
constant may not be set and accessing it will return an exception.

Exemple of use:

```python
from pathlib import Path

FILE_DIR = Path(__file__).resolve()
BASE_DIR = FILE_DIR.parent
```

### 2- `__doc__`
