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
            min = int(split[0])
            if split[1] == '*':
                max = None
            else:
                max = int(split[1])

            self.structure.append({
                'tag': tag,
                'min': min,
                'max': max
            })

            if tag in self.requirements:
                self.requirements[tag] += min
            else:
                self.requirements[tag] = min


    def generate_from(self, tags):
        pass
