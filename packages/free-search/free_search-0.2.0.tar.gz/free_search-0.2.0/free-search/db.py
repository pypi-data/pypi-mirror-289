import faiss
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
import json
import os


class VectorDB:
    def __init__(self, model_name="intfloat/multilingual-e5-large"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.index = None
        self.texts = []
        self.embeddings = None
        self.free_indices = []

    def _embed_texts(self, texts):
        inputs = self.tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings.numpy()

    def create_db(self, texts):
        embeddings = self._embed_texts(texts)
        self.texts = texts
        d = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(d)
        self.index.add(embeddings)
        self.embeddings = embeddings

    def add_data(self, texts):
        embeddings = self._embed_texts(texts)
        for i, text in enumerate(texts):
            if self.free_indices:
                idx = self.free_indices.pop(0)  # 使用空闲索引
                self.texts[idx] = text
                self.embeddings[idx] = embeddings[i]
            else:
                idx = len(self.texts)
                self.texts.append(text)
                if self.embeddings is None:
                    self.embeddings = embeddings[i:i+1]
                else:
                    self.embeddings = np.vstack([self.embeddings, embeddings[i:i+1]])
                self.index.add(embeddings[i:i+1])

    def update_data(self, idx, new_text):
        # 直接更新指定索引的数据，而不是删除再添加
        new_embedding = self._embed_texts([new_text])[0]
        self.texts[idx] = new_text
        self.embeddings[idx] = new_embedding
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def delete_data(self, indices):
        for idx in indices:
            self.texts[idx] = None  # 标记为已删除
            self.free_indices.append(idx)
        self.free_indices.sort()

    def search(self, query_texts, k=2):
        query_embeddings = self._embed_texts(query_texts)
        D, I = self.index.search(query_embeddings, k)
        results = []
        for i in range(len(query_texts)):
            query_result = []
            for j in range(k):
                neighbor_index = I[i, j]
                neighbor_text = self.texts[neighbor_index]
                similarity = 100 - D[i, j]  # 将距离转化为类似度分数
                query_result.append({
                    'rank': j + 1,
                    'similarity': similarity,
                    'index': neighbor_index,
                    'text': neighbor_text
                })
            results.append(query_result)
        return results

    def save_index(self, index_path, texts_path):
        if self.index:
            faiss.write_index(self.index, index_path)
            with open(texts_path, 'w', encoding='utf-8') as f:
                json.dump(self.texts, f, ensure_ascii=False)
            print(f"Index and texts saved to {index_path} and {texts_path}")
        else:
            print("No index to save.")

    def load_index(self, index_path, texts_path):
        if os.path.exists(index_path) and os.path.exists(texts_path):
            self.index = faiss.read_index(index_path)
            with open(texts_path, 'r', encoding='utf-8') as f:
                self.texts = json.load(f)
            self.embeddings = self._embed_texts(self.texts)
            print(f"Index and texts loaded from {index_path} and {texts_path}")
        else:
            print("Index or texts file not found.")
        
    def batch_add(self, texts):
        self.add_data(texts)
    
    def batch_update(self, indices, new_texts):
        for idx, new_text in zip(indices, new_texts):
            self.update_data(idx, new_text)

    def batch_delete(self, indices):
        self.delete_data(indices)

    def print_all_data(self):
        print("Current data in VectorDB:")
        for i, text in enumerate(self.texts):
            if text is not None:
                print(f"Index {i}: {text}")
    
    def export_data(self):
        print("Export data as list")
        export_list = []
        for i, text in enumerate(self.texts):
            if text is not None:
              export_list.append([i,text])

        return export_list
