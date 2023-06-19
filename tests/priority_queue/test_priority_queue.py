from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert len(queue) == 0

    item1 = {"qtd_linhas": 4, "nome": "Arquivo1.txt"}
    item2 = {"qtd_linhas": 9, "nome": "Arquivo2.txt"}
    item3 = {"qtd_linhas": 2, "nome": "Arquivo3.txt"}

    queue.enqueue(item1)
    queue.enqueue(item2)
    queue.enqueue(item3)

    assert len(queue) == 3
    assert queue.search(0) == item3
    assert queue.search(1) == item1
    assert queue.search(2) == item2
    assert queue.dequeue() == item3
    assert queue.dequeue() == item1
    assert queue.dequeue() == item2
    assert len(queue) == 0