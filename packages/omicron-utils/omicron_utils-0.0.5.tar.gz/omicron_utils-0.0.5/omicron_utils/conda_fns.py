#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: nu:ai:ts=4:sw=4

#
#  Copyright (C) 2024 Joseph Areeda <joseph.areeda@ligo.org>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Set of functions supporting use of conda
"""

__author__ = 'joseph areeda'
__email__ = 'joseph.areeda@ligo.org'

import logging
import shutil
from os import getenv
from pathlib import Path

from omicron_utils.omicron_config import OmicronConfig

PREFIX_SEARCH_LIST = [
    '${home}/.conda/envs/ligo-summary-3.10',
    '${home}/.conda/envs/ligo-summary-3.10-test',
    '/cvmfs/software.igwn.org/conda/envs/igwn',
    '${home}/mambaforge/envs/ligo-omicron-3.10',
    '${home}/mambaforge/envs/ligo-omicron-3.10-test',
    ''
]

def get_conda_init(env=None):
    """
    find a conda.sh script we can use to access it
    :param Path|str env: name of an nvironment
    :return str: path to script
    """
    if env is None:
        omi_config = OmicronConfig()
        config = omi_config.get_config()
        if config.has_option('conda', 'environment'):
            the_env = config['conda']['environment']
        else:
            the_env = 'ligo-omicron-3.10'
    else:
        the_env = env

    prefix = getenv('CONDA_PREFIX')
    env_path =  None
    if prefix is None:
        for pre_opt in PREFIX_SEARCH_LIST:
            env_path = Path(pre_opt.replace('${home}', str(Path.home().absolute()))) / the_env
            if env_path.exists():
                break
    else:
        env_path = Path(prefix)
    if env_path is None:
        raise FileNotFoundError('Conda init script not found')
    conda_init = env_path
    # we may not need this so I am leaving it incomplet e


def get_conda_run(config, env=None, logger=None):
    """
    Determine what is needed to run a command in the specified conda environment
    :param configparser.ConfigParser config: our pipeline configuration
    :param str env: cona env name or path
    :param logging.Logger logger:
    :return str, str: path to executable, run arguments
    """

    if logger is None:
        logger =logging.getLogger('get_conda_run')
        logger.setLevel(logging.INFO)

    executable = shutil.which('conda')
    ermsg = 'conda perogram not found' if executable is None else ''

    if env is None:
        env = getenv('CONDA_PREFIX')

    if env is None and config.has_option('conda', 'environment'):
        env = config['conda']['environment']

    if env is None:
        ermsg += 'Unable to determine conda environment for Omicron pipeline'

    if ermsg:
        raise ValueError(ermsg)

    arguments = 'run '
    try:
        env.index('/')
        arguments += f'--prefix {env} '
    except ValueError:
        arguments += f'--name {env} '

    arguments += '--no-capture-output '

    return executable, arguments




