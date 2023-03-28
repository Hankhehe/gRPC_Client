import grpc
import AtheNAC_pb2
import AtheNAC_pb2_grpc
import datetime
from google.protobuf.timestamp_pb2 import Timestamp

Date_to_timestamp = Timestamp()
Date_to_timestamp.FromDatetime(datetime.datetime(
    year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0))
Date_to_timestamp.FromDatetime(datetime.datetime.utcnow())

channel = grpc.insecure_channel('192.168.13.170:18002')
stub = AtheNAC_pb2_grpc.HostAgentServiceStub(channel)
request = AtheNAC_pb2.HostReportRequest(
    host_name='HostName_Hank',
    MACs=['005056AE328D'],
    domain_name='Domain_Hank',
    logon_users=[],
    os_type='windows',
    os_desc='Windows_Hank',
    share_folder=[],
    pending_hot_fix=[],
    windows_hot_fix_last_check_time=Date_to_timestamp,
    local_admin_account=[],
    timestamp=Date_to_timestamp,
    motherboard_serial_number='Motherboard_Hank',
    softwares=[],
    AgentLastCheckTime=Date_to_timestamp
)

respond = stub.SendHostReport(request)
print(f'AtheNAC reply message {respond}')

# ['Hotfix 123456 - KB123456','Hotfix 666666 - KB666666'] #Hotfix 資料
# [{'logon_account':'Local/Hank','remote_login':True,'gpo_result':''}] logon user
# [{"DisplayName": "Hank_Program_hehe","DisplayVersion": "7.8.8.10","Publisher": "HankMaster","InstallDate": "20230101","EstimatedSize":"888"}] software data
