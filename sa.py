import tweepy, emoji, random

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def makeStory():
  story = ''

  topSubjects = [':cyclone:', ':ocean:', ':ocean:',':ocean:',':whale:', ':swimmer:', ':surfer:', ':rowboat:', ':speedboat:', ':boat:', '  ', '  ','  ', '  ','  ',]
  middleSubjects = [':whale2:', ':dolphin:', ':fish:', ':tropical_fish:', ':octopus:', '  ', '  ','  ', '  ', '  ', '  ', '  ']
  bottomSubjects = [':shell:', ':shell:', ':octopus:', '  ', '  ', ':tropical_fish:', '  ']

  top = [':ocean:']
  middle = []
  bottom = []

  t = ""
  b = ""

  storyArr = []

  while len(top) < 9 and len(bottom) < 9 :
    t = random.choice(topSubjects)
    b = random.choice(bottomSubjects)

    top.append(t)
    bottom.append(b)

    if len(top) == 8:
      top.append("\n")
      bottom.append("\n")


  while len(middle) < 46:
    middle.append(random.choice(middleSubjects))

    if len(middle) % 9 == 0:
      middle.append("\n")

  storyArr = top + middle + bottom

  for i in range (0, len(storyArr)):
    story += storyArr[i]

  # print storyArr
  # print story

  return story

def main():
  cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }

  api = get_api(cfg)
  tweet = emoji.emojize(makeStory(), use_aliases=True)
  status = api.update_status(status=tweet) 

if __name__ == "__main__":
  main()