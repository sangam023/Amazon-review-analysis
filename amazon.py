import pickle

vect=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

def predict(string):
  
    test_vect = vect.transform(([string]))
    pred = model.predict(test_vect)
    # print(pred[0])
    if pred[0] == 'positive':
        prediction = "Positive"
    else:
        prediction = "Negative"
    return prediction


print(predict("i this product on amazon when i ordered its look goood but when it delivered to me it vey bad product please dont buy this, it not worth it waste of money ............i am sad after purchase this product good bye"))