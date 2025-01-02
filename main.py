def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  chars = chars_dict(text)
  sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the document\n")
  for c, value in sorted_chars.items():
    if c in 'abcdefghijklmnopqrstuvwxyz':
      print(f"The '{c}' character was found {value} times")
  print("--- End report ---")

def get_num_words(text):
  words = text.split()
  return len(words)

def chars_dict(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def get_book_text(book_path):
  with open(book_path) as f:
    file_contents = f.read()
  return file_contents

main()