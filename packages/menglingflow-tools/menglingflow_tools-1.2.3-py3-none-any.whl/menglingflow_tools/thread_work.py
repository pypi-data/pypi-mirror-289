from threading import Thread, get_ident
import traceback
import os
import logging
import time
import asyncio
import subprocess
from dataclasses import dataclass, field
from typing import Any
try:
    from menglingtool.queue import Mqueue
except ModuleNotFoundError:
    subprocess.check_call(['pip','install', "menglingtool"])
    from menglingtool.queue import Mqueue
    
@dataclass
class Result:
    index: int = field()
    result: Any = field()
    err: str = field()
    args: tuple = field(default=None)
    kwargs: tuple = field(default=None)
    time: float = field(default=None)

# 便捷获取log对象
def getLogger(name, level=logging.INFO, log_path=None) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.FileHandler(log_path) if log_path else logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


class WorkPool:
    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger if logger else getLogger(f'pid-{get_ident()}')
        self.task_queue = Mqueue()
        self._alive = False
    
    def getTaskNum(self) -> int:
        return self.task_queue.qsize()
    
    def is_alive(self) -> bool:
        return self._alive
    
    def stop(self):
        self._alive = False
    
    def start(self, *, getGood = None, getResult, good_num: int = 3,
                        is_put_args=False,
                        is_put_kwargs=False,
                        is_put_time=True) -> list:
        assert not self._alive, '任务已启动!'
        self.logger.info(f'PID-{os.getpid()} worker num: {good_num}')
        self._alive = True
        
        def _worker():
            gooder = getGood() if getGood else None
            while self._alive:
                que, index, args, kwargs = self.task_queue.get()
                sd = time.time()
                try:
                    result = getResult(gooder, *args, **kwargs) if gooder else getResult(*args, **kwargs)
                    err = None
                except:
                    err = traceback.format_exc()
                    result = None

                self.logger.info(f'args:{args}, kwargs:{kwargs}, is_err:{bool(err)}')
                rt = Result(index, result, err)
                if is_put_args: rt.args = args
                if is_put_kwargs: rt.kwargs = kwargs
                if is_put_time: rt.time = time.time() - sd
                que.put(rt)

        ts = [Thread(target=_worker, daemon=True) for _ in range(good_num)]
        [t.start() for t in ts]
        return ts


    def arg_in_task_puts(self, vs: list) -> Mqueue[Result]: 
        return self.all_in_task_puts([[(v,), {}] for v in vs])


    def args_in_task_puts(self, argss: list) -> Mqueue[Result]:
        return self.all_in_task_puts([[args, {}] for args in argss])


    def kwargs_in_task_puts(self, kwargss: list) -> Mqueue[Result]:
        return self.all_in_task_puts([[(), kwargs] for kwargs in kwargss])


    def all_in_task_puts(self, args_and_kwargs: list) -> Mqueue[Result]:
        result_queue = Mqueue(maxsize=len(args_and_kwargs))
        self.task_queue.puts(*[(result_queue, i, *args_kwargs) for i, args_kwargs in enumerate(args_and_kwargs)])
        return result_queue

    @staticmethod
    def getResults(result_queue: Mqueue[Result], is_sorded=True, is_rt_dict = True, timeout = None) -> list[Result | dict]:
        t = 0
        while not result_queue.full():
            if timeout and t >= timeout: raise TimeoutError(f'process:{result_queue.qsize()}/{result_queue.maxsize}  timeout:{timeout}s')
            time.sleep(1)
            t+=1
        ls = result_queue.to_list()
        ls = sorted(ls, key = lambda x: x.index) if is_sorded else ls
        return [obj.__dict__ for obj in ls] if is_rt_dict else ls

    @staticmethod
    async def async_getResults(result_queue: Mqueue[Result], is_sorded=True, is_rt_dict = True, timeout = None) -> list[Result | dict]:
        t = 0
        while not result_queue.full():
            if timeout and t >= timeout: raise TimeoutError(f'process:{result_queue.qsize()}/{result_queue.maxsize}  timeout:{timeout}s')
            await asyncio.sleep(1)
            t+=1
        ls = result_queue.to_list()
        ls = sorted(ls, key = lambda x: x.index) if is_sorded else ls
        return [obj.__dict__ for obj in ls] if is_rt_dict else ls