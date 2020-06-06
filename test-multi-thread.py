# coding: utf-8
import tr
import os, time
from multiprocessing.pool import ThreadPool

_BASEDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(_BASEDIR)

if __name__ == "__main__":
    imgs = [
        "imgs/line.png",
        "imgs/id_card.jpeg",
        "imgs/name_card.jpg",
        "imgs/web.png",
    ]

    def run_task(i):
        x = tr.run(imgs[i % len(imgs)])
        return i, len(x)

    n = 20
    time_save = time.time()
    for i in range(n):
        run_task(i)
    print("time", (time.time() - time_save) / n)

    time_save = time.time()
    p = ThreadPool(5)
    pool_output = p.map(run_task, range(n))
    assert len(pool_output) == n
    print("time", (time.time() - time_save) / n)



