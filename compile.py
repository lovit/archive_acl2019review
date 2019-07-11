import argparse
from make_readme import load, as_markdown


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--update_readme', dest='update_readme', action='store_true')
    parser.add_argument('--add_tag', type=str, default='', help='space separated. first item is tag and others is index')

    args = parser.parse_args()
    update_readme = args.update_readme
    tags = args.add_tag

    if update_readme:
        articles = load()
        as_markdown(articles)

if __name__ == '__main__':
    main()