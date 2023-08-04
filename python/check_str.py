import sys
import argparse
# 1.how to write main func
# 2.how to parse command line
# 3.how to print format
# 4.some file operation
if __name__ == '__main__':  
    parser = argparse.ArgumentParser(description='input file to be checked')
    parser.add_argument('str',type = str, help = 'input file to be checked')
    args = parser.parse_args()
    file_name = args.str 
    print('file_name is %s' % file_name)
    dict_file = open(file_name)
    dict_name = dict_file.read()
    name_array_str = "pm_query_subsku_cid_dict,pm_degrade_predictor_pos_dict,media_index_dump_v2,pos_logical_control_list,pm_sku_black_list_dict,pm_sku_white_list_dict,google_adx_black_cid3_list,toutiao_adx_black_cid3_list,adx_cid3_black_list,pm_black_cid_dict,pm_advertiser_cid3_white_dict,pm_stock_white_list_dict,xiaomi_adx_black_cid3_list,baidubaichuan_adx_black_cid3_list,pm_black_cid_for_advertiser_dict,pm_black_cid_dict_v2,pm_black_brand_id,pm_black_shop_id,pm_black_brand_id,pm_black_shop_id,oppo_adx_cid3_black_list,dragon_shopping_ad_pos_id_dict,worldwide_cid3_blacklist,bilibili_adx_cid3_black_list,qingting_fm_cid3_black_list,sku_category,dmp_base_dimension_dict,media_channel,color_size,brands,palantir_exp_dict,ip_location_list_new,ad_unrepeat_purchase_info,brand_key_list,brand_cate_dict,city_id_2_stock_bit_dict,vend_price_limit,outside_tcpa_tuning_dict,cid3_price_interval_dict,vender_score_info,spu_info,urlcid_jdcid,cid_expand_info,pm_spu_remove_duplicate_white_list,pm_adx_ctr_conf,pm_adx_ctr_conf_posid,midpage_nature_info"
    name_array = str.split(name_array_str, ',')
    for name in name_array:
        if dict_name.find(name) == -1:
           # print("%s not in file %s" %(name, file_name))
           print(name)
