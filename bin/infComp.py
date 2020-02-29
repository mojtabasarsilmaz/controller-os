import psutil

def cpu():
    data = 0
    ctx_switches = psutil.cpu_stats().ctx_switches
    for count in str(ctx_switches):
        data += int(count)
    return data

def ram():
    data = 0
    used_memory = psutil.virtual_memory().used
    for count in str(used_memory):
        data += int(count)
    return data

def network():
    data_send = 0
    data_recv = 0
    sends = psutil.net_io_counters().bytes_sent
    recvs = psutil.net_io_counters().bytes_recv
    for send in str(sends):
        data_send += int(send)
    for recv in str(recvs):
        data_recv += int(recv)
    return (data_send, data_recv)


if __name__ == "__main__":
    print(cpu())
    print(ram())
    print(network())
