import argparse
from typing import List

from troveclient.extension import Extension

class TroveClientArgumentParser(argparse.ArgumentParser):
    def error(self, message: str): ...

class OpenStackTroveShell(object):
    def get_base_parser(self, argv: List[str]) -> TroveClientArgumentParser: ...
    def _append_global_identity_args(
        self, parser: TroveClientArgumentParser, argv: List[str]
    ): ...
    def get_subcommand_parser(
        self, version: str, argv: List[str]
    ) -> TroveClientArgumentParser: ...
    def _discover_extensions(self, version: str) -> Extension: ...
