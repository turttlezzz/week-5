# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
"""
5. Unique Word Count
Count how many distinct words are in the collection.
Input: "one fish two fish red fish blue fish"
Output: 5
"""
words = set(input("Enter some words: ").split())
print(f"Your text has {len(words)} words.")

"""
I chose to use a set for this problem because a set can only have unique data types. This automatically makes it so that the set doesn't 
contain repeated words. Then all I have to do after that is count the amount of words in the set, and I have my output. The time limit didn't
really shape my decision a ton because I completed this in about 10 minutes. While looking throught the questions from timed_challenge.txt, this
one stood out to me as one that Could see how to do before I started it. If there wasn't a time limit, I may have chosen a more difficult one, 
but I didn't anticipate that it wouldn't take the whole 30 minutes. I decided to add a User Input for testing so that I didn't have to change the
internal code every time I tested something new. I tested all of the edge cases, but the code already works through them. I could not make it 
"break" in any way. 
"""