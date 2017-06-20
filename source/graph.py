import Queue
import numpy as np
import copy

def queue_to_list(q):
    ss = []
    while not q.empty():
        ss.append(q.get())
        
    return ss


#########################################################################
#########################################################################
#########################################################################
class Vertex:
    def __init__(self,key):
        self.connectedTo = {}
        self.Vupdate = 0

        self.id = key
        self.edge = self.Neighbor()

        
    def Neighbor(self):
        return [x.id for x in self.connectedTo]

    def addNeighbor(self,nbr,weight = 0):
        if nbr not in self.connectedTo:
            self.connectedTo[nbr] = weight
            self.connectedTo[nbr] = weight
            self.edge = [x.id for x in self.connectedTo]
        
        if nbr in self.connectedTo:
            self.connectedTo[nbr] = weight
            self.connectedTo[nbr] = weight
            self.edge = [x.id for x in self.connectedTo]

    def remove_Neighbor(self,nbr):

        self.connectedTo[nbr] = 0
        self.edge.remove(nbr.id)
        del self.connectedTo[nbr]   
        self.edge = [x.id for x in self.connectedTo]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def connected(self):
        print self.__str__()

    def getConnections(self):
        return self.connectedTo.keys()  #the type of connected to is also a Vertex 

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        # print 'getWeight-----<<<<>>>>>',self.connectedTo[nbr]
        return self.connectedTo[nbr]

    def Change_Weight(self,nbr,weight = 1):
        self.connectedTo[nbr] = weight
        return weight

############################################################################
# TIPs:
# 1.delete element in edge, and should delete in connected direction first
#
#
##############################################################################
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.numEdges = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def remove_Vertex(self,key):
        self.numVertices = self.numVertices - 1
        for v in self:
            if key in v.edge:
                v.remove_Neighbor(self.vertList[key])
                self.numEdges = self.numEdges - 1

        del self.vertList[key]
        self.vertList = self.vertList

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None


    def getVertices(self):
        return self.vertList.keys()


    def addEdge(self,f,t,cost=1):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)

        if (f in self.vertList) and (t in self.vertList):

            if t not in self.vertList[f].edge:
                self.vertList[f].addNeighbor(self.vertList[t], cost)

            if f not in self.vertList[t].edge:
                self.vertList[t].addNeighbor(self.vertList[f], cost)
                self.numEdges = self.numEdges + 1

    def remove_Edge(self,f,t):
        if f in self.vertList[t].edge:

            self.vertList[t].remove_Neighbor(self.vertList[f])

            if t in self.vertList[f].edge:
                self.vertList[f].remove_Neighbor(self.vertList[t])

                self.numEdges = self.numEdges - 1 
            else:
                return None
        else:
            return None


    def getEdges(self,f):
        if f not in self.vertList:
            print 'without Vertex'
            return None
        else:       
            return [x.id for x in self.vertList[f].connectedTo]

    def getWeights(self,f,t):
        return self.vertList[f].getWeight(self.vertList[t])

    def ChangeWeight(self,f,t,cost = 1):
        self.vertList[f].Change_Weight(self.vertList[t],cost)
        self.vertList[t].Change_Weight(self.vertList[f],cost)

    def __iter__(self):
        return iter(self.vertList.values())

    def __contains__(self,n):
        return n in self.vertList

    def BSF(self,start = 0):
        
        G_len = self.numVertices 

        visited = [0] * G_len
        parents = [None] * G_len

        for v in self:

            i = v.id
            # print '---------',i
            visited[i] = 0
            parents[i] = None

        visited[start] = 1
        parents[start] = None
        q = Queue.Queue()#(maxsize = G_len)
        qq = Queue.Queue()#(maxsize = G_len)
        q.put(start)
        qq.put(start)

        while not q.empty(): #[x.id for x in self.connectedTo]
            ver = q.get()
            # print 'ver',ver

            for i in self.vertList[ver].connectedTo:
                if visited[i.id] == 0:
                    visited[i.id] = 1
                    q.put(i.id)
                    qq.put(i.id)

            visited[ver] = 2

  
        return queue_to_list(qq)


    def DSF(self,start = 0):
        
        G_len = self.numVertices 

        visited = [0] * G_len
        parents = [None] * G_len
        qq = Queue.Queue()

        for v in self:
            visited[v.id] = 0
            parents[v.id] = None

        def DFS_VISIT(v):
            visited[v.id] = 1
            qq.put(v.id)
            for i in v.connectedTo:            
                if visited[i.id] == 0:
                     DFS_VISIT(i)

        for v in self:
            if visited[v.id] == 0:
                DFS_VISIT(v)

        return queue_to_list(qq)

    def get_minCircle(self):
        if self.numEdges < self.numVertices:
            raise 'without circle in the graph'

        elif self.numEdges == self.numVertices:
            return self.vertList.keys()

        elif self.numEdges > self.numVertices:
            new_g = copy.copy(self)

            G_len = self.numVertices 
            visited = [0] * G_len
            circles = []

            qq = Queue.Queue()

            for v in new_g:
                visited[v.id] = 0

                if len(v.connectedTo) < 2:
                    new_g.remove_Vertex(v)

            def DFS_VISIT(v , DFS_graph = None):
                visited[v.id] = 1
                qq.put(v.id)
                for i in v.connectedTo:            
                    if visited[i.id] == 0:
                         DFS_VISIT(i)
                    
                    elif visited[i.id] != 0 and i.id != v.id:
                        qq.put(i.id)

                        cir = queue_to_list(qq)
                        circles.append(cir)
                        # for j in cir:
                        #     new_g.remove_Edge(v, j)
                        

            for v in new_g:
                print 'inline--->',v
                for vv in new_g:
                    visited[vv.id] = 0

                if len(v.connectedTo) < 2:
                    new_g.remove_Vertex(v)
                    continue

                # if visited[v.id] == 0:
                DFS_VISIT(v)
                
        return circles

if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,100)

    g.addEdge(6,1,1)


    print 'numVertices',g.numVertices
    print 'numEdges',g.numEdges
    for v in g:
        print v.id,v.edge

    print '\ng.remove_Vertex(4)\n'
    g.remove_Vertex(4)
    
    print 'numVertices',g.numVertices
    print 'numEdges',g.numEdges
    for v in g:
        print v.id,v.edge

    print '\n del 0 5'
    g.remove_Edge(0,5)
    
    print 'numVertices',g.numVertices
    print 'numEdges',g.numEdges
    for v in g:
        print v.id,v.edge    

    print '\n add 1 3'
    g.addEdge(1,3,10)

    for v in g:
        print v

    print 'numVertices',g.numVertices
    print 'numEdges',g.numEdges

    g.addEdge(5,2,104000000000040)
    # g.ChangeWeight(5,2,104000000000040)
    # g.remove_Vertex(2)
    print g.numVertices, g.numEdges
    for v in g:
        print v.id,v.edge
    # print g.getWeights(5,2)


    gg = Graph()
    for i in range(6):
        gg.addVertex(i)

    gg.addEdge(0,1,5)
    gg.addEdge(0,5,2)
    gg.addEdge(1,2,4)
    gg.addEdge(2,3,9)
    gg.addEdge(3,4,7)
    gg.addEdge(3,5,3)
    gg.addEdge(5,4,8)

    print gg.numVertices, gg.numEdges
    print gg.BSF()
    print gg.DSF()
    
    for v in gg:
        print v

    print 'circlrsss-->',gg.get_minCircle()