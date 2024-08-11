import pandas as pd
import numpy as np
import re

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.preprocessing import RobustScaler, MaxAbsScaler, MinMaxScaler
from nltk.tokenize import word_tokenize, sent_tokenize, TweetTokenizer, regexp_tokenize
import nltk

from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif, mutual_info_classif, chi2, RFE, SequentialFeatureSelector
from sklearn.linear_model import LassoCV
from sklearn.tree import DecisionTreeClassifier

from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import cross_val_score, KFold, LeaveOneOut



# Information

def information(data):
    """
    This function provides basic information about a pandas DataFrame.
    Parameters:
        data (pd.DataFrame): The DataFrame for which you want to obtain information.
    Returns:
        None
    """
    print("Columns:", data.columns)
    print("Column Types:", type(data.columns))
    print("Descriptive Statistics:\n", data.describe())
    print("Info:")
    data.info()
    return data


def handlingNullValues(data, columns=None, drop_rows=False, drop_columns=False, impute_mean=False, impute_median=False, impute_mode=False, impute_knn=False, forward_fill=False, backward_fill=False, interpolate_linear=False, interpolate_polynomial=False, fill_constant=None, domain_specific=None, flag_missing=False):
    """
    This function handles missing (null) values in a pandas DataFrame.
    Techniques:
        1. Removal of missing values
            Drop Rows.
            Drop Columns.
        2. Imputation techniques
            Mean
            Median
            Mode
            K-Nearest Neighbors
        3. Forward and Backward Fill
            Last observed values
            Next observed values
        4. Interpolation
            Linear interpolation
            Polynomial Interpolation
        5. Specific values
            Fill with Constant
            Domain Specific Values
        6. Flagging Missing values (as feature)
    Parameters:
        data (pd.DataFrame): The input DataFrame with missing values to be handled.
        columns (list or None): Specific columns to handle. If None, all columns are handled.
        drop_rows (bool): Drop rows with missing values.
        drop_columns (bool): Drop columns with missing values.
        impute_mean (bool): Impute missing values using the mean.
        impute_median (bool): Impute missing values using the median.
        impute_mode (bool): Impute missing values using the mode.
        impute_knn (bool): Impute missing values using K-Nearest Neighbors.
        forward_fill (bool): Fill missing values with the last observed value.
        backward_fill (bool): Fill missing values with the next observed value.
        interpolate_linear (bool): Interpolate missing values linearly.
        interpolate_polynomial (bool): Interpolate missing values using polynomial interpolation.
        fill_constant (any): Fill missing values with a constant value.
        domain_specific (dict): Fill missing values with domain-specific values, specified as a dictionary with column names as keys and fill values as values.
        flag_missing (bool): Flag missing values as a feature.
    Returns:
        pd.DataFrame: A DataFrame with missing values handled according to specified techniques.
    """
    if columns is None:
        columns = data.columns
    else:
        columns = [col for col in columns if col in data.columns]

    # Create a copy of the columns to work on specific columns without affecting the original data
    data_copy = data.copy()

    # 1. Removal of missing values
    if drop_rows:
        data_copy.dropna(subset=columns, inplace=True)
        # Update the original data to match the row indices
        data = data.loc[data_copy.index]
        
    if drop_columns:
        cols_to_drop = [col for col in columns if data_copy[col].isna().any()]
        data_copy.drop(columns=cols_to_drop, inplace=True)
        columns = [col for col in columns if col not in cols_to_drop]

    # 2. Imputation techniques
    if impute_mean or impute_median or impute_mode or impute_knn:
        for column in columns:
            if data_copy[column].isna().any():
                if pd.api.types.is_numeric_dtype(data_copy[column]):
                    if impute_mean:
                        data_copy[column].fillna(data_copy[column].mean(), inplace=True)
                    if impute_median:
                        data_copy[column].fillna(data_copy[column].median(), inplace=True)
                    if impute_mode:
                        data_copy[column].fillna(data_copy[column].mode()[0], inplace=True)
                    if impute_knn:
                        # K-Nearest Neighbors imputation logic here
                        pass
                else:
                    print(f"'{column}' Contains Non-Numeric Values, First Convert it to Numeric then try again.")

    # 3. Forward and Backward Fill
    if forward_fill:
        data_copy.fillna(method='ffill', inplace=True)
    if backward_fill:
        data_copy.fillna(method='bfill', inplace=True)

    # 4. Interpolation
    if interpolate_linear or interpolate_polynomial:
        for column in columns:
            if data_copy[column].isna().any():
                if pd.api.types.is_numeric_dtype(data_copy[column]):
                    if interpolate_linear:
                        data_copy[column].interpolate(method='linear', inplace=True)
                    if interpolate_polynomial:
                        data_copy[column].interpolate(method='polynomial', order=2, inplace=True)

    # 5. Specific values
    if fill_constant is not None:
        data_copy.fillna(value=fill_constant, inplace=True)
    if domain_specific is not None:
        for column, value in domain_specific.items():
            if column in data_copy.columns:
                data_copy[column].fillna(value=value, inplace=True)

    # 6. Flagging Missing values (as feature)
    if flag_missing:
        for column in columns:
            if data_copy[column].isna().any():
                data_copy[column + '_missing'] = data_copy[column].isna().astype(int)

    # Update original data with the modified columns
    existing_columns = data_copy.columns.intersection(columns)
    data.update(data_copy[existing_columns])

    return data



