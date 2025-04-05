# sort_strategy.py

class SortStrategy:
    """
    Abstract base class for defining a sorting strategy.
    All concrete sorting strategies should inherit from this class
    and implement the 'sort' method.
    """
    def sort(self, transactions):
        """
        Sorts a list of transaction dictionaries.

        Args:
            transactions (list[dict]): List of transaction records.

        Returns:
            list[dict]: Sorted list of transactions.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError
    

class SortByAmount(SortStrategy):
    """
    Concrete sorting strategy that sorts transactions by the 'amount' field in ascending order.
    """
    def sort(self, transactions):
        return sorted(transactions, key=lambda x: x['amount'])


class SortByDate(SortStrategy):
    """
    Concrete sorting strategy that sorts transactions by the 'date' field in ascending order.
    """
    def sort(self, transactions):
        return sorted(transactions, key=lambda x: x['date'])
    

class SortByCategory(SortStrategy):
    """
    Concrete sorting strategy that sorts transactions alphabetically by the 'category' field.
    """
    def sort(self, transactions):
        return sorted(transactions, key=lambda x: x['category'])
