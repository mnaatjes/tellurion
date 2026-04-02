# tests/unit/test_prototype.py
import pytest
from rich import inspect
from llama_index.core import SimpleDirectoryReader, Settings, VectorStoreIndex, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.extractors import TitleExtractor, SummaryExtractor
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

def test_run():
    # Configure
    embedding = GoogleGenAIEmbedding(
        model_name="models/gemini-embedding-2-preview",
        api_key="AIzaSyDmekoeaPFmb-LKKioNBRH2mR8swTcv0O4",
        embed_batch_size=25,
        retries=5,
        timeout=30,
        num_workers=4,
        task_type="retrieval_document"
    )
    
    llm = GoogleGenAI(model="models/gemini-2.5-flash", api_key="AIzaSyDmekoeaPFmb-LKKioNBRH2mR8swTcv0O4")

    Settings.embed_model = embedding
    Settings.llm = llm

    # Assign Reader
    reader = SimpleDirectoryReader(input_files=["tests/data/sources/tmp/readme.md"])
    
    # Read Content
    documents = reader.load_data()
    
    # Parse
    #Initialize Parser
    parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
    nodes = parser.get_nodes_from_documents(documents)

    # Enrichment
    # Define Strategy
    extractors = [
        TitleExtractor(nodes=5),
        SummaryExtractor(summaries=["self","prev"])
    ]

    # Loop Extractor Strategies
    for ext in extractors:
        # Execute API Call
        metadata_dicts = ext.extract(nodes)

        # Zip information from dict into node
        for node, metadata in zip(nodes, metadata_dicts):
            node.metadata.update(metadata)
    
    # Embed and Index
    index = VectorStoreIndex(nodes)

    # Persist
    index.storage_context.persist(persist_dir="tests/data/persist/human_patterns")

    # Test
    query = index.as_query_engine()
    res = query.query("Give me a one paragraph summary of this document.")
    inspect(res)