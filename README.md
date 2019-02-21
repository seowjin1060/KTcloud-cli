#UCLOUD CLI


- Ucloud KT 명령어 인터페이스

개발 1단계  python ucloudbiz 명령어 파라미터로 실행
-2/20 4시 35분 개발완료
구현 기능: 

================Supported configure commands===========

-> ucloudcli configure init:  APIkey, SecretKey, Zone, response_type을 초기화
-> ucloudcli configure list:  등록된 사용자 크레딧을 조회
-> ucloudcli configure help: 명령어 가이드

==========Supported server commands==========

ucloudcli server  help  
ucloudcli server  listAvailableProductTypes  
ucloudcli server  deployVirtualMachine  [ serviceofferingid ]  [ templateid ]  [ diskofferingid ]  [ zoneid ]  
ucloudcli server  startVirtualMachine  [ id ]  
ucloudcli server  listVirtualMachines  [ state ]  
ucloudcli server  listVirtualMachineForCharge  
ucloudcli server  stopVirtualMachine  [ id ]  
ucloudcli server  changeServiceForVirtualMachine  [ id ]  [ serviceofferingid ]  
ucloudcli server  checkVirtualMachineName  [ display_name ]  
ucloudcli server  changeServiceForVirtualMachineVerify  [ id ]  [ serviceofferingid ]  
ucloudcli server  restoreVirtualMachine  [ virtualmachineid ]  
ucloudcli server  updateVirtualMachine  [ id ]  [ displayname ]  [ haenable ]  
ucloudcli server  updateVirtualMachineForCharge  [ id,usageplantype ]  
ucloudcli server  createVolume  [ name ]  [ diskofferingid ]  [ zoneid ]  [ usageplantype ]  [ account ]  [ domainid ]  
[ size ]  [ snapshotid ]  [ virtualmachineid ]  [ productcode ]  [ iops ]  
ucloudcli server  attachVolume  [ id ]  [ virtualmachineid ]  
ucloudcli server  detatchVolume  [ deviceid ]  [ id ]  [ virtualmachineid ]  
ucloudcli server  deleteVolume  [ id ]  
ucloudcli server  listVolumes  [ account ]  [ domainid ]  [ hostid ]  [ id ]  [ isrecursive ]  [ keyword ]  [ name ]  [ page ]  [ pagesize ]  [ podid ]  [ type ]  [ virtualmachineid ]  [ zoneid ]  [ install ]  
ucloudcli server  resizeVolume  [ id ]  [ vmid ]  [ size ]  [ isLinux ]  
ucloudcli server  updateUsagePlanTypeForServer  [ type ]  [ usagePlanType ]  [ id ]  
ucloudcli server  destroyVirtualMachine  [ id ]  
ucloudcli server  associateIpAddress  [ zoneid ]  [ usageplantype ]  [ account ]  [ domainid ]  [ networkid ]  
ucloudcli server  listPublicIpAddresses  [ id ]  
ucloudcli server  disassociateIpAddress  [ id ]  

->listVirtualMachineForCharge (url 체계가 달라서 수행 안됨.)


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
