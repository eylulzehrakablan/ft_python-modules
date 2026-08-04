from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise ValueError("No data left in the processor.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._total_processed, str(item)))
                self._total_processed += 1
        else:
            self._storage.append((self._total_processed, str(data)))
            self._total_processed += 1

class TextProcessor(DataProcessor):
    def validate(self, data: any) -> bool:
        if isinstance(data, (str)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._total_processed, str(item)))
                self._total_processed += 1
        else:
            self._storage.append((self._total_processed, str(data)))
            self._total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: any) -> bool:
        def is_valid_dict(d) -> bool:
            return (
                isinstance(d, dict) and
                all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in d.items()
                )
            )

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(item) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(log_dict: dict[str, str]) -> str:
            if "log_level" in log_dict and "log_message" in log_dict:
                return f"{log_dict['log_level']}: {log_dict['log_message']}"

        if isinstance(data, list):
            for item in data:
                formatted = format_log(item)
                self._storage.append((self._total_processed, formatted))
                self._total_processed += 1
        else:
            self._storage.append((self._total_processed, formatted))
            self._total_processed += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    n_proc = NumericProcessor()
    print(f" Tring to validate input '42': {n_proc.validate(42)}")
    print(f" Tring to validate input 'Hello': {n_proc.validate('Hello')}")

    print(f" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        n_proc.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")

    n_list = [1, 2, 3, 4, 5]
    n_proc.ingest(n_list)
    print(f" Processing data: {n_list}")
    print(" Extracting 3 values...")
    for _ in range(3):
        order, value = n_proc.output()
        print(f" Numeric value {order}: {value}")

    print("\nTesting Text Processor...")
    t_proc = TextProcessor()
    print(f" Tring to validate input '42': {t_proc.validate(42)}")
    print(f" Tring to validate input 'Hello': {t_proc.validate('Hello')}")
    t_list = ["Hello", "Nexus", "World"]
    t_proc.ingest(t_list)
    print(f" Processing data: {t_list}")
    print(" Extracting 1 value...")
    order, value = t_proc.output()
    print(f" Text value: {order} {value}")

    print("\nTesting Log Processor...")
    l_proc = LogProcessor()
    print(f" Tring to validate input 'Hello': {l_proc.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Conntection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    l_proc.ingest(logs)
    print(f" Processing data: {logs}")
    print(" Extracting 2 values...")
    for _ in range(2):
        order, value = l_proc.output()
        print(f" Log entry {order}: {value}")
