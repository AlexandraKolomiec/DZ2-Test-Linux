import subprocess
import zlib
path_arch: str = 'arx2.7z'

# h_arch = hash('arx2.7z')
# h_crc = zlib.crc32(b'arx2.7z')
# print(h_arch)
# print(h_crc)


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True,
                            stdout=subprocess.PIPE, encoding='utf 8')
    # print(result.stdout)
    if result.returncode == 0 and text in result.stdout:
        return True
    else:
        return False


def crc32(b, s):
    h_crc = zlib.crc32(b'path_arch')
    return h_crc

