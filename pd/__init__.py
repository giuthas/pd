#
# Copyright (c) 2019-2020 Pertti Palo.
#
# This file is part of Pixel Difference toolkit 
# (see https://github.com/giuthas/pd/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# The example data packaged with this program is licensed under the
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0
# International (CC BY-NC-SA 4.0) License. You should have received a
# copy of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
# International (CC BY-NC-SA 4.0) License along with the data. If not,
# see <https://creativecommons.org/licenses/by-nc-sa/4.0/> for details.
#

import logging
import logging.config
import json

from .pd import *

# Load config from json file.
with open("pd_logging_configuration.json", 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)
    logging.config.dictConfig(config_dict)
 
# Create the module logger.
_pd_logger = logging.getLogger('pd')

# Log that the logger was configured.
_pd_logger.info('Completed configuring logger.')
