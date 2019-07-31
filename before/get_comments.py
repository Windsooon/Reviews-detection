import csv
import time
import logging
import requests

from base import get_current_logger

logger = get_current_logger(__name__, 'crawl_error.log', logging.ERROR)

# DATA
MOST_RECENT = 'https://itunes.apple.com/cn/rss/customerreviews/id={0}/sortBy=mostRecent/page={1}/json'
MOST_HELPFUL = 'https://itunes.apple.com/cn/rss/customerreviews/id={0}/sortBy=mostHelpful/page={1}/json'

PAGE = 10

TYPE = ['财务', '儿童', '工具', '购物', '旅游', '美食佳饮', '社交', '体育', '娱乐', '游戏']

# 2019 - 7 - 10 石器时代 -> 一亿小目标
TYPE_LIST = [
    {'财务': {
        '京东金融': 895682747,
        '云闪付': 600273928,
        '中国建设银行': 391965015,
        '360 借条': 1178856715,
        '中国工商银行': 423514795}},
    {'儿童': {
        '伴鱼绘本': 1203189645,
        '叽里呱啦': 928864273,
        '儿歌多多': 894495836,
        '宝宝巴士儿歌': 1278795670,
        '凯叔讲故事': 998790080}},
    {'工具': {
        'TestFlight': 899247664,
        '百度': 382201985,
        '章鱼输入法': 1448813622,
        '酷狗铃声': 1138236198,
        'QQ邮箱': 473225145}},
    {'购物': {
        '拼多多': 1044283059,
        '闲鱼': 510909506,
        '淘宝': 387682726,
        '京东': 414245413,
        '海豚家': 1407705608}},
    {'旅游': {
        '马蜂窝': 406596432,
        '携程旅行': 379395415,
        '哈啰出行': 1165227346,
        '滴滴出行': 554499054,
        '铁路12306': 564818797}},
    {'美食佳饮': {
        '美团外卖': 737310995,
        '饿了么': 507161324,
        '瑞幸咖啡': 1296749505,
        '盒马': 1063183999,
        '每日优鲜': 960158896}},
    {'社交': {
        '小红书': 741292507,
        'QQ': 444934666,
        '微信': 414478124,
        '第一弹': 983337376,
        'Uki': 1298912284}},
    {'体育': {
        '毒': 1012871328,
        '识货': 875177200,
        'nice': 641895599,
        '虎扑': 906632439,
        '腾讯体育': 570608623}},
    {'娱乐': {
        '优酷视频': 336141475,
        '人人视频': 1453979465,
        '腾讯视频': 458318329,
        '爱奇艺': 393765873,
        '西瓜视频': 1134496215}},
    {'游戏': {
        '跑跑卡丁车': 1438842875,
        '权力的游戏': 1342309192,
        '全民漂移': 1453467684,
        '和平精英': 1321803705,
        '一亿小目标': 1347796610}},
]

REVIEW_TYPE = {'most_recent': MOST_RECENT, 'most_helpful': MOST_HELPFUL}

# Custom Header
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko)'}

# Access Data
# for in the app inside APP_LIST
for type in TYPE_LIST:
    for type_name, type_dic in type.items():
        for app_name, app_id in type_dic.items():
            # for in type inside REVIEW_TYPE
            for review_name, review_url in REVIEW_TYPE.items():
                # create a csv file for every type in every app
                review_file = open('{0}/{1}_{2}.csv'.format(type_name, app_name, review_name), 'w')
                review_writer = csv.writer(
                    review_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                # access PAGE number data
                for i in range(1, PAGE+1):
                    logger.info('Writing the number {0} page from {1} to {2}'.format(
                        i, app_name, review_name))
                    try:
                        response = requests.get(review_url.format(app_id, i))
                    except ConnectionResetError:
                        time.sleep(5)
                        # do request again
                        response = requests.get(review_url.format(app_id, i))
                    else:
                        if response.status_code == 200:
                            try:
                                response.json()['feed']['entry']
                            except KeyError:
                                # do request again
                                logger.error('Missed page {0} from {1}'.format(i, app_name))
                            else:
                                for review in response.json()['feed']['entry']:
                                    name = review['author']['name']['label']
                                    rating = review['im:rating']['label']
                                    title = review['title']['label']
                                    content = review['content']['label']
                                    # wrtie data to the csv file
                                    review_writer.writerow([name, rating, title, content])
                        else:
                            logger.error('Error from {0}'.format(app_name))
                            logger.error('Error code is {0}'.format(response.status_code))
                            logger.error('Error message is {0}'.format(response.json()))
                review_file.close()