def deleteMultipleColumns(data, columns_to_delete):
    """
    Delete multiple columns from a pandas DataFrame.
    Parameters:
        data (pd.DataFrame): The input DataFrame from which columns will be deleted.
        columns_to_delete (list): List of column names to be deleted.
    Returns:
        pd.DataFrame: A DataFrame with specified columns removed.
    """
    # Use the drop method to remove the specified columns
    data = data.drop(columns=columns_to_delete, axis=1)
    return data  # Return the modified DataFrame
def handleCategoricalData(data, categorical_columns=None, binning_equal_width=False, binning_equal_frequency=False, label_encoding=False, one_hot_encoding=False, grouping=False):
    """
    Handle categorical data in a DataFrame.
    Methods:
    1. Binning
        - Equal width Binning
        - Equal Frequency Binning
    2. Label Encoding
    3. One-Hot Encoding
    Parameters:
        data (pd.DataFrame): The input DataFrame.
        categorical_columns (list, optional): List of column names with categorical data. If not provided, the function
            will automatically determine which columns to categorize.
        binning_equal_width (bool): Apply equal width binning.
        binning_equal_frequency (bool): Apply equal frequency binning.
        label_encoding (bool): Apply label encoding.
        one_hot_encoding (bool): Apply one-hot encoding.

    Returns:
        pd.DataFrame: A DataFrame with categorical data processed.
    """
    special_characters_pattern = r'[?@#&,|%^*()$]'
    data = data.replace(special_characters_pattern, None, regex=True)
    
    if categorical_columns is None:
        # Automatically determine categorical columns based on unique value count
        categorical_columns = []
        for column in data.columns:
            unique_values = data[column].nunique()
            if unique_values <= 3:
                categorical_columns.append(column)
    
    if one_hot_encoding:
        for col in categorical_columns:
            if col in data.columns:
                dummies = pd.get_dummies(data[col], prefix=col, drop_first=False)
                data = pd.concat([data, dummies], axis=1)
                data.drop(col, axis=1, inplace=True)
                data[dummies.columns] = data[dummies.columns].astype(int)
                print(f"One-Hot Encoding applied to column: {col}")
    
    if label_encoding:
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        for col in categorical_columns:
            if col in data.columns:
                data[col] = le.fit_transform(data[col].astype(str))
                print(f"Label Encoding applied to column: {col}")
    
    if binning_equal_width or binning_equal_frequency:
        for col in categorical_columns:
            if col in data.columns:
                if binning_equal_width:
                    data[col], bins = pd.cut(data[col], bins=5, labels=False, retbins=True)
                    print(f"Equal Width Binning applied to column: {col}")
                if binning_equal_frequency:
                    data[col], bins = pd.qcut(data[col], q=5, labels=False, retbins=True, duplicates="drop")
                    print(f"Equal Frequency Binning applied to column: {col}")
    
    if grouping:
        # Example: Grouping by the first column if grouping is enabled
        for col in categorical_columns:
            if col in data.columns:
                data = data.groupby(col).mean()
                print(f"Grouping applied to column: {col}")


    return data

