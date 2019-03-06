# ucloud-cli
Command Line Interface for KT Ucloud biz

This package provides a unified command line interface to Amazon Web Services.

The aws-cli package works on Python versions:

3.3.x and greater

3.4.x and greater

3.5.x and greater

3.6.x and greater

3.7.x and greater

# Installation 

The easiest way to install ucloud-cli is to use pip in a virtualenv: <br /> 

> <strong> $ pip install ucloudcli </strong> <br /> 

or, if you are not installing in a virtualenv, to install globally: <br /> 

> <strong> $ sudo pip install ucloudcli </strong> <br /> 

or for your user: <br />

> <strong> $ pip install --user ucloudcli </strong> <br /> 

If you have the aws-cli installed and want to upgrade to the latest version you can run: <br />

> <strong> $ pip install --upgrade ucloudcli </strong> 




#UCLOUD CLI
- Ucloud KT 명령어 인터페이스

개발 1단계  python ucloudbiz 명령어 파라미터로 실행
-2/20 4시 35분 개발완료
구현 기능:  ucloud server help 참조
          ucloud help


3/5 issue1. listVirtualMachineForCharge (url 체계가 달라서 수행 안됨.)


오류 처리: 

모든 명령어의 파라미터가 부족하거나 많을때 예외처리
올바르지 않은 명령어 입력시 예외처리 + help 명령어를 통해 해당 카테고리의 명령어들 조회 (2/20)

- configure
-> zone과 json의 경우 지원되는 타입만 사용 가능하게 함
-> help를 통해 지원되는 타입 조회 가능
-> credit이 없을 경우 list기능 제한

- server




개발 2단계   ucloudbiz 명령어타입 명령어 파라미터 (배쉬 셀  등록과 pip으로 배포시 자동화해야함)
- 실행 권한 부여   (chmod , grep)
- 셔뱅 추가 (#!/path   python)
- 확장자 제거 
- bin에 path 추가   (export)


개발 3단계  pip을 통한 설치 후, 2단계의 설정 자동화 (2/24)
