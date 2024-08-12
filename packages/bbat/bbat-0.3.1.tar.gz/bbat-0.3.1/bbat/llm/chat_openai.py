import openai
import httpx


class ChatOpenaiAPI:
    """openai version is openai==0.27.8"""

    def __init__(self, model_name=None, api_url="https://api.openai.com/v1", api_key="", proxy=None, history=[]):
        # gpt-3.5-turbo
        # gpt-4
        self.model_name = "gpt-3.5-turbo"
        if model_name:
            self.model_name = model_name

        self.api_url = api_url
        self.api_key = api_key
        self.proxy = proxy
        http_client = httpx.Client(
            proxies="http://127.0.0.1:15777",
            transport=httpx.HTTPTransport(local_address="0.0.0.0"),
        )
        self.tokenizer = None
        self.history = history
        self.openai: openai.OpenAI = openai.OpenAI(api_key=self.api_key, base_url=self.api_url, http_client=http_client)

    def generate(self, messages, system_prompt=None, stream=True, **kwargs):
        # 避免传入的messages内容过大，保持最新的5条数据
        params = dict(
            model=self.model_name,
            temperature=0.3,
            top_p=0.9,
            max_tokens=512,
            frequency_penalty=1,
            presence_penalty=1,
            timeout=1,
        )
        params.update(kwargs)

        completion = self.openai.chat.completions.create(messages=messages, stream=stream, **params)
        # content = {'role': '', 'content': ''}
        for event in completion:
            if event.choices[0].delta.content is None:
                break
            for delta_v in event.choices[0].delta.content:
                if delta_v:
                    yield delta_v

    def chat(self, query, system_prompt=None, history=[], **kwargs):
        history = self.get_history()
        kwargs["model"] = self.model_name
        messages = history + [{"role": "user", "content": query}]
        return self.generate(messages, system_prompt, stream=True, **kwargs)

    def get_history(self):
        history = self.history
        type_map = {
            1: "user",
            0: "assistant",
        }
        history = [{"role": type_map[h.get("status", 0)], "content": h.get("content", "")} for h in history]

        return history


if __name__ == "__main__":
    # model = ChatLLM(api_key="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", proxy="http://127.0.0.1:15777")
    # llama2 chinese: http://192.168.110.192:30000/v1
    # baichuan2_vllm:  http://192.168.110.180:31113/v1
    # qwen 14b: http://192.168.110.180:31114/v1
    llm = ChatOpenaiAPI(
        api_url="https://api.openai.com/v1",
        api_key="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",
        proxy="http://127.0.0.1:15777",
    )
    response = llm.chat("server 转为大写")
    for item in response:
        print(item, end="")
