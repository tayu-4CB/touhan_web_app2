from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
import time
import pprint
import collections as cl
import json

driver = webdriver.Chrome('chromedriver.exe')

#辞書オブジェクトを作成
data_dict = cl.OrderedDict()
data_dict = {
    "chapter1":{
        "number1":{
            "scope":"", "title":"", "choice":[], "option":[], "answer":0, "explanation":[]
            }
    }, 
    "chapter2":{}, 
    "chapter3":{}, 
    "chapter4":{}, 
    "chapter5":{}
}

for j in range(1,6):
    for i in range(1, 21):
        data_dict[f"chapter{j}"][f"number{i}"] = {"scope":"", "title":"", "choice":[], "option":[], "answer":0, "explanation":[]}
data_dict["chapter3"]["number3"] = {}
for i in range(1, 41):
    data_dict["chapter3"][f"number{i}"] = {"scope":"", "title":"", "choice":[], "option":[], "answer":0, "explanation":[]}
        
    
#pprint.pprint(data_dict, indent=4)

driver.get("https://www.35189.jp/test/shutoken_r4/?no=tab1")

test_chapter_title = driver.find_elements(by=By.CLASS_NAME, value='test_chapter_title')
test_question_titles = driver.find_elements(by=By.CLASS_NAME, value='test_question_title')
test_question_choices = driver.find_elements(by=By.CLASS_NAME, value='test_question')
test_combi = driver.find_elements(by=By.CLASS_NAME, value='test_combi')

print("#")


#第１章
#問題の章を取得 (第１章　医薬品に共通する特性と基本的な知識)
for elem in test_chapter_title[:1]:
    try:
        scope = elem.text.replace("　", ":")
        print(scope)
    except:
        pass
for i in range(1, 21):
    data_dict["chapter1"][f"number{i}"]["scope"] = scope
    
print("#")

#問題番号と設問を取得 
#1
#医薬品の本質に関する次の記述のうち、正しいものの組合せはどれか。
for elem in test_question_titles[:20]:
    try:
        question = elem.text
        num = int(question.split(" ")[1].split("　")[0])
        title = question.split(" ")[1].split("　")[1]
        print(num)
        print(title)
        data_dict["chapter1"][f"number{num}"]["title"] = title
    except:
        pass
    time.sleep(0.2)
    
print("#")

#設問の選択肢を取得
#['a 一般用医薬品は、効能効果、用法用量、副作用等の情報を購入者等に適切に伝達するため、添付文書や製品表示に必要な情報が記載されている。', 'b 医薬品は、人の疾病の診断、治療若しくは予防に使用されること、又は人の身体の構造や機能に影響を及ぼすことを目的とする生命関連製品である。', 'c 一般用医薬品は、一 般の生活者が自ら選択し、使用するものであり、添付文書を見れば、効能効果や副作用等について誤解や認識不足を生じることはない。', 'd 検査薬の検査結果については、正しい解釈や判断がなされなくても、適切な治療を受ける機会を失うおそれはない。']
i = 1
for elem in test_question_choices[:20]:
    try:
        choice = elem.text
        choice = choice.splitlines()
        data_dict["chapter1"][f"number{i}"]["choice"] = choice
        print(choice)
        i += 1
    except:
        pass
    time.sleep(0.2)
    
print("#")

i = 1
#解答の選択肢を取得
#['1 :（ａ、ｂ）', '2 :（ａ、ｃ）', '3 :（ａ、ｄ）', '4 :（ｂ、ｃ）', '5 :（ｃ、ｄ）']
for elem in test_combi[:20]:
    try:
        print(i)
        option = elem.text
        option = option.splitlines()
        option = "!".join(option) 
        if "（" in option:
            option = list(map(lambda x: x.replace("（"," :（"), option.split(" ")))
        else:
            option = list(map(lambda x: x.replace(" "," : ").replace("\u3000", " "), option.split("!")))[1:]
        data_dict["chapter1"][f"number{i}"]["option"] = option
        print(option)
        i += 1
    except:
        pass
    time.sleep(0.2)


