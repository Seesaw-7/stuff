async def fetch_data2(): 
    print("Start fetching data...")
    await asyncio.sleep(2)  # 模拟I/O操作
    print("Data fetched")
    return "data"


async def main():
    data = await fetch_data2()
    print(data)

# Run the main function in an async context
import asyncio
asyncio.run(main())
