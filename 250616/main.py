# from pyhub.llm import UpstageLLM
from pyhub.llm import OpenAILLM

# 내부적으로 UPSTAGE_API_KEY 환경변수 값이 있으면,
# 자동으로 활용합니다.
# llm = UpstageLLM()
llm = OpenAILLM()
reply = llm.ask("hello")
print(reply)
print(reply.usage)

# stream=True 지정하시면, Generator 반환
for chunk in llm.ask("hello", stream=True):
    print(chunk.text, end="")
print()

reply = llm.ask("우울해서 빵을 샀어.", choices=["기쁨", "슬픔", "분노", "불안", "무기력함"])
print(reply.choice)        # "슬픔"
print(reply.choice_index)  # 1