__author__ = 'wzhvictor@outlook.com'

def is_sql_injection(payload):
    cdef c_sfilter *sfp = <c_sfilter *> malloc(sizeof(c_sfilter))
    libinjection_sqli_init(sfp, payload.encode('utf_8'), len(payload), 0)

    res = dict(is_sqli=libinjection_is_sqli(sfp),
               fingerprint=sfp.fingerprint.decode('utf_8'))
    free(sfp)
    return res

def is_xss(payload):
    return any(libinjection_is_xss(payload.encode('utf_8'), len(payload), flag) for flag in range(5))
