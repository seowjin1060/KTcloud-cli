# UcloudCli


개발 1단계  python ucloudbiz 명령어 파라미터로 실행
-2/20 4시 35분 개발완료

구현 기능:

-configure
-> init:  APIkey, SecretKey, Zone, response_type을 초기화
-> list:  등록된 사용자 크레딧을 조회
-> help: 명령어 가이드

-server
->listAvailableProductTypes
->delpoyVirtualMachine
->startVirtualMachine
->listVirtualMachines

->listVirtualMachineForCharge (url 체계가 달라서 수행 안됨.)


오류 처리: 
- configure
-> zone과 json의 경우 지원되는 타입만 사용 가능하게 함
-> help를 통해 지원되는 타입 조회 가능
-> credit이 없을 경우 list기능 제한
