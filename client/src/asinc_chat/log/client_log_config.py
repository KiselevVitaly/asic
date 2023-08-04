import logging
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
log_dir = os.path.join(current_dir, 'logs')
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
logging_file = os.path.join(log_dir, 'client.log')
print(f'Логирование настроено в {logging_file}')

logging.basicConfig(
    filename=logging_file,
    format='%(asctime)s %(levelname)s %(module)s %(funcName)s: %(message)s',
    level=logging.INFO
)

log = logging.getLogger('client')

_format = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s: %(message)s')

# CRITICAL
crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(_format)

applog_hand = logging.FileHandler(logging_file, encoding='utf-8')
applog_hand.setFormatter(_format)
applog_hand.setLevel(logging.DEBUG)

log.addHandler(applog_hand)
log.addHandler(crit_hand)
log.setLevel(logging.INFO)

if __name__ == '__main__':
    console = logging.StreamHandler(sys.stderr)
    console.setLevel(logging.DEBUG)
    console.setFormatter(_format)
    log.addHandler(console)
    log.info('Тестовый запуск логирования')
    log.critical('critical!')
    log.error('error!')
    log.warning('warning!')
    log.info('info!')
    log.debug('debug!')
