{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "___\n",
    "# Recommender Systems with Python\n",
    "\n",
    "Welcome to the code notebook for Recommender Systems with Python. In this lecture we will develop basic recommendation systems using Python and pandas.\n",
    "\n",
    "In this notebook, we will focus on providing a basic recommendation system by suggesting items that are most similar to a particular item, in this case, movies. Keep in mind, this is not a true robust recommendation system, to describe it more accurately,it just tells you what movies/items are most similar to your movie choice.\n",
    "\n",
    "There is no project for this topic, instead you have the option to work through the advanced lecture version of this notebook (totally optional!).\n",
    "\n",
    "Let's get started!\n",
    "\n",
    "## Import Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Get the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "column_names = ['user_id', 'item_id', 'rating', 'timestamp']\n",
    "df = pd.read_csv('u.data', sep='\\t', names=column_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>item_id</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>172</td>\n",
       "      <td>5</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>133</td>\n",
       "      <td>1</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>196</td>\n",
       "      <td>242</td>\n",
       "      <td>3</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>186</td>\n",
       "      <td>302</td>\n",
       "      <td>3</td>\n",
       "      <td>891717742</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   user_id  item_id  rating  timestamp\n",
       "0        0       50       5  881250949\n",
       "1        0      172       5  881250949\n",
       "2        0      133       1  881250949\n",
       "3      196      242       3  881250949\n",
       "4      186      302       3  891717742"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's get the movie titles:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>item_id</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>GoldenEye (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Four Rooms (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Get Shorty (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Copycat (1995)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   item_id              title\n",
       "0        1   Toy Story (1995)\n",
       "1        2   GoldenEye (1995)\n",
       "2        3  Four Rooms (1995)\n",
       "3        4  Get Shorty (1995)\n",
       "4        5     Copycat (1995)"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_titles = pd.read_csv(\"Movie_Id_Titles\")\n",
    "movie_titles.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can merge them together:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>item_id</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>881250949</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>290</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>880473582</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>79</td>\n",
       "      <td>50</td>\n",
       "      <td>4</td>\n",
       "      <td>891271545</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>888552084</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>879362124</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   user_id  item_id  rating  timestamp             title\n",
       "0        0       50       5  881250949  Star Wars (1977)\n",
       "1      290       50       5  880473582  Star Wars (1977)\n",
       "2       79       50       4  891271545  Star Wars (1977)\n",
       "3        2       50       5  888552084  Star Wars (1977)\n",
       "4        8       50       5  879362124  Star Wars (1977)"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.merge(df,movie_titles,on='item_id')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# EDA\n",
    "\n",
    "Let's explore the data a bit and get a look at some of the best rated movies.\n",
    "\n",
    "## Visualization Imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "sns.set_style('white')\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a ratings dataframe with average rating and number of ratings:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "title\n",
       "Marlene Dietrich: Shadow and Light (1996)     5.0\n",
       "Prefontaine (1997)                            5.0\n",
       "Santa with Muscles (1996)                     5.0\n",
       "Star Kid (1997)                               5.0\n",
       "Someone Else's America (1995)                 5.0\n",
       "Name: rating, dtype: float64"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('title')['rating'].mean().sort_values(ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "title\n",
       "Star Wars (1977)             584\n",
       "Contact (1997)               509\n",
       "Fargo (1996)                 508\n",
       "Return of the Jedi (1983)    507\n",
       "Liar Liar (1997)             485\n",
       "Name: rating, dtype: int64"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('title')['rating'].count().sort_values(ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>2.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>2.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>2.908257</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>4.344000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>3.024390</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             rating\n",
       "title                              \n",
       "'Til There Was You (1997)  2.333333\n",
       "1-900 (1994)               2.600000\n",
       "101 Dalmatians (1996)      2.908257\n",
       "12 Angry Men (1957)        4.344000\n",
       "187 (1997)                 3.024390"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings = pd.DataFrame(df.groupby('title')['rating'].mean())\n",
    "ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now set the number of ratings column:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "      <th>num of ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>2.333333</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>2.600000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>2.908257</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>4.344000</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>3.024390</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             rating  num of ratings\n",
       "title                                              \n",
       "'Til There Was You (1997)  2.333333               9\n",
       "1-900 (1994)               2.600000               5\n",
       "101 Dalmatians (1996)      2.908257             109\n",
       "12 Angry Men (1957)        4.344000             125\n",
       "187 (1997)                 3.024390              41"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())\n",
    "ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now a few histograms:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1258f8780>"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x125a06ac8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,4))\n",
    "ratings['num of ratings'].hist(bins=70)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x125d12908>"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nQWcAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x125d12080>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,4))\n",
    "ratings['rating'].hist(bins=70)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.JointGrid at 0x126005320>"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\ndN2hmqPv2bOHVCrFPffcQzgcxjRN7r///gFbkcT4SSITQky4pqYm9u3bx69+9StOnz7Nl770JX79\n618Petyzzz7Ls88+S01NDQCHDh3i4MGDbN++nZaWFr74xS/ym9/8ZtLiHMvznTx5kv/9v/837e3t\nfOITnxjzta+77jquu+46IN0c/YYbbsDv93PXXXfxkY98hLVr1/Lyyy9z7NgxSWQXSBKZEAVix44d\n7Ny5k2g0Sm9vL1/84he59tpr2bt3Lw8++CAOh4P58+fzrW99i3g8nv1W39HRwc0338yNN97Ihg0b\nqKiooK+vj69//et87WtfQ9M0bNvmgQceoKqqivvvv5/9+/ejKAr/43/8DzZs2MBdd92F0+mkpaWF\nzs5O7rvvPpYuXcqaNWuora1l8eLFbN68ORvrxo0bicVi2Z8XL17MN77xjezP+/fvZ+XKlQDMnj0b\ny7Lo6elhxowZ2cc0Nzfzq1/9iv/1v/5XNsktXbqU//N//g8ALS0t2ZZ0zz//PK+//jqf/exns7/f\n0tLCl7/8ZSorK2lra+PKK6/kjjvuGPA3HS3O4Z6vv1gsxt/93d/xk5/8ZMDt3//+99m/fz+mafKZ\nz3yGtWvXDvn/NdMcPfO8r7zyCu94xzv4q7/6K+bOncvdd9895O+JcbCnkJMnT9oXX3yxffLkyXyH\nIsS4PfHEE/Ytt9xi27Ztd3Z22mvWrLF1XbevvfZau6ury7Zt237wwQft7du3201NTfYf/vAH27Zt\nu7293b722mtt27btT33qU/bOnTtt27btxx57zL733nttwzDsF1980T5y5Ij99NNP21/60pds27Zt\nXdftT3ziE/bhw4ftzZs32w8//LBt27a9fft2e8uWLbZt2/aSJUvsUCg07tfy0EMP2b/4xS+yP998\n8812c3Nz9udoNGrfcsstdldXl/3SSy/Zd9xxx4Df//73v2+/5z3vsXfs2DHsc5w6dcp+3/veZ/f1\n9dmmadqf/OQn7aampnHHOtbn27x5s/3888/btm3bzz77rL1p0ybbtm07mUzaH/3oR+1wODzk7912\n2232yy+/nP35Xe96V/Z5fvzjH9s//OEPzyvm4UzHz0EZkQlRQDJNtCsqKggGg3R0dHDmzBluv/12\nAJLJJO9///u56qqr+NnPfsbvf/97fD7fgE7nCxYsAGDdunU88sgj3HrrrZSWlnL77bfz5ptvUl9f\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x12554f8d0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Okay! Now that we have a general idea of what the data looks like, let's move on to creating a simple recommendation system:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Recommending Similar Movies"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's create a matrix that has the user ids on one access and the movie title on another axis. Each cell will then consist of the rating the user gave to that movie. Note there will be a lot of NaN values, because most people have not seen most of the movies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>title</th>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <th>187 (1997)</th>\n",
       "      <th>2 Days in the Valley (1996)</th>\n",
       "      <th>20,000 Leagues Under the Sea (1954)</th>\n",
       "      <th>2001: A Space Odyssey (1968)</th>\n",
       "      <th>3 Ninjas: High Noon At Mega Mountain (1998)</th>\n",
       "      <th>39 Steps, The (1935)</th>\n",
       "      <th>...</th>\n",
       "      <th>Yankee Zulu (1994)</th>\n",
       "      <th>Year of the Horse (1997)</th>\n",
       "      <th>You So Crazy (1994)</th>\n",
       "      <th>Young Frankenstein (1974)</th>\n",
       "      <th>Young Guns (1988)</th>\n",
       "      <th>Young Guns II (1990)</th>\n",
       "      <th>Young Poisoner's Handbook, The (1995)</th>\n",
       "      <th>Zeus and Roxanne (1997)</th>\n",
       "      <th>unknown</th>\n",
       "      <th>Á köldum klaka (Cold Fever) (1994)</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>user_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 1664 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "title    'Til There Was You (1997)  1-900 (1994)  101 Dalmatians (1996)  \\\n",
       "user_id                                                                   \n",
       "0                              NaN           NaN                    NaN   \n",
       "1                              NaN           NaN                    2.0   \n",
       "2                              NaN           NaN                    NaN   \n",
       "3                              NaN           NaN                    NaN   \n",
       "4                              NaN           NaN                    NaN   \n",
       "\n",
       "title    12 Angry Men (1957)  187 (1997)  2 Days in the Valley (1996)  \\\n",
       "user_id                                                                 \n",
       "0                        NaN         NaN                          NaN   \n",
       "1                        5.0         NaN                          NaN   \n",
       "2                        NaN         NaN                          NaN   \n",
       "3                        NaN         2.0                          NaN   \n",
       "4                        NaN         NaN                          NaN   \n",
       "\n",
       "title    20,000 Leagues Under the Sea (1954)  2001: A Space Odyssey (1968)  \\\n",
       "user_id                                                                      \n",
       "0                                        NaN                           NaN   \n",
       "1                                        3.0                           4.0   \n",
       "2                                        NaN                           NaN   \n",
       "3                                        NaN                           NaN   \n",
       "4                                        NaN                           NaN   \n",
       "\n",
       "title    3 Ninjas: High Noon At Mega Mountain (1998)  39 Steps, The (1935)  \\\n",
       "user_id                                                                      \n",
       "0                                                NaN                   NaN   \n",
       "1                                                NaN                   NaN   \n",
       "2                                                1.0                   NaN   \n",
       "3                                                NaN                   NaN   \n",
       "4                                                NaN                   NaN   \n",
       "\n",
       "title                   ...                  Yankee Zulu (1994)  \\\n",
       "user_id                 ...                                       \n",
       "0                       ...                                 NaN   \n",
       "1                       ...                                 NaN   \n",
       "2                       ...                                 NaN   \n",
       "3                       ...                                 NaN   \n",
       "4                       ...                                 NaN   \n",
       "\n",
       "title    Year of the Horse (1997)  You So Crazy (1994)  \\\n",
       "user_id                                                  \n",
       "0                             NaN                  NaN   \n",
       "1                             NaN                  NaN   \n",
       "2                             NaN                  NaN   \n",
       "3                             NaN                  NaN   \n",
       "4                             NaN                  NaN   \n",
       "\n",
       "title    Young Frankenstein (1974)  Young Guns (1988)  Young Guns II (1990)  \\\n",
       "user_id                                                                       \n",
       "0                              NaN                NaN                   NaN   \n",
       "1                              5.0                3.0                   NaN   \n",
       "2                              NaN                NaN                   NaN   \n",
       "3                              NaN                NaN                   NaN   \n",
       "4                              NaN                NaN                   NaN   \n",
       "\n",
       "title    Young Poisoner's Handbook, The (1995)  Zeus and Roxanne (1997)  \\\n",
       "user_id                                                                   \n",
       "0                                          NaN                      NaN   \n",
       "1                                          NaN                      NaN   \n",
       "2                                          NaN                      NaN   \n",
       "3                                          NaN                      NaN   \n",
       "4                                          NaN                      NaN   \n",
       "\n",
       "title    unknown  Á köldum klaka (Cold Fever) (1994)  \n",
       "user_id                                               \n",
       "0            NaN                                 NaN  \n",
       "1            4.0                                 NaN  \n",
       "2            NaN                                 NaN  \n",
       "3            NaN                                 NaN  \n",
       "4            NaN                                 NaN  \n",
       "\n",
       "[5 rows x 1664 columns]"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "moviemat = df.pivot_table(index='user_id',columns='title',values='rating')\n",
    "moviemat.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most rated movie:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "      <th>num of ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Star Wars (1977)</th>\n",
       "      <td>4.359589</td>\n",
       "      <td>584</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Contact (1997)</th>\n",
       "      <td>3.803536</td>\n",
       "      <td>509</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fargo (1996)</th>\n",
       "      <td>4.155512</td>\n",
       "      <td>508</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return of the Jedi (1983)</th>\n",
       "      <td>4.007890</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Liar Liar (1997)</th>\n",
       "      <td>3.156701</td>\n",
       "      <td>485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>English Patient, The (1996)</th>\n",
       "      <td>3.656965</td>\n",
       "      <td>481</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Scream (1996)</th>\n",
       "      <td>3.441423</td>\n",
       "      <td>478</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Toy Story (1995)</th>\n",
       "      <td>3.878319</td>\n",
       "      <td>452</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Air Force One (1997)</th>\n",
       "      <td>3.631090</td>\n",
       "      <td>431</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Independence Day (ID4) (1996)</th>\n",
       "      <td>3.438228</td>\n",
       "      <td>429</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 rating  num of ratings\n",
       "title                                                  \n",
       "Star Wars (1977)               4.359589             584\n",
       "Contact (1997)                 3.803536             509\n",
       "Fargo (1996)                   4.155512             508\n",
       "Return of the Jedi (1983)      4.007890             507\n",
       "Liar Liar (1997)               3.156701             485\n",
       "English Patient, The (1996)    3.656965             481\n",
       "Scream (1996)                  3.441423             478\n",
       "Toy Story (1995)               3.878319             452\n",
       "Air Force One (1997)           3.631090             431\n",
       "Independence Day (ID4) (1996)  3.438228             429"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings.sort_values('num of ratings',ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's choose two movies: starwars, a sci-fi movie. And Liar Liar, a comedy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "      <th>num of ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>2.333333</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>2.600000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>2.908257</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>4.344000</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>3.024390</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             rating  num of ratings\n",
       "title                                              \n",
       "'Til There Was You (1997)  2.333333               9\n",
       "1-900 (1994)               2.600000               5\n",
       "101 Dalmatians (1996)      2.908257             109\n",
       "12 Angry Men (1957)        4.344000             125\n",
       "187 (1997)                 3.024390              41"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's grab the user ratings for those two movies:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "user_id\n",
       "0    5.0\n",
       "1    5.0\n",
       "2    5.0\n",
       "3    NaN\n",
       "4    5.0\n",
       "Name: Star Wars (1977), dtype: float64"
      ]
     },
     "execution_count": 162,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "starwars_user_ratings = moviemat['Star Wars (1977)']\n",
    "liarliar_user_ratings = moviemat['Liar Liar (1997)']\n",
    "starwars_user_ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can then use corrwith() method to get correlations between two pandas series:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/marci/anaconda/lib/python3.5/site-packages/numpy/lib/function_base.py:2487: RuntimeWarning: Degrees of freedom <= 0 for slice\n",
      "  warnings.warn(\"Degrees of freedom <= 0 for slice\", RuntimeWarning)\n"
     ]
    }
   ],
   "source": [
    "similar_to_starwars = moviemat.corrwith(starwars_user_ratings)\n",
    "similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's clean this by removing NaN values and using a DataFrame instead of a series:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>0.872872</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>-0.645497</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>0.211132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>0.184289</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>0.027398</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           Correlation\n",
       "title                                 \n",
       "'Til There Was You (1997)     0.872872\n",
       "1-900 (1994)                 -0.645497\n",
       "101 Dalmatians (1996)         0.211132\n",
       "12 Angry Men (1957)           0.184289\n",
       "187 (1997)                    0.027398"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])\n",
    "corr_starwars.dropna(inplace=True)\n",
    "corr_starwars.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now if we sort the dataframe by correlation, we should get the most similar movies, however note that we get some results that don't really make sense. This is because there are a lot of movies only watched once by users who also watched star wars (it was the most popular movie). "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Commandments (1997)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Cosi (1996)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>No Escape (1994)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Stripes (1981)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Man of the Year (1995)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Hollow Reed (1996)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Beans of Egypt, Maine, The (1994)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Good Man in Africa, A (1994)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Old Lady Who Walked in the Sea, The (Vieille qui marchait dans la mer, La) (1991)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outlaw, The (1943)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                    Correlation\n",
       "title                                                          \n",
       "Commandments (1997)                                         1.0\n",
       "Cosi (1996)                                                 1.0\n",
       "No Escape (1994)                                            1.0\n",
       "Stripes (1981)                                              1.0\n",
       "Man of the Year (1995)                                      1.0\n",
       "Hollow Reed (1996)                                          1.0\n",
       "Beans of Egypt, Maine, The (1994)                           1.0\n",
       "Good Man in Africa, A (1994)                                1.0\n",
       "Old Lady Who Walked in the Sea, The (Vieille qu...          1.0\n",
       "Outlaw, The (1943)                                          1.0"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars.sort_values('Correlation',ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fix this by filtering out movies that have less than 100 reviews (this value was chosen based off the histogram from earlier)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>num of ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>0.872872</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>-0.645497</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>0.211132</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>0.184289</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>0.027398</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           Correlation  num of ratings\n",
       "title                                                 \n",
       "'Til There Was You (1997)     0.872872               9\n",
       "1-900 (1994)                 -0.645497               5\n",
       "101 Dalmatians (1996)         0.211132             109\n",
       "12 Angry Men (1957)           0.184289             125\n",
       "187 (1997)                    0.027398              41"
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars = corr_starwars.join(ratings['num of ratings'])\n",
    "corr_starwars.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now sort the values and notice how the titles make a lot more sense:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>num of ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Star Wars (1977)</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>584</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Empire Strikes Back, The (1980)</th>\n",
       "      <td>0.748353</td>\n",
       "      <td>368</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return of the Jedi (1983)</th>\n",
       "      <td>0.672556</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Raiders of the Lost Ark (1981)</th>\n",
       "      <td>0.536117</td>\n",
       "      <td>420</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Austin Powers: International Man of Mystery (1997)</th>\n",
       "      <td>0.377433</td>\n",
       "      <td>130</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                    Correlation  \\\n",
       "title                                                             \n",
       "Star Wars (1977)                                       1.000000   \n",
       "Empire Strikes Back, The (1980)                        0.748353   \n",
       "Return of the Jedi (1983)                              0.672556   \n",
       "Raiders of the Lost Ark (1981)                         0.536117   \n",
       "Austin Powers: International Man of Mystery (1997)     0.377433   \n",
       "\n",
       "                                                    num of ratings  \n",
       "title                                                               \n",
       "Star Wars (1977)                                               584  \n",
       "Empire Strikes Back, The (1980)                                368  \n",
       "Return of the Jedi (1983)                                      507  \n",
       "Raiders of the Lost Ark (1981)                                 420  \n",
       "Austin Powers: International Man of Mystery (1997)             130  "
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now the same for the comedy Liar Liar:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>num of ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Liar Liar (1997)</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Batman Forever (1995)</th>\n",
       "      <td>0.516968</td>\n",
       "      <td>114</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mask, The (1994)</th>\n",
       "      <td>0.484650</td>\n",
       "      <td>129</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Down Periscope (1996)</th>\n",
       "      <td>0.472681</td>\n",
       "      <td>101</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Con Air (1997)</th>\n",
       "      <td>0.469828</td>\n",
       "      <td>137</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Correlation  num of ratings\n",
       "title                                             \n",
       "Liar Liar (1997)          1.000000             485\n",
       "Batman Forever (1995)     0.516968             114\n",
       "Mask, The (1994)          0.484650             129\n",
       "Down Periscope (1996)     0.472681             101\n",
       "Con Air (1997)            0.469828             137"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])\n",
    "corr_liarliar.dropna(inplace=True)\n",
    "corr_liarliar = corr_liarliar.join(ratings['num of ratings'])\n",
    "corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}