## pre-trained model
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

def find_aspects(text, aspects):
  """
  arguments:
    text: review text (string)
    aspect: aspect of review specified manually in a list
  output:
    contains positive and negative sentimensts of the aspects in string and all in dictionary
  """
  # Load the ABSA model
  model_name = "yangheng/deberta-v3-base-absa-v1.1"
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSequenceClassification.from_pretrained(model_name)
  classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

  positive_aspects = []
  negative_aspects = []

  for aspect in aspects:
    if classifier(text, text_pair=aspect)[0]['label'] == 'Positive':
      positive_aspects.append(aspect)
    elif classifier(text, text_pair=aspect)[0]['label'] == 'Negative':
      negative_aspects.append(aspect)

  absa = {
      'positive': ', '.join(positive_aspects),
      'negative': ', '.join(negative_aspects)
  }
  return absa
