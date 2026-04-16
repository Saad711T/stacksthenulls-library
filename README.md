# stackthenulls

A lightweight Python library for exploring what happens *behind your code*.

Focuses on:

* tracing execution
* understanding `None` values
* explaining results
* analyzing code flow

---

## Installation

```bash
pip install stackthenulls
```

---

## Quick Usage

```python
from stackthenulls import explain

print(explain(None))
```

---

## Features

* **Explain results**

```python
explain(value)
```

* **Check null values**

```python
nullcheck(data)
```

* **Trace function calls**

```python
@trace_stack
def my_function():
    pass
```

* **Track data flow**

```python
track_flow(["input", "process", "output"])
```

* **Analyze functions**

```python
analyze(func)
```

* **Scan for empty / weak code**

```python
voidscan_code(source)
```

---

## Philosophy

> Code is not just what runs —
> it’s what happens in between.

---

## Project Status

Early stage — experimental and evolving.

---

## Author

Built by [Saad711T](https://github.com/Saad711T)
