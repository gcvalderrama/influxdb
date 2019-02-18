from influxdb import InfluxDBClient
import requests
import time
from random import randint
from datetime import datetime
from datetime import timedelta

def send_file():
    start = datetime(2019, 2, 16, 2, 5, 1, 0)
    payload = ""
    for i in range(1, 100):
        start = start + timedelta(milliseconds=i)
        now = int(round(start.timestamp() * 1000000000))
        payload += "http_status,hostname=server02 value={} {} \n".format(randint(100, 501), now)

    res = requests.post(url='http://127.0.0.1:8086/write?db=testdb',
                        data=payload,
                        headers={'Content-Type': 'application/octet-stream'})
    print(res.text)




if __name__ == "__main__":
    send_file()
    '''
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2009-11-10T23:00:00Z",
            "fields": {
                "value": 0.64
            }
        }
    ]
    client = InfluxDBClient('127.0.0.1', 8086, database="testdb")
    databases = client.get_list_database()
    client.create_database("testdb")
    client.create_retention_policy('awesome_policy', '3d', 3, default=True)
    client.write_points(json_body)
    result = client.query('select value from cpu_load_short;')
    print("Result: {0}".format(result))
    client.close()

    '''
