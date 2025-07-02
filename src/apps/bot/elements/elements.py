from typing import Any


class Element:
    """Класс для представления элемента, который может быть выполнен с использованием модели и инструментов."""
    def __init__(self, model: str, tools: list, prompt: str, obj: Any):
        self.model = model
        self.tools = tools
        self.prompt = prompt
        self.obj = obj

    def __call__(self, *args, **kwargs):
        return self.run()

    def run(self) -> dict:
        raise NotImplementedError()


class FileElement(Element):
    """Класс для представления элемента файла."""
    def run(self):
        with open(self.obj) as f:
            content = f.read()
            if self.tools:
                for tool in self.tools:
                    content = tool(content)
            return content

    def __str__(self):
        return f'FileElement: {self.model} {self.prompt}'


class TextElement(Element):
    """Класс для представления текстового элемента."""
    def run(self):
        if self.tools:
            for tool in self.tools:
                self.obj = tool(self.obj)
        return self.obj

    def __str__(self):
        return f'TextElement: {self.model} {self.prompt}'


class PromptElement(Element):
    """Класс для представления элемента запроса."""

    def run(self) -> str:
        prompt = self.prompt.format(text=self.obj)
        return prompt

    def __str__(self):
        return f'PromptElement: {self.model} {self.prompt}'


class ImageElement(Element):
    """Класс для представления элемента изображения."""

    def run(self) -> str:
        prompt = self.prompt.format(image=self.obj)
        return prompt

    def __str__(self):
        return f'ImageElement: {self.model} {self.prompt}'