#第２章
driver.get("https://www.35189.jp/test/shutoken_r4/?no=tab2")
time.sleep(1)
test_chapter_title = driver.find_elements(by=By.CLASS_NAME, value='test_chapter_title')
test_question_titles = driver.find_elements(by=By.CLASS_NAME, value='test_question_title')
test_question_choices = driver.find_elements(by=By.CLASS_NAME, value='test_question')
test_combi = driver.find_elements(by=By.CLASS_NAME, value='test_combi')

print("#")

#問題の章を取得 (第１章　医薬品に共通する特性と基本的な知識)
for elem in test_chapter_title[1:2]:
    try:
        scope = elem.text.replace("　", ":")
        print(scope)
    except:
        pass
for i in range(1, 21):
    data_dict["chapter2"][f"number{i}"]["scope"] = scope
    
print("#")

#問題番号と設問を取得 
#1
#医薬品の本質に関する次の記述のうち、正しいものの組合せはどれか。
for elem in test_question_titles[20:40]:
    try:
        question = elem.text
        num = int(question.split(" ")[1].split("　")[0])
        title = question.split(" ")[1].split("　")[1]
        print(num)
        print(title)
        data_dict["chapter2"][f"number{num}"]["title"] = title
    except:
        pass
    time.sleep(0.2)
    
print("#")

#設問の選択肢を取得
#['a 一般用医薬品は、効能効果、用法用量、副作用等の情報を購入者等に適切に伝達するため、添付文書や製品表示に必要な情報が記載されている。', 'b 医薬品は、人の疾病の診断、治療若しくは予防に使用されること、又は人の身体の構造や機能に影響を及ぼすことを目的とする生命関連製品である。', 'c 一般用医薬品は、一 般の生活者が自ら選択し、使用するものであり、添付文書を見れば、効能効果や副作用等について誤解や認識不足を生じることはない。', 'd 検査薬の検査結果については、正しい解釈や判断がなされなくても、適切な治療を受ける機会を失うおそれはない。']
i = 1
for elem in test_question_choices[20:40]:
    try:
        choice = elem.text
        choice = choice.splitlines()
        data_dict["chapter2"][f"number{i}"]["choice"] = choice
        print(choice)
        i += 1
    except:
        pass
    time.sleep(0.2)
    
print("#")

i = 1
#解答の選択肢を取得
#['1 :（ａ、ｂ）', '2 :（ａ、ｃ）', '3 :（ａ、ｄ）', '4 :（ｂ、ｃ）', '5 :（ｃ、ｄ）']
for elem in test_combi[20:40]:
    try:
        print(i)
        option = elem.text
        option = option.splitlines()
        option = "!".join(option) 
        if "（" in option:
            option = list(map(lambda x: x.replace("（"," :（"), option.split(" ")))
        else:
            option = list(map(lambda x: x.replace(" "," : ").replace("\u3000", " "), option.split("!")))[1:]
        data_dict["chapter2"][f"number{i}"]["option"] = option
        print(option)
        i += 1
    except:
        pass
    time.sleep(0.2)



#第３章
driver.get("https://www.35189.jp/test/shutoken_r4/?no=tab3")
time.sleep(1)
test_chapter_title = driver.find_elements(by=By.CLASS_NAME, value='test_chapter_title')
test_question_titles = driver.find_elements(by=By.CLASS_NAME, value='test_question_title')
test_question_choices = driver.find_elements(by=By.CLASS_NAME, value='test_question')
test_combi = driver.find_elements(by=By.CLASS_NAME, value='test_combi')

print("#")

#問題の章を取得 (第１章　医薬品に共通する特性と基本的な知識)
for elem in test_chapter_title[2:3]:
    try:
        scope = elem.text.replace("　", ":")
        print(scope)
    except:
        pass
print(scope)
for i in range(1, 41):
    data_dict["chapter3"][f"number{i}"]["scope"] = scope
    
print("#")

#問題番号と設問を取得 
#1
#医薬品の本質に関する次の記述のうち、正しいものの組合せはどれか。
for elem in test_question_titles[40:80]:
    try:
        question = elem.text
        num = int(question.split(" ")[1].split("　")[0])
        title = question.split(" ")[1].split("　")[1]
        print(num)
        print(title)
        data_dict["chapter3"][f"number{num}"]["title"] = title
    except:
        pass
    time.sleep(0.2)
    
