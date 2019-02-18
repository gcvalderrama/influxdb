
echo off
rem https://docs.docker.com/network/network-tutorial-standalone/
rem https://docs.docker.com/network/network-tutorial-host/
rem https://docs.docker.com/network/network-tutorial-overlay/
echo on
docker pull influxdb
docker pull chronograf
rem docker run --rm influxdb influxd config > influxdb.conf

docker network create --driver bridge influxdb-net

docker network ls

docker run --rm -d -p 8086:8086 --name influxdb --network influxdb-net -v F:\git\influxdb\server\data:/var/lib/influxdb -v F:\git\influxdb\server\influxdb.conf:/etc/influxdb/influxdb.conf:ro influxdb -config /etc/influxdb/influxdb.conf

docker run --rm -d -p 8888:8888 --name chronograf --network influxdb-net chronograf