#! /usr/bin/env python3
from sys import path

path.insert(0, ".")

from pymyenergi.cli import cli
import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
cli()

