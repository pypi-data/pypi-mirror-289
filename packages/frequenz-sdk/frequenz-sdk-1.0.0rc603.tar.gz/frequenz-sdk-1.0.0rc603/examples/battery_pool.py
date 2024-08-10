# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Script with an example how to use BatteryPool."""


import asyncio
import logging
from datetime import timedelta

from frequenz.channels import merge

from frequenz.sdk import microgrid
from frequenz.sdk.actor import ResamplerConfig

HOST = "microgrid.sandbox.api.frequenz.io"  # it should be the host name.
PORT = 61060


async def main() -> None:
    """Create the battery pool, activate all formulas and listen for any update."""
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s:%(message)s"
    )
    await microgrid.initialize(
        host=HOST,
        port=PORT,
        resampler_config=ResamplerConfig(resampling_period=timedelta(seconds=1.0)),
    )

    battery_pool = microgrid.battery_pool()
    receivers = [
        battery_pool.soc.new_receiver(limit=1),
        battery_pool.capacity.new_receiver(limit=1),
        # pylint: disable=protected-access
        battery_pool._system_power_bounds.new_receiver(limit=1),
        # pylint: enable=protected-access
    ]

    async for metric in merge(*receivers):
        print(f"Received new metric: {metric}")


asyncio.run(main())
