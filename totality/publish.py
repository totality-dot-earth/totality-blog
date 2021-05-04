import csv
import yaml
import requests
import os
import tweepy

def publish(item):
    with open(item['path']) as fd:
        y = ''
        b = ''
        seen = 0
        for line in fd.readlines():
            if line.strip() == '---':
                seen += 1
            else:
                if seen >= 2:
                    b += line
                    b += '\n'
                else:
                    y += line
                    y += '\n'
        obj = yaml.load(y)
        if 'publish' in obj:
            publishers = obj['publish']
            if 'medium' in publishers:
                medium_payload = {
                    'title': obj['title'],
                    'content': b,
                    'subtitle': obj['summary'],
                    'tags': obj.get('tags', []),
                    'canonical': item['permalink']
                }
                print('  Posting to Medium')
                resp = requests.post('https://hooks.zapier.com/hooks/catch/5343276/oh4na9i/', json=medium_payload)
                if resp.status_code == 200:
                    print('  Success! -- You need to publish the draft')
                else:
                    print(resp.text)
            elif 'twitter' in publishers:
                twitter_payload = {
                    'message': f"New post: {obj['title']}\n\n{obj['summary']}\n{item['permalink']}"
                }
                if item['section'] == 'shares':
                    twitter_payload = {
                        'message': f"{obj['summary']}\n{item['permalink']}"
                    }
                
                resp = requests.post('https://hooks.zapier.com/hooks/catch/5343276/oh62s92/', json=twitter_payload)

before = {}
with open('prev.csv') as fd:
    rd = csv.DictReader(fd)
    for line in rd:
        before[line['path']] = line

after = {}
with open('current.csv') as fd:
    rd = csv.DictReader(fd)
    for line in rd:
        after[line['path']] = line

for p in after.keys():
    before_item = before.get(p, None)
    after_item = after[p]
    # print(before_item['draft'])
    # print(after_item['draft'])
    
    after_item['section'] = after_item['path'].split('/')[1]
    
    if after_item['draft'] == 'true':
        print(f"  SKIPPING   {p} is still draft") 
        continue
    elif not before_item:
        print(f"  PUBLISHING {p} is new (no previous draft)")
        publish(after_item)
    elif before_item['draft'] == 'true' and after_item['draft'] == 'false':
        print(f"  PUBLISHING {p} was draft, but is now published")
        publish(after_item)
    else:
        print(f"  SKIPPING   {p} was already published")
        continue
           