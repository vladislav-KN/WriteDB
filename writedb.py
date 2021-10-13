import time
from writeinfluxe import WriteInflux

time_influx = int(time*1000000000)
field_name = "fild_name"
measurements = "Table1"
json = [{
    "measurements": measurements,
    "time": time_influx,
    "fields":
    {
            field_name: "1"
    }
}]
insert = WriteInflux(json)