def normalization(data, 
                   columns_to_normalize=None, 
                   min_value=0, 
                   max_value=1, 
                   decimal_scaling=False, 
                   log_transformation=False, 
                   root_transformation=False, 
                   robust_scaling=False, 
                   maxabs_scaling=False,
                   sparse_minmax_scaling=False):
    """
    Normalize specified columns in a pandas DataFrame using various scaling methods.
    Methods
    1. Min-Max Normalization
    2. Z-Score Normalization (Standardization)
    3. Decimal Scaling Normalization
    4. Logarithmic Transformation
    5. Root Transformation
    6. Robust Scaling
    7. MaxAbs Scaling
    8. Sparse Min-Max Scaling
    Parameters:
        data (pd.DataFrame): The input DataFrame to be normalized.
        columns_to_normalize (list, optional): List of column names to be normalized. If None, normalize all numeric columns.
        min_value (float, optional): Minimum value after normalization (default is 0).
        max_value (float, optional): Maximum value after normalization (default is 1).
        z_score_standardization (bool): Apply Z-Score Standardization.
        decimal_scaling (bool): Apply Decimal Scaling Normalization.
        log_transformation (bool): Apply Logarithmic Transformation.
        root_transformation (bool): Apply Root Transformation.
        robust_scaling (bool): Apply Robust Scaling.
        maxabs_scaling (bool): Apply MaxAbs Scaling.
        sparse_minmax_scaling (bool): Apply Sparse Min-Max Scaling.
    Returns:
        pd.DataFrame: A DataFrame with specified columns normalized according to selected methods.
    """
    if columns_to_normalize is None:
        columns_to_normalize = data.select_dtypes(include='number').columns.tolist()
    
    # Min-Max Normalization
    if min_value is not None and max_value is not None:
        for column in columns_to_normalize:
            if min_value < max_value:
                data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min()) * (max_value - min_value) + min_value
    
    # Decimal Scaling Normalization
    if decimal_scaling:
        for column in columns_to_normalize:
            max_value = data[column].abs().max()
            scaling_factor = 10 ** np.ceil(np.log10(max_value)) if max_value != 0 else 1
            data[column] = data[column] / scaling_factor
    
    # Logarithmic Transformation
    if log_transformation:
        for column in columns_to_normalize:
            data[column] = np.log1p(data[column])  # log1p handles zero values
    
    # Root Transformation
    if root_transformation:
        for column in columns_to_normalize:
            data[column] = np.sqrt(data[column])  # Use np.cbrt for cube root
    
    # Robust Scaling
    if robust_scaling:
        for column in columns_to_normalize:
            scaler = RobustScaler()
            data[column] = scaler.fit_transform(data[[column]])
    
    # MaxAbs Scaling
    if maxabs_scaling:
        for column in columns_to_normalize:
            scaler = MaxAbsScaler()
            data[column] = scaler.fit_transform(data[[column]])
    
    # Sparse Min-Max Scaling
    if sparse_minmax_scaling:
        for column in columns_to_normalize:
            scaler = MinMaxScaler()
            data[column] = scaler.fit_transform(data[[column]])

    return data
