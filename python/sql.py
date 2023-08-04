import mysql.connector
import json
import configparser

class DataSource:
  def __init__(self, msg_type, topic):
    self.msg_type = msg_type
    self.topic = topic

class DataVisionMeta: 
  def __init__(self):
    self.data_name = ''
    self.data_max_length = 0
    self.data_max_time = 0
    self.is_snappy = 0
    self.data_schema = ""
    self.delay_time = 0
    self.data_dimension = [] 
    self.producer = []
    self.consumer = []
    self.business_line = ""
    self.data_source = DataSource("", "")
    self.star_map_path = ""
    self.owner = ""
    self.data_desc = ""
    self.data_attr = ""

  def gen_data_attr(self):
    attr_json = {}
    attr_json["data_max_length"] = self.data_max_length
    attr_json["is_snapy"] = self.is_snapy
    attr_json["owner"] = self.owner
    attr_json["data_max_time"] = self.data_max_time
    attr_json["data_schema"] = self.data_schema
    attr_json["delay_time"] = self.delay_time
    attr_json["data_dimension"] = self.data_dimension
    attr_json["data_name"] = self.data_name
    attr_json["producer"] = self.producer
    attr_json["consumer"] = self.consumer
    attr_json["business_line"] = self.business_line
    attr_json["apply_for"] = self.apply_for
    attr_json["data_source"] = {}
    attr_json["data_source"]["msg_type"] = self.data_source.msg_type
    attr_json["data_source"]["topic"] = self.data_source.topic
    attr_json["star_map_path"] = self.star_map_path
    self.data_attr = json.dumps(attr_json)

  def gen_sql_value(self):
    self.gen_data_attr()
    result = []
    result.append(self.data_name)
    result.append(self.owner)
    result.append(self.data_desc)
    result.append(self.data_attr)
    return tuple(result)
    
  def init(self, data_name,conf):
    self.data_max_length = conf["data_max_length"]
    self.is_snapy= conf["is_snapy"]
    self.owner = conf["owner"]
    self.data_max_time = conf["data_max_time"]
    self.data_schema = conf["data_schema"]
    self.delay_time = conf["delay_time"]
    self.data_dimension = conf["data_dimension"]
    self.data_name = data_name
    self.producer = conf["producer"]
    self.consumer = conf["consumer"]
    self.business_line = conf["business_line"]
    self.apply_for = conf["apply_for"]
    self.data_source.msg_type = conf["msg_type"]
    self.data_source.topic = conf["topic"]
    self.star_map_path= conf["star_map_path"]

def getAttr(db,data_name):
 sql = "select from data_vision_meta_table where data_name = %s" %data_name
 print(sql)
 mycursor = db.cursor()
 mycursor.execute(sql)

def insertData(db):
  conf_path = "./sql_data.ini"
  conf = configparser.ConfigParser()
  conf.read(conf_path, encoding="utf-8") 
  data_names = conf["data_names"]["all_data"]
  for one_name in data_names.split(","):
    one_meta = DataVisionMeta()
    one_meta.init(one_name, conf[one_name])
    sql = "replace into data_vision_meta_table (data_name, owner, data_desc, data_attr) VALUES (%s, %s, %s, %s)"
    mycursor = db.cursor()
    mycursor.execute(sql, one_meta.gen_sql_value())
  db.commit()

if __name__ == '__main__':
  db = mysql.connector.connect(
    host="gateht111a.jed.jddb.com",
    user="star_shine_test_rw",
    password="SY8yQ8VRm9oolOvM",
    port=3358
  )
  #insertData(db)

