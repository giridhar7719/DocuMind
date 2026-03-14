import tiktoken


class TextChunker:

    def __init__(self, chunk_size=500, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def count_tokens(self, text):
        return len(self.tokenizer.encode(text))

    def split_text(self, text):

        tokens = self.tokenizer.encode(text)

        chunks = []

        start = 0

        while start < len(tokens):

            end = start + self.chunk_size

            chunk_tokens = tokens[start:end]

            chunk_text = self.tokenizer.decode(chunk_tokens)

            chunks.append(chunk_text)

            start = end - self.overlap

        return chunks