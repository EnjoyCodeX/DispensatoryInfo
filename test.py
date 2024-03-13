import requests
from bs4 import BeautifulSoup
import re

# req = requests.get("https://www.yaopinnet.com/huayao1/a1.htm")
# req.encoding = 'utf-8'
# print(req.status_code)
# soup = BeautifulSoup(req.text,'lxml')
# area = soup.find(attrs={'id':'sms_page'})
# # url = '<div id="sms_page">第 <span>1</span><a href="/zhongyao1/a2.htm">2</a> <a href="/zhongyao1/a3.htm">3</a> 页</div>'
# pages = int(re.findall('[\d]+(?=</a>[\s]+页)',str(area))[0])
# print(pages)

# url = "https://www.yaopinnet.com/huayao1/a1.htm"
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text,'lxml')
# area = soup.find(attrs={'id':'c_list2'})
# med = re.findall('[\w]+(?=.htm)',str(area))
# print(med)

# url = "https://www.yaopinnet.com/huayao/hy6122m.htm"
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text,'lxml')
# area = soup.find_all(attrs={'class':'smsli'})
# # print(area)
# print(area,"\n")
# # print(soup.prettify())
# # Med_warning = re.search('【禁忌】(.*?)(?=<)',str(area))
# # print(Med_warning)
# Med_function = re.search('【适应症】<br/>(.*?)(?=<)',str(area))
# if Med_function:
#     Med_function ="【适应症】" + Med_function.group(1).replace('<br/>','') 
# print(Med_function)


# url = "https://www.yaopinnet.com/huayao/hy1028t.htm"
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text,'lxml')
# img = soup.find(attrs={'id':'yaopintupian'})
# img = re.search('(https://[\w./]+)',str(img))
# print(img.group())

# import json

# # # # Python字典
# data = [
#     {
#         "name": "Jane Doe",
#         "age": 25,
#         "is_employee": False
#     },
#     {
#         "name": "Andrew",
#         "age": 25,
#         "is_employee": False
#     }
# ]

# # 将字典转换为JSON格式的字符串
# json_string = json.dumps(data, indent=4)

# # 输出JSON字符串
# # with open('output_data.json', 'w') as file:
# #     json.dump(data, file, indent=4)
# with open('output_data.json','r') as file:
#     data = json.load(file)
# print(data)

# import json
# data = []
# with open('CH_MED_Info.json','r') as file:
#     data = json.load(file) 
# print(data[6558]["Med_name"])

# req = requests.get("https://www.yaopinnet.com/zhongyao/zy4943u.htm")
# req.encoding = 'utf-8'
# print(req.status_code)
# soup = BeautifulSoup(req.text,'lxml')
# # area = soup.find(attrs={'id':'sms_page'})
# # url = '<div id="sms_page">第 <span>1</span><a href="/zhongyao1/a2.htm">2</a> <a href="/zhongyao1/a3.htm">3</a> 页</div>'
# # pages = int(re.findall('[\d]+(?=</a>[\s]+页)',str(area))[0])
# area = soup.find(attrs={"id":"top_nav"})
# project = re.findall('(?!a href)[\u4e00-\u9fa5]+',str(area))
# Med_type = ""
# for name in project:
#     if "科" in name:
#         Med_type = name
# print(Med_type)


# CH_List = ['a','b','c','d','e','f','g','h','j','k','l','m','n','p','q','r','s','t','w','x','y','z']
# count = 0
# for chartype in CH_List:
#     url = "https://www.yaopinnet.com/zhongyao1"+ "/" + chartype + "1.htm"
#     html = requests.get(url)
#     html.encoding = 'utf-8'
#     soup = BeautifulSoup(html.text,'lxml')
#     area = soup.find(attrs={'id':'sms_page'})
#     # 获取当前字母检索页数
#     pages = int(re.findall('[\d]+(?=</a>[\s]+页)',str(area))[0])
#     print(pages,"\n")
#     i = 1
#     while(i <= pages):
#         url = "https://www.yaopinnet.com/zhongyao1/"+ chartype + "{}.htm".format(i)
#         html = requests.get(url)
#         html.encoding = 'utf-8'
#         # 获取 左侧 边栏 药物链接
#         soup = BeautifulSoup(html.text,'lxml')
#         area = soup.find(attrs={'id':'c_list1'})
#         med_left = re.findall('[\w]+(?=.htm)',str(area))
#         # 获取 右侧 边栏 药物链接
#         soup = BeautifulSoup(html.text,'lxml')
#         area = soup.find(attrs={'id':'c_list2'})
#         med_right = re.findall('[\w]+(?=.htm)',str(area))
#         med_list = med_left + med_right
#         for med in med_list:
#             count = count + 1
#         i = i+1
# print(count) # 6559