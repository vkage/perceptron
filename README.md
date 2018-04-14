# Installing python with Anaconda and TensorFlow
On window i open anaconda prompt and there create a new environment named chatbot

	conda create -n chatbot python=3.6 anaconda

After that i activate a virtual environment.
For windows anaconda prompt type

	activate chatbot

Now iam in chatbot environment. Here iam installing Tensor flow as

	pip install tensorflow

Ok, then close the prompt and goto anaconda navigator and switch to chatbot environment.Here i use spyder to do all the coding. Then all set to work.

# Getting dataset 
I found a dataset which is called [Cornell Movie DialogsCorpus](http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html).This corpus contains a large metadata-rich collection of fictional conversations extracted from raw movie scripts:

[zip file](http://www.cs.cornell.edu/~cristian/data/cornell_movie_dialogs_corpus.zip)

DESCRIPTION:
- 220,579 conversational exchanges between 10,292 pairs of movie characters

- involves 9,035 characters from 617 movies

- in total 304,713 utterances(a line said by a character)

- movie metadata included:

    - genres

    - release year

    - IMDB rating

    - number of IMDB votes

    - IMDB rating

- character metadata included:

    - gender (for 3,774 characters)

    - position on movie credits (3,321 characters)

[SOURCE LINK](http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)

From this corpus i get data and metadata files, out of these i only need movie_conversations.txt and movie_lines.txt. Next i created a dictionary that map each line and its id.
