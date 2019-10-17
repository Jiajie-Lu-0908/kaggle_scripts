import pandas as pd

def check_detail(df, verbose=True):
	"""
	Show details of a data frame. 
	Including:
	size, missing values, categorical cols and numerical cols

	Input:
	- df : pd.DataFrame  dataframe
	- verbose : whether to print information, defaultly True

	Return:
	- cate_cols : categorical cols
	- numb_cols : numercical cols
	- cate_miss_cols : categorical cols with missing values
	- numb_miss_cols : numerical cols with missing values
	"""
	rows, cols = df.shape()

	cate_cols = []
	numb_cols = []
	cate_miss_cols = []
	numb_miss_cols = []

	for col in train.columns:
	    if train[col].dtype == object:
		    if train[col].isnull().sum() != 0:
				CATE_MISSING_COLS.append(col)
			CATE_COLS.append(col)
		else:
			if train[col].isnull().sum() != 0:
				NUM_MISSING_COLS.append(col)
			NUM_COLS.append(col)
	
	if verbose:
		print(f"There are {rows} rows and {cols} columns in the dataframe.")
		print()
		print(f'There are {len(CATE_COLS)} categorical features.')
		print(f'They are {CATE_COLS}.')
		print('='*20)
		print(f'There are {len(NUM_COLS)} numerical features.')
		print(f'They are {NUM_COLS}.')
		print('='*20)
		print(f'Among all the cate features, these features have missing values: {CATE_MISSING_COLS}')
		print(f'Among all the num features, these features have missing values: {NUM_MISSING_COLS}')

		print('#'*20)
		print('Categorical columns with missing values.')
		print(df[cate_miss_cols].isnull().sum())
		print('='*20)
		print('Numerical columns with missing values.')
		print(df[numb_miss_cols].isnull().sum())

	return cate_cols, numb_cols, cate_miss_cols, numb_miss_cols


