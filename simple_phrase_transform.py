from simple_grammar import SimpleGrammar

grammars = []


def init(grammar_strings):
    for grammar_string in grammar_strings:
        grammars.append(
            SimpleGrammar(grammar_string)
        )


def transform(phrase):
    results = []
    raise NotImplementedError()
    return results


def transform_batch(phrase_list):
    results = []
    for phrase in phrase_list:
        sub_results = transform(phrase)
        for sub_result in sub_results:
            results.append(sub_result)
    return results


def __get_tags(phrase):
    pass
