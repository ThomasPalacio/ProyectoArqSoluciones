import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

# Configuración de las claves de la API de Twitter
API_KEY = "your_api_key"
API_SECRET_KEY = "your_api_secret_key"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Autenticación con la API de Twitter
def authenticate_twitter():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

# Función para obtener tweets relacionados con un tema
def fetch_tweets(api, query, count=100):
    tweets = api.search_tweets(q=query, count=count, lang="en")
    return tweets

# Análisis de sentimientos
def analyze_sentiments(tweets):
    sentiments = []
    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        sentiments.append(analysis.sentiment.polarity)
    return sentiments

# Visualización de resultados
def plot_sentiments(sentiments):
    plt.hist(sentiments, bins=20, color='blue', edgecolor='black')
    plt.title('Distribución de Sentimientos')
    plt.xlabel('Polaridad')
    plt.ylabel('Frecuencia')
    plt.show()

if __name__ == "__main__":
    api = authenticate_twitter()
    query = "#mercados"
    tweets = fetch_tweets(api, query)
    sentiments = analyze_sentiments(tweets)
    plot_sentiments(sentiments)