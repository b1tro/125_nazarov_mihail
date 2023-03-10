import asyncio
i = 0
async def every_second(i) -> None:
    await asyncio.sleep(1)
    i+=1
    print(str(i) + "секунд прошло")
    await every_second(i)

async def every_three_second()-> None:
    await asyncio.sleep(3)
    print("3 second passed")
    await every_three_second()
async def main()-> None:
    task1 = asyncio.create_task(every_second(i))
    task2 = asyncio.create_task(every_three_second())

    await task1
    await task2

asyncio.run(main())