print("#")

#設問の選択肢を取得
#['a 一般用医薬品は、効能効果、用法用量、副作用等の情報を購入者等に適切に伝達するため、添付文書や製品表示に必要な情報が記載されている。', 'b 医薬品は、人の疾病の診断、治療若しくは予防に使用されること、又は人の身体の構造や機能に影響を及ぼすことを目的とする生命関連製品である。', 'c 一般用医薬品は、一 般の生活者が自ら選択し、使用するものであり、添付文書を見れば、効能効果や副作用等について誤解や認識不足を生じることはない。', 'd 検査薬の検査結果については、正しい解釈や判断がなされなくても、適切な治療を受ける機会を失うおそれはない。']
i = 1
for elem in test_question_choices[40:80]:
    try:
        choice = elem.text
        choice = choice.splitlines()
        data_dict["chapter3"][f"number{i}"]["choice"] = choice
        print(choice)
        i += 1
    except:
        pass
    time.sleep(0.2)
    
print("#")

i = 1
#解答の選択肢を取得
#['1 :（ａ、ｂ）', '2 :（ａ、ｃ）', '3 :（ａ、ｄ）', '4 :（ｂ、ｃ）', '5 :（ｃ、ｄ）']
for elem in test_combi[40:80]:
    try:
        print(i)
        option = elem.text
        option = option.splitlines()
        option = "!".join(option) 
        if "（" in option:
            option = list(map(lambda x: x.replace("（"," :（"), option.split(" ")))
        else:
            option = list(map(lambda x: x.replace(" "," : ").replace("\u3000", " "), option.split("!")))[1:]
        data_dict["chapter3"][f"number{i}"]["option"] = option
        print(option)
        i += 1
    except:
        pass
    time.sleep(0.2)



#第４章
driver.get("https://www.35189.jp/test/shutoken_r4/?no=tab4")
time.sleep(1)
test_chapter_title = driver.find_elements(by=By.CLASS_NAME, value='test_chapter_title')
test_question_titles = driver.find_elements(by=By.CLASS_NAME, value='test_question_title')
test_question_choices = driver.find_elements(by=By.CLASS_NAME, value='test_question')
test_combi = driver.find_elements(by=By.CLASS_NAME, value='test_combi')

print("#")

#問題の章を取得 (第１章　医薬品に共通する特性と基本的な知識)
for elem in test_chapter_title[3:4]:
    try:
        scope = elem.text.replace("　", ":")
        print(scope)
    except:
        pass
for i in range(1, 21):
    data_dict["chapter4"][f"number{i}"]["scope"] = scope
    
print("#")

#問題番号と設問を取得 
#1
#医薬品の本質に関する次の記述のうち、正しいものの組合せはどれか。
for elem in test_question_titles[80:100]:
    try:
        question = elem.text
        num = int(question.split(" ")[1].split("　")[0])
        title = question.split(" ")[1].split("　")[1]
        print(num)
        print(title)
        data_dict["chapter4"][f"number{num}"]["title"] = title
    except:
        pass
    time.sleep(0.2)
    
print("#")

#設問の選択肢を取得
#['a 一般用医薬品は、効能効果、用法用量、副作用等の情報を購入者等に適切に伝達するため、添付文書や製品表示に必要な情報が記載されている。', 'b 医薬品は、人の疾病の診断、治療若しくは予防に使用されること、又は人の身体の構造や機能に影響を及ぼすことを目的とする生命関連製品である。', 'c 一般用医薬品は、一 般の生活者が自ら選択し、使用するものであり、添付文書を見れば、効能効果や副作用等について誤解や認識不足を生じることはない。', 'd 検査薬の検査結果については、正しい解釈や判断がなされなくても、適切な治療を受ける機会を失うおそれはない。']
i = 1
for elem in test_question_choices[80:100]:
    try:
        choice = elem.text
        choice = choice.splitlines()
        data_dict["chapter4"][f"number{i}"]["choice"] = choice
        print(choice)
        i += 1
    except:
        pass
    time.sleep(0.2)
    
