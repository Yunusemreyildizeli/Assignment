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
