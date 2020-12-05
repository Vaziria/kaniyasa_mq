import time

from kaniyasa import Kaniyasa, RabbitCon
from kaniyasa.campaign import IklanProducer, Akun

app = Kaniyasa()
app.config['rabbitmq_server'] = '192.168.1.2'
app.config['rabbitmq_user'] = 'rabbitmq'
app.config['rabbitmq_password'] = 'rabbitmq'

con = RabbitCon()
prod = IklanProducer(con)

akun = Akun(2, 'Heri Santoso', 'asdasdas@gmail.com', 'asdasdasdgsadsasasdasdasdasd')


con.init_app(app)
con.channel.queue_declare(queue='ads')

for c in range(0, 10):
	prod.update_akun(akun)
	print(" [ {} ] Sent {}".format(c, akun))