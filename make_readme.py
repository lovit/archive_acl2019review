import json

json_path = 'acl2019list.json'

def load():
    with open(json_path, encoding='utf-8') as f:
        return json.load(f)

def as_markdown(articles):
    def has_tag(article):
        for tag in ["word embedding", "summarization"]:
            if tag in article['tags']:
                return True
        return False

    head = '# Reviews of ACL 2019 Papers\n'
    revieweds = []
    taggeds = []
    notyets = []
    for article in articles:
        if article['review']:
            revieweds.append(article)
        elif has_tag(article):
            taggeds.append(article)
        else:
            notyets.append(article)

    def as_text(article):
        # (order) [link]title, [review][tags]
        form = '({}) **{}**{}{}\n, {}\n'

        order = article['order']

        if article['link']:
            title = '[{}]({})'.format(article['title'], article['link'])
        else:
            title = '{}'.format(article['title'])

        if article['review']:
            review = ', [review]({})'.format(article['review'])
        else:
            review = ''

        if article['tags']:
            tags = ', '.join('`[{}]`'.format(tag) for tag in article['tags'])
            tags = ', {}'.format(tags)
        else:
            tags = ''
    
        authors = article['authors']
        text = form.format(order, title, review, tags, authors)
        return text

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('{}\n'.format(head))

        for article in revieweds + taggeds + notyets:
            f.write('{}\n'.format(as_text(article)))

    print('README.md has been updated.')
