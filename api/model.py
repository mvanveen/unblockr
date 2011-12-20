from google.appengine.ext import db

class Group(db.Model):
  name = db.StringProperty
  admin = db.ReferencePropery(User)


class User(db.Model):
  fbid          = db.IntegerPropery()
  name          = db.StringProperty()
  group         = db.ReferencePropery(Group, required=True)
  blocks        = db.ListProperty(db.ReferenceProperty(Block))
  date_created  = db.DateTimeProperty()
  date_modified = db.DateTimeProperty()


class Block(db.Model):
  # Note: creating a block should be a one-time thing.
  # OK to send email at this point. (KISS)

  blocker       = db.ReferencePropery()
  blockee       = db.ReferencePropery()
  date_created  = db.DateTimeProperty()
  date_modified = db.DateTimeProperty()
  mitigated     = db.BooleanProperty()
  reminder_date = db.DatetimeProperty()
  resolved      = db.BooleanProperty()
  reason   = db.StringProperty()
  priority = db.IntegerProperty()

#TODO: custom fbid property
