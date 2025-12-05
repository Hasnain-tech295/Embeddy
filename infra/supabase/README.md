# Supabase + pgvector — Quick Setup

1. Create a free Supabase project at https://app.supabase.com.
2. In the project, open the SQL editor and run the SQL in `scripts/setup_supabase.sql`.
   - This creates `embeddings` table and a `match_embeddings` RPC function.
   - Adjust `vector(384)` to your embedding dimension (check your model).
3. Get your project URL and `anon` or service role key:
   - Project settings -> API -> Project URL and anon/service_role key.
   - For server operations (upsert) prefer the **service_role** key (keep it secret).
4. (Optional) Enable Row Level Security (RLS) if you plan to use Supabase Auth.
5. Test with `supabase-py` (or curl via the REST endpoints) — ensure you can insert & select rows.
6. Add SUPABASE_URL and SUPABASE_KEY to `.env` or your deployment secrets.
