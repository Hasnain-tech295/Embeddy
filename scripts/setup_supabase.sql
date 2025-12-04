-- SQL snippets for pgvector table/index
-- This file shows a minimal example of a pgvector table and an RPC for matching.
-- Adjust to your Supabase schema and create via supabase SQL editor.

create extension if not exists vector;

create table if not exists embeddings (
  id text primary key,
  embedding vector(384), -- adjust dimension based on model
  metadata jsonb
);

create index if not exists embeddings_embedding_idx
  on embeddings using ivfflat (embedding vector_l2_ops) with (lists = 100);

-- Example RPC function that returns top-k nearest neighbors by inner product/distance
create or replace function match_embeddings(query_embedding vector, match_count int)
returns table (id text, score float, metadata jsonb)
language sql
as $$
  select id, 1 - (embedding <#> query_embedding) as score, metadata
  from embeddings
  order by embedding <#> query_embedding
  limit match_count;
$$;
