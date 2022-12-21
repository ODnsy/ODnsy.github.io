import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

folder_name='c:/research_temp/'
file_list=['vis.csv','lis.csv','obj.csv','sme.csv','tou.csv']
dict=[]
for file_name in file_list:
  df = pd.read_csv(str(folder_name+file_name),encoding='utf-8-sig')
  result = []
  for element in df.values.tolist():
      result.extend(element)
  dict.append(result)

print(len(dict))

text_1="我有一個四四方方咖啡色的背包，前面有粉紅的卡通圖案，旁邊掛著可愛的鈴鐺，每當我拿起背包時，便會叮叮咚咚作響。這個背包質地輕柔，摸起來柔軟舒適，是我最喜歡的背包。"
text_2="我有一件紫色的外套，前面繡著花紋，後面有美麗的花邊圖案，領口還有毛絨絨的絲質圍巾，摸起來非常輕柔，有淡淡的香味，這是媽媽送給我的生日禮物，也是我最喜歡的衣服。"
text_3="我有一支鉛筆，外型細細圓圓的，有著五彩繽紛的外表，上面還鑲著金黃的亮片，遠遠看去閃閃發亮，摸起來光滑細緻，帶著淡淡的香水味，是我最喜歡的一支鉛筆。"
text_4="我有一個洋娃娃，金黃色的頭髮，水汪汪的眼睛，櫻桃小嘴，白皙的皮膚，穿著一件紅黃相間的洋裝，是媽媽送給我的禮物。"
text_5="升上三年級後，媽媽送給我一個嶄新的書包，紅色的外型代表濃濃的喜氣，寬寬大大的身體可以裝進我的書和文具，旁邊還有一對紫色小鈴鐺，每當我一走動，就會發出叮叮咚咚的聲響。這個書包的質地輕柔，摸起來光滑柔順，是我上學的好夥伴，它是我最喜歡的書包。"
def cut_sentence(sentence):
  s = re.split('。|，|；', sentence)
  if s[len(s)-1] == "":
    s.pop() #去掉最後一個空值
  return(s)
sentence_test_1=cut_sentence(text_1)
sentence_test_2=cut_sentence(text_2)
sentence_test_3=cut_sentence(text_3)
sentence_test_4=cut_sentence(text_4)
sentence_test_5=cut_sentence(text_5)

def get_dict(sentence,dict,dict_add):
  count_dict=0
  for i in range (len(sentence)):
    for j in range (len(dict)):
      if(sentence[i].find(dict[j])>-1):
        sentence[i]+=dict_add
        count_dict+=1
        break
  return(sentence,count_dict)

def show_dict(sentence_dict):
  dict_c=["(視覺)","(聽覺)","(形狀大小)","(味覺和嗅覺)","(觸覺)"]
  dict_p=[]
  for d in dict_c:
    result=get_dict(sentence_dict,dict[dict_c.index(d)],d)
    dict_p.append(result[1])
  return(result[0],dict_p)

result=show_dict(sentence_test_1)
print(result[0])
print(result[1])


votes=result[1]           #2020總統大選得票數
candidates=["(視覺)","(聽覺)","(形狀大小)","(味覺和嗅覺)","(觸覺)"]  #X軸刻度
print(candidates)
x=np.arange(len(candidates))                     #產生X軸座標序列
plt.bar(x, votes, tick_label=candidates)     #繪製長條圖
plt.title('2020 Presidential Election')          #設定圖形標題
plt.xlabel('Candidates')                               #設定X軸標籤
plt.ylabel('Votes(million)')                          #設定Y軸標籤
plt.show()

