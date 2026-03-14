from pathlib import Path


class DocumentLoader:

    def __init__(self, data_path):
        self.data_path = Path(data_path)

    def load_documents(self):
        documents = []

        for file_path in self.data_path.glob("*.md"):

            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            document = {
                "text": text,
                "source": file_path.name
            }

            documents.append(document)

        return documents