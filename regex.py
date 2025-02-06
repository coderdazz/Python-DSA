re_digits = '[0-9]'
re_wildcard = '1.3' # '.' is a wild card, except new line
# . is for a single character
# ^ anchors match at start of string \A alt expression
# $ anchors match at the end of string alt expression \Z
# $ also matches before single newline but not \Z
# * matches zero or more repetitions
# a* matches zero or more 'a' characters, '', 'a', 'aa', ...
# + matches one or more repetitions
# ? matches/verifies the zero or single occurrence of the group preceding it
# pattern = re.compile(r'(\d{2}-)?\d{10}') -> two character digit is optional
# .* arbitrary string of any arbitrary length
# *? non-greedy matches, match shortes element
# {} matches an explicitly specified number of repetitions
# -{3} 3 repetitions of dash, {2-4} repetition between 2 and 4
# {1,} greater or equal to, {,} any number
# \ Escapes a metacharater of its special meaning e.g. \n
# [] specifies a character class
# () creates a group
# : # = ! designate a specialised group
# <> named group
# \d decimal digit
# \D opposite, not decimal digit
# \w is [a-zA-Z0-9_] includes \d
# \W is the opposite = [^a-zA-Z0-9_]
# \s whitespace will match newline \S is opposite
# \b anchors to a word boundary, beginning or end of word
# \B anchors to a location that isn't a word boundary
# | matches at most one of foo|bar|baz

# re.unicode or re.U specifies unicode
# re.I, ignores cases
# re.S, causes . to also match embedded newlines
# re.findall() # list of all regex matches in a string
# re.match() look for match at the beginning of a string
# it = re.finditer() # returns iterator, do next(it)
# for i in re.finditer(): print(i)
# re.split() split by certain pattern
# split by '(group)' will return split and also the delimiter
# re.escape() returns str with each non word character preceded by \
# obj = re.compile(), obj.search() split out uses


import re
re.findall(r'(\d+.*) ', '123foobar sfsfs')

re.search('\d{1,5}.\d{1,}%','your return 1-1 is 22.3% this i not')
# treat as group
re.search('(bar)+', 'foo barbar baz')
# The input string
text = "The total return of your portfolio is: 21.2%, your portfolio was valued at $1,000,000 with YTD return at 5.4%. Investment manager: Ben Does."

# Regex pattern to find the specific percentage after the phrase
pattern = r"your portfolio is: \s*([\d.]+%)?"
re.search('ba[artz]', 'foobarqux')
# Search for the pattern in the text
re.search(pattern, text)
match =re.search(r'total return of your portfolio is:\s*(?P<return>\d+\.\d%)',text)
# re.search searches for first occurrence
match.groupdict('return')


# look for non-digit character
# You can complement a character class by specifying ^
# as the first character, in which case it matches any character
# that isn’t in the set.
re.search('[^0-9]', '12345foo')

# ^ has special meaning if it's the first character in []
re.search('[#:^][a-z]', 'foo#^bar:baz#qux')
re.findall('[#:^][a-z]', 'foo#^bar:baz#qux')
# range of characters separated with a hyphen
re.search('[-abc]', '123-456')
re.search('[abc-]', '123-456')
re.search('[0-9ab\-c]', '123-456')

# [] is a character class
re.search('[]]', 'foo[1]')
re.search('[\[ab\]cd]', 'foo[1]')

re.search('[)*+|]', '123+4)56')
re.search('foo.bar', 'foo1bar')
re.search('[\d\w\s]', '--3---')
re.search('\\\\', r'foo\bar')
re.search(r'\Bar\B', 'bar.foobaz')

re.search('foo-?bar', 'foo--bar')
re.search('<.*?>', '%<foo> <bar> <baz>%')
re.findall('<.*?>', '%<foo> <bar> <baz>%')

re.search('(foo(bar)?)+(\d\d\d)?', 'foofoo123')


re.sub(r'(\w+),bar,baz,(\w+)',
        r'\2,bar,baz,\1',
      'foo,bar,baz,qux')


import re
from datetime import datetime

# Custom exceptions for error handling
class InvalidDateFormat(Exception):
    pass

class InvalidMonthName(Exception):
    pass


def extract_datetime(dateTimeString):
    # Define regex patterns for the 3 formats provided
    patterns = [
        r'^(?P<year>\d{4})[-/](?P<month>\d{1,2})[-/](?P<day>\d{2}) '
        r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})$',
        # YYYY-MM-DD HH:mm:ss or YYYY/MM/DD HH:mm:ss
        r'^(?P<day>\d{2}) (?P<month_name>[A-Za-z]+) '
        r'(?P<year>\d{4}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})$'
        # DD Month YYYY HH:mm:ss
    ]

    # Try matching the string to the first two patterns
    for pattern in patterns:
        match = re.match(pattern, dateTimeString)
        if match:
            output = match.groupdict()

            # If month is a name, validate and convert it to a number
            if 'month_name' in output:
                try:
                    output['month'] = datetime.strptime(output['month_name'], '%B').month
                except ValueError:
                    raise InvalidMonthName("Invalid month name")
            else:
                output['month'] = int(output['month'])

            # Validate the numeric components
            try:
                dt = datetime(
                    year=int(output['year']),
                    month=int(output['month']),
                    day=int(output['day']),
                    hour=int(output['hour']),
                    minute=int(output['minute']),
                    second=int(output['second'])
                )
            except ValueError:
                raise InvalidDateFormat("Invalid date or time format")

            # Return the formatted string
            return (
                f"Year: {dt.year}, Month: {dt.month}, Day: {dt.day}, "
                f"Hour: {dt.hour}, Minute: {dt.minute}, Second: {dt.second}"
            )

    # If no pattern matched, raise invalid format exception
    raise InvalidDateFormat("Invalid date and time format")

m = re.search('(?P<name>(?P<name2>\w+),(\w+),(\w+))', 'foo,quux,baz')
m.groups()
m.group()
m.groupdict()
m = re.search(r'(?P<word>\w+),(?P=word)', 'foo,foo')
m.groups()
m.groupdict()





def word_stemmer(word):
    return re.sub(r'(ed|ly|ing)$', '', word)[:8]
    # suffix_list = ['ed', 'ly', 'ing']

    # return word if len(word) <= 8 else word_stemmed[:8]
word_stemmer('playing')


def stemmer(text):
    words = text.split()

    stemmed_words = [word_stemmer(word) for word in words]

    stemmed_text = ' '.join(stemmed_words)

    return stemmed_text
