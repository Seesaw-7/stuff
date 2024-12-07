import asyncio

# 定义协程
async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)  # 模拟I/O操作
    print("Data fetched")
    return "data"

async def process_data():
    print("Start processing data...")
    await asyncio.sleep(1)  # 模拟I/O操作
    print("Data processed")

async def main():
    # 启动多个协程
    data = await fetch_data()
    await process_data()

# 运行事件循环
asyncio.run(main())

# output
# Start fetching data...
# Data fetched
# Start processing data...
# Data processed

async def fetch_data2():
    print("Start fetching data...")
    await asyncio.sleep(2)  # 模拟I/O操作
    print("Data fetched")
    return "data"

async def process_data2():
    print("Start processing data...")
    await asyncio.sleep(1)  # 模拟I/O操作
    print("Data processed")

# async def main():
#     # 启动多个协程
#     data = await fetch_data()
#     await process_data()

# 运行事件循环
tasks = [process_data2(), fetch_data2()]

asyncio.run(asyncio.wait(tasks))