# -*- encoding: utf-8 -*-
"""
Hebbian potentiation refers to the means by which a neuron will have an
increased activation when it is used. It is the primary means by which the
brain stores protocols, and provides evidence for an emergent connectionist
network in cognitive function as opposed to a symbolic mental lexicon.

In this case, this file is used to set up the application's "models". A loose
term, when one considers we are storing to an object database, as opposed to a
relational one.

The application's objects and relations are defined in this file.
"""
from settings import MONGOSERVER

from mongoengine import *
connect(MONGOSERVER)

def slugfy(text, separator='-'):
  ret = ""
  for c in text.lower():
    try:
      ret += htmlentitydefs.codepoint2name[ord(c)]
    except:
      ret += c
  ret = re.sub("([a-zA-Z])(uml|acute|grave|circ|tilde|cedil)", r"\1", ret)
  ret = re.sub("\W", " ", ret)
  ret = re.sub(" +", separator, ret)
  return ret.strip()

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    username = StringField(max_length=40)

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=80))
    comments = ListField(EmbeddedDocumentField(Comment))

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()