def standardiz(data, columns_to_normalize=None, z_score_standardization=False):
    """
    Normalize specified columns in a pandas DataFrame using Z-Score Standardization.
    Methods
    1. Z-Score Standardization (Normalization)
    Parameters:
        data (pd.DataFrame): The input DataFrame to be normalized.
        columns_to_normalize (list, optional): List of column names to be normalized. If None, normalize all numeric columns.
        z_score_standardization (bool): Apply Z-Score Standardization.
    Returns:
        pd.DataFrame: A DataFrame with specified columns normalized using Z-Score Standardization.
    """
    # If columns_to_normalize is not specified, normalize all numeric columns
    if columns_to_normalize is None:
        columns_to_normalize = data.select_dtypes(include='number').columns.tolist()
    
    # Z-Score Standardization
    if z_score_standardization:
        for column in columns_to_normalize:
            mean = data[column].mean()
            std_dev = data[column].std()
            if std_dev != 0:
                data[column] = (data[column] - mean) / std_dev
            else:
                print(f"Column '{column}' has a standard deviation of 0; skipping Z-Score normalization.")
    
    return data

def extract_numeric_values(data, columns_to_process):
    """
    Extract numeric values from specified columns in a DataFrame and replace the columns.
    Parameters:
        data (pd.DataFrame): The input DataFrame.
        columns_to_process (list): List of column names to process.
    Returns:
        pd.DataFrame: A DataFrame with specified columns replaced by extracted numerical values (as strings).
    """
    for column_name in columns_to_process:
        column_data = data[column_name]
        # Use regular expression to extract numerical values
        numeric_values = column_data.apply(lambda x: re.findall(r'\d+', str(x)))
        # Replace the column with extracted numerical values (as strings)
        data[column_name] = numeric_values.apply(lambda x: ', '.join(x) if x else None)
    return data

def tokenize_and_categorize(data, columns_to_process, separators=[', '], use_word_tokenize=False, use_sentence_tokenize=False, 
                            use_character_tokenize=False, use_ngram_tokenize=False, use_subword_tokenize=False, subword_length=4,
                            use_punctuation_tokenize=False, use_penn_treebank_tokenize=False):
    nltk.download('punkt')
    """
    Tokenize and process text values in specified columns in a DataFrame and categorize based on tokenized words.
    Parameters:
        data (pd.DataFrame): The input DataFrame.
        columns_to_process (list): List of column names to process.
        separators (list): List of separators to use for splitting text values.
        use_word_tokenize (bool): Apply word tokenization if True.
        use_sentence_tokenize (bool): Apply sentence tokenization if True.
        use_character_tokenize (bool): Apply character tokenization if True.
        use_ngram_tokenize (bool): Apply n-gram tokenization if True.
        use_subword_tokenize (bool): Apply subword tokenization if True.
        subword_length (int): Length of subwords for subword tokenization.
        use_punctuation_tokenize (bool): Apply punctuation-based tokenization if True.
        use_penn_treebank_tokenize (bool): Apply Penn Treebank tokenization if True.
    Returns:
        pd.DataFrame: A DataFrame with specified columns tokenized and categorized.
    """
    def apply_tokenizer(text):
        tokens = []
        if use_word_tokenize:
            tokens.extend(word_tokenize(text))
        if use_sentence_tokenize:
            tokens.extend(sent_tokenize(text))
        if use_character_tokenize:
            tokens.extend(list(text))
        if use_ngram_tokenize:
            tokens.extend([''.join(ngram) for ngram in zip(*[text[i:] for i in range(3)])])  # Example: 3-gram
        if use_subword_tokenize:
            tokens.extend(re.findall(rf'\w{{1,{subword_length}}}', text))  # Example: subwords of specified length
        if use_punctuation_tokenize:
            tokens.extend(regexp_tokenize(text, pattern=r'\w+|[^\w\s]'))
        if use_penn_treebank_tokenize:
            tknzr = TweetTokenizer()
            tokens.extend(tknzr.tokenize(text))
        if not tokens:
            tokens = word_tokenize(text)  # Default to word tokenization if no other option is selected
        return tokens
    
    combined_separator = '|'.join(map(re.escape, separators))
    for column_name in columns_to_process:
        column_data = data[column_name]
        # Split text values by provided separators and create a list of values
        split_values = column_data.str.split(combined_separator)
        # Apply the chosen tokenizer
        tokenized_values = split_values.apply(lambda x: [apply_tokenizer(text) for text in x])
        # Flatten the list and create a new DataFrame with binary columns for each token
        tokenized_data = pd.get_dummies(tokenized_values.apply(pd.Series).stack().explode()).groupby(level=0).max()
        # Replace the original column with tokenized values
        data = pd.concat([data, tokenized_data], axis=1)
        data.drop(columns=[column_name], inplace=True)
        data = data.replace({True: 1, False: 0})
    return data
