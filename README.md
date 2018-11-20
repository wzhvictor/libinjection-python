# Libinjection-python

![](https://img.shields.io/badge/license-GPLv3-red.svg)
![](https://img.shields.io/badge/python-2.7%20%7C%203.4%2B-blue.svg)

Libinjection-python is a wrapper based on Cython for the [Libinjection library](https://github.com/client9/libinjection).

> Libinjection Version: v3.10.0(Released on 22 May 2017)

### Requirements
- Python 2.7 or 3.4+
- Cython module (install via pip)

### Installation
```
pip install libinjection-python
```

### Usage
- Check for SQL Injection
  ```
  >> import libinjection
  >> libinjection.is_sql_injection("http://testphp.vulnweb.com/main.php?SmallClass=' union select * from news where 1=2 and ''='")
  {'is_sqli': True, 'fingerprint': 'sUEok'}
  ```

- Check for Cross Site Scripting
  ```
  >> import libinjection
  >> libinjection.is_xss("http://testphp.vulnweb.com/index.php?name=guest<script>alert('attacked')</script>")
  True
  ```

### License
Copyright (c) 2018 wzhvictor

Licensed under the GNU General Public License v3.

![image](https://www.gnu.org/graphics/gplv3-127x51.png)