import asyncio

async def sum(n1, n2, seconds):
    await asyncio.sleep(seconds)
    return n1 + n2

print(asyncio.run(sum(2, 3, 5)))
