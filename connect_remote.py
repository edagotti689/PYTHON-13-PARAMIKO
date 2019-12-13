    '''
    To install module
python -m pip install paramiko
'''
import paramiko

h_name = '11.12.32.8'
u_name ='admin'
p_word = 'admin123'
port_no = 22

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(h_name, username=u_name, password=p_word, port=port_no)
except :
    raise AssertionError("\n\n Couldn't able to connect host : {0} with credentials -> {1}/{2}".foramt(h_name,u_name,p_word) )


stdin, stdout, stderr = ssh.exec_command('ls /usr/sririam')

print(' stdout is ::', stdout.read())
print(' \nstderr is ::', stderr.read())
#print(' \nstdin is ::', stdin)




'''
SSH = Secure Shell [or] Secure Socket Shell

Secure Shell
SSH stands for Secure Shell. SSH uses port 22 to connect your computer to another computer on the internet. Network administrators will use this technique so they can remote login / remote control a business server in some other part of the city
'''













