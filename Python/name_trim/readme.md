# Name Trim

Simple script to trim names of files with long names. This also removes all the
special characters from the file name excluding `.`, `-`, and `_`.

* Change the value of `directory` to set the directory to execute upon.
* Set the value of `total_max_len` to change the length of trimmed names.

### Usage

#### Method 1

Make it executable and run.
```sh
chmod +x trim_name.py
./trim_name.py
```
#### Method 2

If the above method does not run, try running with `python`
```sh
python trim_name.py
```

Note:
> By default runs on the test cases from
> [size-calculator/test/](../size-calculator/test/). Feel free to update
> `directory` to change as per your need.
>
> Also, it does not run recursively. Feel free to raise a PR to to that. :)
