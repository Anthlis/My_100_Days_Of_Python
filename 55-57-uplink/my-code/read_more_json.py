import json
str = '''
    {
        "page" : 0,
        "size" : 20,
        "totalCount" : 2,
        "data" : [ {
            "namespace" : "android",
            "id" : "0000001111111",
            "creationTs" : 1516216756819,
            "name" : "Eric's phone",
            "description" : "This device was auto registered by [mqtt] ",
            "tags" : [ ],
            "properties" : { },
            "lastUpdateTs" : 1518610495832,
            "connected" : false,
            "path" : [ ],
            "metadata" : {
                "api_key_id" : "XXX000XXX000XXX",
                "connection_start_time" : "2018-02-14T12:14:04.778Z",
                "mqtt_version" : 4,
                "mqtt_username" : "json+device",
                "mqtt_timeout" : 20,
                "remote_addr" : "00.00.00.00/PORT"
            },
            "groupId" : "root",
            "groupPath" : "/"
        }, {
            "namespace" : "sensor",
            "id" : "temp001",
            "creationTs" : 1520415684605,
            "name" : "mySensor001",
            "description" : "moisture sensor",
            "tags" : [ "france", "lyon" ],
            "properties" : {
                "manufacturer" : "miel",
                "model" : "MoistureSensorV3"
            },
            "lastUpdateTs" : 1520415684605,
            "connected" : false,
            "path" : [ ],
            "groupId" : "root",
            "groupPath" : "/"
    } ]}'''
d = json.loads(str)
print(d)
# {u'totalCount': 2, u'data': [{u'lastUpdateTs': 1518610495832L, u'description': u'This device was auto registered by [mqtt] ', u'tags': [], u'namespace': u'android', u'creationTs': 1516216756819L, u'properties': {}, u'connected': False, u'groupPath': u'/', u'groupId': u'root', u'path': [], u'metadata': {u'api_key_id': u'XXX000XXX000XXX', u'remote_addr': u'00.00.00.00/PORT', u'mqtt_username': u'json+device', u'mqtt_timeout': 20, u'connection_start_time': u'2018-02-14T12:14:04.778Z', u'mqtt_version': 4}, u'id': u'0000001111111', u'name': u"Eric's phone"}, {u'lastUpdateTs': 1520415684605L, u'description': u'moisture sensor', u'tags': [u'france', u'lyon'], u'namespace': u'sensor', u'creationTs': 1520415684605L, u'properties': {u'model': u'MoistureSensorV3', u'manufacturer': u'miel'}, u'connected': False, u'groupPath': u'/', u'groupId': u'root', u'path': [], u'id': u'temp001', u'name': u'mySensor001'}], u'page': 0, u'size': 20}

for i in d['data']:
    print(i['name'])

#
# ...
# Eric's phone
# mySensor001