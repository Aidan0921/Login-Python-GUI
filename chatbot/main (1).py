from guizero import App, TextBox, ListBox, PushButton, Text, Box
import json

questions = []
answers = []
keywords = []

f = open("questions.json", "r")
data = f.read()

obj = json.loads(data)
for item in obj["questionLists"]:
  questions.append(item["q"].lower())
  answers.append(item["a"])
  keywords.append(item["k"])


def askbutton():
  listbox.append("Q: {}".format(textbox.value))
  if textbox.value.lower() in questions:
    listbox.append("A: {}".format(answers[questions.index(textbox.value.lower())]))
  else:
    a = textbox.value.lower().split(" ")
    b = [] # to get index of questions and answers
    # 유저가 입력한 질문에서 키워드를 찾는것에 중점을 두고 짠코드다
    # 키워드를 찾는것의 좋은점은 긴 질문을 전부다 입력할 필요가 없다
    # 우선 유저가 textbox에 입력한 값을 리스트화 시킨다
    # questions.json에서 가져온 각 질문에 해당한 keywords 리스트를 가져와서 순서대로 유저입력값리스트value들과 같은지 비교한다
    # keywords의 value와 유저입력value가 같은지 확인할 b라는 변수를 만든다
    # b를 리스트로 만든이유는 traking과 if condition에 사용하기 편하게 하기위함이다
    # 그래서 if len(b)>0일때 제일 root for loop를 break 했다, 이유는 list b 가 다른 키워드로 바뀌지 않게 하기 위함이다
    # for loop에서 나와 if else문으로 b가 값을 가지고 있으면 답을 listbox에 append하고 
    # b 가 값을 가지고 있지 않으면 listbox에 답이 없음을 알려준다
    for i in range(0, len(keywords)):
      for j in range(0, len(keywords[i])):
        if keywords[i][j] in a:
          b = [i]
      if len(b) > 0:
        break
        
    if len(b) > 0:
      listbox.append("A: {}".format(answers[b[0]]))
    else:
      listbox.append("Couldn't find an answer for that question.")
  textbox.value = ""

app = App(title="NLCS SG CHATBOT")
text = Text(app, text="NLCS SG CHATBOT", width="fill")
listbox = ListBox(app, width="fill",scrollbar=True)

textbox = TextBox(app,width="fill")
button = PushButton(app, text="Ask", command=askbutton)

listbox.append("Ask me any questions about NLCS or Singapore")

app.display()
