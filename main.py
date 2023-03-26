import grpc,AtheNAC_pb2,AtheNAC_pb2_grpc,datetime,time
from google.protobuf.timestamp_pb2 import Timestamp

pass
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
    pending_hot_fix=[],
    windows_hot_fix_last_check_time=None,
    local_admin_account=[],
    timestamp=None,
    motherboard_serial_number='Test_Motherboard',
    softwares=[],
    AgentLastCheckTime=None
)

timestampaa = Timestamp()
timestampaa.FromDatetime(datetime.datetime.now())
request.timestamp.CopyFrom(timestampaa)
request.AgentLastCheckTime.CopyFrom(timestampaa)
request.windows_hot_fix_last_check_time.CopyFrom(timestampaa)

respond = stub.SendHostReport(request)
pass