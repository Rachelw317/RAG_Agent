## 1. RAG到底解决了什么问题
LLM只能看到Prompt里的内容。所以RAG本质上不是增强LLM，而是prompt。
## 2. 为什么一定要设计 Embedding、Vector Database 和 Retriever？
所有Token都参与计算 & Noise。RAG = 从大量信息中，找到与当前问题最相关的那一小部分内容。
Retriever：帮 LLM 找到最有可能回答这个问题的文档。
## 3. 凭什么判断「相关性」？
Text → Embedding → Cosine Similarity。Embedding = 哪些词经常出现在相似的上下文。
为什么几乎所有 RAG 系统都要先把文档切成很多 Chunk，再分别做 Embedding，而不是对整本 PDF 做一次 Embedding？
Retriever 的计算开销其实不是主要问题。从数量上来说，Chunk 更多，比较次数反而更多。所以，如果只是为了减少 Retriever 的计算，我们应该不切 Chunk 才对。但现实世界所有 RAG 都会切 Chunk。说明真正的问题一定不是计算量。Chunk 不是为了让 Retriever 更快，而是为了让 Retriever 更精准。
**Embedding 的粒度，决定了 Retriever 能检索的粒度。**
而Chunk 太小，会破坏语义完整性（Semantic Integrity）。一个 Chunk 最好能够表达一个完整的意思。每个 Chunk 都应该尽可能包含一个完整的语义单元（Semantic Unit）。

LLM 无法记住所有企业知识
        ↓
需要把知识放到外部知识库
        ↓
Retriever 不可能读取所有文档
        ↓
Retriever 用 Embedding 判断语义相似性
        ↓
Embedding 的粒度决定了检索粒度
        ↓
因此需要 Chunk
        ↓
Chunk Size 是"检索精度"与"语义完整性"之间的平衡

Document对象：内容 + 元数据（Metadata）

{Document(
    page_content="Employees are allowed to ...",

    metadata={
        "source": "employee_handbook.pdf",
        "page": 3
    }
)
}

Document
├── page_content
│      ↓
│      真正的文本
│
└── metadata
       ↓
       关于这段文本的信息，回答数据来源


TextSplitter 的输入是 List[Document]，而不是一个 PDF 文件。继承原来的 Metadata。而不会跨页
LangChain 操作的不是字符串，而是 Document 对象。

                    LangChain Ecosystem

                    langchain
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
langchain-core   langchain-community   langgraph
        │                │
        │                ├──── PyPDFLoader
        │                ├──── Chroma
        │                ├──── FAISS
        │                ├──── Web Loader
        │                └──── ...
        │
        ├──── Document
        ├──── PromptTemplate
        ├──── Runnable
        └──── Base Classes
