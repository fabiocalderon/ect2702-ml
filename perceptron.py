class Perceptron(object):

    def __init__(self, input_size, epochs = 100, learning_rate = 0.4):
        import numpy as calc
        self._weights = calc.zeros(input_size + 1)
        self._epochs = epochs
        self._learninig_rate = learning_rate

    def ativa(self, input):
        return 1 if input >= 0 else 0

    def prediz(self,input):
        import numpy as calc
        S = calc.dot(input,self._weights[1:])+self._weights[0]
        return self.ativa(S)

    def treina(self, input, label):
        import numpy as calc
        for _ in range(self._epochs):
            #for input,label in zip(input,label):
            previsao = self.prediz(input)
            self._weights[1:] += self._learninig_rate * (label - previsao) * input
            self._weights[0] += self._learninig_rate * (label - previsao)

