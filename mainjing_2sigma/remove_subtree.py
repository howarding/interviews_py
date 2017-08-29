class Node:
    def __init__(self, parent, val, valid = True):
        self.parent = parent
        self.val = val
        self.valid = valid
        # TODO: new field
        self.visited = False


class Tree:
    def __init__(self, nodes):
        '''
        :param List[Node] nodes:
        '''
        # TODO: initialize
        self.nodes = nodes
        self.capacity = len(nodes)
        self.size = self.capacity

    def deleteSubtree(self, index):
        # TODO: complete this function
        if index < 0 or index > self.capacity:
            print 'index out of range.'
            return
        if self.nodes[index].valid == False:
            return

        self.nodes[index].valid = False
        self.nodes[index].visited = True
        for i in range(self.capacity):
            if self.nodes[i].visited:
                continue
            self.__mark(i)

        self.size = 0
        for node in self.nodes:
            if node.valid:
                node.visited = False
                self.size += 1

    # TODO: new recursive function
    def __mark(self, index):
        if index == -1:
            return True
        if self.nodes[index].visited:
            return self.nodes[index].valid
        self.nodes[index].valid = self.__mark(self.nodes[index].parent)
        self.nodes[index].visited = True
        return self.nodes[index].valid


