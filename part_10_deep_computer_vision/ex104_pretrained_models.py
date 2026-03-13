from tensorflow import keras
model = keras.applications.resnet50.ResNet50(weights="imagenet", include_top=False)
print("Pre-trained ResNet50 (headless) loaded.")
