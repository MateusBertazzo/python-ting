from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    mock = [
        {"qtd_linhas": 5},
        {"qtd_linhas": 3},
        {"qtd_linhas": 8},
        {"qtd_linhas": 2},
    ]

    result_priority_queue = PriorityQueue()

    result_priority_queue.enqueue(mock[0])
    result_priority_queue.enqueue(mock[1])
    result_priority_queue.enqueue(mock[2])
    result_priority_queue.enqueue(mock[3])

    assert len(result_priority_queue) == 4
    assert result_priority_queue.search(0) == mock[1]
    assert result_priority_queue.search(1) == mock[3]
    assert result_priority_queue.search(2) == mock[0]
    assert result_priority_queue.search(3) == mock[2]

    result_priority_queue.dequeue()
    assert len(result_priority_queue) == 3
    assert result_priority_queue.search(0) == mock[3]

    result_priority_queue.dequeue()
    assert len(result_priority_queue) == 2
    assert result_priority_queue.search(0) == mock[0]

    result_priority_queue.dequeue()
    assert len(result_priority_queue) == 1
    assert result_priority_queue.search(0) == mock[2]

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        result_priority_queue.search(26)
