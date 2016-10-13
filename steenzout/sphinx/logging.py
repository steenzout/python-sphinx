# -*- coding: utf-8 -*-
"""
.. module:: steenzout.sphinx.logging
    :platform: Unix
    :synopsis: Logging utilities.

.. moduleauthor:: Your Name <email address>
"""

from __future__ import absolute_import


import logging
import logging.config as config

import os


DEFAULT_CONFIG_FILE = '/etc/sphinx/logging.conf'


def load_configuration(config_file=DEFAULT_CONFIG_FILE):
    """
    Loads logging configuration from the given configuration file.

    :param config_file: the configuration file (default=/etc/sphinx/logging.conf)
    :type config_file: str
    """
    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        msg = '%s configuration file does not exist!', config_file
        logging.getLogger(__name__).error(msg)
        raise ValueError(msg)

    try:
        config.fileConfig(config_file, disable_existing_loggers=False)
        logging.getLogger(__name__).info('%s configuration file was loaded.', config_file)
    except Exception as e:
        logging.getLogger(__name__).error('Failed to load configuration from %s!', config_file)
        logging.getLogger(__name__).debug(str(e), exc_info=True)
        raise e
