from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, collection):
        pass

class QuickSortStrategy(SortStrategy):
    def sort(self, collection):
        # Implement Quick Sort algorithm
        return sorted(collection)

class MergeSortStrategy(SortStrategy):
    def sort(self, collection):
        # Implement Merge Sort algorithm
        return sorted(collection)
class Sorter:
    def __init__(self, strategy:"SortStrategy"):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_collection(self, collection):
        return self.strategy.sort(collection)

# Usage
collection = [3, 1, 4, 1, 5, 9, 2, 6]
quick_sorter = Sorter(QuickSortStrategy())
sorted_collection = quick_sorter.sort_collection(collection)
print("Quick Sort:", sorted_collection)

merge_sorter = Sorter(MergeSortStrategy())
sorted_collection = merge_sorter.sort_collection(collection)
print("Merge Sort:", sorted_collection)