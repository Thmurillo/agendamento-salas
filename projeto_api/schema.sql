--
-- PostgreSQL database dump
--

-- Dumped from database version 14.17 (Homebrew)
-- Dumped by pg_dump version 14.17 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: blocks; Type: TABLE; Schema: public; Owner: thalesmurillo
--

CREATE TABLE public.blocks (
    id integer NOT NULL,
    block_name character varying(20)
);




--
-- Name: blocks_id_seq; Type: SEQUENCE; Schema: public; Owner: thalesmurillo
--

CREATE SEQUENCE public.blocks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;




--
-- Name: blocks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: thalesmurillo
--

ALTER SEQUENCE public.blocks_id_seq OWNED BY public.blocks.id;


--
-- Name: reservations; Type: TABLE; Schema: public; Owner: thalesmurillo
--

CREATE TABLE public.reservations (
    id integer NOT NULL,
    room_id integer NOT NULL,
    user_id integer NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL,
    confirmation boolean NOT NULL,
    reason text,
    block_id integer NOT NULL,
    date date NOT NULL,
    requester_course character varying(50) NOT NULL
);




--
-- Name: reservations_id_seq; Type: SEQUENCE; Schema: public; Owner: thalesmurillo
--

CREATE SEQUENCE public.reservations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;




--
-- Name: reservations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: thalesmurillo
--

ALTER SEQUENCE public.reservations_id_seq OWNED BY public.reservations.id;


--
-- Name: rooms; Type: TABLE; Schema: public; Owner: thalesmurillo
--

CREATE TABLE public.rooms (
    id integer NOT NULL,
    room_name character varying(50),
    number integer NOT NULL,
    block_id integer NOT NULL,
    capacity integer NOT NULL,
    resources text,
    restriction character varying(50) NOT NULL
);




--
-- Name: rooms_id_seq; Type: SEQUENCE; Schema: public; Owner: thalesmurillo
--

CREATE SEQUENCE public.rooms_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;




--
-- Name: rooms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: thalesmurillo
--

ALTER SEQUENCE public.rooms_id_seq OWNED BY public.rooms.id;


--
-- Name: students; Type: TABLE; Schema: public; Owner: thalesmurillo
--

CREATE TABLE public.students (
    id integer NOT NULL,
    user_id integer NOT NULL,
    full_name character varying(30) NOT NULL,
    cpf character varying(14) NOT NULL,
    academic_registry character varying(30) NOT NULL,
    email character varying(50) NOT NULL,
    course character varying(50) NOT NULL
);




--
-- Name: student_id_seq; Type: SEQUENCE; Schema: public; Owner: thalesmurillo
--

CREATE SEQUENCE public.student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;




--
-- Name: student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: thalesmurillo
--

ALTER SEQUENCE public.student_id_seq OWNED BY public.students.id;


--
-- Name: teachers; Type: TABLE; Schema: public; Owner: thalesmurillo
--

CREATE TABLE public.teachers (
    id integer NOT NULL,
    user_id integer NOT NULL,
    full_name character varying(30) NOT NULL,
    cpf character varying(14) NOT NULL,
    academic_registry character varying(30) NOT NULL,
    email character varying(50) NOT NULL,
    academic_title character varying(50) NOT NULL
);




--
-- Name: teacher_id_seq; Type: SEQUENCE; Schema: public; Owner: thalesmurillo
--

CREATE SEQUENCE public.teacher_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;




--
-- Name: teacher_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: thalesmurillo
--

ALTER SEQUENCE public.teacher_id_seq OWNED BY public.teachers.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: thalesmurillo
--

CREATE TABLE public.users (
    id integer NOT NULL,
    login character varying(50) NOT NULL,
    user_password character varying(100) NOT NULL,
    user_type character varying(20) NOT NULL,
    user_name character varying(50) NOT NULL
);




--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: thalesmurillo
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;




--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: thalesmurillo
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: blocks id; Type: DEFAULT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.blocks ALTER COLUMN id SET DEFAULT nextval('public.blocks_id_seq'::regclass);


--
-- Name: reservations id; Type: DEFAULT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.reservations ALTER COLUMN id SET DEFAULT nextval('public.reservations_id_seq'::regclass);


--
-- Name: rooms id; Type: DEFAULT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.rooms ALTER COLUMN id SET DEFAULT nextval('public.rooms_id_seq'::regclass);


--
-- Name: students id; Type: DEFAULT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.student_id_seq'::regclass);


--
-- Name: teachers id; Type: DEFAULT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.teachers ALTER COLUMN id SET DEFAULT nextval('public.teacher_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: blocks blocks_pkey; Type: CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.blocks
    ADD CONSTRAINT blocks_pkey PRIMARY KEY (id);


--
-- Name: reservations reservations_pkey; Type: CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.reservations
    ADD CONSTRAINT reservations_pkey PRIMARY KEY (id);


--
-- Name: rooms rooms_pkey; Type: CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_pkey PRIMARY KEY (id);


--
-- Name: students student_pkey; Type: CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);


--
-- Name: teachers teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teacher_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: reservations fk_reservations_block; Type: FK CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.reservations
    ADD CONSTRAINT fk_reservations_block FOREIGN KEY (block_id) REFERENCES public.blocks(id);


--
-- Name: reservations reservations_room_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.reservations
    ADD CONSTRAINT reservations_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.rooms(id);


--
-- Name: reservations reservations_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.reservations
    ADD CONSTRAINT reservations_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: rooms rooms_block_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_block_id_fkey FOREIGN KEY (block_id) REFERENCES public.blocks(id);


--
-- Name: students student_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT student_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: teachers teacher_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: thalesmurillo
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teacher_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

