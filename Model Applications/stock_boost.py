import xgboost as xgb
from xgboost import DMatrix

def stock_boost(X_train, y_train, X_test):
    # Create DMatrix objects with categorical feature support
    train_matrix = DMatrix(
        data=X_train,
        label=y_train,
        enable_categorical=True
    )
    
    test_matrix = DMatrix(
        data=X_test,
        enable_categorical=True
    )
    
    # Model parameters
    model_params = {
        "objective": "binary:logistic",
        "tree_method": "exact",
        "max_cat_to_onehot": 11,
        "learning_rate": 0.32,
        "max_depth": 7
    }
    
    # Train model
    trading_model = xgb.train(
        params=model_params,
        dtrain=train_matrix
    )
    
    # Generate predictions
    prediction_scores = trading_model.predict(test_matrix)
    
    # Apply decision threshold
    binary_signals = [
        1 if score > 0.44 else 0 
        for score in prediction_scores
    ]
    
    # Format output
    X_test.loc[:, "buy_signal"] = binary_signals
    output_predictions = X_test[["buy_signal"]].copy()
    X_test.drop(columns=["buy_signal"], inplace=True)
    
    return output_predictions