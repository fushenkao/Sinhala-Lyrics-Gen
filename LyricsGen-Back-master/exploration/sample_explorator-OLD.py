"""OLD EXPLORATION FILE"""

from textgenrnn import textgenrnn
import re
import random


def text_cleaner(text):
    regex_patterns = []
    regex_patterns.append(("\n ", "\n"))  # space at beginning of line
    regex_patterns.append(("\n{2,}", "\n"))  # multiple newlines
    regex_patterns.append(("i ' m", "i'm"))  # i ' m -->i'm
    for (p, r) in regex_patterns:
        text = re.sub(re.compile(p), r, text)

    return text


"""Beginning of experiments"""

textgen = textgenrnn(config_path='weights/RapLyrics_word2_01_config.json',
                     vocab_path='weights/RapLyrics_word2_01_vocab.json',
                     weights_path='weights/RapLyrics_word2_01_weights.hdf5')

#textgen.generate_samples(prefix="everyday i",
                        # temperatures=[0.2, 0.5, 1.0])



print(textgen.generate(prefix="EVERYDAY I", return_as_list=True, n=1, temperature=0.5)[0])


def front_generator_old(prefix, temperatures=[0.4,0.5,0.6], num_line=10, full_memory=True, varying_temperatures=True, varying_newline_char= True, use_prefix=True):
    """

    :param prefix:
    :param temperatures:
    :param num_line:
    :param full_memory: if True, next line generation has in prefiw the full previous line.
    Else, next line generation is based on the last half of the previous line
    :param varying_temperatures: if True, will make the temperature randomly choosed in temperatures list
    at each line generation. Else, temperature will always be 0.5
    :param varying_newline_char:
    :param use_prefix: rather to use prefix in next line or start from random seed
    :return:
    """

    #TRY: maybe make the memory vary too? instead of only full or only half? maybe add no prefix too?
    #TRY: broke the function don't know where lol

    #generate first line
    temperature = random.choice(temperatures) if varying_temperatures else 0.5
    line_list = textgen.generate(prefix=prefix, return_as_list=True, n=1, temperature=temperature)

    for i in range(num_line -1):
        #get last line as a space separated list
        if full_memory:
            prefix = line_list[-1]
        else:
            #only get the last half of the previous sentence
            last_line_split = line_list[-1].split()
            last_words = last_line_split[(len(last_line_split)//2):]
            prefix = " ".join(last_words)

        temperature = random.choice(temperatures) if varying_temperatures else 0.5
        newline_char = random.choice(["","\n"]) if varying_newline_char else "\n"


        prefix = prefix + newline_char if use_prefix else None
        new_line = textgen.generate(prefix=prefix, return_as_list=True, n=1, temperature=temperature)[0]
        new_line = new_line.replace(prefix[:-0],'') if use_prefix else new_line
        line_list.append(new_line)
    text = '\n'.join(line_list)

    #clean text:
    text = text_cleaner(text)


    return text



#when full memory = true, generation tends to give the exact same output as the prefix
test_prefix = "low life"
test_text=front_generator_old(test_prefix, full_memory=True, varying_temperatures=False, varying_newline_char=False, use_prefix=True)
print(test_text)