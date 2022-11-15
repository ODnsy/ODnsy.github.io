<!DOCTYPE html>
<html lang="en">
  <head>
    <!--<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />-->
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  </head>
  <body>
    Hello world! <br>
    <label>請輸入句子：</label>
    <input type="text" id="test-input"/>
    <button id="submit-button" type="submit" pys-onClick="my_function">OK</button>
    <div id="test-output"></div>
    <py-script>
      import re
      dict_vision=["咖啡","金黃","蔚藍","翠綠","鮮紅","湛藍","烏溜溜","黃澄澄","綠油油","白皚皚","黑漆漆","毛絨絨","水汪汪","白皙的","閃閃發亮","紅黃","紅色","嶄新的","白色","紅色","黃色","綠色","藍色","紫色"]
      dict_listen=["叮叮咚咚","嘩啦嘩啦","淅瀝淅瀝","滴滴答答","轟隆轟隆","吱吱喳喳","叩叩叩","撲簌撲簌","呼嚕呼嚕"]
      dict_object=["細細","長長","尖尖","長長","扁扁","方方","正正","寬寬","厚厚","小小","圓圓","大大"]
      dict_smell=["酸甜","苦澀","酸中帶甜","白Q細滑","油而不膩","香醇鮮美","香味四溢","香味"]
      dict_touch=["粗粗的","光滑柔順","質地輕柔","濕濕黏黏","柔軟"]
      text_1="我有一個四四方方咖啡色的背包，前面有粉紅的卡通圖案，旁邊掛著可愛的鈴鐺，每當我拿起背包時，便會叮叮咚咚作響。這個背包質地輕柔，摸起來柔軟舒適，是我最喜歡的背包。"
      text_2="我有一件紫色的外套，前面繡著花紋，後面有美麗的花邊圖案，領口還有毛絨絨的絲質圍巾，摸起來非常輕柔，有淡淡的香味，這是媽媽送給我的生日禮物，也是我最喜歡的衣服。"
      text_3="我有一支鉛筆，外型細細圓圓的，有著五彩繽紛的外表，上面還鑲著金黃的亮片，遠遠看去閃閃發亮，摸起來光滑細緻，帶著淡淡的香水味，是我最喜歡的一支鉛筆。"
      text_4="我有一個洋娃娃，金黃色的頭髮，水汪汪的眼睛，櫻桃小嘴，白皙的皮膚，穿著一件紅黃相間的洋裝，是媽媽送給我的禮物。"
      text_5="升上三年級後，媽媽送給我一個嶄新的書包，紅色的外型代表濃濃的喜氣，寬寬大大的身體可以裝進我的書和文具，旁邊還有一對紫色小鈴鐺，每當我一走動，就會發出叮叮咚咚的聲響。這個書包的質地輕柔，摸起來光滑柔順，是我上學的好夥伴，它是我最喜歡的書包。"
      def cut_sentence(sentence):
        s = re.split('。|，|；', sentence)
        s.pop() #去掉最後一個空值
        return(s)

      sentence_test_1=cut_sentence(text_1)
      sentence_test_2=cut_sentence(text_2)
      sentence_test_3=cut_sentence(text_3)
      sentence_test_4=cut_sentence(text_4)
      sentence_test_5=cut_sentence(text_5)
      
      def get_dict(sentence,dict,dict_add):
        for i in range (len(sentence)):
          for j in range (len(dict)):
            if(sentence[i].find(dict[j])>-1):
              sentence[i]+=dict_add
              break
        return(sentence)
      
      def show_dict(sentence_dict):
        sentence_dict=get_dict(sentence_dict,dict_vision,"(視覺)")
        sentence_dict=get_dict(sentence_dict,dict_listen,"(聽覺)")
        sentence_dict=get_dict(sentence_dict,dict_object,"(形狀大小)")
        sentence_dict=get_dict(sentence_dict,dict_smell,"(味覺和嗅覺)")
        sentence_dict=get_dict(sentence_dict,dict_touch,"(觸覺)")
        return(sentence_dict)

      from js import console     
      def my_function(*args, **kwargs):   
          console.log(f'args: {args}')
          console.log(f'kwargs: {kwargs}')
          text = Element('test-input').element.value 
          #print('text:', text)
          console.log(f'text: {text}')
      
          Element('test-output').element.innerText = show_dict(cut_sentence(text))
    </py-script>
  </body>
</html>
