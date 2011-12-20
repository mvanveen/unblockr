from google.appengine.ext import db

class Group(db.Model):
  name = db.StringProperty


class User(db.Model):
  fbid          = db.IntegerPropery()
  name          = db.StringProperty()
  group         = db.ReferencePropery(Group, required=True)
  blocks        = db.ListProperty(db.ReferenceProperty(Block))
  date_created  = db.DateTimeProperty()
  date_modified = db.DateTimeProperty()


class Block(db.Model):
  blocker       = db.ReferencePropery()
  blockee       = db.ReferencePropery()
  date_created  = db.DateTimeProperty()
  date_modified = db.DateTimeProperty()
  mitigated     = db.BooleanProperty()
  resolved      = db.BooleanProperty()

#TODO: custom fbid property
