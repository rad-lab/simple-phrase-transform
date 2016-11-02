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

            if req_key not in available_words:
                return False

            elif req_amount < len(available_words[req_key]):
                return False

        return True

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

    def generate_from(self, tags):
        available = self.__get_available_words_from_tags(tags)

        # Does not meet these rule's requirements
        if not self.__meets_requirements(available):
            return []

        # If it does meet requirements, do permutations
        return []
