__author__ = 'wzhvictor@outlook.com'

def is_sql_injection(payload):
    cdef c_sfilter *sfp = <c_sfilter *> malloc(sizeof(c_sfilter))
    encoded_payload = payload.encode('utf_8')
    libinjection_sqli_init(sfp, encoded_payload, len(encoded_payload), 0)
    res = dict(
        is_sqli=libinjection_is_sqli(sfp),
        fingerprint=sfp.fingerprint.decode('utf_8'),
        token_vector=sfp.tokenvec
    )
    free(sfp)
    return res

def is_xss(payload):
    encoded_payload = payload.encode('utf_8')
    for flag in range(5):
        if libinjection_is_xss(encoded_payload, len(encoded_payload), flag):
            return dict(
                is_xss=True,
                flag=flag
            )
    return dict(
        is_xss=False,
        flag=-1,
    )
