# -*- coding: utf-8 -*-
# Copyright (c) 2014 Vlad Temian <vladtemian@gmail.com>
# Copyright (c) 2015-2020 Claudiu Popa <pcmanticore@gmail.com>
# Copyright (c) 2015 Ionel Cristian Maries <contact@ionelmc.ro>
# Copyright (c) 2017 guillaume2 <guillaume.peillex@gmail.col>
# Copyright (c) 2019-2020 Pierre Sassoulas <pierre.sassoulas@gmail.com>
# Copyright (c) 2019 Hugo van Kemenade <hugovk@users.noreply.github.com>
# Copyright (c) 2020 Clément Pit-Claudel <cpitclaudel@users.noreply.github.com>
# Copyright (c) 2020 Thomas Wucher <thomas.wucher@gtd-gmbh.de>

# Licensed under the GPL:
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

"""JSON reporter"""
from __future__ import absolute_import, print_function

import json
import sys
import hashlib

try:
    from pylint.reporters.base_reporter import BaseReporter
except ImportError:
    from pylint.reporters import BaseReporter


class CodeClimateReporter(BaseReporter):
    """Report messages and layouts in JSON."""

    name = "codeclimate"
    extension = "json"

    category_map = {
        "convention": ["Style"],
        "refactor": ["Complexity"],
        "warning": ["Bug Risk"],
        "error": ["Bug Risk"],
        "fatal": ["Bug Risk"],
    }
    severity_map = {
        "convention": "info",
        "refactor": "minor",
        "warning": "major",
        "error": "critical",
        "fatal": "blocker",
    }

    def __init__(self, output=None):
        BaseReporter.__init__(self, output or sys.stdout)
        self.messages = []

    def handle_message(self, msg):
        """
        Manage message of different type and in the context of path.
        """
        digest = hashlib.sha256()
        digest.update("{}{}{}".format(msg.msg_id, msg.path, msg.obj).encode("utf-8"))
        fingerprint = digest.hexdigest()
        try:
            explanation = self.linter.msgs_store.get_message_definitions(msg.symbol)[0].format_help()
        except AttributeError:
            explanation = ""
        message = msg.msg.replace("'", "`").splitlines()[0]
        version = sys.version.split()[0]

        if sys.version_info.major == 2:
            message = message.encode("utf-8")

        self.messages.append(
            {
                "type": "issue",
                "check_name": msg.symbol,
                "description": "{} (Python {})".format(message, version),
                "categories": self.category_map[msg.category],
                "content": {"body": explanation},
                "fingerprint": fingerprint,
                "location": {
                    "path": msg.path,
                    "positions": {
                        "begin": {"line": msg.line, "column": msg.column},
                        "end": {"line": msg.line, "column": msg.column},
                    },
                },
                "severity": self.severity_map[msg.category],
            }
        )

    def display_messages(self, layout):
        """Launch layouts display"""
        if self.messages:
            print(json.dumps(self.messages, indent=4), file=self.out)

    def display_reports(self, layout):
        """Don't do anything in this reporter."""

    def _display(self, layout):
        """Do nothing."""


def register(linter):
    """Register the reporter classes with the linter."""
    linter.register_reporter(CodeClimateReporter)
