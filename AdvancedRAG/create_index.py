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
#from llama_index.llms import OpenAI
from llama_index.llms.openai import OpenAI


def create_index_with_doc():
    retVal = "default"
    openai.api_key = "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"
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
    
    node_parser = HierarchicalNodeParser.from_defaults(
            chunk_sizes=[2048, 512, 128]
    )

    #create service context
    auto_merging_context = ServiceContext.from_defaults(
            llm=llm,
            embed_model="local:BAAI/bge-small-en-v1.5",
            node_parser=node_parser,
    )
    
    #if index file is not present, create the index
    if not os.path.exists("./merging_index"):
    
        #get each page as documents[n]
        documents = SimpleDirectoryReader(
            input_files=["./eBook-How-to-Build-a-Career-in-AI.pdf"]
        ).load_data()
        
        #join all pages
        document = Document(text="\n\n".join([doc.text for doc in documents]))

        # create the hierarchical node parser w/ default settings
        nodes = node_parser.get_nodes_from_documents([document])

        leaf_nodes = get_leaf_nodes(nodes)

        nodes_by_id = {node.node_id: node for node in nodes}
        parent_node = nodes_by_id[leaf_nodes[30].parent_node.node_id]

        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(nodes)

        automerging_index = VectorStoreIndex(
            leaf_nodes, storage_context=storage_context, service_context=auto_merging_context
        )

        automerging_index.storage_context.persist(persist_dir="./merging_index")
        retVal = "Created mew directory"
    else:
        
        automerging_index = load_index_from_storage(
        StorageContext.from_defaults(persist_dir="./merging_index"),
        service_context=auto_merging_context
        )
        
        retVal = "Use old directory"
     
    
    
    return retVal

