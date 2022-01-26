from ast import operator
from multiprocessing.dummy import current_process
import random
import itertools
from typing import List


class STestGenerator():

    def __init__(self, level: str):
        self.level = level


    def __generate_stest_easy(self):
        MAX_OPERAND_NUMBER = 9
        MIN_OPERAND_NUMBER = 1
        NUM_OPERANDS = 2
        OPERATORS = ['-', '+']
        operands = sorted([random.randint(MIN_OPERAND_NUMBER, MAX_OPERAND_NUMBER) for _ in range(NUM_OPERANDS)], reverse=True)
        selected_operators = [random.choice(OPERATORS) for _ in range(NUM_OPERANDS - 1)]
        return operands, selected_operators


    def __generate_stest_medium(self):
        MAX_OPERAND_NUMBER = 30
        MIN_OPERAND_NUMBER = 1
        NUM_OPERANDS = 3
        OPERATORS = ['-', '+']
        operands = sorted([random.randint(MIN_OPERAND_NUMBER, MAX_OPERAND_NUMBER) for _ in range(NUM_OPERANDS)], reverse=True)
        selected_operators = [random.choice(OPERATORS) for _ in range(NUM_OPERANDS - 1)]
        return operands, selected_operators


    def __generate_stest_hard(self):
        MAX_OPERAND_NUMBER = 50
        MIN_OPERAND_NUMBER = 1
        NUM_OPERANDS = 4
        OPERATORS = ['-', '+']
        selected_operators = [random.choice(OPERATORS) for _ in range(NUM_OPERANDS - 1)]
        multiply_index = random.choice(range(NUM_OPERANDS - 1))
        selected_operators[multiply_index] = '*'
        operands = []
        for i in range(len(selected_operators)):
            operator = selected_operators[i] 
            if operator == '*':
                first_operand = random.randint(2, 9)
                second_operand = random.randint(10, 25)
                operands += [first_operand, second_operand]
            else: operands.append(random.randint(MIN_OPERAND_NUMBER, MAX_OPERAND_NUMBER))
        return operands, selected_operators



    def __get_answer_for_stest(self, operands: List[int], operators: List[str]):
        # Compute multiplication first
        j = 0
        for i, operator in enumerate(operators.copy()):
            if operator == '*':
                operand = operands[j] * operands[j + 1]
                operators.pop(i)
                operands.pop(j)
                operands.pop(j)
                operands.insert(j, operand)
            else: j += 1
        result = operands[0]
        j = 1
        for operator in operators:
            if operator == '+':
                result += operands[j]
            elif operator == '-':
                result -= operands[j]
            j += 1

        return result
                

    def generate_stest(self):
        if self.level == 'Easy':
            operands, operators = self.__generate_stest_easy()
        elif self.level == 'Medium':
            operands, operators = self.__generate_stest_medium()
        elif self.level == 'Hard':
            operands, operators = self.__generate_stest_hard()
        answer = self.__get_answer_for_stest(operands.copy(), operators.copy())
        operands = list(map(str, operands))
        operators.append('=')
        formula_elements = list(itertools.chain.from_iterable(zip(operands, operators)))
        formula = ' '.join(formula_elements) + ' ?'
        return formula, answer 


                    




