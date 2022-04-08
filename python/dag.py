# coding=utf-8
import json
import Queue

class Node:
    def __init__(self, name, op_type, inputs, attr):
        self.name_ = name
        self.type_ = op_type
        self.inputs_ = inputs
        self.attr_ = attr
        self.wait_ = 0

    def __str__(self):
        result = "op name: %s\n op type: %s\n inputs: %s\n attr: %s\n" %(self.name_, self.type_, self.inputs_, self.attr_)
        return result

class DAG:
    def __init__(self, graph_conf):
        self.graph_conf_ = graph_conf

    def NodeNums(self):
        return len(self.nodes_)

    def Init(self):
        with open(self.graph_conf_) as fl:
          flstr = fl.read()
          self.conf_json_ = json.loads(flstr)
        #print("graph config is %s" % self.conf_json_)

        self.nodes_ = {}
        for node_name,node_value in self.conf_json_.items():
            op_type = node_value["type"]
            op_inputs = node_value["inputs"]
            op_attr = node_value["attr"]
            self.nodes_[node_name] = Node(node_name, op_type, op_inputs, op_attr)
            if (op_type == "graph_input"):
                self.begin_node_ = self.nodes_[node_name]
                print("begin node:%s" %self.begin_node_)
            if (op_type == "graph_output"):
                self.end_node_ = self.nodes_[node_name]
        self.CalcDepends()
        if (self.CheckCycle()):
            print("the dag has cycles")

    def CalcDepends(self):  ## 遍历节点，计算依赖关系
        self.depends_ = {}
        for node_name, node in self.nodes_.items():
            #print("node is: %s" %node)
            for depend_name in node.inputs_:
              node.wait_ += 1
              if (self.depends_.has_key(depend_name)):
                  self.depends_[depend_name].append(node_name)
              else:
                  self.depends_[depend_name] = [node_name]
        print("depends: %s" %self.depends_)

    def CheckCycle(self):
        queue = Queue.Queue()
        queue.put(self.begin_node_)
        node_num = 1
        while (not queue.empty()):
            cur_node = queue.get()
            print("cur_node: %s" %cur_node)
            node_num += 1
            if (self.depends_.has_key(cur_node.name_)):
              for node in self.depends_[cur_node.name_]:
                  self.nodes_[node].wait_ -= 1
                  if (self.nodes_[node].wait_ == 0):
                      queue.put(self.nodes_[node])
        print("node_num: %d" %node_num)
        return node_num == self.NodeNums()

    def GetBeginNode(self):
        return self.begin_node_

    def GetEndNode(self):
        return self.end_node_


if __name__ == '__main__':
  graph_conf = "./graph.json"
  dag = DAG(graph_conf)
  dag.Init()
