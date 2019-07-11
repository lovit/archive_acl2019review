import argparse
import json
from make_readme import load, as_markdown

def save_article(articles):
    with open('acl2019list.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--update_readme', dest='update_readme', action='store_true')
    parser.add_argument('--add_tag', type=str, default='', help='space separated. first item is tag and others is index')

    args = parser.parse_args()
    update_readme = args.update_readme
    tag_args = args.add_tag

    if tag_args:
        update_readme = True
        tag_items = tag_args.split()
        tag = tag_items[0]
        items = {int(idx) for idx in tag_items[1:]}

        articles = load()
        for idx in items:
            article = articles[idx]
            tags = set(article['tags'])
            tags.add(tag)
            article['tags'] = list(tags)
        save_article(articles)

    if update_readme:
        articles = load()
        as_markdown(articles)

if __name__ == '__main__':
    main()