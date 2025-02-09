Microsoft Windows [Version 10.0.19045.4529]
(c) Microsoft Corporation. All rights reserved.

C:\Users\raj>E:

E:\>cd E:\Download\Fake review detection Ml

E:\Download\Fake review detection Ml>pip install pandas numpy scikit-learn nltk flask
Requirement already satisfied: pandas in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (2.2.3)
Requirement already satisfied: numpy in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (2.2.2)
Requirement already satisfied: scikit-learn in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (1.6.1)
Requirement already satisfied: nltk in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (3.9.1)
Requirement already satisfied: flask in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (3.1.0)
Requirement already satisfied: python-dateutil>=2.8.2 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from pandas) (2025.1)
Requirement already satisfied: tzdata>=2022.7 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from pandas) (2025.1)
Requirement already satisfied: scipy>=1.6.0 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from scikit-learn) (1.15.1)
Requirement already satisfied: joblib>=1.2.0 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from scikit-learn) (1.4.2)
Requirement already satisfied: threadpoolctl>=3.1.0 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from scikit-learn) (3.5.0)
Requirement already satisfied: click in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from nltk) (8.1.8)
Requirement already satisfied: regex>=2021.8.3 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from nltk) (2024.11.6)
Requirement already satisfied: tqdm in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from nltk) (4.67.1)
Requirement already satisfied: Werkzeug>=3.1 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from flask) (3.1.3)
Requirement already satisfied: Jinja2>=3.1.2 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from flask) (3.1.5)
Requirement already satisfied: itsdangerous>=2.2 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from flask) (2.2.0)
Requirement already satisfied: blinker>=1.9 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from flask) (1.9.0)
Requirement already satisfied: colorama in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from click->nltk) (0.4.6)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from Jinja2>=3.1.2->flask) (3.0.2)
Requirement already satisfied: six>=1.5 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)

E:\Download\Fake review detection Ml>python train_model.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\raj\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Traceback (most recent call last):
  File "E:\Download\Fake review detection Ml\train_model.py", line 15, in <module>
    df = pd.read_csv("fake_reviews_dataset.csv")
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'fake_reviews_dataset.csv'

E:\Download\Fake review detection Ml>python train_model.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\raj\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Accuracy: 0.00%

E:\Download\Fake review detection Ml>python train_model.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\raj\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Accuracy: 0.00%

E:\Download\Fake review detection Ml>python train_model.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\raj\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Traceback (most recent call last):
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'review'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "E:\Download\Fake review detection Ml\train_model.py", line 19, in <module>
    df['cleaned_review'] = df['review'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]))
                           ~~^^^^^^^^^^
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'review'

E:\Download\Fake review detection Ml>python train_model.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\raj\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Traceback (most recent call last):
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'review'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "E:\Download\Fake review detection Ml\train_model.py", line 19, in <module>
    df['cleaned_review'] = df['review'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]))
                           ~~^^^^^^^^^^
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\raj\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'review'

E:\Download\Fake review detection Ml>python train_model.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\raj\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Accuracy: 88.20%

E:\Download\Fake review detection Ml>python test_model.py
Real Review

E:\Download\Fake review detection Ml>python test_model.py
Real Review

E:\Download\Fake review detection Ml>python test_model.py
Real Review

E:\Download\Fake review detection Ml>python test_model.py
Real Review

E:\Download\Fake review detection Ml>print(df['label'].unique())
Unable to initialize device PRN

E:\Download\Fake review detection Ml>python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> df = pd.read_csv("fake_reviews_dataset.csv")
>>> print(df['label'].unique())
['CG' 'OR']
>>>
>>> import pandas as pd
>>> df = pd.read_csv("fake_reviews_dataset.csv")
>>> print(df['label'].unique())
['CG' 'OR']
>>> exit

E:\Download\Fake review detection Ml>python check_labels.py
['CG' 'OR']

E:\Download\Fake review detection Ml>python train_model.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\raj\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Accuracy: 88.20%
Model and vectorizer saved successfully!

E:\Download\Fake review detection Ml>python train_model.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\raj\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Accuracy: 88.20%
Model and vectorizer saved successfully!

E:\Download\Fake review detection Ml>python test_model.py

Enter a review to check (or type 'exit' to quit): it is good product
Prediction: Fake Review

Enter a review to check (or type 'exit' to quit): This product is really good! I’ve been using it for months and love it
Prediction: Fake Review

Enter a review to check (or type 'exit' to quit): Great quality and fast delivery. Would definitely buy again
Prediction: Real Review

Enter a review to check (or type 'exit' to quit): The customer service was helpful, and the item works perfectly
Prediction: Real Review

Enter a review to check (or type 'exit' to quit): exit

E:\Download\Fake review detection Ml>pip install flask
Requirement already satisfied: flask in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (3.1.0)
Requirement already satisfied: Werkzeug>=3.1 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from flask) (3.1.3)
Requirement already satisfied: Jinja2>=3.1.2 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from flask) (3.1.5)
Requirement already satisfied: itsdangerous>=2.2 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from flask) (2.2.0)
Requirement already satisfied: click>=8.1.3 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from flask) (8.1.8)
Requirement already satisfied: blinker>=1.9 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from flask) (1.9.0)
Requirement already satisfied: colorama in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from click>=8.1.3->flask) (0.4.6)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\raj\appdata\local\programs\python\python313\lib\site-packages (from Jinja2>=3.1.2->flask) (3.0.2)

E:\Download\Fake review detection Ml>python -c "import flask; print('Flask Installed Successfully!')"
Flask Installed Successfully!

E:\Download\Fake review detection Ml>python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 580-863-471
127.0.0.1 - - [08/Feb/2025 22:55:43] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Feb/2025 22:56:39] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Feb/2025 22:57:15] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Feb/2025 22:58:51] "GET /favicon.ico HTTP/1.1" 404 -
