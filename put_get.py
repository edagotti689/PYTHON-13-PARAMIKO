import paramiko

host_name = '19,98,76,67'
u_name ='admin'
p_word = 'admin123'
port_no = 22

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host_name, username=u_name, password=p_word, port=port_no)
except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials")


# Create FTP object to copy file from local to remote and remote to local
ftp = ssh.open_sftp()

## Copy file from remote machine to local machine
#rsrc = '/usr/sriram/remote.py'
#ldst = r'C:\INST\remote.py'
#ftp.get(rsrc, ldst)

## Copy file from local machine to remote machine
lsrc = r'C:\INST\local.py'
rdst = '/usr/sriram/local.py'
ftp.put(lsrc, rdst)

# close ftp and ssh connections
ftp.close()
ssh.close()