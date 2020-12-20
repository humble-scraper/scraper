#!/usr/bin/env python3


from multiprocessing import Process
from time import sleep
from typing import Dict, Optional

import uvicorn

from core.scraper import SCRAPER

procs: Dict[str, Process] = {}


def _web_service_worker() -> None:
    uvicorn.run("webservice.webscrapp:scrapp", host="127.0.0.1", port=9999, log_level="debug")


def _main_loop_worker() -> None:
    # while True:
    while False:
        print(SCRAPER.scrape_bundles_from())
        print("-----------------------------------------------------------------")
        print("-----------------------------------------------------------------")
        sleep(1)


def run_web_app(in_new_process: Optional[bool] = True) -> None:
    print(f"Running web app{' in new process' if in_new_process else ''}...")
    if in_new_process:
        procs["scrapp"] = Process(target=_web_service_worker)
        procs["scrapp"].start()
    else:
        # Run the service in current thread
        _web_service_worker()


def run_main_loop(in_new_process: Optional[bool] = False) -> None:
    if in_new_process:
        procs["mainloop"] = Process(target=_main_loop_worker)
        procs["mainloop"].start()
    else:
        _main_loop_worker()


def joinall() -> None:
    for proc in procs.values():
        proc.join()


def killall() -> None:
    for proc in procs.values():
        proc.kill()


def main() -> None:
    run_web_app()
    run_main_loop()
    joinall()


if __name__ == "__main__":
    main()
