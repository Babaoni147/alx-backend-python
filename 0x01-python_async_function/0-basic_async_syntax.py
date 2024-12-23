#!/usr/bin/env python3
'''
Task_0 module.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number and return wait time.'''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
