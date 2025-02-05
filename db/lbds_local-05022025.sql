--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2025-02-05 08:58:00

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
-- TOC entry 226 (class 1259 OID 16564)
-- Name: buggy_position; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.buggy_position (
    id integer NOT NULL,
    prediction_id integer NOT NULL,
    "position" integer NOT NULL,
    start_index integer NOT NULL,
    original_token text NOT NULL,
    predicted_token text NOT NULL,
    is_used boolean DEFAULT false NOT NULL
);


ALTER TABLE public.buggy_position OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16527)
-- Name: model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.model (
    id integer NOT NULL,
    model_type text NOT NULL,
    problem_id integer NOT NULL,
    model_path text NOT NULL,
    hyperparameter jsonb
);


ALTER TABLE public.model OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16526)
-- Name: model_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.model_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.model_id_seq OWNER TO postgres;

--
-- TOC entry 4841 (class 0 OID 0)
-- Dependencies: 222
-- Name: model_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.model_id_seq OWNED BY public.model.id;


--
-- TOC entry 225 (class 1259 OID 16536)
-- Name: prediction; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prediction (
    id integer NOT NULL,
    source_code_id integer NOT NULL,
    model_id integer NOT NULL
);


ALTER TABLE public.prediction OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16535)
-- Name: prediction_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.prediction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.prediction_id_seq OWNER TO postgres;

--
-- TOC entry 4842 (class 0 OID 0)
-- Dependencies: 224
-- Name: prediction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.prediction_id_seq OWNED BY public.prediction.id;


--
-- TOC entry 218 (class 1259 OID 16459)
-- Name: problem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problem (
    id integer NOT NULL,
    name text NOT NULL,
    description text,
    constrain text[],
    testcase jsonb[]
);


ALTER TABLE public.problem OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16458)
-- Name: problem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.problem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.problem_id_seq OWNER TO postgres;

--
-- TOC entry 4843 (class 0 OID 0)
-- Dependencies: 217
-- Name: problem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.problem_id_seq OWNED BY public.problem.id;


--
-- TOC entry 221 (class 1259 OID 16517)
-- Name: source_code; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.source_code (
    id integer NOT NULL,
    problem_id integer NOT NULL,
    source_code text NOT NULL,
    score integer,
    verdict jsonb[],
    status integer NOT NULL,
    user_id integer NOT NULL,
    submit_time timestamp with time zone NOT NULL
);


ALTER TABLE public.source_code OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16516)
-- Name: source_code_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.source_code_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.source_code_id_seq OWNER TO postgres;

--
-- TOC entry 4844 (class 0 OID 0)
-- Dependencies: 220
-- Name: source_code_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.source_code_id_seq OWNED BY public.source_code.id;


--
-- TOC entry 219 (class 1259 OID 16497)
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    email text NOT NULL,
    name text NOT NULL,
    model_type text NOT NULL
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- TOC entry 4666 (class 2604 OID 16530)
-- Name: model id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.model ALTER COLUMN id SET DEFAULT nextval('public.model_id_seq'::regclass);


--
-- TOC entry 4667 (class 2604 OID 16539)
-- Name: prediction id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prediction ALTER COLUMN id SET DEFAULT nextval('public.prediction_id_seq'::regclass);


--
-- TOC entry 4664 (class 2604 OID 16462)
-- Name: problem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problem ALTER COLUMN id SET DEFAULT nextval('public.problem_id_seq'::regclass);


--
-- TOC entry 4665 (class 2604 OID 16520)
-- Name: source_code id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.source_code ALTER COLUMN id SET DEFAULT nextval('public.source_code_id_seq'::regclass);


--
-- TOC entry 4835 (class 0 OID 16564)
-- Dependencies: 226
-- Data for Name: buggy_position; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.buggy_position (id, prediction_id, "position", start_index, original_token, predicted_token, is_used) FROM stdin;
3	7	82	204	=	<	f
4	7	83	206	%	x	f
7	7	96	230	"	\\	f
8	7	98	233	gcd	&	f
9	7	104	242	)	;	f
0	7	79	200	G	%	f
1	7	80	201	C	"	t
5	7	84	207	d	x	f
6	7	85	208	"	x	f
2	7	81	202	D	%	t
\.


