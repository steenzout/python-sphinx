# -*- coding: utf-8 -*-
"""Tests for the steenzout.sphinx package."""

import unittest

from steenzout.sphinx import ResourceGenerator


class ResourceGeneratorTestCase(unittest.TestCase):
    """Tests for the steenzout.sphinx.ResourceGenerator class."""

    def setUp(self):
        self.generator = ResourceGenerator('steenzout', 'steenzout.sphinx')

    def test_generate_conf(self):
        assert self.generator.conf() is None

    def test_generate_makefile(self):
        assert self.generator.generate_makefile() is None
