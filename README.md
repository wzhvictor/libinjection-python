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
  {'is_sqli': True, 'fingerprint': 'sUEok', 'token_vector': [{'pos': 0, 'len': 31, 'count': 0, 'type': 115, 'str_open': 0, 'str_close': 39, 'val': b'http://testphp.vulnweb.com/main'}, {'pos': 49, 'len': 5, 'count': 0, 'type': 85, 'str_open': 0, 'str_close': 0, 'val': b'union'}, {'pos': 55, 'len': 6, 'count': 0, 'type': 69, 'str_open': 0, 'str_close': 0, 'val': b'select'}, {'pos': 62, 'len': 1, 'count': 0, 'type': 111, 'str_open': 0, 'str_close': 0, 'val': b'*'}, {'pos': 64, 'len': 4, 'count': 0, 'type': 107, 'str_open': 0, 'str_close': 0, 'val': b'from'}, {'pos': 69, 'len': 4, 'count': 0, 'type': 110, 'str_open': 0, 'str_close': 0, 'val': b'news'}, {'pos': 0, 'len': 0, 'count': 0, 'type': 0, 'str_open': 0, 'str_close': 0, 'val': b''}, {'pos': 0, 'len': 0, 'count': 0, 'type': 0, 'str_open': 0, 'str_close': 0, 'val': b''}]}
  ```

- Check for Cross Site Scripting
  ```
  >> libinjection.is_xss("http://testphp.vulnweb.com/index.php?name=guest<script>alert('attacked')</script>")
  {'is_xss': True, 'flag': 0}
  ```

### License
Copyright (c) 2021 wzhvictor

Licensed under the GNU General Public License v3.

![image](https://www.gnu.org/graphics/gplv3-127x51.png)