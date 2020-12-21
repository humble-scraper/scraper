#!/usr/bin/env python3


from multiprocessing import Process
from typing import Dict, Optional
from time import sleep, time

import uvicorn

from core.scraper import SCRAPER


procs: Dict[str, Process] = {}


def better_sleep(sleep_time: Optional[float] = 60):
    start = time()
    while time() - start < sleep_time:
        sleep(min((sleep_time - time() + start), 60))


def _web_service_worker() -> None:
    uvicorn.run("webservice.webscrapp:scrapp", host="127.0.0.1", port=9999, log_level="debug")


def _main_loop_worker(sleep_time: float) -> None:
    while True:
        print(SCRAPER.scrape_bundles_from())
        print("-----------------------------------------------------------------")
        print("-----------------------------------------------------------------")
        better_sleep(sleep_time)


def run_web_app(in_new_process: Optional[bool] = True) -> None:
    print(f"Running web app{' in new process' if in_new_process else ''}...")
    if in_new_process:
        procs["scrapp"] = Process(target=_web_service_worker)
        procs["scrapp"].start()
    else:
        # Run the service in current thread
        _web_service_worker()


def run_main_loop(in_new_process: Optional[bool] = True,
                  sleep_time: Optional[float] = 60**60) -> None:
    print(f"Running main loop{' in new process' if in_new_process else ''}...")
    if in_new_process:
        procs["mainloop"] = Process(target=_main_loop_worker, args=(sleep_time, ))
        procs["mainloop"].start()
    else:
        _main_loop_worker(sleep_time)


def joinall() -> None:
    for proc in procs.values():
        proc.join()


def killall() -> None:
    for proc in procs.values():
        proc.kill()


def main() -> None:
    run_web_app()
    run_main_loop(sleep_time=60**60)
    joinall()


if __name__ == "__main__":
    main()
