from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.queue)
   
    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index > self.__len__() - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
