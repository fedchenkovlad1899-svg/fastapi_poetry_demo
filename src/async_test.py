import asyncio

import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://poetrydemo.com/')
        print(html)

if __name__ == '__main__':
    asyncio.run(main())

# import  asyncio
# import time
#
#
# async def fun_1(x: int):
#     print("fun1 before sleep")
#     await asyncio.sleep(x)
#     print("fun1 after sleep")
#
# async def fun_2(x: int = 3):
#     print("fun2 before sleep")
#     await fun_3(x)
#     await fun_4()
#     print(f"fun2 after sleep.result {x**x}")
#
# async def fun_3(x: int = 3):
#     print("fun3 before sleep")
#     await asyncio.sleep(x)
#     print(f"fun3 after sleep.result {x**x}")
#
# async def fun_4():
#     print("fun4 before sleep")
#     await asyncio.sleep(1)
#     print(f"fun4 after sleep")
#
#
# async def main():
#     task1 = asyncio.create_task(fun_1(5))
#     task2 = asyncio.create_task(fun_2())
#     await task1
#     await task2
#
#
# if __name__ == "__main__":
#     s = time.perf_counter()
#     asyncio.run(main())
#     after_s = time.perf_counter() - s
#     print(f"{after_s:0.4f}")