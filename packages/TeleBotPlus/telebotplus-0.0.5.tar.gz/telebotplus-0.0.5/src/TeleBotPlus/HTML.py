import html
import random
from .utils import id_bot2client
from typing import *
__all__ = [
    "bold",
    "code",
    "from_list",
    "hide",
    "italic",
    "link",
    "mono",
    "normal",
    "quote",
    "spoiler",
    "strike",
    "text_mention",
    "underline",
    "url",
    "user",
    "userlink",
]
EXAMPLE_SIMPLE = {
    "type": "simple",
    "text": [
        "Hello ",
        {
            "formats": {
                "bold": None,
                "user": "%(id)s"
            },
            "text": "%(name)s"
        }
    ]
}
EXAMPLE_RANDOM = {
    "type": "random",
    "texts": [
        EXAMPLE_SIMPLE["text"],
        "Hi"
    ]
}


def normal(text: str, escape: bool = True):
  """Не изменяет текст"""
  if escape:
    text = html.escape(text)
  return text


def bold(text: str, escape: bool = True):
  """Жирный"""
  if escape:
    text = html.escape(text)
  return "<b>{}</b>".format(text)


def code(text: str, lang: str = "", escape: bool = True):
  """Блок кода"""
  if escape == True:
    escape = (True, True)
  elif escape == False:
    escape = (False, True)
  elif type(escape) == dict:
    escape = (escape["text"], escape["lang"])
  if escape[0]:
    text = html.escape(text)
  if escape[1]:
    lang = html.escape(lang)
  return '<pre><code class="{}">{}</code></pre>'.format(lang.lower(), text)


def italic(text: str, escape: bool = True):
  """Курсив"""
  if escape:
    text = html.escape(text)
  return "<i>{}</i>".format(text)


def link(text: str, url: str, escape: bool = True):
  """Ссылка в тексте"""
  if escape == True:
    escape = (True, True)
  elif escape == False:
    escape = (False, True)
  elif type(escape) == dict:
    escape = (escape["text"], escape["url"])
  if escape[0]:
    text = html.escape(text)
  if escape[1]:
    url = html.escape(url)
  return '<a href="{}">{}</a>'.format(url, text)


url = link


def mono(text: str, escape: bool = True):
  """Моноширинный текст"""
  if escape:
    text = html.escape(text)
  return "<code>{}</code>".format(text)


def quote(text: str, escape: bool = True):
  """Цитата"""
  if escape:
    text = html.escape(text)
  return "<blockquote>{}</blockquote>".format(text)


def spoiler(text: str, escape: bool = True):
  """Скрытый текст"""
  if escape:
    text = html.escape(text)
  return "<tg-spoiler>{}</tg-spoiler>".format(text)


hide = spoiler


def strike(text: str, escape: bool = True):
  """Зачёркнутый текст"""
  if escape:
    text = html.escape(text)
  return "<s>{}</s>".format(text)


def underline(text: str, escape: bool = True):
  """Подчёркнутый текст"""
  if escape:
    text = html.escape(text)
  return "<u>{}</u>".format(text)


def user(text: str, id: int, convert_id: bool = False, *args, **kw):
  """Упоминание в тексте по ID"""
  if convert_id:
    id = id_bot2client(id)
  return link(text, f"tg://user?id={id}", *args, **kw)


text_mention = user


def userlink(text: str, id: int, convert_id: bool = False, *args, **kw):
  """Ссылка на пользователя в тексте (без упоминания)"""
  if convert_id:
    id = id_bot2client(id)
  return link(text, f"tg://openmessage?user_id={id}", *args, **kw)


_functions = {}
for k, v in locals().items():
  if k in __all__:
    _functions[k] = v


def _build_text(l: Union[str, list]) -> str:
  if type(l) == str:
    return html.escape(l)
  t = ""
  for i in l:
    if type(i) == str:
      t += html.escape(i)
      continue
    if type(i) == dict:
      for k, v in i["formats"].items():
        if v == None:
          t += _functions[k](i["text"])
        else:
          t += _functions[k](i["text"], v)
  return t


def from_dict(d: dict[str, Any]) -> str:
  if d["type"] == "simple":
    return _build_text(d["text"])
  if d["type"] == "random":
    return _build_text(random.choice(d["texts"]))
  raise ValueError("Unknown type: %s" % d["type"])
