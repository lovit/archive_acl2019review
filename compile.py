import argparse
import json
import os
from make_readme import load, as_markdown

def save_article(articles):
    with open('acl2019list.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

def prepare_blank_md(path, title):
    text = '---\ntitle : {}\n\n---\n\nsnippest\n\ncontent'.format(title)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--update_readme', dest='update_readme', action='store_true')
    parser.add_argument('--add_tag', type=str, default='', help='space separated. first item is tag and others is index')
    parser.add_argument('--add_link', type=str, default='', help='space separated. first is index second is url')
    parser.add_argument('--prepare_review', type=str, default='', help='space separated indices')
    parser.add_argument('--prefer_tags', type=str, default='', help='[ / ] separated')

    args = parser.parse_args()
    update_readme = args.update_readme
    tag_args = args.add_tag
    link_args = args.add_link
    prepare_review = args.prepare_review
    if args.prefer_tags:
        prefer_tags = set(args.prefer_tags.split(' / '))
    else:
        prefer_tags = None

    print('Preference of tags : {}'.format(prefer_tags))

    articles = load()

    if tag_args:
        update_readme = True
        tag_items = tag_args.split()
        tag = tag_items[0]
        items = {int(idx) for idx in tag_items[1:]}

        for idx in items:
            article = articles[idx]
            tags = set(article['tags'])
            tags.add(tag)
            article['tags'] = list(tags)
        save_article(articles)

    if link_args:
        update_readme = True
        args = link_args.split()
        n_args = int(len(args) / 2)
        idxs = [int(args[2*i]) for i in range(n_args)]
        urls = [args[2*i+1] for i in range(n_args)]
        for idx, url in zip(idxs, urls):
            article = articles[idx]
            article['link'] = url
        save_article(articles)

    if update_readme:
        as_markdown(articles, prefer_tags)

    if prepare_review:
        idxs = [int(idx) for idx in prepare_review.split()]
        for idx in idxs:
            path = 'reviews/{}.md'.format(idx)
            if not os.path.exists(path):
                title = articles[idx]['title']
                prepare_blank_md(path, title)

if __name__ == '__main__':
    main()