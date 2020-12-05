import time
from datetime import datetime

from ..kaniyasa import Kaniyasa, RabbitCon
from ..kaniyasa.campaign import IklanProducer, Akun, AddAcount, Campaign

app = Kaniyasa()
app.config['rabbitmq_server'] = '192.168.1.2'
app.config['rabbitmq_user'] = 'rabbitmq'
app.config['rabbitmq_password'] = 'rabbitmq'

con = RabbitCon()
prod = IklanProducer(con)



con.init_app(app)
con.channel.queue_declare(queue='database')

for c in range(0, 10):
	akun = AddAcount(c, 'bambang {}'.format(c), datetime.utcnow())
	
	prod.send('database', 'update_ad_account', akun)
	print(" [ {} ] Sent {}".format(c, akun))

# sending campaign
for c in range(0, 10):
	data = Campaign(c, c, '', 'name campaign {}'.format(c), 'asd', 1200, 12000, 2, datetime.utcnow())
	
	prod.send('database', 'update_campaign', data)
	print(" [ {} ] Sent {}".format(c, data))