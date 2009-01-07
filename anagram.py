import sys


def load_wordlist(filename):
    data = ''.join(open(filename, 'r').readlines()).lower()
    data = data.split(', ')
    wordlist = {}
    for word in data:
        key = ''.join(sorted(word))
        wordlist.setdefault(key, []).append(word)
    return wordlist


def solve(anagram, wordlist=None):
    return ', '.join(wordlist.get(''.join(sorted(anagram)), ['No solution for %s' % anagram]))


if __name__ == '__main__':
    wordlist = load_wordlist('wordlist.txt')
    print solve(sys.argv[1], wordlist)
