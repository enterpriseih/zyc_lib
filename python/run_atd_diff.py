import json
import os

def diff(base_json, test_json):
  base_res = json.loads(base_json)
  test_res = json.loads(test_json)
  # parse test t
  ad_response_num_base = "0"
  ad_response_num_test = "0"
  base_ad_group_ids = []
  test_ad_group_ids = []
  if "querys" in test_res:
    querys = test_res["querys"]
    res0 = querys[0]
    pos_id = res0["pos_id"]
    posinfo = res0["posinfo"]
    ad_response_num_test = str(posinfo["ad_response_num"])
    if ad_response_num_test != "0":
      test_ad_array = querys[0]["mats"]
      test_ad_group_ids = get_ad_groups(test_ad_array)
  # print("test ad groups:")
  # print(test_ad_group_ids)
  # parse base atd
  if "Count" in base_res:
    pos_id = next(iter(base_res["Count"]))
    PosAdInfo = base_res["PosAdInfo"]
    res1 = PosAdInfo[pos_id]
    ad_response_num_base = res1["ad_response_num"] 
    #print(ad_response_num_base)
    if ad_response_num_base != "0":
      Query = base_res["Query"]
      base_ad_array = Query[str(pos_id)]
      base_ad_group_ids = get_ad_groups(base_ad_array)
  # print("base ad groups:")
  # print(base_ad_group_ids)
  #print(ad_response_num)
  base_set = set(base_ad_group_ids)
  test_set = set(test_ad_group_ids)
  base_ad_group_ids = list(base_set)
  test_ad_group_ids = list(test_set)

  base_ad_group_ids.sort()
  test_ad_group_ids.sort()

  if (ad_response_num_base != ad_response_num_test):
     # print(type(ad_response_num_base))
     # print(type(ad_response_num_test))
      print("res num diff")
      print("base is: %s" %ad_response_num_base)
      print("test is: %s" %ad_response_num_test)
  if test_ad_group_ids == base_ad_group_ids: 
    return False 
  print("adgroups diff")
  print("base ad groups: ")
  print(base_ad_group_ids)
  print("test ad groups: ")
  print(test_ad_group_ids)
  if len(base_ad_group_ids) == 30:
    return False
  return True

def get_base_ad_num(base_json):
  base_res = json.loads(base_json)
  Count = base_res["Count"]
  for obj in Count:
      pos_id = obj
  PosAdInfo = base_res["PosAdInfo"]
  res1 = PosAdInfo[str(pos_id)]
  ad_response_num_base = res1["ad_response_num"] 
  return ad_response_num_base

def get_test_ad_num(test_json):
  test_res = json.loads(test_json)
  querys = test_res["querys"]
  res0 = querys[0]
  pos_id = res0["pos_id"]
  posinfo = res0["posinfo"]
  ad_response_num_test = str(posinfo["ad_response_num"])
  return ad_response_num_test

def load_result(file_name):
  request = []
  result = []
  result_file = open(file_name, 'r')
  all_lines = result_file.readlines()
  one_result = ""
  for line in all_lines:
    if line.startswith("http"):
      request.append(line)
      continue
    one_result += line
    #print(one_result)
    if line.startswith("}"):
      result.append(one_result)
      one_result = ""
  # print(result[0])
  return [request, result]

def get_ad_groups(ad_array):
    result = []
    for ad in ad_array:
        result.append(str(ad["ad_group_id"]))
    return result

def Run(base_file, test_file):
   base_request, base_result = load_result(base_file)
   test_request, test_result = load_result(test_file) 
   result_num = len(base_result)
   diff_num = 0
   for i in range(result_num):
     if diff(base_result[i], test_result[i]):
       diff_num += 1
       print("base request is: %s" %base_request[i])
       print("test request is: %s" %test_request[i])
   #rint("total reques num is: %s" %result_num)
   #print("diff reques num is: %s" %diff_num)
   #print("diff ratio is: %f" %(diff_num *1.0 / result_num)) 
   return diff_num, result_num

def RunDiff(index):
  base_path = "/export/servers/diff_test/querydiff/result/%s/diff/" %(index)
  print(base_path)
  diff_file = os.listdir(base_path)
  base_file = ""
  test_file = ""
  for file in diff_file:
    if file.count("old") == 1:
      base_file = file
    elif file.count("new") == 1:
      test_file = file
  #print(base_file)
  #print(test_file)
  return Run(base_path + base_file, base_path + test_file)


def AnalizeResult(result_array):
  total_request = 0
  total_diff = 0 
  for one_result in result_array:
    total_diff += one_result[0]
    total_request += one_result[1]
  print("total request is: %d" %total_request)
  print("total diff is: %d" %total_diff)
  print("diff ratio is: %f" %(total_diff / total_request))

if __name__ == '__main__':
   # base_file = open("/Users/zhangyichi/workplace/zyc_lib/python/base.json")
   # test_file = open("/Users/zhangyichi/workplace/zyc_lib/python/test.json")
   # base = base_file.read()
   # test = test_file.read()
   # base_ad_num = get_base_ad_num(base)
   # test_ad_num = get_test_ad_num(test) 
   # #print (base_ad_num) #print (test_ad_num)
   # diff(base, test)
   #Run("/Users/zhangyichi/workplace/zyc_lib/python/10.207.150.162_12231.old",
    #   "/Users/zhangyichi/workplace/zyc_lib/python/10.207.151.3_12231.new")
   result_array = []
   for i in range(30):
     result_array.append(RunDiff(i))
   AnalizeResult(result_array) 