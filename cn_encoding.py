#!/usr/bin/env python
# coding: utf-8

import unittest


def guess_coding(st):
    '''Guess the codepage by try-except'''
    fits_coding = ['utf-8', 'gbk', 'gb18030']
    if not isinstance(st, str):
        raise ValueError('%s is not a str object.' % st)
    for code in fits_coding:
        try:
            st.decode(code)
            return code
        except UnicodeDecodeError:
            pass
    return 'unknow'


class CnEncoding():
    '''The encoding converter'''

    def __init__(self, st, encoding=''):
        '''
        Initial the converter. 'st' could be an str or unicode object.
        'encoding' refers the original encoding.
        If do not know anything about the encoding,
        use the default value or leave it blank.
        '''
        if isinstance(st, unicode):
            self._encoding = 'utf-8'
            self._st = st.decode('utf-8')
        elif isinstance(st, str):
            if encoding == '':
                self._encoding = guess_coding(st)
            else:
                self._encoding = encoding
            self._st = st
        else:
            raise ValueError('%s is not a str nor unicode object.' % st)

    def __str__(self):
        return self._st

    def __unicode__(self):
        return self._st.decode(self._encoding)

    def to_encode(self, encoding='utf-8'):
        '''
        return an printable str object in specific encoding.
        '''
        return self._st.decode(self._encoding).encode(encoding)


class _SimpleTest(unittest.TestCase):

    def test(self):
        sst = u'简体中文'
        tst = u'正體中文'
        self.failUnless(unicode(CnEncoding(sst)) == sst)
        self.failUnless(unicode(CnEncoding(sst)) == sst)
        self.failUnless(unicode(CnEncoding(sst.encode('gbk'))) == sst)
        self.failUnless(unicode(CnEncoding(sst.encode('utf-8'))) == sst)
        self.failUnless(unicode(CnEncoding(sst.encode('gb18030'))) == sst)
        self.failUnless(unicode(CnEncoding(tst.encode('big5'), 'big5')) == tst)


if __name__ == '__main__':
    unittest.main()
