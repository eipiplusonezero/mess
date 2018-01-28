import os
import requests
from lxml import html


def mag_data():
  magnum_site_id = os.getenv('MAGNUM_SITE_ID')
  base_url = 'http://data.magnumenergy.com'
  url = '/'.join([base_url, magnum_site_id])
  page = requests.get(url)
  tree = html.fromstring(page.content)
  date = tree.xpath('//span[@id="dataDate"]/text()')[0]
  battery_charge_percent_raw = tree.xpath('//span[@id="battCharge"]/text()')[0]
  battery_charge_percent = int(battery_charge_percent_raw.lstrip().replace('%',''))
  volts_amps = tree.xpath('//span[@id="voltsAmps"]/text()')[0]
  net_power_w = int(volts_amps.split('(')[1].split(' ')[0])
  return {'battery_charge_percent': battery_charge_percent,
          'net_power_w': net_power_w,
          'date': date}




