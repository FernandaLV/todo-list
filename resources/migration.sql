-- Table: public.tasks

-- DROP TABLE public.tasks;

CREATE TABLE public.tasks
(
    id integer NOT NULL DEFAULT nextval('tasks_id_seq'::regclass),
    key character(50) COLLATE pg_catalog."default" NOT NULL,
    "timestampCreate" timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    task character(200) COLLATE pg_catalog."default" NOT NULL,
    details text COLLATE pg_catalog."default",
    status character(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tasks_pkey PRIMARY KEY (id),
    CONSTRAINT key_unique UNIQUE (key)
)

TABLESPACE pg_default;
