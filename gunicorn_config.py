import multiprocessing

bind = "<内网IP>:5000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() + 1
reload = True
daemon = True