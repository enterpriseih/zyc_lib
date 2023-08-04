
if __name__ == '__main__':
  campaign_bidding_map = {
    2:[1,2,256,8192],
    3:[2,256],
    28:[1,2,256,8192],
    55:[256],
    61:[256],
    63:[256],
    65:[256],
    68:[256],
    84:[2],
    86:[256],
    92:[2,256],
  }

  #print(campaign_bidding_map)
  sort_map = dict(sorted(campaign_bidding_map.items()))
  #print(sort_map)

  result = ''
  map = []
  for campaign, bidding_types in sort_map.items():
    for bidding_type in bidding_types:
      result = campaign*100 + bidding_type
      if result not in map:
       print("no dup:")
       print(result)
       map.append(result)
      else:
       print("dup :")
       print(campaign)
       print(bidding_type)
       print(result)
   
