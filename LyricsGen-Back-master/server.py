from textgenrnn import textgenrnn
import sampler


def get_model_api():
    '''Return lambda function for API'''
    # 1 Initilize model once and for all and reload weights

    config_path = 'weights/RapLyrics_word2_01_config.json'
    vocab_path = 'weights/RapLyrics_word2_01_vocab.json'
    weights_path = 'weights/RapLyrics_word2_01_weights.hdf5'

    textgen = textgenrnn(config_path=config_path,
                         vocab_path=vocab_path,
                         weights_path=weights_path)
    textgen.generate() #resolved a memory addressing bug of keras, DO NOT remove

    def model_api(input_data):
        # 2. pre-process input
        punc = ["(", ")", "[",
                "]"]  # FIXME: add other cleaning if necessary, check if not redundant with library cleaning
        prefix = "".join(c.lower() for c in input_data if c not in punc)

        # 3.0 initialize generation parameters
        temperatures = [0.5, 0.6, 0.7] #TODO: to tweak.
        num_line = 5
        prefix_mode = 2  # see doc of sampler.py for mode 0,1,2
        prefix_proba = 0.5

        # 3.1 call model predict function
        prediction = sampler.lyrics_generator(textgen, prefix,
                                              temperatures=temperatures, num_line=num_line,
                                              prefix_mode=prefix_mode, prefix_proba=prefix_proba)

        # 4. process the output
        output_data = {"output": prediction}

        # 5. return the output for the api
        print(output_data)
        return output_data

    return model_api