--
-- TOC entry 4832 (class 0 OID 16527)
-- Dependencies: 223
-- Data for Name: model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.model (id, model_type, problem_id, model_path, hyperparameter) FROM stdin;
1	BiLSTM	1	app\\\\prediction_models\\\\model_correct_code_seq50_epoch_15.pth	{"dropout": 0.5, "embed_size": 64, "num_layers": 2, "seq_length": 50, "vocab_size": 157, "hidden_size": 200}
\.


--
-- TOC entry 4834 (class 0 OID 16536)
-- Dependencies: 225
-- Data for Name: prediction; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.prediction (id, source_code_id, model_id) FROM stdin;
7	17	1
\.


--
-- TOC entry 4827 (class 0 OID 16459)
-- Dependencies: 218
-- Data for Name: problem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.problem (id, name, description, constrain, testcase) FROM stdin;
1	Greatest Common Divisor (GCD)	Viết chương trình tìm ước chung lớn nhất cho 2 số nguyên dương <code class="code-style">a</code> và <code class="code-style">b</code>	{"1 ≤ <code class=\\"code-style\\">a</code>, <code class=\\"code-style\\">b</code> ≤ 10<sup>9</sup>","<code class=\\"code-style\\">a</code> và <code class=\\"code-style\\">b</code> là các số nguyên dương"}	{"{\\"id\\": 1, \\"input\\": \\"10 15\\\\n\\", \\"output\\": \\"5\\"}"}
\.


--
-- TOC entry 4830 (class 0 OID 16517)
-- Dependencies: 221
-- Data for Name: source_code; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.source_code (id, problem_id, source_code, score, verdict, status, user_id, submit_time) FROM stdin;
10	1	#include <iostream>\\nusing namespace std;\\n\\nint gcd(int a, int b) {\\n    if (a == 0 || b == 0) return 0; // Sai: GCD với số 0 không phải là 0\\n    while (a != b) {\\n        if (a > b) {\\n            a = a - b;\\n        } else {\\n            b = b - a;\\n        }\\n    }\\n    return a;\\n}\\n\\nint main() {\\n    int a = 0, b = 15;\\n    cout << \\"GCD của \\" << a << \\" và \\" << b << \\" là: \\" << gcd(a, b) << endl;\\n    return 0;\\n}	0	{}	0	0	2025-01-24 16:32:55.304012+07
11	1	#include <iostream>\nusing namespace std;\n\nint gcd(int a, int b) {\n    if (a == 0 || b == 0) return 0; // Sai: GCD với số 0 không phải là 0\n    while (a != b) {\n        if (a > b) {\n            a = a - b;\n        } else {\n            b = b - a;\\n        }\n    }\n    return a;\n}\n\nint main() {\n    int a = 0, b = 15;\\n    cout << \\"GCD của \\" << a << \\" và \\" << b << \\" là: \\" << gcd(a, b) << endl;\\n    return 0;\\n}	0	{}	0	0	2025-01-24 16:36:36.619843+07
12	1	#include <iostream>\nusing namespace std;\n\nint gcd(int a, int b) {\n    if (a == 0) return b; // GCD của 0 và b là b\n    if (b == 0) return a; // GCD của a và 0 là a\n    while (a != b) {\n        if (a > b) {\n            a = a - b;\n        } else {\n            b = b - a;\n        }\n    }\n    return a;\n}\n\nint main() {\n    int a = 0, b = 15;\n    cout << "GCD của " << a << " và " << b << " là: " << gcd(a, b) << endl;\n    return 0;\n}	0	{"{\\"status\\": false, \\"testcase_id\\": 1}"}	1	0	2025-01-24 16:37:18.56568+07
13	1	#include <stdio.h>\n\nint gcd(int a, int b) {\n    while (b != 0) {\n        int temp = b;\n        b = a % b;\n        a = temp;\n    }\n    return a;\n}\n\nint main() {\n    int x = 56, y = 98;\n    printf("GCD of %d and %d is %d\\n", x, y, gcd(x, y));\n    return 0;\n}	0	{"{\\"status\\": false, \\"testcase_id\\": 1}"}	1	0	2025-02-03 17:29:59.559511+07
14	1	#include <stdio.h>\n\nint gcd(int a, int b) {\n    while (b != 0) {\n        int temp = b;\n        b = a % b;\n        a = temp;\n    }\n    return a;\n}\n\nint main() {\n    scanf("%d", &x);\n scanf("%d", &y);\n    printf(gcd(x, y));\n    return 0;\n}	0	{}	0	0	2025-02-03 17:45:46.105924+07
15	1	#include <stdio.h>\n\nint gcd(int a, int b) {\n    while (b != 0) {\n        int temp = b;\n        b = a % b;\n        a = temp;\n    }\n    return a;\n}\n\nint main() {\n  int x, y; \n  scanf("%d", &x);\n scanf("%d", &y);\n    printf(gcd(x, y));\n    return 0;\n}	0	{}	0	0	2025-02-03 17:46:08.499674+07
16	1	#include <stdio.h>\n\nint gcd(int a, int b) {\n    while (b != 0) {\n        int temp = b;\n        b = a % b;\n        a = temp;\n    }\n    return a;\n}\n\nint main() {\n  int x, y; \n  scanf("%d", &x);\n scanf("%d", &y);\n    printf("%d", gcd(x, y));\n    return 0;\n}	1	{"{\\"status\\": true, \\"testcase_id\\": 1}"}	4	0	2025-02-03 17:46:42.094328+07
17	1	#include <stdio.h>\n\nint gcd(int a, int b) {\n    while (b != 0) {\n        int temp = b;\n        b = a % b;\n        a = temp;\n    }\n    return a;\n}\n\nint main() {\n  int x, y; \n  scanf("%d", &x);\n scanf("GCD = %d", &y);\n    printf("%d", gcd(x, y));\n    return 0;\n}	0	{"{\\"status\\": false, \\"testcase_id\\": 1}"}	1	0	2025-02-03 17:47:56.358657+07
\.


