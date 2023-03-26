import grpc,AtheNAC_pb2,AtheNAC_pb2_grpc,datetime,time
from google.protobuf.timestamp_pb2 import Timestamp

Date_to_timestamp = Timestamp()
Date_to_timestamp.FromDatetime(datetime.datetime(1970,1,1,0,0,0))

channel = grpc.insecure_channel('192.168.13.170:18002')
stub = AtheNAC_pb2_grpc.HostAgentServiceStub(channel)
request = AtheNAC_pb2.HostReportRequest(
    host_name='HankHHHHHHH',
    MACs=['005056AE328D'],
    domain_name='HankDomain',
    logon_users=[{'logon_account':'Local/Hank','remote_login':True,'gpo_result':''}],
    os_type='windows',
    os_desc='WindowsTest',
    share_folder=[],
    pending_hot_fix=['Hotfix 123456 - KB123456','Hotfix 666666 - KB666666'],
    windows_hot_fix_last_check_time=Date_to_timestamp,
    local_admin_account=[],
    timestamp=Date_to_timestamp,
    motherboard_serial_number='Test_Motherboard',
    softwares=[{"DisplayName": "Hank_Program_hehe","DisplayVersion": "7.8.8.10","Publisher": "HankMaster","InstallDate": "20230101","EstimatedSize":"888"}],
    AgentLastCheckTime=Date_to_timestamp
)


respond = stub.SendHostReport(request)
print(f'AtheNAC reply message {respond}')