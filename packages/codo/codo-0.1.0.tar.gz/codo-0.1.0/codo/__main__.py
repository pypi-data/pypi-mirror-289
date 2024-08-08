import asyncio
from pathlib import Path
import argparse
from typing import Literal
from pykit.err import ValueErr
import yaml

from codo.core import CodoCore

RunMode = Literal["migrate"]

async def main():
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument("-c", type=Path, dest="cfg_path")

    mode_subparser = main_parser.add_subparsers(dest="mode")

    migrate_parser = mode_subparser.add_parser("migrate")
    migrate_parser.add_argument("version", type=str)

    args = main_parser.parse_args()

    cfg_path = args.cfg_path
    if cfg_path is None:
        cfg_path = Path("codo.yml")

    assert isinstance(cfg_path, Path)
    if not cfg_path.exists():
        raise ValueErr(f"{cfg_path} doest not exist")

    with cfg_path.open() as f:
        cfg = yaml.load(f, yaml.SafeLoader)

    core = CodoCore(cfg)

    match args.mode:
        case "migrate":
            core.migrate(args.version)
        case _:
            raise ValueErr(f"unrecognized mode {args.mode}")

if __name__ == "__main__":
    asyncio.run(main())
