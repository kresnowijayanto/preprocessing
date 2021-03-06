{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-7-3ef51201e221>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-7-3ef51201e221>\"\u001b[1;36m, line \u001b[1;32m6\u001b[0m\n\u001b[1;33m    [['France' 44.0 72000.0]\u001b[0m\n\u001b[1;37m                  ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "dataset = pd.read_csv('Data.csv')\n",
    "x = dataset.iloc[:, :-1].values\n",
    "y = dataset.iloc[:, -1].values\n",
    "\n",
    "print(X)\n",
    "[['Asia' 44.0 72000.0]\n",
    " ['Eropa' 27.0 48000.0]\n",
    " ['Amerika' 30.0 54000.0]\n",
    " ['Eropa' 38.0 61000.0]\n",
    " ['Amerika' 40.0 nan]\n",
    " ['Asia' 35.0 58000.0]\n",
    " ['Eropa' nan 52000.0]\n",
    " ['Asia' 48.0 79000.0]\n",
    " ['Amerika' 50.0 83000.0]\n",
    " ['Asia' 37.0 67000.0]]\n",
    "\n",
    "print(y)\n",
    "['No' 'Yes' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'No' 'Yes']\n",
    "\n",
    "from sklearn.impute import SimpleImputer\n",
    "imputer = SimpleImputer(missing_values=np.nan, strategy='mean')\n",
    "imputer.fit(X[:, 1:3])\n",
    "X[:, 1:3] = imputer.transform(X[:, 1:3])\n",
    "\n",
    "print(X)\n",
    "[['France' 44.0 72000.0]\n",
    " ['Spain' 27.0 48000.0]\n",
    " ['Germany' 30.0 54000.0]\n",
    " ['Spain' 38.0 61000.0]\n",
    " ['Germany' 40.0 63777.77777777778]\n",
    " ['France' 35.0 58000.0]\n",
    " ['Spain' 38.77777777777778 52000.0]\n",
    " ['France' 48.0 79000.0]\n",
    " ['Germany' 50.0 83000.0]\n",
    " ['France' 37.0 67000.0]]\n",
    "\n",
    "from sklearn.compose import ColumTransformer\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "ct = ColumTransformer(transformer=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')\n",
    "x = np.array(ct,fit_transform(X))\n",
    "\n",
    "print(X)\n",
    "[[1.0 0.0 0.0 44.0 72000.0]\n",
    " [0.0 0.0 1.0 27.0 48000.0]\n",
    " [0.0 1.0 0.0 30.0 54000.0]\n",
    " [0.0 0.0 1.0 38.0 61000.0]\n",
    " [0.0 1.0 0.0 40.0 63777.77777777778]\n",
    " [1.0 0.0 0.0 35.0 58000.0]\n",
    " [0.0 0.0 1.0 38.77777777777778 52000.0]\n",
    " [1,0 0.0 0.0 48.0 79000.0]\n",
    " [0.0 1.0 0.0 50.0 83000.0]\n",
    " [1.0 0.0 0.0 37.0 67000.0]]\n",
    "\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "le = LabelEncoder()\n",
    "y =  le.fit_tranform\n",
    "\n",
    "print(y)\n",
    "[0 1 0 0 1 1 0 1 0 1]\n",
    "\n",
    "from sklearn.model+selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)\n",
    "print(X_train)\n",
    "[[0.0 0.0 1.0 38.77777777777778 52000.0]\n",
    " [0.0 1.0 0.0 40.0 63777.77777777778]\n",
    " [1.0 0.0 0.0 44.0 72000.0]\n",
    " [0.0 0.0 1.0 27.0 48000.0]\n",
    " [0.0 1.0 0.0 30.0 54000.0]\n",
    " [0.0 0.0 1.0 38.0 61000.0]\n",
    " [1.0 0.0 0.0 35.0 58000.0]\n",
    " [1,0 0.0 0.0 48.0 79000.0]\n",
    " [0.0 1.0 0.0 50.0 83000.0]\n",
    " [1.0 0.0 0.0 37.0 67000.0]]\n",
    "print(X_test)\n",
    "[[0.0 1.0 0.0 30.0 54000.0]\n",
    " [1.0 0.0 0.0 37.0 67000.0]]\n",
    "print(y_train)\n",
    "[0 1 0 0 1 1 0 1]\n",
    "print(y_test)\n",
    "[0 1]\n",
    "\n",
    "from sklearn.proccessing import StandardScaler\n",
    "sc = StandardScaler()\n",
    "X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])\n",
    "X_test[:, 3:] = sc.tarnsform(X_test[:, 3;])\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
