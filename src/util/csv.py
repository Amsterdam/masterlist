import csv

from django.http import HttpResponse, StreamingHttpResponse


class CSVBuffer:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Return the string to write."""
        return value


class CSVExport:
    """Class to (download) an iterator to a
    CSV file."""

    def __init__(self, encoding='utf-8', delimiter=','):
        self.encoding = encoding
        self.delimiter = delimiter

    def serializer(self, iterator):
        writer = csv.writer(CSVBuffer(), delimiter=self.delimiter, lineterminator='\n')
        try:
            row = next(iterator)
            yield writer.writerow(row.keys())
            yield writer.writerow(row.values())

            for row in iterator:
                yield writer.writerow(row.values())
        except StopIteration:
            return

    def export(
        self,
        filename,
        iterator,
        serializer=None,
        header=None,
        streaming=False,
        download=True,
    ):
        if not serializer:
            serializer = self.serializer

        # 2. Create the HttpResponse using our iterator as content
        cls = StreamingHttpResponse if streaming else HttpResponse

        response = cls(self.serializer(iterator), charset=self.encoding)

        # 3. Add additional headers to the response
        if download:
            response['content-type'] = "text/csv"
            response['Content-Disposition'] = f"attachment; filename={filename}.csv"
        # 4. Return the response
        return response
