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