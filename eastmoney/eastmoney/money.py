# import requests
# # import json
# # import re
# #
# # # res = requests.get('http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2017-09-17&ed=2018-09-17&qdii=&tabSubtype=,,,,,&pi=88&pn=50&dx=1').text
# # # allpage = re.search('allPages:(\d+)',res).group(1)
# # # for page in range(int(allpage)):
# # #     url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2017-09-17&ed=2018-09-17&qdii=&tabSubtype=,,,,,&pi=88&pn=50&dx=' + str(page)
# # #     print(url)
# #
# #
# # # response = res.replace('var rankData = ', '').replace(",allRecords:4246,pageIndex:1,pageNum:50,allPages:85,allNum:4246,gpNum:802,hhNum:2233,zqNum:1015,zsNum:535,bbNum:54,qdiiNum:140,etfNum:0,lofNum:213,fofNum:14};",'}').replace('{datas', '{"datas"').split()
# # # replace(",allRecords:4246,pageIndex:1,pageNum:50,allPages:85,allNum:4246,gpNum:802,hhNum:2233,zqNum:1015,zsNum:535,bbNum:54,qdiiNum:140,etfNum:0,lofNum:213,fofNum:14};'","}").
# # # print(response)
# # # for i in response:
# # #     i = json.loads(i)
# # #     print(i)
# # #     print(type(i))
# # #     print(i['datas'])
# #
# # url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2017-09-17&ed=2018-09-17&qdii=&tabSubtype=,,,,,&pi=86&pn=50&dx=1'
# #
# # newpage = re.search('pi=(\d+)',url).group(1)
# # print(newpage)
# #
# #
# # # a  =  {'datas': ['005212,汇安稳裕债券,HAWYZQ,2018-09-17,1.0567,1.0567,4.5927,4.5513,4.3139,4.8730,,,,,,5.67,2018-03-27,1,5.67,0.80%,0.08%,1,0.08%,1,', '004224,南方军工改革灵活配置混合,NFJGGGLHPZHH,2018-09-17,0.6638,0.6638,-0.1204,3.9787,6.3782,1.0504,-16.0491,-31.3405,,,-20.8820,-33.62,2017-03-08,1,-31.6023,1.50%,0.15%,1,0.15%,1,', '573003,诺德增强收益债券,NDZQSYZQ,2018-09-17,1.1090,1.1360,0.0903,3.6448,3.6448,4.2293,5.2182,4.6226,0.3620,-0.6272,5.1185,13.8356,2009-03-04,1,4.5241,0.00%,0.00%,,0.00%,0,10.5683', '162411,华宝标普油气上游股票,HBBPYQSYGP,2018-09-14,0.6970,0.6970,0.2878,3.4125,0,6.0883,28.5978,33.7812,16.7504,25.8123,15.3974,-30.30,2011-09-29,1,,1.50%,0.15%,1,0.15%,1,-35.5823', '003834,华夏能源革新股票,HXNYGXGP,2018-09-17,0.8050,0.8050,-2.0681,3.0730,-4.5077,-18.1911,-26.8847,-32.4097,,,-26.0790,-19.50,2017-06-07,1,-33.4160,1.50%,0.15%,1,0.15%,1,', '004243,广发道琼斯石油指数C,GFDQSSYZSC,2018-09-14,1.2057,1.2057,0.2411,2.7702,-1.0180,7.3069,27.8715,37.2609,,,17.0242,20.57,2017-02-28,1,,,0.00%,,,,', '162719,广发道琼斯石油指数A,GFDQSSYZSA,2018-09-14,1.1988,1.1988,0.2509,2.7602,-1.0809,7.0071,26.9243,36.3357,,,16.1065,19.88,2017-02-28,1,,1.20%,0.12%,1,0.12%,1,', '162416,华宝港股通恒生香港35,HBGGTHSXG35,2018-09-17,0.9992,0.9992,-0.4186,2.7349,-1.4887,-1.4207,,,,,,-0.08,2018-03-30,1,-0.08,1.00%,0.10%,1,0.10%,1,', '163208,诺安油气能源,NAYQNY,2018-09-14,0.9760,0.9760,0.2053,2.4134,-0.7121,4.9462,20.0492,19.4614,14.8235,28.4211,8.4444,-2.40,2011-09-27,1,,1.50%,0.15%,1,0.15%,1,-6.4238', '160416,华安标普全球石油指数,HABPQQSYZS,2018-09-14,1.10,1.14,0.3650,2.3256,-0.3623,6.7961,19.8258,22.3583,23.4569,39.0645,12.1306,14.3180,2012-03-29,1,,1.20%,0.12%,1,0.12%,1,5.0621', '378546,上投摩根全球天然资源混合,STMGQQTRZYHH,2018-09-14,0.7170,0.7170,0.2797,2.2825,-1.6461,-3.4993,5.2863,7.4963,24.6957,48.7552,-0.1393,-28.30,2012-03-26,1,,1.60%,0.16%,1,0.16%,1,-8.8945', '118002,易方达标普消费品指数A,YFDBPXFPZSA,2018-09-14,1.9090,1.9090,0.7920,2.2496,-1.0368,-0.4692,6.3510,13.8342,43.75,44.4024,6.0556,90.90,2012-06-04,1,,1.20%,0.12%,1,0.12%,1,49.0242', '001156,申万菱信新能源汽车混合,SWLXXNYQCHH,2018-09-17,0.7890,0.7890,-1.3750,2.2021,-1.1278,-16.8599,-27.2811,-24.4253,-15.1613,-17.2956,-23.7681,-21.10,2015-05-07,1,-25.4253,1.50%,0.15%,1,0.15%,1,', '000049,中银标普全球资源等权重指数,ZYBPQQZYDQZZS,2018-09-14,1.0980,1.0980,0.2740,2.1395,-1.5247,-1.8767,3.1955,7.4364,23.2323,58.4416,0.3656,9.80,2013-03-19,1,,1.50%,0.15%,1,0.15%,1,8.3909', '000614,华安德国30(DAX)联接,HADG30DAXLJ,2018-09-14,1.1740,1.1740,0.8591,1.9983,-0.0851,-2.8146,-0.6768,-3.2949,16.6998,21.4064,-5.6270,17.40,2014-08-12,1,,1.20%,0.12%,1,0.12%,1,', '161128,易标普信息科技人民币,YBPXXKJRMB,2018-09-14,1.4734,1.4734,-0.1626,1.9231,1.2507,9.7014,15.0644,32.5596,,,21.8089,47.34,2016-12-13,1,,1.20%,0.12%,1,0.12%,1,', '160723,嘉实原油(QDII-LOF),JSYYQDIILOF,2018-09-14,1.3685,1.3685,-0.1168,1.8760,4.4816,11.7873,26.6192,43.8255,,,24.2171,36.85,2017-04-20,1,,1.20%,0.12%,1,0.12%,1,', '501018,南方原油,NFYY,2018-09-14,1.2863,1.2863,-0.2404,1.8690,4.1538,11.6774,26.8165,44.2526,42.0698,,23.4927,28.63,2016-06-15,1,,1.20%,0.12%,1,0.12%,1,', '486002,工银全球精选,GYQQJX,2018-09-14,2.2430,2.2430,0.2234,1.8157,1.4932,7.3206,10.4926,21.9022,41.0692,55.8721,15.6186,124.30,2010-05-25,1,,1.60%,0.16%,1,0.16%,1,102.2543', '161129,易方达原油A类人民币,YFDYYALRMB,2018-09-14,1.3039,1.3039,-0.1532,1.7956,4.0456,12.2117,26.8509,45.6383,,,23.6745,30.39,2016-12-19,1,,1.20%,0.12%,1,0.12%,1,', '003321,易方达原油C类人民币,YFDYYCLRMB,2018-09-14,1.2943,1.2943,-0.1543,1.7932,4.01,12.0897,26.5943,44.9709,,,23.2902,29.43,2016-12-19,1,,,0.00%,,,,', '000041,华夏全球精选,HXQQJX,2018-09-14,1.0710,1.0710,0.4690,1.7094,2.8818,1.5166,2.0972,3.9806,39.0909,40.9211,2,7.10,2007-10-09,1,,1.60%,0.16%,1,0.16%,1,29.9757', '000043,嘉实美国成长股票,JSMGCZGP,2018-09-14,2.04,2.04,-0.0979,1.6949,2.9263,11.7808,18.4669,31.0212,53.1532,65.8537,23.3374,104,2013-06-14,1,,1.50%,0.15%,1,0.15%,1,99.0244', '160213,国泰纳斯达克100指数,GTNSDK100ZS,2018-09-14,3.4850,3.5850,-0.4001,1.6924,0.8391,10.4596,15.2828,30.6222,60.5251,84.9788,22.1521,279.4873,2010-04-29,1,,1.50%,0.15%,1,0.15%,1,161.6365', '160644,鹏华港美互联股票,PHGMHLGP,2018-09-14,0.9160,0.9160,0.6704,1.6761,0.3506,-3.0585,-4.3941,,,,-5.5281,-8.40,2017-11-16,1,,1.50%,0.15%,1,0.15%,1,', '539002,建信新兴市场混合(QDII),JXXXSCHHQDII,2018-09-14,0.9170,0.9170,0.6586,1.6630,0.7692,0.7692,-5.1706,0.7692,21.1361,29.7030,-4.3796,-8.30,2011-06-21,1,,1.60%,0.16%,1,0.16%,1,2.5727', '000834,大成纳斯达克100指数,DCNSDK100ZS,2018-09-14,1.8370,1.8370,-0.3796,1.6602,0.7680,10.1319,14.7408,29.4574,53.9816,70.2502,21.4947,83.70,2014-11-13,1,,1.20%,0.12%,1,0.12%,1,', '003835,鹏华沪深港新兴成长混合,PHHSGXXCZHH,2018-09-17,1.0530,1.0530,-0.2841,1.6409,-0.0949,4.6720,-4.1856,-4.9639,,,-7.8740,5.30,2016-12-02,1,-5.9821,1.50%,0.15%,1,0.15%,1,', '160216,国泰商品,GTSP,2018-09-14,0.5620,0.5620,0,1.6275,3.1193,11.7296,25.7271,45.9740,44.4730,8.4942,23.2456,-43.80,2012-05-03,1,,1.50%,0.15%,1,0.15%,1,-35.4023', '270042,广发纳斯达克100指数,GFNSDK100ZS,2018-09-14,2.3470,2.6170,-0.3397,1.6017,0.6001,9.6217,15.0490,32.0765,60.9739,88.0226,24.0486,184.8899,2012-08-15,1,,1.30%,0.13%,1,0.13%,1,157.3531', '040046,华安纳斯达克100指数,HANSDK100ZS,2018-09-14,2.2970,2.2970,-0.3903,1.5922,0.7898,9.5374,14.85,29.9208,56.3649,76.1503,21.3418,129.70,2013-08-02,1,,1.20%,0.12%,1,0.12%,1,127.6511', '164705,汇添富恒生指数分级,HTFHSZSFJ,2018-09-17,1.1660,1.2660,-0.9346,1.5679,-1.0187,-4.3479,-6.4206,1.3657,18.0826,32.7718,-5.1165,28.2082,2014-03-06,1,0.1682,1.20%,0.12%,1,0.12%,1,', '000988,嘉实全球互联网股票人民币,JSQQHLWGPRMB,2018-09-14,1.49,1.49,0.1344,1.5678,-2.6780,-5.2765,-4.7315,0.9485,44.1006,97.3510,3.9052,49,2015-04-15,1,,1.50%,0.15%,1,0.15%,1,', '270027,广发全球农业指数(QDII),GFQQNYZSQDII,2018-09-14,1.2490,1.2490,0,1.5447,2.2932,4.9580,3.9101,4.1701,16.2942,24.90,-0.5573,24.90,2011-06-28,1,,1.30%,0.13%,1,0.13%,1,31.1975', '160924,大成恒生指数,DCHSZS,2018-09-17,0.99,0.99,-1,1.5385,-1.0989,-4.4402,-7.2165,-0.9009,,,-5.5344,-1,2017-08-10,1,-1.4925,1.20%,0.12%,1,0.12%,1,', '004936,中航混改精选混合A,ZHHGJXHHA,2018-09-17,0.9139,0.9139,0.0328,1.4768,-1.0288,-5.7446,-9.1280,,,,-8.7742,-8.61,2017-12-14,1,-8.61,1.50%,0.15%,1,0.15%,1,', '002193,东方利群混合C,DFLQHHC,2018-09-17,1.1896,1.1896,-0.0252,1.4757,2.7555,-1.9696,-4.7558,-6.7347,-2.4679,,-4.1419,-1.3599,2016-04-20,1,-6.8734,,0.00%,,,,', '004937,中航混改精选混合C,ZHHGJXHHC,2018-09-17,0.9074,0.9074,0.0331,1.4648,-1.0361,-5.8030,-9.3325,,,,-9.4230,-9.26,2017-12-14,1,-9.26,,0.00%,,,,', '000948,华夏沪港通恒生ETF联接A,HXHGTHSETFLJA,2018-09-17,1.2094,1.2094,-1.0068,1.4512,-1.4264,-4.5009,-6.3134,2.1712,19.8969,35.2796,-4.5386,20.94,2015-01-13,1,0.9853,1.20%,0.12%,1,0.12%,1,', '001874,前海开源沪港深价值精选混合,QHKYHGSJZJXHH,2018-09-17,0.9860,1.1560,-0.9045,1.4404,-1.0040,-4.1788,-6.4292,0.8785,,,-4.8797,14.7997,2016-11-18,1,-0.1742,1.50%,0.15%,1,0.15%,1,', '000369,广发全球医疗保健(QDII),GFQQYLBJQDII,2018-09-14,1.4890,1.5990,-0.2679,1.4305,2.1963,14.2748,15.8755,13.9250,25.7601,29.5104,14.3625,63.8307,2013-12-10,1,,1.30%,0.13%,1,0.13%,1,', '004453,前海开源盈鑫A,QHKYYXA,2018-09-17,1.0120,1.0660,0,1.4028,2.9502,8.5837,-0.7843,2.5164,,,-0.8815,6.6292,2017-03-21,1,2.4160,1.50%,0.15%,1,0.15%,1,', '004454,前海开源盈鑫C,QHKYYXC,2018-09-17,1.0190,1.0730,0,1.3930,3.0334,8.5197,-0.7790,3.1997,,,-0.8754,7.3399,2017-03-21,1,3.0986,,0.00%,,,,', '005813,华安CES港股通ETF联接A,HACESGGTETFLJA,2018-09-17,0.9519,0.9519,-1.0293,1.3630,-0.9778,-4.4469,,,,,,-4.81,2018-05-30,1,-4.81,1.20%,0.12%,1,0.12%,1,', '005814,华安CES港股通ETF联接C,HACESGGTETFLJC,2018-09-17,0.9653,0.9653,-1.0456,1.3545,-1.0152,-4.4257,,,,,,-3.47,2018-05-30,1,-3.47,,0.00%,,,,', '501016,国泰中证申万证券行业指数,GTZZSWZQHYZS,2018-09-17,0.7192,0.7192,-0.4292,1.3529,-0.3464,-11.9275,-21.0191,-35.7914,,,-25.0130,-28.08,2017-04-27,1,-36.4889,1.20%,0.12%,1,0.12%,1,', '096001,大成标普500,DCBP500,2018-09-14,1.8810,2.0390,-0.0531,1.3470,1.7306,9.8715,12.9729,17.9688,31.4764,47.7759,10.6084,108.8351,2011-03-23,1,,1.50%,0.15%,1,0.15%,1,75.7871', '162415,华宝标普美国消费人民币,HBBPMGXFRMB,2018-09-14,1.5140,1.5140,-0.4602,1.3387,2.3665,10.2695,17.7294,32.5744,47.4197,,21.8021,51.40,2016-03-18,1,,1.20%,0.12%,1,0.12%,1,', '005659,南方恒指ETF联接C,NFHZETFLJC,2018-09-17,1.03,1.03,-0.9806,1.3381,-1.2275,-4.6296,-6.5251,,,,,3,2018-03-09,1,3,,0.00%,,,,', '160633,鹏华证券分级,PHZQFJ,2018-09-17,0.9860,0.4210,-0.4040,1.3359,-0.5046,-12.4853,-21.9906,-36.4094,-32.9257,-38.9267,-25.7892,-59.3252,2015-05-06,1,-37.0965,1.20%,0.12%,1,0.12%,1,']}
# # #
# # # # print(a['datas']    )
# # # for i in a['datas']:
# # #     print(i)
# #
# # # a = '004224,南方军工改革灵活配置混合,NFJGGGLHPZHH,2018-09-17,0.6638,0.6638,-0.1204,3.9787,6.3782,1.0504,-16.0491,-31.3405,,,-20.8820,-33.62,2017-03-08,1,-31.6023,1.50%,0.15%,1,0.15%,1,'
# # # a = a.split(',')
# # # print(a)
# # # print(len(a))
# # """
# # {datas:["005212,汇安稳裕债券,HAWYZQ,2018-09-17,1.0567,1.0567,4.5927,4.5513,4.3139,4.8730,,,,,,5.67,2018-03-27,1,5.67,0.80%,0.08%,1,0.08%,1,","004224,南方军工改革灵活配置混合,NFJGGGLHPZHH,2018-09-17,0.6638,0.
# # 6638,-0.1204,3.9787,6.3782,1.0504,-16.0491,-31.3405,,,-20.8820,-33.62,2017-03-08,1,-31.6023,1.50%,0.15%,1,0.15%,1,","573003,诺德增强收益债券,NDZQSYZQ,2018-09-17,1.1090,1.1360,0.0903,3.6448,3.6448,4.2293,5.21
# # 82,4.6226,0.3620,-0.6272,5.1185,13.8356,2009-03-04,1,4.5241,0.00%,0.00%,,0.00%,0,10.5683","162411,华宝标普油气上游股票,HBBPYQSYGP,2018-09-14,0.6970,0.6970,0.2878,3.4125,0,6.0883,28.5978,33.7812,16.7504,25.81
# # 23,15.3974,-30.30,2011-09-29,1,,1.50%,0.15%,1,0.15%,1,-35.5823","003834,华夏能源革新股票,HXNYGXGP,2018-09-17,0.8050,0.8050,-2.0681,3.0730,-4.5077,-18.1911,-26.8847,-32.4097,,,-26.0790,-19.50,2017-06-07,1,-33
# # .4160,1.50%,0.15%,1,0.15%,1,","004243,广发道琼斯石油指数C,GFDQSSYZSC,2018-09-14,1.2057,1.2057,0.2411,2.7702,-1.0180,7.3069,27.8715,37.2609,,,17.0242,20.57,2017-02-28,1,,,0.00%,,,,","162719,广发道琼斯石油指数
# # A,GFDQSSYZSA,2018-09-14,1.1988,1.1988,0.2509,2.7602,-1.0809,7.0071,26.9243,36.3357,,,16.1065,19.88,2017-02-28,1,,1.20%,0.12%,1,0.12%,1,","162416,华宝港股通恒生香港35,HBGGTHSXG35,2018-09-17,0.9992,0.9992,-0.4
# # 186,2.7349,-1.4887,-1.4207,,,,,,-0.08,2018-03-30,1,-0.08,1.00%,0.10%,1,0.10%,1,","163208,诺安油气能源,NAYQNY,2018-09-14,0.9760,0.9760,0.2053,2.4134,-0.7121,4.9462,20.0492,19.4614,14.8235,28.4211,8.4444,-2.40
# # ,2011-09-27,1,,1.50%,0.15%,1,0.15%,1,-6.4238","160416,华安标普全球石油指数,HABPQQSYZS,2018-09-14,1.10,1.14,0.3650,2.3256,-0.3623,6.7961,19.8258,22.3583,23.4569,39.0645,12.1306,14.3180,2012-03-29,1,,1.20%,0.1
# # 2%,1,0.12%,1,5.0621","378546,上投摩根全球天然资源混合,STMGQQTRZYHH,2018-09-14,0.7170,0.7170,0.2797,2.2825,-1.6461,-3.4993,5.2863,7.4963,24.6957,48.7552,-0.1393,-28.30,2012-03-26,1,,1.60%,0.16%,1,0.16%,1,-8.8
# # 945","118002,易方达标普消费品指数A,YFDBPXFPZSA,2018-09-14,1.9090,1.9090,0.7920,2.2496,-1.0368,-0.4692,6.3510,13.8342,43.75,44.4024,6.0556,90.90,2012-06-04,1,,1.20%,0.12%,1,0.12%,1,49.0242","001156,申万菱信新
# # 能源汽车混合,SWLXXNYQCHH,2018-09-17,0.7890,0.7890,-1.3750,2.2021,-1.1278,-16.8599,-27.2811,-24.4253,-15.1613,-17.2956,-23.7681,-21.10,2015-05-07,1,-25.4253,1.50%,0.15%,1,0.15%,1,","000049,中银标普全球资源等
# # 权重指数,ZYBPQQZYDQZZS,2018-09-14,1.0980,1.0980,0.2740,2.1395,-1.5247,-1.8767,3.1955,7.4364,23.2323,58.4416,0.3656,9.80,2013-03-19,1,,1.50%,0.15%,1,0.15%,1,8.3909","000614,华安德国30(DAX)联接,HADG30DAXLJ,201
# # 8-09-14,1.1740,1.1740,0.8591,1.9983,-0.0851,-2.8146,-0.6768,-3.2949,16.6998,21.4064,-5.6270,17.40,2014-08-12,1,,1.20%,0.12%,1,0.12%,1,","161128,易标普信息科技人民币,YBPXXKJRMB,2018-09-14,1.4734,1.4734,-0.162
# # 6,1.9231,1.2507,9.7014,15.0644,32.5596,,,21.8089,47.34,2016-12-13,1,,1.20%,0.12%,1,0.12%,1,","160723,嘉实原油(QDII-LOF),JSYYQDIILOF,2018-09-14,1.3685,1.3685,-0.1168,1.8760,4.4816,11.7873,26.6192,43.8255,,,24
# # .2171,36.85,2017-04-20,1,,1.20%,0.12%,1,0.12%,1,","501018,南方原油,NFYY,2018-09-14,1.2863,1.2863,-0.2404,1.8690,4.1538,11.6774,26.8165,44.2526,42.0698,,23.4927,28.63,2016-06-15,1,,1.20%,0.12%,1,0.12%,1,","48
# # 6002,工银全球精选,GYQQJX,2018-09-14,2.2430,2.2430,0.2234,1.8157,1.4932,7.3206,10.4926,21.9022,41.0692,55.8721,15.6186,124.30,2010-05-25,1,,1.60%,0.16%,1,0.16%,1,102.2543","161129,易方达原油A类人民币,YFDYYALR
# # MB,2018-09-14,1.3039,1.3039,-0.1532,1.7956,4.0456,12.2117,26.8509,45.6383,,,23.6745,30.39,2016-12-19,1,,1.20%,0.12%,1,0.12%,1,","003321,易方达原油C类人民币,YFDYYCLRMB,2018-09-14,1.2943,1.2943,-0.1543,1.7932,
# # 4.01,12.0897,26.5943,44.9709,,,23.2902,29.43,2016-12-19,1,,,0.00%,,,,","000041,华夏全球精选,HXQQJX,2018-09-14,1.0710,1.0710,0.4690,1.7094,2.8818,1.5166,2.0972,3.9806,39.0909,40.9211,2,7.10,2007-10-09,1,,1.60
# # %,0.16%,1,0.16%,1,29.9757","000043,嘉实美国成长股票,JSMGCZGP,2018-09-14,2.04,2.04,-0.0979,1.6949,2.9263,11.7808,18.4669,31.0212,53.1532,65.8537,23.3374,104,2013-06-14,1,,1.50%,0.15%,1,0.15%,1,99.0244","16021
# # 3,国泰纳斯达克100指数,GTNSDK100ZS,2018-09-14,3.4850,3.5850,-0.4001,1.6924,0.8391,10.4596,15.2828,30.6222,60.5251,84.9788,22.1521,279.4873,2010-04-29,1,,1.50%,0.15%,1,0.15%,1,161.6365","160644,鹏华港美互联股
# # 票,PHGMHLGP,2018-09-14,0.9160,0.9160,0.6704,1.6761,0.3506,-3.0585,-4.3941,,,,-5.5281,-8.40,2017-11-16,1,,1.50%,0.15%,1,0.15%,1,","539002,建信新兴市场混合(QDII),JXXXSCHHQDII,2018-09-14,0.9170,0.9170,0.6586,1.
# # 6630,0.7692,0.7692,-5.1706,0.7692,21.1361,29.7030,-4.3796,-8.30,2011-06-21,1,,1.60%,0.16%,1,0.16%,1,2.5727","000834,大成纳斯达克100指数,DCNSDK100ZS,2018-09-14,1.8370,1.8370,-0.3796,1.6602,0.7680,10.1319,14.7
# # 408,29.4574,53.9816,70.2502,21.4947,83.70,2014-11-13,1,,1.20%,0.12%,1,0.12%,1,","003835,鹏华沪深港新兴成长混合,PHHSGXXCZHH,2018-09-17,1.0530,1.0530,-0.2841,1.6409,-0.0949,4.6720,-4.1856,-4.9639,,,-7.8740,5.3
# # 0,2016-12-02,1,-5.9821,1.50%,0.15%,1,0.15%,1,","160216,国泰商品,GTSP,2018-09-14,0.5620,0.5620,0,1.6275,3.1193,11.7296,25.7271,45.9740,44.4730,8.4942,23.2456,-43.80,2012-05-03,1,,1.50%,0.15%,1,0.15%,1,-35.402
# # 3","270042,广发纳斯达克100指数,GFNSDK100ZS,2018-09-14,2.3470,2.6170,-0.3397,1.6017,0.6001,9.6217,15.0490,32.0765,60.9739,88.0226,24.0486,184.8899,2012-08-15,1,,1.30%,0.13%,1,0.13%,1,157.3531","040046,华安纳
# # 斯达克100指数,HANSDK100ZS,2018-09-14,2.2970,2.2970,-0.3903,1.5922,0.7898,9.5374,14.85,29.9208,56.3649,76.1503,21.3418,129.70,2013-08-02,1,,1.20%,0.12%,1,0.12%,1,127.6511","164705,汇添富恒生指数分级,HTFHSZSFJ
# # ,2018-09-17,1.1660,1.2660,-0.9346,1.5679,-1.0187,-4.3479,-6.4206,1.3657,18.0826,32.7718,-5.1165,28.2082,2014-03-06,1,0.1682,1.20%,0.12%,1,0.12%,1,","000988,嘉实全球互联网股票人民币,JSQQHLWGPRMB,2018-09-14,1.
# # 49,1.49,0.1344,1.5678,-2.6780,-5.2765,-4.7315,0.9485,44.1006,97.3510,3.9052,49,2015-04-15,1,,1.50%,0.15%,1,0.15%,1,","270027,广发全球农业指数(QDII),GFQQNYZSQDII,2018-09-14,1.2490,1.2490,0,1.5447,2.2932,4.958
# # 0,3.9101,4.1701,16.2942,24.90,-0.5573,24.90,2011-06-28,1,,1.30%,0.13%,1,0.13%,1,31.1975","160924,大成恒生指数,DCHSZS,2018-09-17,0.99,0.99,-1,1.5385,-1.0989,-4.4402,-7.2165,-0.9009,,,-5.5344,-1,2017-08-10,1,-
# # 1.4925,1.20%,0.12%,1,0.12%,1,","004936,中航混改精选混合A,ZHHGJXHHA,2018-09-17,0.9139,0.9139,0.0328,1.4768,-1.0288,-5.7446,-9.1280,,,,-8.7742,-8.61,2017-12-14,1,-8.61,1.50%,0.15%,1,0.15%,1,","002193,东方利群
# # 混合C,DFLQHHC,2018-09-17,1.1896,1.1896,-0.0252,1.4757,2.7555,-1.9696,-4.7558,-6.7347,-2.4679,,-4.1419,-1.3599,2016-04-20,1,-6.8734,,0.00%,,,,","004937,中航混改精选混合C,ZHHGJXHHC,2018-09-17,0.9074,0.9074,0.0
# # 331,1.4648,-1.0361,-5.8030,-9.3325,,,,-9.4230,-9.26,2017-12-14,1,-9.26,,0.00%,,,,","000948,华夏沪港通恒生ETF联接A,HXHGTHSETFLJA,2018-09-17,1.2094,1.2094,-1.0068,1.4512,-1.4264,-4.5009,-6.3134,2.1712,19.8969,
# # 35.2796,-4.5386,20.94,2015-01-13,1,0.9853,1.20%,0.12%,1,0.12%,1,","001874,前海开源沪港深价值精选混合,QHKYHGSJZJXHH,2018-09-17,0.9860,1.1560,-0.9045,1.4404,-1.0040,-4.1788,-6.4292,0.8785,,,-4.8797,14.7997,201
# # 6-11-18,1,-0.1742,1.50%,0.15%,1,0.15%,1,","000369,广发全球医疗保健(QDII),GFQQYLBJQDII,2018-09-14,1.4890,1.5990,-0.2679,1.4305,2.1963,14.2748,15.8755,13.9250,25.7601,29.5104,14.3625,63.8307,2013-12-10,1,,1.30
# # %,0.13%,1,0.13%,1,","004453,前海开源盈鑫A,QHKYYXA,2018-09-17,1.0120,1.0660,0,1.4028,2.9502,8.5837,-0.7843,2.5164,,,-0.8815,6.6292,2017-03-21,1,2.4160,1.50%,0.15%,1,0.15%,1,","004454,前海开源盈鑫C,QHKYYXC,201
# # 8-09-17,1.0190,1.0730,0,1.3930,3.0334,8.5197,-0.7790,3.1997,,,-0.8754,7.3399,2017-03-21,1,3.0986,,0.00%,,,,","005813,华安CES港股通ETF联接A,HACESGGTETFLJA,2018-09-17,0.9519,0.9519,-1.0293,1.3630,-0.9778,-4.44
# # 69,,,,,,-4.81,2018-05-30,1,-4.81,1.20%,0.12%,1,0.12%,1,","005814,华安CES港股通ETF联接C,HACESGGTETFLJC,2018-09-17,0.9653,0.9653,-1.0456,1.3545,-1.0152,-4.4257,,,,,,-3.47,2018-05-30,1,-3.47,,0.00%,,,,","501016
# # ,国泰中证申万证券行业指数,GTZZSWZQHYZS,2018-09-17,0.7192,0.7192,-0.4292,1.3529,-0.3464,-11.9275,-21.0191,-35.7914,,,-25.0130,-28.08,2017-04-27,1,-36.4889,1.20%,0.12%,1,0.12%,1,","096001,大成标普500,DCBP500,2
# # 018-09-14,1.8810,2.0390,-0.0531,1.3470,1.7306,9.8715,12.9729,17.9688,31.4764,47.7759,10.6084,108.8351,2011-03-23,1,,1.50%,0.15%,1,0.15%,1,75.7871","162415,华宝标普美国消费人民币,HBBPMGXFRMB,2018-09-14,1.5140
# # ,1.5140,-0.4602,1.3387,2.3665,10.2695,17.7294,32.5744,47.4197,,21.8021,51.40,2016-03-18,1,,1.20%,0.12%,1,0.12%,1,","005659,南方恒指ETF联接C,NFHZETFLJC,2018-09-17,1.03,1.03,-0.9806,1.3381,-1.2275,-4.6296,-6.5
# # 251,,,,,3,2018-03-09,1,3,,0.00%,,,,","160633,鹏华证券分级,PHZQFJ,2018-09-17,0.9860,0.4210,-0.4040,1.3359,-0.5046,-12.4853,-21.9906,-36.4094,-32.9257,-38.9267,-25.7892,-59.3252,2015-05-06,1,-37.0965,1.20%,0.1
# # 2%,1,0.12%,1,"}
# #
# # """


# import base64
#
# import re
# from urllib.parse import unquote
# import urllib3
#
# import requests
#
#
# def convert_thunder_url(thunder_url):
#     request_url = "https://tool.lu/urlconvert/ajax.html"
#
#     params = {
#         "link": thunder_url
#     }
#
#     res = requests.post(request_url, params=params).json()
#     http_str = res['text']['http']
#     return http_str
#
#
# def jie_ma(http_str):
#     print(unquote(http_str))
#
#
# def convert_2(thunder_url):
#     tmp = thunder_url.replace('thunder://', '')
#     http_str = base64.b64decode(tmp.encode()).decode('gbk')[2:-2]
#     return http_str
#
#
# if __name__ == '__main__':
#     print("将迅雷链接转换为真实地址:")
#
#     while True:
#         thunder_url = input("请输入迅雷链接:")
#         http_str = convert_2(thunder_url)
#         jie_ma(http_str)


import os
str = 'you-get http://www.acfun.cn/v/ac4230409 --debug'
mystr = os.popen(str)
mystr = mystr.read()
print(mystr)
