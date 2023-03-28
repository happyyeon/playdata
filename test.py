"""
jupyter notebook과 mysql 이미지를 제외하고 모든 이미지 제거하는 코드
"""

import subprocess
text = subprocess.check_output("docker images",shell=True).decode()
except_set = {'jupyter/datascience-notebook','mysql'}
for x in text.split('\n')[1:-1]:
    temp = x.split()
    if temp[0] not in except_set:
        subprocess.call("docker rmi {}".format(temp[2]), shell=True)