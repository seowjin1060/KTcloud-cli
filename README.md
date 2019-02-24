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
ucloudcli server  destroyVirtualMachine  [ id ]  
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
ucloudcli server  createVolume  [ name ]  [ diskofferingid ]  [ zoneid ]  [ usageplantype ]  [ account ] [ domainid ][ size ]  [ snapshotid ]  [ virtualmachineid ]  [ productcode ]  [ iops ]  
ucloudcli server  attachVolume  [ id ]  [ virtualmachineid ]  
ucloudcli server  detatchVolume  [ deviceid ]  [ id ]  [ virtualmachineid ]  
ucloudcli server  deleteVolume  [ id ]  
ucloudcli server  listVolumes  
ucloudcli server  resizeVolume  [ id ]  [ vmid ]  [ size ]  [ isLinux ]  
ucloudcli server  updateUsagePlanTypeForServer  [ type ]  [ usagePlanType ]  [ id ]  
ucloudcli server  associateIpAddress  [ zoneid ]  [ usageplantype ]  [ account ]  [ domainid ]  [ networkid ]  
ucloudcli server  disassociateIpAddress  [ id ]  
ucloudcli server  listPublicIpAddresses  [ account ]  
ucloudcli server  updateIpAddress  [ desc ]  [ id ]  
ucloudcli server  upateUsagePlanTypeForServer  [ type ]  [ usagePlanType ]  [ id ]  
ucloudcli server  createPortForwardingRule  [ ipaddressid ]  [ privateport ]  [ protocol ]  [ publicport ][ virtualmachineid ]  [ cidrlist ]  [ openfirewall ]  [ privateendport ]  [ publicendport ]  
ucloudcli server  deletePortForwardingRule  [ id ]  
ucloudcli server  listPortForwardingRules  [ account ]  [ domainid ]  [ id ]  [ ipaddressid ]  [ keyword ]  [ page ]  [ pagesize ]  [ isrecursive ]  [ listall ]  
ucloudcli server  createFirewallRule  [ ipaddressid ]  [ protocol ]  [ cidrlist ]  [ startport ]  [ endport ]  [ icmpcode ]  
[ icmptype ]  [ type ]  
ucloudcli server  deleteFirewallRule  [ id ]  
ucloudcli server  listFirewallRules  [ account ]  [ domainid ]  [ id ]  [ ipaddressid ]  [ keyword ]  [ page ]  [ pagesize ]  [ srecursive ]  
ucloudcli server  listAccounts  [ accounttype ]  [ domainid ]  [ id ]  [ iscleanuprequired ]  [ isrecursive ]  [ keyword ]  
[ name ]  [ page ]  [ pagesize ]  [ state ]  [ listall ]  
ucloudcli server  queryAsyncjobResult  [ jobid ]  
ucloudcli server  listEvents  [ account ]  [ domainid ]  [ duration ]  [ startdate ]  [ enddate ]  [ entrytime ]  [ id ]  
[ keyword ]  [ page ]  [ pagesize ]  [ type ]  [ isrecursive ]  [ listall ]  
ucloudcli server  createSnapshot  [ volumeid ]  [ account ]  [ domainid ]  [ policyid ]  
ucloudcli server  deleteSnapshot  [ id ]  
ucloudcli server  listSnapshots  [ account ]  [ domainid ]  [ id ]  [ intervaltype ]  [ isrecursive ]  [ keyword ]  [ name ]  [ page ]  [ pagesize ]  [ snapshottype ]  [ volumeid ]  [ listall ]  
ucloudcli server  listSnapshotSize  [ id ]  
ucloudcli server  createTemplate  [ displaytext ]  [ name ]  [ ostypeid ]  
ucloudcli server  deleteTemplate  [ id ]  [ zoneid ]  
ucloudcli server  updateTemplate  [ id ]  [ bootable ]  [ displaytext ]  [ format ]  [ name ]  [ ostypeid ]  [ zoneid ]  
[ isgroup ]  [ passwordenable ]  [ sortkey ]  
ucloudcli server  listTemplates  [ templatefilter ]  
ucloudcli server  copyTemplate  [ id ]  [ sourcezoneid ]  [ destzoneid ]  
ucloudcli server  listNetworks  
ucloudcli server  listNetworkUsages  [ startdate ]  [ enddate ]  
ucloudcli server  createNetwork  [ displaytext ]  [ zoneid ]  [ account ]  [ domainid ]  [ ipcount ]  
ucloudcli server  deleteNetwork  [ id ]  
ucloudcli server  interAzStatus  [ destnetworkid ]  [ sourcenetworkid ]  
ucloudcli server  listNetworkFlatRate  
ucloudcli server  networkFlatRate  [ type ]  
ucloudcli server  addNicToVirtualMachine  [ networkid ]  [ virtualmachineid ]  [ eid ]  
ucloudcli server  removeNicFromVirtualMachine  [ nicid ]  [ virtualmachineid ]  
ucloudcli server  requestForInterAz  [ destnetworkid ]  [ sourcenetworkid ]  [ destzoneid ]  [ sourcezoneid ]  
ucloudcli server  listZones  
ucloudcli server  createSSHKeyPair  [ Name ]  
ucloudcli server  deleteSSHKeyPair  [ Name ]  
ucloudcli server  listSSHKeyPairs  [ Name ]  
ucloudcli server  enableStaticNat  [ ipaddressid ]  [ virtualmachineid ]  
ucloudcli server  disableStaticNat  [ ipaddressid ]  
ucloudcli server  createTags  [ resourceids ]  [ resoucretype ]  [ Tags ]  
ucloudcli server  deleteTags  [ resourceids ]  [ resourcetype ]  
ucloudcli server  listTags 
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


개발 3단계  pip을 통한 설치 후, 2단계의 설정 자동화 (2/24)