--
-- TOC entry 4828 (class 0 OID 16497)
-- Dependencies: 219
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, email, name, model_type) FROM stdin;
0	thao.vonguyen@hcmut.edu.vn	Thao	BiLSTM
\.


--
-- TOC entry 4845 (class 0 OID 0)
-- Dependencies: 222
-- Name: model_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.model_id_seq', 1, true);


--
-- TOC entry 4846 (class 0 OID 0)
-- Dependencies: 224
-- Name: prediction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.prediction_id_seq', 7, true);


--
-- TOC entry 4847 (class 0 OID 0)
-- Dependencies: 217
-- Name: problem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.problem_id_seq', 1, true);


--
-- TOC entry 4848 (class 0 OID 0)
-- Dependencies: 220
-- Name: source_code_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.source_code_id_seq', 17, true);


--
-- TOC entry 4680 (class 2606 OID 16571)
-- Name: buggy_position buggy_position_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.buggy_position
    ADD CONSTRAINT buggy_position_pkey PRIMARY KEY (id, prediction_id);


--
-- TOC entry 4676 (class 2606 OID 16534)
-- Name: model model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.model
    ADD CONSTRAINT model_pkey PRIMARY KEY (id);


--
-- TOC entry 4678 (class 2606 OID 16543)
-- Name: prediction prediction_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prediction
    ADD CONSTRAINT prediction_pkey PRIMARY KEY (id);


--
-- TOC entry 4670 (class 2606 OID 16466)
-- Name: problem problem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problem
    ADD CONSTRAINT problem_pkey PRIMARY KEY (id);


--
-- TOC entry 4674 (class 2606 OID 16524)
-- Name: source_code source_code_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.source_code
    ADD CONSTRAINT source_code_pkey PRIMARY KEY (id);


--
-- TOC entry 4672 (class 2606 OID 16503)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


-- Completed on 2025-02-05 08:58:00

--
-- PostgreSQL database dump complete
--

