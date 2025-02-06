# Python Regular Expressions (Regex) Cheat Sheet

## Basic Syntax
- **`.`**: Matches any single character except a newline.  
  Example: `a.c` matches `"abc"`, `"axc"`, etc.
- **`^`**: Anchors the match at the **start** of the string.  
  Example: `^hello` matches `"hello world"`, but not `"world hello"`.
- **`$`**: Anchors the match at the **end** of the string.  
  Example: `world$` matches `"hello world"`, but not `"world hello"`.
- **`*`**: Matches zero or more repetitions of the preceding character.  
  Example: `a*` matches `""`, `"a"`, `"aaa"`, etc.
- **`+`**: Matches one or more repetitions of the preceding character.  
  Example: `a+` matches `"a"`, `"aaa"`, etc., but not `""`.
- **`?`**: Matches zero or one occurrence of the preceding character.  
  Example: `a?` matches `""`, `"a"`.
- **`{}`**: Matches an explicitly specified number of repetitions.
  - `{n}`: Exactly `n` times.  
    Example: `a{3}` matches `"aaa"`.
  - `{n,}`: At least `n` times.  
    Example: `a{2,}` matches `"aa"`, `"aaa"`, etc.
  - `{n,m}`: Between `n` and `m` times (inclusive).  
    Example: `a{1,3}` matches `"a"`, `"aa"`, or `"aaa"`.

---

## Escaping Characters
- **`\`**: Escapes a metacharacter of its special meaning.  
  Example: `\.` matches `"."`, not any character.
- **`re.escape(string)`**: Escapes all non-alphanumeric characters in the string.

---

## Character Classes
- **`[]`**: Specifies a set of characters to match.
  - Example: `[abc]` matches `"a"`, `"b"`, or `"c"`.
  - Ranges: `[a-z]`, `[0-9]` match letters and digits respectively.
  - Negation: `[^...]` matches characters **not** in the set.  
    Example: `[^0-9]` matches non-digit characters.
- **`\d`**: Matches any decimal digit (`[0-9]`).
- **`\D`**: Matches any non-decimal digit (`[^0-9]`).
- **`\w`**: Matches any alphanumeric character (`[a-zA-Z0-9_]`).
- **`\W`**: Matches any non-alphanumeric character (`[^a-zA-Z0-9_]`).
- **`\s`**: Matches any whitespace character (spaces, tabs, newlines).
- **`\S`**: Matches any non-whitespace character.

---

## Anchors and Boundaries
- **`\b`**: Anchors to a **word boundary** (start or end of a word).  
  Example: `\bfoo\b` matches `"foo"` in `"foo bar"`, but not in `"foobar"`.
- **`\B`**: Anchors to a location **not** at a word boundary.  
  Example: `\Bfoo` matches `"foobar"` but not `"foo bar"`.

---

## Special Groups
- **`()`**: Creates a capturing group.
  - Example: `(abc)` captures `"abc"`.
- **`(?:...)`**: Non-capturing group.  
  Example: `(?:abc)` matches `"abc"` but does not capture it.
- **`(?P<name>...)`**: Named capturing group.  
  Example: `(?P<digit>\d)` captures a digit with the name `"digit"`.
- **`(?=...)`**: Positive lookahead (asserts presence without consuming).  
  Example: `foo(?=bar)` matches `"foo"` in `"foobar"`.
- **`(?!...)`**: Negative lookahead.  
  Example: `foo(?!bar)` matches `"foo"` not followed by `"bar"`.
- **`(?<=...)`**: Positive lookbehind (asserts preceding pattern).  
  Example: `(?<=\$)\d+` matches digits preceded by `"$"`.
- **`(?<!...)`**: Negative lookbehind.  
  Example: `(?<!\$)\d+` matches digits not preceded by `"$"`.

---

## Useful Methods
- **`re.compile(pattern)`**: Compiles a regex pattern into a regex object for reuse.
- **`re.findall(pattern, string)`**: Returns a list of all matches in a string.
- **`re.search(pattern, string)`**: Searches for the first match; returns a match object or `None`.
- **`re.match(pattern, string)`**: Matches the pattern **only** at the start of the string.
- **`re.split(pattern, string)`**: Splits the string at each match of the pattern.
- **`re.sub(pattern, repl, string)`**: Replaces matches with a replacement string.

---

## Flags
- **`re.I`**: Ignore case.
- **`re.M`**: Multiline mode (`^` and `$` match start/end of each line).
- **`re.S`**: Dot-all mode (`.` matches newlines).
- **`re.X`**: Verbose mode (allows whitespace and comments in patterns).
- **`re.U`**: Unicode mode.

---

## Examples
1. **Extracting Percentages**:
   ```python
   text = "Your portfolio return is 21.2%."
   match = re.search(r'return is (\d+\.\d+%)', text)
   if match:
       print(match.group(1))  # Output: 21.2%
   ```

2. **Named Groups**:
   ```python
   pattern = r"(?P<dollars>\$\d+)"
   match = re.search(pattern, "Total: $100")
   print(match.group("dollars"))  # Output: $100
   ```

3. **Non-Greedy Matches**:
   ```python
   re.findall('<.*?>', '<div>hello</div>')  # Output: ['<div>', '</div>']
   ```

4. **Substitution**:
   ```python
   re.sub(r'(\w+),bar,baz,(\w+)', r'\2,bar,baz,\1', 'foo,bar,baz,qux')
   # Output: 'qux,bar,baz,foo'
   ```

---

## Additional Tips for Interviews
1. **Understand Greedy vs Non-Greedy Matches**:
   - Greedy: Matches as much as possible.  
     Example: `<.*>` matches `"<div>hello</div>"`.
   - Non-Greedy: Matches as little as possible.  
     Example: `<.*?>` matches `"<div>"` and `"</div>"`.

2. **Practice Regex Debugging**:
   - Use online tools like [regex101](https://regex101.com) or [Regexr](https://regexr.com) for testing patterns.

3. **Memorize Common Patterns**:
   - Emails: `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`
   - URLs: `https?://[^\s]+`
   - Phone Numbers: `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}`

4. **Explain Regex Efficiency**:
   - Avoid catastrophic backtracking with complex nested patterns. Test on large inputs.

5. **Showcase Regex with Real Use Cases**:
   - Data validation, text parsing, web scraping, and log analysis.

