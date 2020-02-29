import infComp
import config

path = config.PATH_JS

def replace_data(src, st_replace, en_replace):
    data_read = open(src, 'r')
    data = data_read.read()
    data_read.close()
    data = data.replace(st_replace, en_replace)
    data_write = open(src, 'w')
    data_write.write(data)
    data_write.close()

def _find(target):
        while True:
            content = target.readline()
            if content.find("CPU") > -1:
                content = target.readline()
                origin_data = content
                data = eval(content.replace(" ", "").split(':')[1])
                data.pop(0)
                data.append(infComp.cpu())
                data = (" "*12)+"data: " + str(data) + "\n"
                replace_data(path, origin_data, data)
                content = target.readline()
            if content.find("RAM") > -1:
                content = target.readline()
                origin_data = content
                data = eval(content.replace(" ", "").split(':')[1])
                data.pop(0)
                data.append(infComp.ram())
                data = (" "*12)+"data: " + str(data) + "\n"
                replace_data(path, origin_data, data)
                content = target.readline()
            if content.find('Network (SEND)') > -1:
                content = target.readline()
                origin_data = content
                data = eval(content.replace(" ", "").split(':')[1])
                data.pop(0)
                data.append(infComp.network()[0])
                data = (" "*12)+"data: " + str(data) + "\n"
                replace_data(path, origin_data, data)
                content = target.readline()
            if content.find('Network (RECV)') > -1:
                content = target.readline()
                origin_data = content
                data = eval(content.replace(" ", "").split(':')[1])
                data.pop(0)
                data.append(infComp.network()[1])
                data = (" "*12)+"data: " + str(data) + "\n"
                replace_data(path, origin_data, data)
                content = target.readline()
                break
def start():
    with open(path, 'r') as _jsFile:
        _find(_jsFile)

