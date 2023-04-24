# import subprocess
#
#
# def checkout(cmd, text):
#     result = subprocess.run(cmd, shell=True,
#                             stdout=subprocess.PIPE, encoding='utf 8')
#     # print(result.stdout)
#     if result.returncode == 0 and text in result.stdout:
#         return True
#     else:
#         return False
#

# def test_step1():
#     # test 1
#     assert checkout('cd /home/user/tst; 7z a ../user/arx2', "Everything is OK"), "Test1 fail"


# def test_step2():
#     # test 1
#     assert checkout('cd /home/user/out; 7z e arx2.7z -o/home/user/folder1 -y', "Everything is OK"), 'Test2 fail'
# #
#
# def test_step2():
#     # test 1
#     assert checkout('cd /home/user/out; 7z t arx2.7z', "Everything is OK"), 'Test3 fail'
