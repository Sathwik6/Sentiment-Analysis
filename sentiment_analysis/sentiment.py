from textblob import TextBlob

def analyze_sentiment(comments):
    
    outputBlob = []

    for comment in comments:
        blob = TextBlob(comment)
        outputBlob.append(blob)
    return outputBlob

def analysis(comments):
    outputBlob = analyze_sentiment(comments)

    for blob in outputBlob:
        print(f'Polarity: {blob.sentiment.polarity} | Subjectivity: {blob.sentiment.subjectivity}')