def featureSelection(data, target, num_features=10, variance_threshold=False, pearson_correlation=False, 
                     mutual_info=False, anova=False, chi_square=False, rfe=False, sequential=False, 
                     exhaustive=False, lasso=False, decision_tree=False, random_forest=True):
    """
    Select the top features based on the specified feature selection method.
    
    Methods:
    1. Variance Threshold
    2. Pearson Correlation
    3. Mutual Information
    4. ANOVA F-test
    5. Chi-Square
    6. Recursive Feature Elimination (RFE)
    7. Sequential Feature Selection
    8. Exhaustive Feature Selection (Not implemented due to high computational cost)
    9. Lasso Regression
    10. Decision Tree feature importance
    11. Random Forest feature importance

    Parameters:
        data (pd.DataFrame): The input feature dataset.
        target (pd.Series or np.ndarray): The target variable.
        num_features (int): Number of top features to select. Default is 10.
        variance_threshold (bool): Whether to use Variance Threshold. Default is False.
        pearson_correlation (bool): Whether to use Pearson Correlation. Default is False.
        mutual_info (bool): Whether to use Mutual Information. Default is False.
        anova (bool): Whether to use ANOVA F-test. Default is False.
        chi_square (bool): Whether to use Chi-Square. Default is False.
        rfe (bool): Whether to use Recursive Feature Elimination. Default is False.
        sequential (bool): Whether to use Sequential Feature Selection. Default is False.
        exhaustive (bool): Whether to use Exhaustive Feature Selection. Default is False.
        lasso (bool): Whether to use Lasso Regression. Default is False.
        decision_tree (bool): Whether to use Decision Tree feature importance. Default is False.
        random_forest (bool): Whether to use Random Forest feature importance. Default is True.

    Returns:
        pd.DataFrame: The dataset with selected features.

    Raises:
        ValueError: If no valid feature selection method is specified.
        ValueError: If `target` is not of the correct length.
    """

    # Ensure target is a Series or ndarray
    if isinstance(target, pd.Series):
        target = target.values
    elif not isinstance(target, (list, np.ndarray)):
        raise ValueError("Target variable must be a pandas Series, list, or numpy array.")
    
    # Check for consistency in length between data and target
    if len(data) != len(target):
        raise ValueError(f"Inconsistent number of samples between data ({len(data)}) and target ({len(target)}).")

    # Handle missing values
    data = data.fillna(data.mean())
    
    if variance_threshold:
        # Variance Threshold feature selection
        selector = VarianceThreshold()
        selected_data = data.loc[:, selector.fit(data).get_support()]

    elif pearson_correlation:
        # Pearson Correlation feature selection
        cor = data.corrwith(pd.Series(target)).abs().sort_values(ascending=False)
        selected_data = data[cor.index[:num_features]]
        
    elif mutual_info:
        # Mutual Information feature selection
        selector = SelectKBest(mutual_info_classif, k=num_features)
        selector.fit(data, target)
        selected_data = data.iloc[:, selector.get_support(indices=True)]
        
    elif anova:
        # ANOVA F-test feature selection
        selector = SelectKBest(f_classif, k=num_features)
        selector.fit(data, target)
        selected_data = data.iloc[:, selector.get_support(indices=True)]
        
    elif chi_square:
        # Chi-Square feature selection
        selector = SelectKBest(chi2, k=num_features)
        selector.fit(data, target)
        selected_data = data.iloc[:, selector.get_support(indices=True)]
        
    elif rfe:
        # Recursive Feature Elimination (RFE)
        estimator = RandomForestClassifier(n_estimators=100, random_state=42)
        selector = RFE(estimator, n_features_to_select=num_features)
        selector.fit(data, target)
        selected_data = data.iloc[:, selector.get_support(indices=True)]
        
    elif sequential:
        # Sequential Feature Selection
        estimator = RandomForestClassifier(n_estimators=100, random_state=42)
        selector = SequentialFeatureSelector(estimator, n_features_to_select=num_features, direction='forward')
        selector.fit(data, target)
        selected_data = data.iloc[:, selector.get_support(indices=True)]
        
    elif exhaustive:
        # Exhaustive feature selection placeholder
        raise NotImplementedError("Exhaustive feature selection is not implemented due to its high computational cost.")
        
    elif lasso:
        # Lasso Regression feature selection
        selector = LassoCV(tol=1e-4,max_iter=10000)
        selector.fit(data, target)
        importance = selector.coef_
        selected_data = data.iloc[:, importance.argsort()[::-1][:num_features]]
        
    elif decision_tree:
        # Decision Tree feature importance
        clf = DecisionTreeClassifier(random_state=42)
        clf.fit(data, target)
        importances = clf.feature_importances_
        selected_data = data.iloc[:, importances.argsort()[::-1][:num_features]]
        
    elif random_forest:
        # Random Forest feature importance
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(data, target)
        importances = clf.feature_importances_
        selected_data = data.iloc[:, importances.argsort()[::-1][:num_features]]
        
    else:
        raise ValueError("No valid feature selection method specified.")
    
    return selected_data
