import mysql.connector
import mySQLdb
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='manasmb', ssh_password='Modi&123',
    remote_bind_address=('manasmb.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user='manasmb',
        passwd='manas4321',
        host='127.0.0.1', port=tunnel.local_bind_port,
        db='manasmb$sitetest',
    )

mydb = mysql.connector.connect(
    host ="manasmb.mysql.pythonanywhere-services.com",
    user = "manasmb",
    passwd = "manas4321"
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE manasmb$sitetest")