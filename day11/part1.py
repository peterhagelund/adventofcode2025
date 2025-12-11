import networkx as nx


def main():
    graph = nx.DiGraph()
    with open('puzzle_input.txt') as f:
        for line in f:
            source, destinations = line.strip().split(':')
            if not graph.has_node(source):
                graph.add_node(source)
            for destination in destinations.split():
                if not graph.has_node(destination):
                    graph.add_node(destination)
                graph.add_edge(source, destination)
    paths = nx.all_simple_paths(graph, 'you', 'out')
    answer = len(list(paths))
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
