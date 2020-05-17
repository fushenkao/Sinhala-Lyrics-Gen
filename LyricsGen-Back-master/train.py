from textgenrnn import textgenrnn

"""Sample code to train a model"""

"""
new_model: True to create a new model or False to train based on an existing one.
rnn_layers: Number of recurrent LSTM layers in the model (default: 2)
rnn_size: Number of cells in each LSTM layer (default: 128)
rnn_bidirectional: Whether to use Bidirectional LSTMs, which account for sequences both forwards and backwards. Recommended if the input text follows a specific schema. (default: False)
max_length: Maximum number of previous characters/words to use before predicting the next token. This value should be reduced for word-level models (default: 40)
max_words: Maximum number of words (by frequency) to consider for training (default: 10000)
dim_embeddings: Dimensionality of the character/word embeddings (default: 100)
num_epochs: number of epochs. (model is save at eah epoch by default)
word_level: Whether to train the model at the word level (default: False)
dropout: ratio of character to ignore on each sentence, may lead to better results. Don't use with word model
train_size: ratio to use as training set. The remaining ratio will make a validation set. Default is 1. (no validation set)
gen_epochs: during the training, a generation test will be made at each multiple of gen_epochs. Default is 1 (generation at each epoch)
max_gen_length: length of the generation during training
"""


def main():
    # Generate word level model
    textgen = textgenrnn(name="RapLyrics_word2_01")

    textgen.reset()

    # TODO choose between lowered, augmented and vanilla dataset
    textgen.train_from_file('datasets/sinhala_data.txt',
                            new_model=True,
                            rnn_layers=2,
                            rnn_size=128, #default 128
                            rnn_bidirectional=True,
                            max_length=10,
                            max_words=41000,  # reduce to 34000 if we use the lowered dataset
                            dim_embeddings=300,
                            num_epochs=50,
                            word_level=True,
                            dropout=0,  # don't use with word model
                            train_size=1.0,
                            gen_epochs=5,
                            max_gen_length=50
                            )

    print(textgen.model.summary())

    # Generate a char level model
    # textgen2 = textgenrnn(name="RapLyrics_char2_01")

    # textgen2.reset()

    # TODO choose between lowered, augmented and vanilla dataset"""
    # textgen2.train_from_file('datasets/rapus_generalist_vanilla.txt',
    #                          new_model=True,
    #                          rnn_layers=2,
    #                          rnn_size=128,
    #                          rnn_bidirectional=True,
    #                          max_length=40,
    #                          dim_embeddings=300,
    #                          num_epochs=25,  # default is 50
    #                          dropout=0,  # may be tweaked
    #                          train_size=1.0,
    #                          gen_epochs=5,
    #                          )

    # print(textgen.model.summary())


if __name__ == '__main__':
    main()
