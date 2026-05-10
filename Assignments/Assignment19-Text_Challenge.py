'''Assignment (20/03/2026) 
Assignment Name : Text Challenges 
Description :Collect 20 messy sentences and identify slang, emojis, typos; explain preprocessing needed.

Messy Sentences with Issues Identified
No	Sentence	Issues (Slang / Emoji / Typo)
1	I'm gonna go now lol 😂	Slang (gonna, lol), Emoji
2	This is sooo gooood!!! 🔥🔥	Typo (sooo, gooood), Emoji
3	idk what u r saying 🤔	Slang (idk, u, r), Emoji
4	Plzz send me d file asap!!!	Slang (Plzz, d, asap), Typo
5	That movie was lit af 😎	Slang (lit, af), Emoji
6	I cant beleive this happend 😢	Typo (beleive, happend), Emoji
7	brb, will text u later 👍	Slang (brb, u), Emoji
8	OMG!!! This is awsm 😍	Slang (OMG, awsm), Emoji
9	wat r u doing???	Typo (wat), Slang (r, u)
10	Thx for ur help 😊	Slang (Thx, ur), Emoji
11	Hav a gr8 day!! ✨	Slang (gr8), Typo (Hav), Emoji
12	dis is not gud 😒	Typo (dis, gud), Emoji
13	c u soon bro 🤙	Slang (c u), Emoji
14	I'm sooo tired rn 😴	Slang (rn), Typo (sooo), Emoji
15	Yaaas!! I luv it ❤️	Slang (Yaaas, luv), Emoji
16	pls fix this bug asap 😤	Slang (pls, asap), Emoji
17	wht is dis??? 😕	Typo (wht, dis), Emoji
18	LOL that was funny 😂😂	Slang (LOL), Emoji
19	gud mrng everyone 🌞	Typo (gud, mrng), Emoji
20	I wil cal u ltr 📞	Typo (wil, cal, ltr), Slang

Preprocessing Steps Required
To clean the above text, the following preprocessing steps are needed:

1. Lowercasing
Convert all text to lowercase to maintain consistency.
Example: “OMG” → “omg”

2. Remove Emojis
Emojis do not contribute to most NLP models and should be removed.
Example: 😂, 😍 → removed

3. Remove Punctuation
Remove unnecessary symbols like !, ?, etc.
Example: “hello!!!” → “hello”

4. Expand Slang
Convert informal words into proper form.

Examples:
“u” → “you”
“idk” → “I don’t know”
“brb” → “be right back”
5. Correct Spelling (Typos)
Fix incorrect spellings.
Examples:
“beleive” → “believe”
“happend” → “happened”

6. Remove Stopwords (Optional)
Remove common words like “is”, “the”, “and” if needed.

7. Tokenization
Split sentences into words for processing.

Conclusion
Messy text data contains slang, emojis, and typos that can affect model performance. Proper preprocessing helps in improving the accuracy and efficiency of NLP models by converting raw text into clean and meaningful data.
'''
#Run in JUPYPER NOTEBOOK
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Strong slang dictionary
slang_dict = {
    "u": "you",
    "r": "are",
    "idk": "i do not know",
    "lol": "laughing",
    "brb": "be right back",
    "asap": "as soon as possible",
    "pls": "please",
    "plzz": "please",
    "thx": "thanks",
    "gr8": "great",
    "luv": "love",
    "omg": "oh my god",
    "rn": "right now",
    "gonna": "going"
}

def clean_text(text):
    # 1. Lowercase
    text = text.lower()

    # 2. Remove emojis (simple way without library)
    text = ''.join(char for char in text if char.isalnum() or char.isspace())

    # 3. Expand slang BEFORE anything else
    words = text.split()
    words = [slang_dict[word] if word in slang_dict else word for word in words]

    # 4. Remove punctuation (already mostly handled)
    text = " ".join(words)
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 5. Tokenization
    words = word_tokenize(text)

    # 6. Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # 7. Remove unnecessary duplicates (like "going go")
    cleaned = []
    for w in words:
        if w not in cleaned:
            cleaned.append(w)

    return " ".join(cleaned)


# Test
sentences = [
    "I'm gonna go now lol 😂",
    "idk what u r saying 🤔",
    "Plzz send me d file asap!!!",
    "OMG!!! This is awsm 😍",
    "I cant beleive this happend 😢"
]

for s in sentences:
    print("Original:", s)
    print("Cleaned :", clean_text(s))
    print("-" * 40)


#OUTPUT:
'''Original: I'm gonna go now lol 😂
Cleaned : im going go laughing
----------------------------------------
Original: idk what u r saying 🤔
Cleaned : know saying
----------------------------------------
Original: Plzz send me d file asap!!!
Cleaned : please send file soon possible
----------------------------------------
Original: OMG!!! This is awsm 😍
Cleaned : oh god awsm
----------------------------------------
Original: I cant beleive this happend 😢
Cleaned : cant beleive happend
----------------------------------------
[nltk_data] Downloading package punkt to /root/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package stopwords to /root/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!'''