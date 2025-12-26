import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

# Create / select experiment
mlflow.set_experiment("day2-local-training")

with mlflow.start_run():
    # Load dataset
    X, y = load_diabetes(return_X_y=True)
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    alpha = 0.2
    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)

    # Evaluate
    r2 = model.score(X_test, y_test)

    # Log to MLflow
    mlflow.log_param("alpha", alpha)
    mlflow.log_metric("r2_score", r2)
    mlflow.sklearn.log_model(model, "model")

    print("Training completed")
    print("R2 score:", r2)
