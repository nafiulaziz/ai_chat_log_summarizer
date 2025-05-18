import re
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

STOPWORDS = set(stopwords.words('english'))

def parse_chat_log(file_obj):
    lines = file_obj.read().decode('utf-8').splitlines()
    user_msgs, ai_msgs, all_msgs = [], [], []

    for line in lines:
        if line.startswith("User:"):
            msg = line[5:].strip()
            user_msgs.append(msg)
            all_msgs.append(msg)
        elif line.startswith("AI:"):
            msg = line[3:].strip()
            ai_msgs.append(msg)
            all_msgs.append(msg)

    return user_msgs, ai_msgs, all_msgs

def count_words(messages):
    words = ' '.join(messages).lower()
    words = re.findall(r'\b[a-z]{2,}\b', words)
    filtered = [w for w in words if w not in STOPWORDS]
    return Counter(filtered).most_common(5)

def extract_keywords_tfidf(all_msgs):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5)
    X = vectorizer.fit_transform(all_msgs)
    return vectorizer.get_feature_names_out()

def summarize_chat(user_msgs, ai_msgs, all_msgs, use_tfidf=False):
    total_exchanges = len(user_msgs) + len(ai_msgs)
    keywords = extract_keywords_tfidf(all_msgs) if use_tfidf else [kw for kw, _ in count_words(all_msgs)]
    summary = {
        'total': total_exchanges,
        'user_count': len(user_msgs),
        'ai_count': len(ai_msgs),
        'keywords': keywords,
        'topic': ', '.join(keywords[:1])
    }
    return summary