def check_and_resample(data, target_column, threshold=0.5, 
                       bootstrap=False, cross_validation=False, k_fold=False, 
                       leave_one_out=False, jackknife=False, permutation_test=False, 
                       n_permutations=10, n_jobs=-1):
    """
    Checks for class imbalance in the dataset and applies resampling if necessary.
    
    Methods:
    1. Bootstrapping
    2. Cross-validation
        2.1 K-Fold cross-validation
        2.2 Leave-One-Out cross-validation
    3. Jackknife
    4. Permutation test

    Parameters:
        data (pd.DataFrame): The dataset containing features and the target variable.
        target_column (str): The name of the target variable column.
        threshold (float): The imbalance ratio threshold for deciding if resampling is needed. Default is 0.5.
        bootstrap (bool): Apply bootstrapping if True.
        cross_validation (bool): Apply cross-validation if True.
        k_fold (bool): Apply K-Fold cross-validation if True.
        leave_one_out (bool): Apply Leave-One-Out cross-validation if True.
        jackknife (bool): Apply jackknife resampling if True.
        permutation_test (bool): Apply permutation test if True.
        n_permutations (int): Number of permutations for the permutation test. Default is 10.
        n_jobs (int): Number of CPU cores used when parallelizing cross-validation (-1 uses all cores).

    Returns:
        pd.DataFrame: The resampled dataset if imbalance is detected, otherwise the original dataset.
    """

    # Check the class distribution
    class_counts = data[target_column].value_counts()
    minority_class = class_counts.idxmin()
    majority_class = class_counts.idxmax()

    # Calculate imbalance ratio
    imbalance_ratio = class_counts[majority_class] / class_counts[minority_class]
    print(f"Initial Imbalance Ratio: {imbalance_ratio}")

    # Resampling if imbalance is detected
    if imbalance_ratio > threshold:
        print("Imbalanced dataset detected. Resampling...")

        if imbalance_ratio > 1.0:
            oversampler = RandomOverSampler(random_state=42)
            X_resampled, y_resampled = oversampler.fit_resample(data.drop(columns=[target_column]), data[target_column])
        else:
            undersampler = RandomUnderSampler(random_state=42)
            X_resampled, y_resampled = undersampler.fit_resample(data.drop(columns=[target_column]), data[target_column])

        # Combine the resampled data back into a DataFrame
        resampled_data = pd.concat([pd.DataFrame(X_resampled, columns=data.drop(columns=[target_column]).columns),
                                    pd.DataFrame({target_column: y_resampled})], axis=1)

        # Calculate and display the new imbalance ratio after resampling
        new_class_counts = resampled_data[target_column].value_counts()
        new_imbalance_ratio = new_class_counts.max() / new_class_counts.min()
        print(f"Imbalance Ratio after Resampling: {new_imbalance_ratio}")

        # Applying additional methods based on user input
        if bootstrap:
            print("Applying Bootstrapping...")
            bootstrapped_data = resampled_data.sample(frac=1, replace=True, random_state=42)
            resampled_data = pd.concat([resampled_data, bootstrapped_data])
            print("Bootstrapping done.")

        if cross_validation:
            print("Applying Cross-Validation...")
            scores = cross_val_score(RandomForestClassifier(), resampled_data.drop(columns=[target_column]), 
                                     resampled_data[target_column], cv=5, n_jobs=n_jobs)
            print(f"Cross-Validation Scores: {scores}")

        if k_fold:
            print("Applying K-Fold Cross-Validation...")
            kf = KFold(n_splits=5)
            for train_index, test_index in kf.split(resampled_data):
                print(f"Train: {train_index}, Test: {test_index}")

        if leave_one_out:
            print("Applying Leave-One-Out Cross-Validation...")
            loo = LeaveOneOut()
            for train_index, test_index in loo.split(resampled_data):
                print(f"Train: {train_index}, Test: {test_index}")

        if jackknife:
            print("Applying Jackknife...")
            jackknife_samples = [resampled_data.drop(resampled_data.index[i]) for i in range(len(resampled_data))]
            print("Jackknife resampling done.")

        if permutation_test:
            print("Applying Permutation Test...")
            permutation_scores = []
            for _ in range(n_permutations):  # Reduced number of permutations for speed
                permuted_target = np.random.permutation(resampled_data[target_column])
                permuted_score = cross_val_score(RandomForestClassifier(), resampled_data.drop(columns=[target_column]), 
                                                 permuted_target, cv=5, n_jobs=n_jobs)
                permutation_scores.append(np.mean(permuted_score))
            print(f"Permutation Test Scores: {permutation_scores}")

        return resampled_data

    else:
        print("Dataset is not imbalanced.")
        return data

