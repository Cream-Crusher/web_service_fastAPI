-- Создание модели categories
CREATE TABLE IF NOT EXISTS public.categories
(
  id serial PRIMARY KEY,
  title varchar(50),
  created_at timestamp,
  updated_at timestamp,
  clues_count integer
);

CREATE INDEX IF NOT EXISTS ix_categories_title ON public.categories USING btree(title);

-- Создание модели quizzes
CREATE TABLE IF NOT EXISTS public.quizzes
(
  id serial PRIMARY KEY,
  answer varchar(50),
  question varchar(500),
  created_at timestamp,
  updated_at timestamp,
  category_id integer NOT NULL,
  parsed_at timestamp DEFAULT now(),

  CONSTRAINT quizzes_category_id_fkey
  FOREIGN KEY (category_id) REFERENCES public.categories (id)
);

CREATE INDEX IF NOT EXISTS ix_quizzes_answer ON public.quizzes USING btree(answer);
CREATE INDEX IF NOT EXISTS ix_quizzes_question ON public.quizzes USING btree(question);
