db_url = 'sqlite:///db.sqlite'

ref_pay_perc_1lvl=0.09  #������� ������� �� 1 ������� ��������� �� ������
ref_pay_perc_2lvl=0.03  #������� ������� �� 2 ������� ��������� �� ������
ref_view_pay_1lvl=0.15  #������� ������� �� 1 ������� ��������� �� ��������
ref_view_pay_2lvl=0.05  #������� ������� �� 2 ������� ��������� �� ��������
new_ref_cost=0.30       #�������������� �� ������ ��������.� ��������.
user_view_perc=0.40  #������� ������� ������������ �� ����������(�������� �� ��������� ������������� ����������)
min_out_pay=20  #����������� ����� ��� ������
min_post_cost=0.4  #����������� ��������� 1 ����������
user_post_perc=0.40 #������� �� ���� ���������  
user_timewait_sec=6  #����� ��������� �����
min_view_cost=0.05   #����������� ��������� 1 ���������


number = +7
qiwi_token = 'qiwi_token'

ya_number = +7
ya_token = 'yandex_token'

telegram_token='telegram_token'

uah_to_rub = 2.16
usd_to_rub = 57.85
eur_to_rub = 67.73

admins = []
bans = []

tutorial_url = 'https'

WEBHOOK_HOST = 'xx.xxx.xxx.xx'
WEBHOOK_PORT = 8000
WEBHOOK_LISTEN = '127.0.0.1'

WEBHOOK_SSL_CERT = '/etc/nginx/keys/webhook_cert.key'
WEBHOOK_SSL_PRIV = '/etc/nginx/keys/webhook_pkey.pem'

WEBHOOK_URL_BASE = "https://{}:443".format(WEBHOOK_HOST)
WEBHOOK_URL_PATH = "/ppdemo/{}/".format(telegram_token)

out_comment = ""
