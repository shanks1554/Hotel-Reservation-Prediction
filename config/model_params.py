from scipy.stats import randint, uniform

LIGHTGBM_PARAMS = {
    'n_estimators': randint(100, 200),       # Smaller number of trees
    'max_depth': randint(3, 10),              # Shallower trees
    'learning_rate': uniform(0.05, 0.1),      # Moderate learning rate (0.05 to 0.15)
    'num_leaves': randint(15, 31),            # Fewer leaves
    'boosting_type': ['gbdt']                  # Use only gbdt boosting
}

RANDOM_SEARCH_PARAMS = {
    'n_iter': 10,          # More iterations for better search
    'cv': 3,               # 3-fold cross validation for stability
    'n_jobs': -1,
    'verbose': 2,
    'random_state': 42,
    'scoring': 'accuracy'
}
