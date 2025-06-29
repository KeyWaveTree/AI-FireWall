#파이썬은 기본적으로 비동기 함수를 지원하지 않으며 asyncio를 imoprt 하여 사용한다,
#동기
import time

def task(name):
    print(f"{name} 시작")
    time.sleep(1)
    print(f"{name} 완료")

def main():
    start = time.time()

    task("작업1")
    task("작업2")
    task("작업3")
    task("작업4")
    task("작업5")

    end = time.time()
    print(f"총 소요시간: {end - start:.2f}초")

main()

#비동기
import asyncio

async def task(name):
    print(f"{name} 시작")
    await asyncio.sleep(1)
    print(f"{name} 완료")

async def main():
    start = asyncio.get_event_loop().time()

    await asyncio.gather(
        task("작업1"),
        task("작업2"),
        task("작업3")
    )

    end  = asyncio.get_event_loop().time()
    print(f"총 소요 시간 {end - start:.2f}초")

asyncio.run(main())