import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after(self, prev_node_data, data):
        current_node = self.head
        while current_node and current_node.data != prev_node_data:
            current_node = current_node.next
        if not current_node:
            print(f"Node with data {prev_node_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
    def visualize(self, filename):
        G = nx.DiGraph()
        current_node = self.head
        while current_node:
            G.add_node(current_node.data)
            if current_node.next:
                G.add_edge(current_node.data, current_node.next.data)
            current_node = current_node.next
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", arrows=True)
        plt.savefig(filename)
        plt.close()


linked_list = LinkedList()


linked_list.visualize("/output/initial_list.png")

linked_list.insert_at_beginning(3)
linked_list.visualize("/output/after_insert_3.png")

linked_list.insert_at_beginning(2)
linked_list.visualize("/output/after_insert_2.png")

linked_list.insert_at_end(4)
linked_list.visualize("/output/after_insert_4.png")

linked_list.insert_after(3, 5)
linked_list.visualize("/output/after_insert_5.png")

