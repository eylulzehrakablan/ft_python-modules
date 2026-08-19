from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise ValueError("No data left in the processor.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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
    def validate(self, data: typing.Any) -> bool:
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
    def validate(self, data: typing.Any) -> bool:
        def is_valid_dict(d: typing.Any) -> bool:
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
            return ": ".join(f"{k}: {v}" for k, v in log_dict.items())

        if isinstance(data, list):
            for item in data:
                formatted = format_log(item)
                self._storage.append((self._total_processed, formatted))
                self._total_processed += 1
        else:
            formatted = format_log(data)
            self._storage.append((self._total_processed, formatted))
            self._total_processed += 1


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        csv_output = ",".join(item[1] for item in data)
        print(csv_output)


class JsonPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_output = "{"
        for item in data:
            json_output += f'"item_{item[0]}": "{item[1]}", '
        json_output += "}"
        print(json_output)


class DataStream:
    def __init__(self) -> None:
        print("Initialize Data Stream...")
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            handled = False

            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    handled = True
                    break

            if not handled:
                print("DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            proc_name = proc.__class__.__name__.replace(
                "Processor", " Processor")
            total = proc._total_processed
            remaining = len(proc._storage)
            print(f"{proc_name}: total {total} items processed, "
                  f"remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            data_to_export: list[tuple[int, str]] = []

            for _ in range(nb):
                try:
                    data_to_export.append(proc.output())
                except ValueError:
                    break

            if data_to_export:
                plugin.process_output(data_to_export)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    stream = DataStream()
    stream.print_processors_stats()

    n_proc = NumericProcessor()
    t_proc = TextProcessor()
    l_proc = LogProcessor()
    print("\nRegistering Processors\n")
    stream.register_processor(n_proc)
    stream.register_processor(t_proc)
    stream.register_processor(l_proc)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)

    stream.print_processors_stats()

    csv_plugin = CsvPlugin()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)

    stream.print_processors_stats()

    batch2 = [
        21,
        [
            'I love AI',
            'LLMs are wonderful',
            'Stay healthy'
        ],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    json_plugin = JsonPlugin()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)

    stream.print_processors_stats()
