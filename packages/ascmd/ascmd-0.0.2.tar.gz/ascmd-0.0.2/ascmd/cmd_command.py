import os
def Enable_firewall():
    os.system('''netsh advfirewall reset
''')
def service_iptables_stop():
    os.system('''netsh advfirewall set allprofiles state off
''')
def ls():
    os.system("dir")
def Check_Windows_version():
    os.system("winver")
def start_Messenger():
    os.system('''net start messenger''')
def Windows_file_protection():
    os.system('''sfc /scannow''')
def Character_Mapping_Table():
    os.system('''charmap''')
def Performance_monitoring():
    os.system("perfmon.msc")
def Object_packaging():
    os.system("packager")
def computer_manager():
    os.system("compmgmt.msc")
def Garbage_sorting():
    os.system("cleanmgr")
def Chkdsk_disk_inspection():
    os.system("chkdsk.exe")
def Stop_DLL_file_running():
    os.system('''regsvr32 /u *.dll''')
def Character_creation_program():
    os.system("eudcedit")
def event_viewer():
    os.system("eventvwr")
def Certificate_Management_Utility():
    os.system("certmgr.msc")
def SQL_SERVER_Client_Network_Utility():
    os.system("cliconfg")
def IP_Address_Detector():
    os.system("Nslookup")
def open_osk():
    os.system("osk")
def Shared_Folder_Manager():
    os.system("fsmgmt.msc")