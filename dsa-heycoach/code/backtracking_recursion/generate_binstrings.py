import time
import asyncio
from typing import List


class GenerateBinStrings:
    def __init__(self, N: List):
        self.n = N

    def brute_force(self):
        return [bin(i)[2:].zfill(self.n) for i in range(2**self.n)]

    def expected_approach(self):
        result = []

        def backtrack(s):
            if len(s) == self.n:
                result.append(s)
                return
            backtrack(s + "0")
            backtrack(s + "1")

        backtrack("")
        return result


async def run_async(n, method):
    start = time.perf_counter()
    gen = GenerateBinStrings(n)
    result = await asyncio.get_event_loop().run_in_executor(
        None, gen.brute_force if method == "brute" else gen.expected_approach
    )
    elapsed = (time.perf_counter() - start) * 1000
    print(
        f"✓ N={n:2d} | {method:10s} | {elapsed:8.2f}ms | Count: {len(result)}"
    )
    return {"n": n, "method": method, "time": elapsed, "count": len(result)}


async def main():
    inputs = [5, 8, 10, 12, 15]

    print("=" * 60)
    print("PARALLEL EXECUTION")
    print("=" * 60)

    tasks = [
        run_async(n, method)
        for n in inputs
        for method in ["backtrack", "brute"]
    ]

    start = time.perf_counter()
    results = await asyncio.gather(*tasks)
    total = (time.perf_counter() - start) * 1000

    print("=" * 60)
    print(f"Total Parallel Time: {total:.2f}ms")
    print(f"Sequential Time: {sum(r['time'] for r in results):.2f}ms")
    print(f"Speedup: {sum(r['time'] for r in results)/total:.2f}x")


asyncio.run(main())
