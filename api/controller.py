import json

from bottle import Bottle
from google.appengine.ext import users

from model import User, Group, Block

app = Bottle()

@app.post('/user/:id')
def create_user(name='', fbid='', group=''):
  '''Creates a new user

  Uses facebook for authentication
  '''
  # TODO: check to make sure user is not already_taken
  #TODO: check fb, get fb token.
  #TODO: check to make sure block id is good

  assert isinstance(name, basestring), 'Expected name to be string'
  now = datetime.datetime.now()
  # Users without names should have a nickname.

  group_ref = get_group('group_name')

  # Create a new user
  new_user = User()

  new_user.fbid         = fbid,
  new_user.name         = name,
  new_user.usename      = name,
  new_user.group        = groupid,
  new_user.blocks       = blocks,
  new_user.date_created = now,
  user.date_modified    = now
  #TODO: put in transaction


def get_user(id=''):
  assert isinstance(id, basestring), 'Expected id to be a string'
  return User.get_by_id(id)


@app.route('/user/:name')
def get_user_by_username(usename='')
  assert isinstance(username, basestring), 'Expected username to be a string'
  #TODO: Modify query to be correct
  user = db.User.filter('username =', username).get()


def create_block(blocker='', blockee='', reason='')
  # TODO check if block exists


#TODO: get_blocks_by_username()