# dates. this in in development
# def preprocess_time_series(data, time_column_name):
#     # Convert the time column to datetime format
#     data[time_column_name] = pd.to_datetime(data[time_column_name])
#
#     # Extract date components
#     data['day'] = data[time_column_name].dt.day
#     data['month'] = data[time_column_name].dt.month
#     data['year'] = data[time_column_name].dt.year
#
#     # Convert the date to DD/MM/YYYY format
#     data['formatted_date'] = data[time_column_name].dt.strftime('%d/%m/%Y')
#
#     # Split the formatted date into day, month, and year
#     data[['day_categorical', 'month_categorical', 'year_categorical']] = data['formatted_date'].str.split('/', expand=True)
#
#     # Convert the split components to categorical values
#     data['day_categorical'] = pd.Categorical(data['day_categorical'])
#     data['month_categorical'] = pd.Categorical(data['month_categorical'])
#     data['year_categorical'] = pd.Categorical(data['year_categorical'])
#
#     return data
# to export data for checking
def export(data, to_csv=True, to_json=False, to_txt=False):
    """
    Export the dataset to specified formats based on user preferences.
    
    Parameters:
        data (pd.DataFrame): The dataset to be exported.
        to_csv (bool): Export the dataset as a CSV file if True.
        to_json (bool): Export the dataset as a JSON file if True.
        to_txt (bool): Export the dataset as a text file if True.
    
    Returns:
        None
    """
    if to_csv:
        data.to_csv("exported_PreProcessed_Data.csv", index=False)
        print("Data exported as CSV.")
    
    if to_json:
        data.to_json("exported_PreProcessed_Data.json", orient='records', lines=True)
        print("Data exported as JSON.")
    
    if to_txt:
        data.to_csv("exported_PreProcessed_Data.txt", sep='\t', index=False)
        print("Data exported as TXT.")

    if not (to_csv or to_json or to_txt):
        raise ValueError("At least one export format must be selected.")
