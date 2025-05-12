from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 dataset for 100 epochs
train_results = model.train(
    data="coco8.yaml",  # Path to dataset configuration file
    epochs=20,  # Number of training epochs
    imgsz=640,  # Image size for training
    device="cpu",  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
)

# Evaluate the model's performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("/Users/fayadh/Downloads/Picnic Shutterstock 1446093992.webp")  # Predict on an image
results[0].show()  # Display results

# Export the model to ONNX format for deployment
path = model.export(format="onnx")  # Returns the path to the exported model

# Fine-tune the model with additional hyperparameter adjustments
train_results = model.train(
    data="coco8.yaml",  # Path to dataset configuration file
    epochs=50,  # Increase the number of training epochs
    imgsz=640,  # Image size for training
    device="cpu",  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
    batch=16,  # Increase batch size for better gradient estimation
    lr0=0.01,  # Adjust learning rate
    optimizer="Adam",  # Use a different optimizer
    augment=True,  # Enable data augmentation
    patience=10,  # Early stopping patience
)
