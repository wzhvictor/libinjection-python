__author__ = 'wzhvictor@outlook.com'

cdef extern from *:
    ctypedef char* const_char_ptr "const char*"


cdef extern from "stdlib.h":
    void* malloc(size_t)
    void free(void* )


cdef extern from "libinjection_sqli.h":
    ctypedef struct c_stoken_t "stoken_t":
        size_t  pos
        size_t  len

        int     count

        char    type
        char    str_open
        char    str_close
        char    val[32]

    ctypedef struct c_sfilter "sfilter":
        const_char_ptr  s
        size_t          slen

        int             flags
        size_t          pos

        c_stoken_t      tokenvec[8]
        c_stoken_t      *current
        char            fingerprint[8]

        int             reason
        int             stats_comment_ddw
        int             stats_comment_ddx
        int             stats_comment_c
        int             stats_comment_hash
        int             stats_folds
        int             stats_tokens

    void libinjection_sqli_init(c_sfilter *,
                                const_char_ptr,
                                size_t,
                                int)

    bint libinjection_is_sqli(c_sfilter *)


cdef extern from "libinjection_xss.h":
    bint libinjection_is_xss(const_char_ptr,
                             size_t,
                             int)
