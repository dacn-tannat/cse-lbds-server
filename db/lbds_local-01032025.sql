PGDMP          	            }         
   lbds_local    17.2    17.2 -               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false                       1262    16667 
   lbds_local    DATABASE     �   CREATE DATABASE lbds_local WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE lbds_local;
                     postgres    false            �            1259    16668    buggy_position    TABLE       CREATE TABLE public.buggy_position (
    id integer NOT NULL,
    prediction_id integer NOT NULL,
    "position" integer NOT NULL,
    start_index integer NOT NULL,
    original_token text NOT NULL,
    predicted_token text NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    line_number integer DEFAULT 0 NOT NULL,
    is_token_error boolean DEFAULT false NOT NULL,
    is_suggestion_useful boolean DEFAULT false NOT NULL
);
 "   DROP TABLE public.buggy_position;
       public         heap r       postgres    false            �            1259    16676    config    TABLE       CREATE TABLE public.config (
    id integer NOT NULL,
    name text NOT NULL,
    value text NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
    DROP TABLE public.config;
       public         heap r       postgres    false            �            1259    16683    config_id_seq    SEQUENCE     �   CREATE SEQUENCE public.config_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.config_id_seq;
       public               postgres    false    218                       0    0    config_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.config_id_seq OWNED BY public.config.id;
          public               postgres    false    219            �            1259    16684    model    TABLE     G  CREATE TABLE public.model (
    id integer NOT NULL,
    model_type text NOT NULL,
    problem_id integer NOT NULL,
    model_path text NOT NULL,
    hyperparameter jsonb,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
    DROP TABLE public.model;
       public         heap r       postgres    false            �            1259    16691    model_id_seq    SEQUENCE     �   CREATE SEQUENCE public.model_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.model_id_seq;
       public               postgres    false    220            	           0    0    model_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.model_id_seq OWNED BY public.model.id;
          public               postgres    false    221            �            1259    16692 
   prediction    TABLE       CREATE TABLE public.prediction (
    id integer NOT NULL,
    source_code_id integer NOT NULL,
    model_id integer NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
    DROP TABLE public.prediction;
       public         heap r       postgres    false            �            1259    16697    prediction_id_seq    SEQUENCE     �   CREATE SEQUENCE public.prediction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.prediction_id_seq;
       public               postgres    false    222            
           0    0    prediction_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.prediction_id_seq OWNED BY public.prediction.id;
          public               postgres    false    223            �            1259    16698    problem    TABLE     �  CREATE TABLE public.problem (
    id integer NOT NULL,
    name text NOT NULL,
    description text,
    constrain text[],
    testcase jsonb[],
    category text,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    is_active boolean DEFAULT true NOT NULL,
    lab_id text,
    template text NOT NULL,
    is_submited_once boolean DEFAULT true NOT NULL
);
    DROP TABLE public.problem;
       public         heap r       postgres    false            �            1259    16706    problem_id_seq    SEQUENCE     �   CREATE SEQUENCE public.problem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.problem_id_seq;
       public               postgres    false    224                       0    0    problem_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.problem_id_seq OWNED BY public.problem.id;
          public               postgres    false    225            �            1259    16707    source_code    TABLE     �  CREATE TABLE public.source_code (
    id integer NOT NULL,
    problem_id integer NOT NULL,
    source_code text NOT NULL,
    verdict jsonb[],
    status integer NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    user_id text DEFAULT 0 NOT NULL,
    score real DEFAULT 0 NOT NULL
);
    DROP TABLE public.source_code;
       public         heap r       postgres    false            �            1259    16716    source_code_id_seq    SEQUENCE     �   CREATE SEQUENCE public.source_code_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.source_code_id_seq;
       public               postgres    false    226                       0    0    source_code_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.source_code_id_seq OWNED BY public.source_code.id;
          public               postgres    false    227            �            1259    16717    user    TABLE       CREATE TABLE public."user" (
    id text NOT NULL,
    email text NOT NULL,
    name text NOT NULL,
    picture text,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
    DROP TABLE public."user";
       public         heap r       postgres    false            B           2604    16724 	   config id    DEFAULT     f   ALTER TABLE ONLY public.config ALTER COLUMN id SET DEFAULT nextval('public.config_id_seq'::regclass);
 8   ALTER TABLE public.config ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    219    218            E           2604    16725    model id    DEFAULT     d   ALTER TABLE ONLY public.model ALTER COLUMN id SET DEFAULT nextval('public.model_id_seq'::regclass);
 7   ALTER TABLE public.model ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    221    220            H           2604    16726    prediction id    DEFAULT     n   ALTER TABLE ONLY public.prediction ALTER COLUMN id SET DEFAULT nextval('public.prediction_id_seq'::regclass);
 <   ALTER TABLE public.prediction ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    223    222            K           2604    16727 
   problem id    DEFAULT     h   ALTER TABLE ONLY public.problem ALTER COLUMN id SET DEFAULT nextval('public.problem_id_seq'::regclass);
 9   ALTER TABLE public.problem ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    225    224            P           2604    16728    source_code id    DEFAULT     p   ALTER TABLE ONLY public.source_code ALTER COLUMN id SET DEFAULT nextval('public.source_code_id_seq'::regclass);
 =   ALTER TABLE public.source_code ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    227    226            �          0    16668    buggy_position 
   TABLE DATA           �   COPY public.buggy_position (id, prediction_id, "position", start_index, original_token, predicted_token, created_at, modified_at, line_number, is_token_error, is_suggestion_useful) FROM stdin;
    public               postgres    false    217   �6       �          0    16676    config 
   TABLE DATA           J   COPY public.config (id, name, value, created_at, modified_at) FROM stdin;
    public               postgres    false    218   �6       �          0    16684    model 
   TABLE DATA           p   COPY public.model (id, model_type, problem_id, model_path, hyperparameter, created_at, modified_at) FROM stdin;
    public               postgres    false    220   A7       �          0    16692 
   prediction 
   TABLE DATA           [   COPY public.prediction (id, source_code_id, model_id, created_at, modified_at) FROM stdin;
    public               postgres    false    222   8       �          0    16698    problem 
   TABLE DATA           �   COPY public.problem (id, name, description, constrain, testcase, category, created_at, modified_at, is_active, lab_id, template, is_submited_once) FROM stdin;
    public               postgres    false    224   ,8       �          0    16707    source_code 
   TABLE DATA           |   COPY public.source_code (id, problem_id, source_code, verdict, status, created_at, modified_at, user_id, score) FROM stdin;
    public               postgres    false    226   ~                 0    16717    user 
   TABLE DATA           S   COPY public."user" (id, email, name, picture, created_at, modified_at) FROM stdin;
    public               postgres    false    228   +~                  0    0    config_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.config_id_seq', 1, true);
          public               postgres    false    219                       0    0    model_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.model_id_seq', 1, true);
          public               postgres    false    221                       0    0    prediction_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.prediction_id_seq', 22, true);
          public               postgres    false    223                       0    0    problem_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.problem_id_seq', 30, true);
          public               postgres    false    225                       0    0    source_code_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.source_code_id_seq', 82, true);
          public               postgres    false    227            X           2606    16730 "   buggy_position buggy_position_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.buggy_position
    ADD CONSTRAINT buggy_position_pkey PRIMARY KEY (id, prediction_id);
 L   ALTER TABLE ONLY public.buggy_position DROP CONSTRAINT buggy_position_pkey;
       public                 postgres    false    217    217            Z           2606    16732    config config_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.config
    ADD CONSTRAINT config_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.config DROP CONSTRAINT config_pkey;
       public                 postgres    false    218            \           2606    16734    model model_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.model
    ADD CONSTRAINT model_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.model DROP CONSTRAINT model_pkey;
       public                 postgres    false    220            ^           2606    16736    prediction prediction_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.prediction
    ADD CONSTRAINT prediction_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.prediction DROP CONSTRAINT prediction_pkey;
       public                 postgres    false    222            `           2606    16738    problem problem_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.problem
    ADD CONSTRAINT problem_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.problem DROP CONSTRAINT problem_pkey;
       public                 postgres    false    224            b           2606    16740    source_code source_code_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.source_code
    ADD CONSTRAINT source_code_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.source_code DROP CONSTRAINT source_code_pkey;
       public                 postgres    false    226            d           2606    16742    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public                 postgres    false    228            �      x������ � �      �   R   x�3�tt�s���wq��Vw��	�U��4202�50�54R02�26�26�30�066�60ǔ51�33175��r��qqq ���      �   �   x�]̱
�0�9}��U�ش��Y'�P���&�QP��=o����N����;&X&D��$�G=x����轢�M���'�(���P<��=}��T49p5�Nh��HT�$�u�}{�8�H��{ϩ#P@r�=�����:g-�?� /&A�ȅ�9ԍPMY�l��A��V^��P*j�#ϲ�C�H�      �      x������ � �      �      x��}k��y�g�W�a�cw��T��)nhR���l�vIj�k�[�������?,�E�A� R����aΗ�X���_��󼧺�g�g�ERR��83��U���9�m{�7n^���'}3�|:4x���Ko}��{[����5�e�fx4���������'�ٴ���r�A��8<��h:����Z��Æ�#����������ҽr2�a��v`M���x7�vb��i�� ��ө������|����߾��׾o?���Rx���������w�z���9��c��3}�������tz��O����ѵ��~��S�;���<���k\>(Ǔ�r�W��d:~��m�۟�=��o>��7��~oh̭��;>�)��5o`���'�fړ�:������霝D��3;~���偓Op_q��?�c������r�>�r{Gg��;�w�m:�as�?���O#��(2���' ?��,����'�hR�d��h9�������+�~����]{o(4o0ɏ�kD��qK����B�f�T�����ӳ�~\��/�h���}�Y�����:�)�#J �1���~�+�<t�k��Ǧ{�Ã]����J$����7�WZ�ґ��.�F�=����nؓ�N�yX�3�`���/L�铟HN��ɿ�]b/�-���d$H	,�ni�O��ݑ���O��/ʣ��r8�5�����[�^o)p[�{����dY$wE��p�����7a.0�j%ܟ;��hh���^u�D([ng�y�W��,'�q��wͽ^�fi 9�cљ�c? ��TjǼ95ݑ�?M���l<4�yPf�)�]s8����K��(f2�zL�F�w���%'�G��AX�(-$�M�٨37p��Et;���'����wh�jq�4�B�9h��!P-��K��?�)�Fm~��~o1��EP�J3�����?��*��~p���}�^�� qlF�$��Ѹ;�x3�O���Ȃԕ�>6�ذ���7&]�L�=�`4�u&�X��/�z���M����k̫��mM!t����L:��h�_��a%��ж^�����UseSW}
��~:+�=�]����=�� {�,f����9���%�����P�d6�m��̐���ï��]����h�딛�G������i� �M |�b�J�7�g>��̾Xy]lha�:�[^�C�.^�i䱋B�	�6�\�b���+;ò߹kL1-nn�My����~9�/޼�?��?�v�6�����O���^�6h2V��x�дF�A��&��Q�\ؠ����mrf�����z|�F�.]�3&��K�-���u����*�� bq��r���l�PeX��#	i���W,EX����s�����������b�l��(������׷����ۯݾ~�5��=kw:GG[��W�wJ��L��_Ė��)K��H�#Q\ٹ/F�O��ϑyo�'�������1�A$4�`�[����n9|�<F8D�}��?���	L�ȫ��Q9������r��İe��������NI1��}��.oo/���s�>nFS�}R��.�z�M9�Ο�|@��n����>���\�^��^yP}��#�ߐ��ū�>��w�Q߯$d�^��ߚ�]��3�TW�%Ԕˏm5�xk[�����������������wv0��Z!c[u"g�{����매c
���˧�dۼR}T�jL��1p_F�ȟ�+�O��m�M��cPC�uVD��/$��y��v�A9-E�k$� -K���%!P��������B-��q��kw�7tpU YW�W_U�ʥ
��mk�k��'�x&�̓�h@&�l�6�؁���!ʏ�w*#+��7T�� ����hgP��va����~�+� }\=fm�����0Vt��T|�kTHt|�	
��Z��'/FRKB�;�<p���'7�e~Z��S_d�<}�ׇմ����ZS�M���3�C��sc&#v�תJ�_��W�����X�h���q���f,���Z��br-h�iM	C���9��6���3��e�Tu慢�ֈ����b���;�"μz��~�Dա|������O�ɕ�uP���$�D]�`ao(�`���[m����#T�"W!��|�3?�ʋ
פ0,﾿}��vuB�^C�ǿT(��䏯&��S�*��D��ݿl��c����z+N
�j�/~����~����PnŘ�s"W��
��2k6ۻ���ݳ�5�7�ϫ���'���(��ū�^ͤRV� W_�9Q�!g��V�΅�-���{!����O�_6Z�TxE�?�i�bmL�UL �f�2�6x|ӣb�}f�խ�3i�)�U�`��S[�Qˋ����Kʴ����v�q���-�֯mb�k�ژV��p�y:�pr؟L�f�(�?�mZ0j�;�Vs�c�~`F��1�(����ԗ?Iىy؟�ẺV{Ńr^���bp�+��)�d��E�����SLJ#~X���ё��2烾���
k2�8���>�i��9�~��C8��X��t4.yG٥\�"��g1-w��VM�p��*��G�r��~^��ȊaV�v=54+�E8FgIB�!�Ҋ�7S�Q7�F�,�@���BHP=�E�Z��R[-
�����T��Q?�҂��|�XiV�U� ޫ�\�w��`
�5���<k�n�x���������=�|,��t���S%�*\���\���r�*�:��
�g@�q�5�ƍ[?��"n*��͏��z��7������L������뇯ݞ�^�y]���w��o�o�w~0�[�l���aq����1��?,1ѭ���͛C���[�*�����Ձw�?:�~q����?ym繑d�r��Q+^(�Me��_{�;���W�^(�Me჻wn����G�����f��������;|����?�y����?�`{px_�/�y�������>~���s���wo~�����dԽ�Q��t�1�ۣGݏ����p �}�-������GGՄoI"����@5�����!=6���qSq���J|��/Ʀ������wz��(����y��{�->�an,n�B�m3
ͫ�$u�6��<}�O�q�;��/����pm^fn*=׮I0�[��@���x�R18�x�;|������r�l��ٗ\�r�ĽK^z�rBl�y����]A���n���`:�J�WEJM��@DiWB��镭yP��=���(�L�?��;�E���{A���O��ڒHv�{�� ���(�q4Q<;��7t�P�]5��l�B��\�b�?얏�}��OzͷL�<��ޢ'�M�*f���B�jl=����jm=�=��1�峙�H�[���n"-
�?=2A@�l~^����@.�L��@�j���`}�
vk���=��G�iU�]��Q���+�W�����x׼�F9xPN����.g��-3��2���b�2IFړr��.�}���8�{��%���d�'/}a���\�[v*K��IB0͆�vg4�w��`�rK�V����?_�|9h\՛N�&���2(� o�S���Ngt�J���ۼޖwf[>|E1km\E�P���*[1� �f��dCE�j���`П��y
[�J�lz^�@q$�=���MZ��8���q�����k��h��*Έ���wAU�ܯ����?�t;բ*�Z��a0�9U����W�֠!oȍ�,�7��L��sI�ϡU	��,�ծ�E�VuЗk%�7��yc�1�):=�VoT�L��ԝG��3�S���G��L���9�� �,|E��`% ��:�H���nJx_(xa�|M����=/*5%���m@)��'VA�6��1u�L���>�.���}!o7��)�3/RW��9�Icַ)���$q�-L̋I��Eʶ*�Z'yZ�i�_�w��E�E��hƫ���R"�X}i)�L�On.JG�l�{��t��A;��n;�\'�b����td)�~X�z�]�7te�S�y�lFr�����MDG�L���e���,��T��u�r��kL��L�Ix��Jrk�SrSҢ�{X��1_H
�%:��    :@����*j�{��'��{#](��_"��i����'�������������*���ɯ�H�\�^9;MW���O~����`�*d{���L��g�Ų�M����#�j۰lw��������sQ����u"C�O�V��/<�YCk��V6�T�K����~<�x�e9!`>,��"��S[~XJ�=���b�^�Ě�G2�T��C�2�>������DlF�γs���ڂ�e5�É��cQ���W�&�$I���t�D�<G���$� #d\���Y��1��A�B.άU���A�5[Y%�X�>7�r���	�dF�����ff���J﹢Ҕ
��<�?W<���/R���OS*kBgb�l�USJ�\�ֺ��F�u!��W���0�"d7=WT�֍h��I�����d����Cċ����'��k�Xw�n�{�dv�Dq�X�7�pmW8�E�v8E�q���.<��f~���6����lB�o�a�ݦ�����F�E޲
���|S���(��]��8����j��6��3�yO(t9�y�;|����aK��������bЙ��?�>a����J|�t�"ɴ<(�I�30�#Y�a�4`c6C:^���LV�`�I������*d�q��qTw��;�����q�ʑ\�ܦz#�|�^sڴ���ʏ��ߡ�
pM��∭�Wv��;S�� ��I�@���/�%�w/���M�Y���3�6�ح����W�<S�l0K|v���/F��V�F��frm�l2irv�����܄��A*��i�ib�Q�v����� �䗋S��dN �Rg���\�3<�Y��"}N��c�T޸P�	S$��&Iy/7��0��:3Q*&�P�����\�I�̜�\í!��nM����qK��	Ј��F��#���]a��8M%Ɩ1��c�ĘA@J�0�1Pb" ��	���.Q��y��#�.��M�],��|*�ˤN&uB�D�׎����E�6��sA$j%�%�2��H�N��� aR��
�\��������
�(  �	��V�u���t�G@��42��n"�
�[%��]եju�[f=l�Ʌ	�7!�rSb+��)�s& R�U*ƹp"��.1r!nA� wDlC� "�ؤ��!>;���&�F�-PO��9N9W�ܕ���8B )�"p-y���8yM�w�m�m��@LD83�n&�Q�����C*8��$�D.Rd�oPYH�����"D�;`�
L��Ta]����A����,(�9HM�"���8c�)�B۔����"0G��	J���q��J�\�
؂��x*O@"�D�DNh�v��z��Ɖ��i(<��,��.�`�`�`�HI
���Y�Y\ 
��+�[��q�o��>!Z&e�-6�0_D���(�PJ�]��?���
ު���Q��8�VdHlhB|q�P����R~X�)&e1#>���0��v�dT�<�$Ftlx���	>M`�bZ:UF�0H@sHB��ג�qŐ�Q��]�^�gsUK���f���K����#7^���~G��Ѹ�,Q��"�/�ϼ��t܈w�*��~y��ğ�o:�t�����^P��~���������o_�׏��Ǒ��ޛ"��\�g���?����U^�P�b��mg����2��������CS>��WfF��l<.�;�����$)ߘ1D\'��_�^����X!�1��z��V��ܝ^��j�Ƈӥ,�!o��UIrh:X���ټ�R�z���z��Q������e�ۋ|��s�����zϥƴ�bX��>=t���qe�Z߯�	��0Z"���x����"�x_7�G���}��+2�?������?�&���l-E�%��^����<0>��u�p�h-�W[9�v�����Ď��=e_݃�p�'��vҰ�^/O�<�.w�*&�ko��]s���-�׺.�|�&{(�j� � �~��Яf���J�A�2ӂ#��vwm�S ��e��bX	H��ľ���p���]��k.c1~��>�8^���;���tR�T����{E��|:j�s��lt��g�Vղ2N��Y��nm�
3}8jw����_-y�MJS���!�������h"�)�m���`��~\�KW���q��R���,�	�P�;D�H�DZԓd�	�[��!
�C㺴e�/�w��e��^��6�gQp;SU����fjg�{����p��@��+�t�>�v2�Q+U��7ZBk�Ab N���b{��=<�f��^W?�S��osU-8��k��f=�ܨ�<&�W��3O�n���FU>�;�M�Q��T�r��"�^NK��J\��<n}���<l�m.�%�h�QKz���.�gsޫ�ZV���U��+��� ��Y�-���'Jb���ZQ ��0\lc���5O*�\Ul;�Bϖ$�0meo���e�4&�k�,ܷϾ�:���T�Th��������%oIj!|,�'x��my,\4奕�-���b8�[�</��\O�')q���P%�[.�\��a����ȭ'��i1߮�_�(�6k%D1H�	��i;Q�T�P>p@H�@xm�po2J��
�H(����\J䉐ҡ�ᑫ�*)���E���) ��VL:B�E�E=dR�I���
��9H{&w 8����ARG���?�]�����'�`Hr�m�B �(��JЀ��:�$��H��G�@0ʔD@�6@��ZZ��MϾ��f�0^@�D7a�g,��ʲ��s�o $,�S�Y��O��B����Ǡ-oZ.��5pY�E�*�&-yC�ԯ$�0@��ca��QL��,AyAbQ/
e����3��(+EP��q+�?$�&��m!�9u�i2
*/�-d ��f��(��-��@�S���0@�E�!;"oy+�^�6�ldƁ����*P�Sր�YD9 ���Vu'%��"!���Mb������J�	6`aHzQ�h7#�L�S>v42��vR
s�py�a�X08-��!�aR���)y!cɐV�辈��%J7�[�!�[��T̀�a��ܙ���-B?�� F��D1-�/�C�aT3Z��iKTH�pi	�DJ�(VGƖi)�jh��a&(	�wj���`L%���&��S! ��
���1�MvNe�����8u�"BNG%M�ю�AiIP�`]5�	�.�cX�4��N����ڌ�%�L�A�� }Ce6uX~���#��zw�R8 q�4� �Y>��$@��Ҕ~X�JD��C�s*7�Q@s�I	\1x��)�p��({�uO!1"���usd*���2S�о��(��ȅ�F����"z)-���g!��N-%j��.4,�} )
!H�v�«�nYއj���2�-��[kI�P5*V��s�it���'�ʣ���1�U�i;��xs���JB\��0Ƒ�؛3�t��Ɛ���UM����޷�p���dPN��Ap V�5��U����3?T�ϡ�p?q�QNe�j#����rt>!=�#����y��aI(:�`��>��#4��[�	��#8�p4}��-TF�t�99�T��p�j�`#��5(��z��K�����i��	�y1��z��������$vL��z�%l�����䁃 ���j,h�AL��q��
hVs�X����*2u$)�����bM�"�Q�6�N��j[y5CH|~��~!�
�%�אό��j.��Ҝ��kuf_2���O��:�$0j(A֘z/pj����2Pʔ�x��;�ŀ��g��kh�`}���QpL[����$��!�a#�@�ܞc�W���,�"T)SA�+0��È�5cxE�x�1�p	a�˖�i��,4"4�`��P�A:��8/�G�X>� ���c�i�����>v���I�v����1��U��d!C�5$�0{��ΝA(�2�y�2�@$��.���"�P�D��p�y	`�P���j$w0jR���
8����Z���dti    n�/���"M��y�$�%�*��.�l��e�1Y��2�o��B����j��Q�2,F*��M-YF�O����j���M�	A-�Z>�\�$4q#XP^��"u�΀1`�9��=�/!��B Q�HS�j������Ba�!%(e5T�bG뤉��54mr�ժD����}����(�Դ��TMo/$�C���0W~E=e>�����4�:Qf�-��Xɞ8)�6@q����H�U�e��0�ZN�V!Յ c�� k`o|����@3��t�[Ő�

��LD���bdZ�\�X��C�.c��ZZ�$�@�X#j��5��@��j&��|����f�^e�v9�P��x�P��;�T3��Ĥ-Sq�k�s8	��C�O�q-�����4�
N�h!��I�P�X�l��z��	ޕ�E�Uy?]%�uZ�K���[�eb� s�_�V�.3P�LI�6�j!���+g�Gk4�>�!F��>�,��:P��#c 3V[�I���P��V�r����MI�}n�D�	!qdoN�H|L��XKJ4Up{�ث9�>�ԅ���T��*ݩ7}u+����c�-�[ޗFj�h�C���;�O�ňn�6�c|�t����.�f�Mi*c_u�?����jG%��D��c��Y^L�y��ՊH�����MĒ��4L�yU���zD����x�B�nV_	;չd�;�$�A,�F� �qZE�S����(� ��T�YpD.��>�Y�M]F�}!����C/�գ�q��y�01����X]k��o������.G��f�Y���@#�}�΄�?�B����Nk0���dᆦ�W:�-u���h�`��V`*rF-�1�I9C�u,Ϊ2o�� �u�7�,N���>�Y��,F�j�`5`L�Z3���iJO-�h�Xi	�0"}�8���.kt�f�
i��Bu��-V;���G�Ye�b����5X�#ﭜF��J~J{�r�DV���k⣥N�ꀈV�B�c���j|�0u
|U+Q����B`�|������!�}�n}}1Ԭ	���%Zȝϡ�҄�!��aK��Ls:��&��L�n�|`�yO��5$����u8���-��TQ�ki����RVo 0�*[5_b5˕iL(\�F���|+�-�J��IB���dhQ�2�e��*�+���r�!� ��]�:u�����#Š
*�4����H�I����{�Ya��A�z1PO��G��{�� ��@(�8�b�.1���0Z����Ƒ,�Qt�E-@x]��ԃ(�C�P�/$/|���A�A���������e�)ZR� �pX0�䤗eȆr�V-�#�����X�SRA�}̑��JXk#�)4Ö��i*hu�����ai�ZA�K�!9�hU%cJ�DǻUV�FՑoYk�f�j��JI����/>�~�p?3D��	��J�%�P=R3n}����l�5PB�V�DM}�PF7�--h0�c���7�I��F�l��G��Rk},�2V�9��%F�1KJ�XÈ+qi�kS�WΏh/ƴÒ�����2#�Ԓ�֨$�ը�Z�J5s��Ӱ�ti��Œ�|M�Y�K��8k�����Ì���\�K�|x�P�"�T.��E�̖P�X��4�@�-M���,�2��^�[�L��n�B��p�{�1=�! ��_��6�̣�Y'��L3LP8Q��Lt}�HыU�r�0�(7�'du�2Z@�Ip����k1�Z\�ػڴR`�ܵ�d��TX]Ce�X�z��2���s����GX���e�eq�<M?�Ĝ%�L+�X®"�4�"n	2�(j�\D�`�HK�7<01�8���5���k��@l�-8�E[-�+�C�Nf��c- @v�J�^{��T#B@��]�ռ��Ќ
��� "�_����ci�S��4gHi9���?�b�tRՆ}P�Xp�A;(.6�8&+�<`2�:	�0�J�Yw���Uіf���bE/b ��<�T�r����s��@�2_�(��땉F�V��Ѡ"4�U�b]t�z�zb�6-��j�B]��6zHzY�0�%/��F�j��b]��/�+�}Ő� F!�K)},�y�j�̕_]�cz��\*���&���59�L���t0>)bX_|I��D���Wq�G#I�>UL�jo`%W����P����k��Ư�G>@��i���QeX�X�8�/���&[w)�05||��l0�/�Ӽ���u��_�#_n�����~q@ƾ3ug��q.���?���hz,N&LIJ���r� p˵G��³N���i����~�;�[5�>��n���%l�fY��o�?RĚ��cb��9t�>�m��#�k푯h�O�6�/K��G^b�<٬R�b���z�{�ern��N��eф�QϺ;��F�[��!�$�t�+S>�&=	�|2ϴ�����$�ڳn�w6�]l��k1��e��Y��]�����p��̚�qG!����y������X��g�w/Ak��&�ꨆ2�q��`J������F.،5ZX�6���2���H���o�e���W��n9�{�}A�����|ENkV�
%���|Vת���E��wqw:��J�a���:���7��I���ې֚!ie(����J�;*��YuQo�|.�WI�j }��sa��[$��	3?�����*p������^��̧љR��X��S����Vm��̿���,�K�c<���%�g�i���6V�9o�ڿl�x>����A�t��*�;�զ�Ԁ^@<���S�����KR��ȝV��~e���;(�!�p�vIa�J=�~'✬YM����ٯI���1M���Qf�d�KB��jz9W�|!����y��r�Vd�)��}���I*������.�UͦV*��2��P���J%�y��šEq(�t���jṷB�<�=,�FI���^T�n��a�/�E�����'����}���y$\�����| 4���o��,5�$��O����GnVH>4��ɿ�e�v��h�q��G����c��|��6��ÊÓO�٥��=�8<�j�^q����+��_-���/�C2����ai:��<��Y�+�~*Dh��fo>ǋ.���h����\�k�n+�����"�0�l�1���]SL��;�{�q�.�I�?P�Sc�Y�h� ��<GFC�BC�->�t�G3ܷv�mz����b"n���}�U�FM-9.�_�1���R��f� h�!�-3�d����3�6�[͟�ǗXh��t�m����cw��B�&��$�J��J�E̶�`6U	7�&a�Zg�E��l�2YS5oS
� �{Xl����ؑ~Ϋ�>� �n-l#�*\	�-`M^,�M�M%T4H�6D-l��Z<8�®ٰ��r���V�i"Zg�ԧq�4�n��l(ҟ����xLk#\.�ȶ쳗*6&��$������.A��Ѯ��-_��-s���/���S���ݬJq@t��D_<�?�_~A����Q����|�ե=�f�p�� |E��V.A��t����ل�n�7�X�u������~�/�k������;�6���ΞK�nX2�Qδ=�;t���C-d�t�{\�;�j����_+����>gr��'�,
 g����(x�zkm�x�mBzYm�Y�_T�`~S8��Սb��M(Px���z��X��Gg����qy4.'�;�`�y��g���r�s64!>_`K �0'�r޴t����m�f�j�t�o�{�gz��ҝ;F�WN��ǜ𖇣�|Z~N%
��+_�dA�UfN2m��9nh���wa-�d+�E��
&TA�H�sL6[��y��"2=5�M�	�>��I]gS=?�ja�:��@�3y�ݬ(;��"��Bvfrڽ$�A3�>S/8|D�WoMX�Ҳ�V,��c�14�
�&�����G�w� U�{��`3ne�Ȏ5)���吏'Ew)v��Ҕ�I"�}�@�<��ֲIb΃Q9N;��
z�x�Bw��H8@�[�9���y�T��$l��#c80gq �M�x*'����N.�fz�'�-���!H�x�m
(���{L$a�l_ѳ�r�;�,�n�    �RQ��a��Z1O߸�������>A��Z�F�����$<��|<�9�^1"OUZ�r4�l�����e�u�gz_�\ժ��yv�p8y�͘�@�|�6m��t��迀z�p~%�y�~Kxj<�`=A���%a�V6H�C�Wņ�<�͉[�w7d������IB�����ߌg�r1�:RF3uOxl���R�K��a<�Ss�j��miC㈭R����g�C�L �&<�P�ڹ��3�{u��	�c�b�}���:3v�AA���a>��j'*���$D<��=��O:ي�m��[��(�O�,�»����ٜ�.�6d4m
I��[�Dl<��<o�sx�[�F<g'4ѱ��j�aF�3'A(�j^-��@lx�/f�ٜ��aϔ���e���-���K�%v9��(;V{��}���  ��x�虩�c02#Y�LzH_�e$*�8p��ࡶ �B���h���`�&1�G�-�G��`~֊��ބ{v���Q/���\�}'��dUz�gh���2d;�y�ܷ�L��1��8�����1;�X��B�Ɗ٨5��;s��)�jw����3e��g�#��@#G�~�r��ܖ��nnL���۬�!Ϙ�g ���x����1c�[mK���<�3��s��>����^��z�����؄�]�����}bt���=Yy���8'j�':������v�l�R����i烖��g��@x�jl�F!)�M�i~�XO�C����d�-��ǳ��
�,�9Ҷ6�$,�i�3�� �l�ʦ%��r���A�3#�#���x@2���B��P���Ur6XІ�1w�X�diex�;�[��¡�8�N��+S�.4x�
���FHu�>�<��O��A��; �z�z�te	{?��U��n�x�<�&P<k�S�S���V q�����Ȭ�#8����C:5�>���q٩��nұݾ�$'A@Řʮ�$�ȱ�w�{lfC�zj���IF[��m��4�*�����(s�oM;����+��[l����K� 4�P|+[6Arַ!I�C/�(��ZD���Ck�\i��9�!�"vN�xB��0��	�}D͎Z U��.�`�̧�M)\@�����F�h��u4TK�|#bv��+��]�x�kJ���B�@3:)� f۲��2��粦���y�υ}Q@J\c����R��zUJuPE��ф���C���I5�p��p!�MD�O�]�Ljs=m���:�HI�V�<��^l)��N��\�I�+fܕ�cFL�H�j�����G��3l��T���Z��p4�=lj� �a]F[�؎@[���@�'G��:�T�K)&�o$�4a�5(g{V�����Ul٢�G�ǯXE?#�h`[�#dN�k�������OH\�����Y�|�f��`�6�2�H�oU ��#X[j9L�5��g�:JGω?@
Xj~�p��	1�����*�^=*��[{���TՖ-��~G��l'����OR��٨0��ĳGaF_l�;ƺl�mDstkLCR�C�m�3��q�&a&�bi�O�v�U��64W`&3��I3t��Ȁr�H֗�Z̵1����ͤ�#RxS�SS����v��i���G����Y���'$4!c�H�
��ZȺ-u@5X��Y՚���s�J��'4=�=��J>~KK�^�3����͎�
��8�}L�Y��$^; E"����l3[J�D�a�㷌h|��PS��7�MI��`n+ֶ�(�0W���ĳ."3,-������RmBH��b�[-�[/U����A"��MiY�q���/�
*��6X�� �mX��	�-g���*Zu���� ���&�^A���q}꿓i���l�Gٱ$G��J{�d�4$ �-ʒ���LN����������5�ौx���-!�9[v�Z�˨�ȫH&�ň��jj�jG���[���OyKG�������C��Mq���RU��z���f"z)�+�$��������{��c��~����=�rm[��2���{ �9j��䤶���t0�	��2B�.����u��Ε��F�l��b5C9wSЕ�M���|Q,a��,��n0� Ģ��c˘4Sa��&�$F�L=�p$#E��([Aj<���`���nD�r�ň�ZdYnA��Z��씜31w>�5�L#%jD����g���(d���9�2�Н�i�W�5��2�c���}�Rz���5�*���|6muʳ�z�����	{�[�oG4��X�A/4���A3�K#/.�!��t$bjA��l?W���o	��@ќ���Gr��ms��:F���N�)I�4-�h��Ho��I�-s�G�{�z���N�����}��V�°eP ��h�3i�"c�|+!���R��� �7��(8�%Lhf3���:P�{K�\;��̃��:f*
���,_��h�KG&h����[���K�4��5�q�;�%d��1u���o�	��ϯ�"{?��X������%d���:��g�rT������e���e�0��1-����zA�s_�h��#�)K�:_�͓� ���-������tu�		��ꢨ۹
`�1�e9��B�Rm![�Ǚ�G�(��Ylɚ@�0���.�6�I��,�m��	���
u�@�#u?�.Q�b��͛���O ����l�F��t@�V��f�r
jĢN�UJ�9�f�6��g�I����7���` L�@iu����Z��\ƾ? 2|���Цf+[�����sh蜆�&�4au�2��(m�Q۳2-�@V%Ô	��|F�D��#G����X/ QX�S��؄1֚[J��4;az� D�B��sM"�J~�Q_9Ϙ��ʣ�.�V��7��K-�2�R�� ۦƴp�Τ�,�s"�T$�u;80��w[J�6�X�r�-i�t:����D>Vg��n�j{s-��|-b��{qe>�~A@�1�f�Zd�̴� �$@{�� �{}��E���A�8��&����G4'We�6�<!��ΰ����9��k�){]��~;3ڜX��LZ�bIP�+�ꭘ�� ���0 ��h��LCzA8�P�\��!A�U&��W4zZ���E�h8r���1g�(��P̥[fjܯY�U�P]�B�W���!��W��ie��rQ�6�|�4)�"���&:��.:���f�2���Q�0��/��ނR���-�w�i+z�P���D�yQ|a���%��a!1��b,-qi1>��AKN���|�W�,+a��{�M��d�zI��RI�B��U�_-]3J#Y�{��t�I�[9��,�:���&�&z�v�"r�:�"Hmr�_ ��JC�aF�e*��_{�����"��b�ɖ~E^U]B��t��)V̗K�a9�#���@5cQ:��I��P]���)���	�մ��sκ7d&�	^��~�Kʱ�n����F�k�&�q�Wt�%�<b&N�/Y�T5M���/���l��,����~���;R2V�m�K��cZ6]��>�x�+�-~Q�iX(�8"��+�;跔Et�U�9.�;/ܙD��U?p��������Х_.]=��_�L�[�&En�-������+[��]���8����Q|�� �>{�_�y�_
�՜۳o�̤�qk�?��g���`��s>�a�����ɧCs_ ���f<"�盤�|2¶{�\H8�>�W�������x�.N����q{Wa�
8f��c���s���_7Pi�3���4�)N4wf�BJ7MW�����];�g�B̟v�EW���#SL&"�����w��yf6T(d��A��Jo%2o��1���A��X!�*R+&��o�ɧr�+��\y�W
�
�\{j¹m��ʌ|�`ze~G����7���+�H��?�Ƃ�u�� B9.���ͽ;7��~��/����e:�b��oIJr�`�|�_��D�'9�����OLG���3� �ʃ�U�����7��b0_F�Vv�'�|�3�4�x�L�@�:��?�xO�UGun�p���g�>���ީ��`��.>X��Vn^��� �  �S�j�\6:;�k{�Kr�ݥ�0� �ƛ<�FM�GMWx�~�D����i���I���2�+��M6;o=lݥy�d��}ei�l��At7_z����5�_��_��%��1��-6k֎T~�g��p��R��o�i�oo����r����I��ݯ~��Ls�T�=B��gz,mt�	ܯ4��ط�ّ��n�&?��EgO��ML��e���#�W}X����z�b�r�h��_E�\��(`�q�������;����7��.Q�5o�����)k�*�D{?����]�*���0A�P��Ѥ?�?(�3w�!�cx�Ueg�u�#��h88����N6Uߛڹ��>O��'���'���\.!�BP%7������FP��8e�T*�݋����B��
HE�3d;�?g�X'vY�Z�3/.\����.�i��e���t��9��ń+\�9<\3�q���fEqD���)�	V�v��)�q����1h���c�{e���k˗|��r����3�-�k��[�_d�,�tc����[;��_��}u�;�L�p\�a1h��ݶK
Ie�n;���oG�]��{E;��i'΂b�D����X̽�V����E�WH��d����������U���)�;Q�wĎKE�c��e������<�n]�"ڴ�B=�Bć���57 ��&c���p�|6;�w	�ME*��:GX�J�9�N�q�i{���W̪�Xǽ�iODp�lﬦpӥ���L<Q��;ZLܪ����1 :1�>}�K3��:����+(�D�զ�v��E^R�]k���Ȳ�A8{IC�Z1t3��@vQ˫���Ѱ=,�z����E��G�h~����e�����P��1aR�·	(���<��4�[���p�F#�]��Q���+�W�����x׼�F9xPN����.g��-3��2�Q�C%}8iO�q_L�=��֪�5qe��-��b�R��H4�N${.�V������p!��� �^Yg��,���KF>s��&�oD�¸�I7�w{��0��v��:�8-�4-�^f���pA�eE�#7��*(#�vGk��c���&2�J�� ������ѻW����md��.=i^
o�������Qv����3ڟ��|�Ë�� j�zunx�h%������?����G!^i}��
��jԃ����+���Ծf!t���P�|���gI8�7�
S�c�a��MbR��|���l ���r_lOC�>�tH�3���<��(��T��|�&k(�Cu}�+X����f�2��?!��	�^�x���:[�u�Z0ED	D���,����|��h��I�� A��1,�*=���磞_�z��8��qC2��[,�_A��	p�hgӒ`��4l�R��בϿy�K/u��ΩX�U��
;������kI�>~\��MC}w���v^z��n��      �      x������ � �         �   x�]�KJ�@  �ur��%���Qb+�T�n�8�A��43��� n���Х^�7ѵo��Q����J	�H$�m<��h�ތ'N1 ��<&7����:��~Ϛ�mw�zm���u�$.��,��#�zo�&Nf�����C�)�3+���V���V�y]_�Z�0�/5}t�q�j�����ݷ׹�lT�xR<�	����g��L�ɔb���+KD ��S���=H����Gn     