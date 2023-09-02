from keras.models import load_model

model = load_model("./model")
print(type(model))