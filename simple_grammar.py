from itertools import permutations, product
from copy import deepcopy


class SimpleGrammar(object):

    def __init__(self, grammar_string):
        self.requirements = {}
        self.structure = []

        self.__parse(grammar_string)

    def __parse(self, grammar_string):
        self.grammar_string = grammar_string
        elements = grammar_string.split(' ')

        for element in elements:
            split = element.split('[')
            tag = split[0]
            split = split[1].split(']')[0].split(',')
            min_elements = int(split[0])
            if split[1] == '*':
                max_elements = None
            else:
                max_elements = int(split[1])

            self.structure.append({
                'tag': tag,
                'min': min_elements,
                'max': max_elements
            })

            if tag in self.requirements:
                self.requirements[tag] += min_elements
            else:
                self.requirements[tag] = min_elements

    def __meets_requirements(self, available_words):
        for req_key in self.requirements.keys():
            req_amount = self.requirements[req_key]

            if req_amount > 0:
                if req_key not in available_words:
                    return False

                elif req_amount > len(available_words[req_key]):
                    return False

        return True

    def __remove_duplciates_from_list(self, collection):
        return list(set(collection))

    @staticmethod
    def __get_available_words_from_tags(tags):
        available = {}
        for tag_tuple in tags:
            word = tag_tuple[0]
            tag = tag_tuple[1]
            if tag not in available:
                available[tag] = []

            available[tag].append(word)
        return available

    def __generate_from_subset(self, subset, structure_index=0):
        if structure_index == len(self.structure):
            return [""]

        results = []

        structural_element = self.structure[structure_index]

        structural_element_max = structural_element['max']
        if structural_element_max is None:
            if structural_element['tag'] in subset.keys():
                structural_element_max = len(subset[structural_element['tag']])
            else:
                structural_element_max = 0

        index = structural_element['min']

        accumulated_words = ""

        working_subset = deepcopy(subset)

        while index <= structural_element_max:
            # Range of how many words I can include here

            if structural_element['tag'] in working_subset.keys():
                if index > 0 and len(working_subset[structural_element['tag']]) > 0:
                    accumulated_words += (" " + working_subset[structural_element['tag']].pop(0))

            returned_results = self.__generate_from_subset(working_subset, structure_index + 1)
            for returned_result in returned_results:
                results.append(accumulated_words + returned_result)

            index += 1

        return results

    def __fix_result(self, phrase):
        phrase = phrase.strip()
        phrase = phrase.replace(" 's", "'s")
        phrase = phrase.replace("  ", " ")
        return phrase

    def generate_from(self, tags):
        available = self.__get_available_words_from_tags(tags)

        # Does not meet these rule's requirements
        if not self.__meets_requirements(available):
            return []

        # If it does meet requirements, do permutations
        productable = []

        for key in available.keys():
            available[key] = list(permutations(available[key]))
            tuples = []
            for a_tuple in available[key]:
                tuples.append(list(a_tuple))

            available[key] = tuples
            productable.append(tuples)

        results = []
        productable = product(*productable)
        productable = list(productable)
        available_keys = list(available.keys())
        for producted in productable:
            working_subset = {}
            for idx, sub_product in enumerate(producted):
                working_subset[available_keys[idx]] = list(sub_product)

            sub_results = self.__generate_from_subset(working_subset)
            for sub_result in sub_results:
                sub_result = self.__fix_result(sub_result)

                results.append(sub_result)

        results = self.__remove_duplciates_from_list(results)
        return results
