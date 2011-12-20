from flow import route, post, get

hitme = lambda: chr(random.choice(
  range(48, 57) + range(65, 90) + range(97, 122))
)

hitme_int = lambda: chr(random.choice(range(48, 57)))
rand_init = lambda f: lambda num: ''.join(x() for x in repeat(f, num or 1))
rand_str  = rand_init(hitme)
rand_int  = rand_init(hitme_int)

#TODO: test email

@test.post('/group/:name')
def test_can_create_group():
  return {
    'name': rand_str(15),
    'sessionid': rand_str(15)
  }


@test.post('/user')
def test_can_create_new_user(name=None, group=None):
  return {
   'name': name or randstr(15)
   'fbid': randstr(15),
   'group': group or test_can_create_group(),
  }


@test.get('/user/:id')
def test_can_get_existing_user(id):
  return json.dumps(
    get_user(id).to_dict()
  ) == test.response


@test.route('/block/:id')
def test_can_create_new_block
  user = test_can_create_new_user()


#@test.route('/block/:id')
#TODO: test_create_new_block_with_bad_user

#TODO: create duplicate user

@test.use_case()
def test_can_check_new_user():
  '''Newly created user has proper state'''
  group = test_can_create_group
  response = user  = test_can_create_new_user(
    name=rand_str('15'),
    group=group
  )
  assert response.get('status') == 'OK'

  user = test_can_get_existing_user(user)
  assert user.get('name') is not None


@test.use_case()
def test_can_create_block(mitgated=False):
  '''Two users can create block'''

  msg = rand_str(255)

  group = test_can_create_new_group()
  user  = test_can_create_new_user() # response from first request
  user2 = test_can_create_new_user() # response from 2nd request
  block = test_make_block(user1, user2, msg)

  assert block.get('blocker') == user.get('name')
  assert block.get('blockee') == user2.get('name')
  assert block.reason == msg

  return (user, user2, block)


@test.use_case()
def test_make_block_unmitigated():
  test_can_create_block(mitgated=True)


