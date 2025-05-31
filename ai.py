from g4f.client import Client
import loguru


class AI:
    def __init__(self,cfg):
        self.client = Client()
        self.chat_history = {}
        self.image_model = cfg['image_model']
        self.text_model = cfg['text_model']
    def clear_dialog(self,uid):
        self.chat_history[uid] = []
    def genrate_text(self,query,uid):
        if uid not in self.chat_history:
            self.chat_history[uid] = []
        self.chat_history[uid].append({
            "role":"user",
            'content': query
        })
        try:
            response = self.client.chat.completions.create(
                model = self.text_model,
                messages = self.chat_history[uid],
                web_search = False
            )
            text = response.choices[0].message.content
            self.chat_history[uid].append({
                "role": "assistant",
                "content": text
            })
            return text
        except Exception as e:
            logger.warning("Произошла ошибка {}",str(e))
            return f"Error({str(e)})"
    def generate_image(self, promt):
        try:
            response = self.client.images.generate(
                model=self.image_model,
                prompt=promt,
                response_format='url'
            )
            url = response.data[0].url
            return url
        except Exception as e:
            logger.warning("Произошла ошибка {}",str(e))
            raise e