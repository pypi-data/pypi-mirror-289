# Copyright 2020-2022 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# For further info, check https://github.com/canonical/charmcraft

from argparse import Namespace

from charmcraft import __version__
from charmcraft.commands.version import VersionCommand


def test_version_result(emitter):
    """Check it produces the right version."""
    cmd = VersionCommand("config")
    args = Namespace(format=None)
    cmd.run(args)
    emitter.assert_message(__version__)


def test_version_result_formatjson(emitter):
    """Format the output."""
    cmd = VersionCommand("config")
    args = Namespace(format="json")
    cmd.run(args)
    emitter.assert_json_output({"version": __version__})
