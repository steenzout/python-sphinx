# -*- coding: utf-8 -*-
"""Tests for the steenzout.sphinx package."""

import unittest

from steenzout.sphinx import ResourceGenerator


class ResourceGeneratorTestCase(unittest.TestCase):
    """Tests for the steenzout.sphinx.ResourceGenerator class."""

    @staticmethod
    def _compare_output(expected, output):

        assert output is not None

        content = None
        with open('tests/resources/%s' % expected, 'r') as fd:
            content = fd.read()

        assert content == output

    def setUp(self):
        self.generator = ResourceGenerator('steenzout', 'steenzout.sphinx')

    def test_conf(self):
        conf = self.generator.conf()

        self._compare_output('conf.py', conf)

    def test_makefile(self):
        makefile = self.generator.makefile()

        self._compare_output('Makefile', makefile)
