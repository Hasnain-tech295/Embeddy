# pgvector instructions & tips

- Dimension: match the vector dimension to the embedding model:
  - `all-MiniLM-L6-v2` -> 384 dims
  - OpenAI `text-embedding-3-small` -> 1536 dims
  - Adjust `vector(<dim>)` in SQL accordingly.

- Index type:
  - For production-scale nearest neighbor: use `ivfflat` or `hnsw`.
  - Example: `using ivfflat (embedding vector_l2_ops) with (lists = 100)`.
  - Tune `lists` according to dataset size. Smaller datasets can use sequential scan.

- Example RPC (already included in scripts/setup_supabase.sql):
  - `match_embeddings(query_embedding vector, match_count int)` returns nearest neighbors.

- Performance:
  - Create the index AFTER inserting initial data.
  - For `ivfflat`, run `ANALYZE embeddings;` then `REINDEX` if necessary.

- Security:
  - Do not expose the service_role key to the browser. Use it server-side only.
