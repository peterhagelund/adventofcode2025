import networkx as nx


def paths_between_nodes(graph: nx.DiGraph, source: str, target: str) -> int:
    copy = nx.DiGraph(graph)
    ancestors = nx.ancestors(copy, target)
    not_needed: set[str] = set()
    for node in copy.nodes:
        if node not in ancestors and node != source and node != target:
            not_needed.add(node)
    copy.remove_nodes_from(not_needed)
    count = 0
    for _ in nx.all_simple_edge_paths(copy, source, target):
        count += 1
    return count


def main():
    graph = nx.DiGraph()
    sources: set[str] = set()
    with open('puzzle_input.txt') as f:
        for line in f:
            source, destinations = line.strip().split(':')
            sources.add(source)
            if not graph.has_node(source):
                graph.add_node(source)
            for destination in destinations.split():
                if not graph.has_node(destination):
                    graph.add_node(destination)
                graph.add_edge(source, destination)
    answer = 0
    fft_to_dac = paths_between_nodes(graph, 'fft', 'dac')
    if fft_to_dac != 0:
        svr_to_fft = paths_between_nodes(graph, 'svr', 'fft')
        dac_to_out = paths_between_nodes(graph, 'dac', 'out')
        answer += svr_to_fft * fft_to_dac * dac_to_out
    dac_to_fft = paths_between_nodes(graph, 'dac', 'fft')
    if dac_to_fft != 0:
        svr_to_dac = paths_between_nodes(graph, 'svr', 'dac')
        fft_to_out = paths_between_nodes(graph, 'fft', 'out')
        answer += svr_to_dac * dac_to_fft * fft_to_out
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
