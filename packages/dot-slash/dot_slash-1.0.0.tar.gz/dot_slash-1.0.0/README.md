# ./

Dot Slash is a filepath helper that does one job; it resolves a filepath relative to the directory of the file where it is invoked. Which sounds more complicated than it is. In other words, if you find yourself thinking, "I need to access a file and I know its location relative to the code I'm writing now, but I don't really know/care where it is relative to the root of my filesystem, and I'd rather not worry about what the working directory is when I run this code" then you are in the right place.

## Usage

```python
from pathlib import Path

from dot_slash import dot_slash

contents = Path(dot_slash("my_sibling.json")).read_text()
print(contents)
```

## A Few Examples
Given the following file layout, where you are invoking `dot_slash()` from `invoker.py`,
which (please note) is not in the working directory

```
/root/some/path/to/working_dir
│
├─ A 
│  ├ invoker.py
│  └ sibling.txt
│
└─ B
   └ cousin.json
```

these paths resolve as follows

``` python
# invoker.py

from dot_slash import dot_slash

dot_slash("..")                # -> /root/some/path/to/working_dir/
dot_slash(".")                 # -> /root/some/path/to/working_dir/A/
dot_slash("sibling.txt")       # -> /root/some/path/to/working_dir/A/sibling.txt
dot_slash("../B/cousin.json")  # -> /root/some/path/to/working_dir/B/cousin.json
```