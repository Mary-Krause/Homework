import asyncio

async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    strongmen = [
        ("Pasha", 3),
        ("Denis", 4),
        ("Apollon", 5)
    ]
    tasks = [asyncio.create_task(start_strongman(name, power)) for name, power in strongmen]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(start_tournament())