print("#")

i = 1
#解答の選択肢を取得
#['1 :（ａ、ｂ）', '2 :（ａ、ｃ）', '3 :（ａ、ｄ）', '4 :（ｂ、ｃ）', '5 :（ｃ、ｄ）']
for elem in test_combi[80:100]:
    try:
        print(i)
        option = elem.text
        option = option.splitlines()
        option = "!".join(option) 
        if "（" in option:
            option = list(map(lambda x: x.replace("（"," :（"), option.split(" ")))
        else:
            option = list(map(lambda x: x.replace(" "," : ").replace("\u3000", " "), option.split("!")))[1:]
        data_dict["chapter4"][f"number{i}"]["option"] = option
        print(option)
        i += 1
    except:
        pass
    time.sleep(0.2)



#第５章
driver.get("https://www.35189.jp/test/shutoken_r4/?no=tab5")
time.sleep(1)
test_chapter_title = driver.find_elements(by=By.CLASS_NAME, value='test_chapter_title')
test_question_titles = driver.find_elements(by=By.CLASS_NAME, value='test_question_title')
test_question_choices = driver.find_elements(by=By.CLASS_NAME, value='test_question')
test_combi = driver.find_elements(by=By.CLASS_NAME, value='test_combi')

print("#")

#問題の章を取得 (第１章　医薬品に共通する特性と基本的な知識)
for elem in test_chapter_title[4:5]:
    try:
        scope = elem.text.replace("　", ":")
        print(scope)
    except:
        pass
for i in range(1, 21):
    data_dict["chapter5"][f"number{i}"]["scope"] = scope
    
print("#")

#問題番号と設問を取得 
#1
#医薬品の本質に関する次の記述のうち、正しいものの組合せはどれか。
for elem in test_question_titles[100:120]:
    try:
        question = elem.text
        num = int(question.split(" ")[1].split("　")[0])
        title = question.split(" ")[1].split("　")[1]
        print(num)
        print(title)
        data_dict["chapter5"][f"number{num}"]["title"] = title
    except:
        pass
    time.sleep(0.2)
    
print("#")

#設問の選択肢を取得
#['a 一般用医薬品は、効能効果、用法用量、副作用等の情報を購入者等に適切に伝達するため、添付文書や製品表示に必要な情報が記載されている。', 'b 医薬品は、人の疾病の診断、治療若しくは予防に使用されること、又は人の身体の構造や機能に影響を及ぼすことを目的とする生命関連製品である。', 'c 一般用医薬品は、一 般の生活者が自ら選択し、使用するものであり、添付文書を見れば、効能効果や副作用等について誤解や認識不足を生じることはない。', 'd 検査薬の検査結果については、正しい解釈や判断がなされなくても、適切な治療を受ける機会を失うおそれはない。']
i = 1
for elem in test_question_choices[100:120]:
    try:
        choice = elem.text
        choice = choice.splitlines()
        data_dict["chapter5"][f"number{i}"]["choice"] = choice
        print(choice)
        i += 1
    except:
        pass
    time.sleep(0.2)
    
print("#")

i = 1
#解答の選択肢を取得
#['1 :（ａ、ｂ）', '2 :（ａ、ｃ）', '3 :（ａ、ｄ）', '4 :（ｂ、ｃ）', '5 :（ｃ、ｄ）']
for elem in test_combi[100:120]:
    try:
        print(i)
        option = elem.text
        option = option.splitlines()
        option = "!".join(option) 
        if "（" in option:
            option = list(map(lambda x: x.replace("（"," :（"), option.split(" ")))
        else:
            option = list(map(lambda x: x.replace(" "," : ").replace("\u3000", " "), option.split("!")))[1:]
        data_dict["chapter5"][f"number{i}"]["option"] = option
        print(option)
        i += 1
    except:
        pass
    time.sleep(0.2)

    
with open("data.json", "w", encoding="utf-8_sig") as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4)
    
    
    
#print(data_dict)    
# pprint.pprint(data_dict, indent=4)