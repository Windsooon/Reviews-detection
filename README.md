# Reviews detection
Project for detect useful reviews in China app store

### Dependence

    pip3 install -r requirements

### Project Structure

    ├── LICENSE
    # Project Markdown file
    ├── Proposal.md
    # Project PDF file
    ├── Proposal.md\ -\ Grip.pdf
    ├── README.md
    ├── base.py
    # scripts for data analyze
    ├── after
    │   ├── bayes.py
    │   ├── chars.py
    │   ├── combine.py
    │   ├── length.py
    │   ├── random_guess.py
    │   └── trans.py
    # scripts for collect and clean data
    ├── before
    │   ├── get_comments.py
    │   ├── mul_to_one.py
    │   ├── simi.py
    │   └── split_comments.py
    # data contain useful and useless reviews
    ├── cleaned_data
    │   ├── fin_final.csv
    │   ├── fin_useful.csv
    │   ├── fin_useless.csv
    │   └── trans.xls
    # image files
    ├── img
    │   ├── hybrid.png
    │   ├── log_pro_useful.png
    │   ├── log_pro_useless.png
    │   ├── long_or_short.png
    │   ├── native_bayes.png
    │   ├── pro.png
    │   ├── pro_less.png
    │   ├── random_guess.png
    │   ├── useful.png
    │   └── useless.png
    # project requirements
    └── requirements.txt

### Time
It took about two hours to run all the code.

### Quick start

#### Data clean
1. Run `get_comments.py` to access all the reviews
2. Run `mul_to_one.py` to combine all the reviews files into one
3. Run `simi.py` to label find the reviews has more than 80% similarity
4. Run `split_comments.py` to split useful and useless reviews after labeled.
5. Now `fin_useless.csv` contains all the useless reviews, `fin_usefull.csv` contains all the useful reviews and `fin_final.csv` contains all reviews.

#### Data analyze
1. Run `random_guess.py` get the scores from random guess
2. Run `length.py` get the scores after label the reviews out of range as useless.
3. Run `bayes.py` get the scores from native bayes algorithm.
4. Run `trans.py` to get POS probability for different reviews
5. Run `combine.py` to get scores from hybrid algorithms
6. Run `chars.py` to create diagrams.
