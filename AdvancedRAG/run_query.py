import warnings
warnings.filterwarnings('ignore')
import utils
import os
import openai
from llama_index.core import SimpleDirectoryReader
from llama_index.core import (
    ServiceContext,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.node_parser import HierarchicalNodeParser
from llama_index.core.node_parser import get_leaf_nodes
from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import AutoMergingRetriever
from llama_index.core import Document
from llama_index.llms.openai import OpenAI
from create_index import create_index_with_doc


def run_the_query(lquery):
    
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
    
    node_parser = HierarchicalNodeParser.from_defaults(
                chunk_sizes=[2048, 512, 128]
        )

    auto_merging_context = ServiceContext.from_defaults(
                llm=llm,
                embed_model="local:BAAI/bge-small-en-v1.5",
                node_parser=node_parser,
        )

    automerging_index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir="./merging_index"),
            service_context=auto_merging_context
            )

    automerging_retriever = automerging_index.as_retriever(
        similarity_top_k=12
    )

    retriever = AutoMergingRetriever(
        automerging_retriever, 
        automerging_index.storage_context, 
        verbose=True
    )

    rerank = SentenceTransformerRerank(top_n=6, model="BAAI/bge-reranker-base")

    auto_merging_engine = RetrieverQueryEngine.from_args(
        automerging_retriever, node_postprocessors=[rerank]
    )

    auto_merging_response = auto_merging_engine.query(lquery)
    
    return(str(auto_merging_response))
