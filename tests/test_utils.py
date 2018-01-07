from __future__ import unicode_literals, absolute_import

import unittest

from kakaoplus.utils import _byteify, PY3


class TestUtils(unittest.TestCase):
    def test__byteify(self):
        if not PY3:
            self.assertEqual(_byteify(u'test'), str('test'))
            self.assertEqual(_byteify([u'test', u'test2']), [str('test'), str('test2')])
            self.assertEqual(_byteify({u'test_key': u'test_value'}), {str('test_key'): str('test_value')})


if __name__ == '__main__':
    unittest.main()