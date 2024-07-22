import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from llama_index.embeddings.together import TogetherEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.llms.together import TogetherLLM
from langchain_community.vectorstores import Milvus
from langchain_text_splitters import CharacterTextSplitter

# Load and preprocess the WELFake dataset
def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['text'] = df['text'].fillna('')
    df['label'] = df['label'].map({0: 'fake', 1: 'real'})
    return df

# Create embeddings using Together AI
def create_embeddings(texts):
    embed_model = TogetherEmbedding(
        model_name="togethercomputer/m2-bert-80M-8k-retrieval",
        api_key="your_together_api_key"
    )
    return [embed_model.get_text_embedding(text) for text in texts]

# Store embeddings in Zilliz Cloud
def store_embeddings(texts, embeddings):
    return Milvus.from_texts(
        texts,
        embeddings,
        connection_args={
            "uri": "your_zilliz_cloud_uri",
            "user": "your_username",
            "password": "your_password",
            "secure": True,
        },
    )

# Set up RAG pipeline with LlamaIndex and Llama 3
def setup_rag_pipeline():
    vector_store = MilvusVectorStore(
        uri="your_zilliz_cloud_uri",
        username="your_username",
        password="your_password",
        secure=True
    )
    index = VectorStoreIndex.from_vector_store(vector_store)
    llm = TogetherLLM(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        api_key="your_together_api_key"
    )
    return index.as_query_engine(llm=llm)

# Detect fake news using RAG pipeline
def detect_fake_news_rag(query_engine, statement):
    context = query_engine.query(statement)
    prompt = f"""
    Given the following context and news statement, determine if the statement is true or false.
    Provide a detailed explanation for your decision.
    
    Context: {context}
    
    News statement: {statement}
    
    Is this news statement true or false? Explain your reasoning step by step.
    """
    response = query_engine._llm.complete(prompt)
    return process_rag_output(response)

# Process RAG output
def process_rag_output(response):
    # Implement logic to parse LLM output
    # This is a simplified version and may need to be adapted based on the actual output format
    if "false" in response.lower():
        classification = "fake"
    else:
        classification = "real"
    explanation = response
    return {"classification": classification, "explanation": explanation}

# Train and evaluate KNN model
def train_and_evaluate_knn(X_train, y_train, X_test, y_test):
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
    return knn, accuracy, precision, recall, f1

# Main function to run the entire pipeline
def main():
    # Load and preprocess data
    df = load_and_preprocess_data('WELFake_Dataset.csv')
    
    # Split data
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    
    # TF-IDF Vectorization for KNN
    tfidf = TfidfVectorizer(max_features=5000)
    X_train_tfidf = tfidf.fit_transform(train_df['text'])
    X_test_tfidf = tfidf.transform(test_df['text'])
    
    # Train and evaluate KNN model
    knn_model, accuracy, precision, recall, f1 = train_and_evaluate_knn(
        X_train_tfidf, train_df['label'], X_test_tfidf, test_df['label']
    )
    print(f"KNN Model Performance:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    
    # Create embeddings and store in Zilliz Cloud
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(df['text'].tolist())
    embeddings = create_embeddings(texts)
    vector_db = store_embeddings(texts, embeddings)
    
    # Set up RAG pipeline
    query_engine = setup_rag_pipeline()
    
    # Example usage of RAG pipeline
    sample_news = test_df['text'].iloc[0]
    rag_result = detect_fake_news_rag(query_engine, sample_news)
    print(f"\nRAG Pipeline Result for sample news:")
    print(f"Classification: {rag_result['classification']}")
    print(f"Explanation: {rag_result['explanation']}")
    
    # Note: In a real-world scenario, you would evaluate the RAG pipeline on a test set
    # and compare its performance with the KNN model.

if __name__ == "__main__":
    main()
