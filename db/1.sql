CREATE SEQUENCE public.seq_id
    INCREMENT 1
    START 28
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

CREATE TABLE public."User"
(
    id bigint NOT NULL DEFAULT nextval('seq_id'::regclass),
    name character(30) NOT NULL,
    surname character(100),
	login character(30) NOT NULL,
	role character(30) NOT NULL,
	password character(500) NOT NULL,
    active boolean NOT NULL default TRUE,
    deleted boolean NOT NULL default FALSE,
    CONSTRAINT "User_pkey" PRIMARY KEY (id)
);
