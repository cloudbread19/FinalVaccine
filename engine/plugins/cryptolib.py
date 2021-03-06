# -*- coding:utf-8 -*-

import hashlib
import zlib
from ctypes import c_ushort


# md5(data)
# 주어진 데이터에 대한 md5 값 구하기
# 입력값 : data - 데이터, 리턴값 : MD5 해시 문자열
def md5(data):
    return hashlib.md5(data).hexdigest()

# CLBMain 클래스
class CLBMain:
    def init(self, plugins_path, verbose=False):  # 플러그인 엔진 초기화
        return 0  # 플러그인 엔진 초기화 성공

    def uninit(self):  # 플러그인 엔진 종료
        return 0  # 플러그인 엔진 종료 성공

    def getinfo(self):  # 플러그인 엔진의 주요 정보
        info = dict()  # 사전형 변수 선언

        info['author'] = 'Cloudbread'   # 제작자 구름빵
        info['version'] = '1.0'  # 첫번째 버전
        info['engine_info'] = 'Crypto Library'  # 엔진 설명
        info['engine_name'] = 'cryptolib'  # 엔진 파일 이름

        return info