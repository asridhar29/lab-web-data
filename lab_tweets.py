# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
import json
import matplotlib.pyplot as plt

# Step 1: build the list of the ten filenames and load every tweet from them
# into one big list.
filenames = []
for year in range(2009, 2019):
    filenames.append(f'master_{year}.json')

tweets = []
for filename in filenames:
    with open(filename, encoding='utf-8') as f:
        jsontext = f.read()
    year_tweets = json.loads(jsontext)
    tweets = tweets + year_tweets

total_tweets = len(tweets)
print('total tweets:', total_tweets)

# Step 2: get the message we will search for each tweet. Older tweets only
# have 'text'; newer tweets have the longer 'full_text' instead.
messages = []
for tweet in tweets:
    if 'full_text' in tweet:
        messages.append(tweet['full_text'])
    else:
        messages.append(tweet['text'])

# Lowercase every message once, so each phrase check below doesn't have to
# repeat that work.
lower_messages = []
for message in messages:
    lower_messages.append(message.lower())

# Step 3: count how many tweets contain each phrase, ignoring case. The
# first five phrases are required by the lab. The last three (wall, maga,
# mainstream media) are the ones we chose to investigate from the catalog.
phrases = ['obama', 'trump', 'mexico', 'russia', 'fake news',
           'wall', 'maga', 'mainstream media']

counts = {}
for phrase in phrases:
    count = 0
    for message in lower_messages:
        if phrase in message:
            count = count + 1
    counts[phrase] = count

print('--- counts ---')
for phrase in phrases:
    print(phrase, counts[phrase])

# Step 4: turn each count into a percentage of all tweets.
percents = {}
for phrase in phrases:
    percents[phrase] = counts[phrase] / total_tweets * 100

# Step 5: build a Markdown table, phrases in alphabetical order, with the
# phrase column right-aligned and percentages shown as 00.00.
sorted_phrases = sorted(phrases)

phrase_width = len('phrase')
for phrase in sorted_phrases:
    if len(phrase) > phrase_width:
        phrase_width = len(phrase)

percent_texts = {}
percent_width = len('percent of tweets')
for phrase in sorted_phrases:
    percent_text = f'{percents[phrase]:05.2f}'
    percent_texts[phrase] = percent_text
    if len(percent_text) > percent_width:
        percent_width = len(percent_text)

lines = []
header = '| ' + 'phrase'.ljust(phrase_width) + ' | ' + 'percent of tweets'.ljust(percent_width) + ' |'
divider = '| ' + '-' * phrase_width + ' | ' + '-' * percent_width + ' |'
lines.append(header)
lines.append(divider)
for phrase in sorted_phrases:
    row = '| ' + phrase.rjust(phrase_width) + ' | ' + percent_texts[phrase].ljust(percent_width) + ' |'
    lines.append(row)

table = '\n'.join(lines)
print('--- table ---')
print(table)

# Step 6: bar chart of every phrase's count, saved as tweets.png.
chart_counts = []
for phrase in sorted_phrases:
    chart_counts.append(counts[phrase])

plt.barh(sorted_phrases, chart_counts)
plt.xlabel('number of tweets')
plt.ylabel('phrase')
plt.title("Phrase counts in Trump's tweet archive (2009-2018)")
plt.tight_layout()
plt.savefig('tweets.png')
print('saved tweets.png')
