# static.py
#
# darch - Difference Archiver
# Copyright (c) 2015-2016 Ammon Smith
#
# darch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# darch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with darch.  If not, see <http://www.gnu.org/licenses/>.
#


FILE_TREE_FILE = "filetree.pickle"
FILE_TREE_IGNORE_FILE = "filetree.ignore"
DEFAULT_IGNORE_TARGETS = (
    FILE_TREE_FILE,
    FILE_TREE_IGNORE_FILE,
    "*~",
    "*.bak",
    ".*.swp",
)

