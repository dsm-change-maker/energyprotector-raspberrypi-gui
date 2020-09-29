# 에너지 지킴이 RaspberryPi GUI

에너지 지킴이 프로젝트에서 라즈베리파이에 들어갈 GUI 프로그램입니다.

## HOW TO RUN

```
# Resource 파일 및 UI 파일들을 Python 코드로 변환
$ python convert_all_to_py.py

# Device ID 생성
$ python script/device_id_generator.py conf device_id.txt

# Device Group 생성
$ python script/device_group_generator.py DSMHS conf device_group.txt

# 프로그램 실행
$ python main.py
```