--
-- PostgreSQL database dump
--

-- Dumped from database version 13.15
-- Dumped by pg_dump version 16.3 (Ubuntu 16.3-0ubuntu0.24.04.1)

-- Started on 2024-07-05 09:54:19 EEST

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

--
-- TOC entry 6 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: cloudsqlsuperuser
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 2 (class 3079 OID 16514)
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- TOC entry 3830 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


--
-- TOC entry 728 (class 1247 OID 17731)
-- Name: outbox_message_type; Type: TYPE; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'outbox_message_type') THEN
        CREATE TYPE public.outbox_message_type AS ENUM (
            'PUBSUB',
            'API'
        );

    END IF;
END
$$;


ALTER TYPE public.outbox_message_type OWNER TO "postgres";

--
-- TOC entry 653 (class 1247 OID 16469)
-- Name: serving_method; Type: TYPE; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'serving_method') THEN
        CREATE TYPE public.serving_method AS ENUM (
            'SITE',
            'HEADERTAG'
        );

    END IF;
END
$$;

ALTER TYPE public.serving_method OWNER TO "postgres";

--
-- TOC entry 738 (class 1247 OID 19822)
-- Name: site_tag_status_type; Type: TYPE; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'site_tag_status_type') THEN
        CREATE TYPE public.site_tag_status_type AS ENUM (
            'ONBOARDED',
            'EVENT_TRACKER_INVALID',
            'SITETAG_LOADER_INVALID',
            'NOT_ONBOARDED'
        );

    END IF;
END
$$;


ALTER TYPE public.site_tag_status_type OWNER TO "postgres";

--
-- TOC entry 656 (class 1247 OID 16474)
-- Name: state_of_infra_integration_service; Type: TYPE; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'state_of_infra_integration_service') THEN
        CREATE TYPE public.state_of_infra_integration_service AS ENUM (
            'DISABLED',
            'ENABLED',
            'INFRA_INTEGRATED'
        );

    END IF;
END
$$;


ALTER TYPE public.state_of_infra_integration_service OWNER TO "postgres";

--
-- TOC entry 659 (class 1247 OID 16488)
-- Name: state_of_integration_service; Type: TYPE; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'state_of_integration_service') THEN
        CREATE TYPE public.state_of_integration_service AS ENUM (
            'INIT',
            'ACTIVATED',
            'ACTIVATING',
            'DEACTIVATED',
            'DEACTIVATING'
        );

    END IF;
END
$$;

ALTER TYPE public.state_of_integration_service OWNER TO "postgres";

--
-- TOC entry 662 (class 1247 OID 16500)
-- Name: state_of_product; Type: TYPE; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'state_of_product') THEN
        CREATE TYPE public.state_of_product AS ENUM (
            'DISABLED',
            'ENABLING',
            'ENABLED',
            'SITETAG_ONBOARDED',
            'ACTIVATED'
        );

    END IF;
END
$$;

ALTER TYPE public.state_of_product OWNER TO "postgres";

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 17440)
-- Name: AnalyticService; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."AnalyticService" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name text,
    service_id character varying NOT NULL,
    analytic_service_category_id uuid NOT NULL,
    analytic_service_account_id uuid NOT NULL
);


ALTER TABLE public."AnalyticService" OWNER TO "postgres";

--
-- TOC entry 215 (class 1259 OID 17414)
-- Name: AnalyticServiceAccount; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."AnalyticServiceAccount" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    analytic_service_account_id character varying NOT NULL,
    tableau_account_id character varying NOT NULL,
    media_owner_id character varying NOT NULL
);


ALTER TABLE public."AnalyticServiceAccount" OWNER TO "postgres";

--
-- TOC entry 216 (class 1259 OID 17429)
-- Name: AnalyticServiceCategory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."AnalyticServiceCategory" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    analytic_service_category_id character varying,
    name text,
    label text
);


ALTER TABLE public."AnalyticServiceCategory" OWNER TO "postgres";

--
-- TOC entry 210 (class 1259 OID 16605)
-- Name: Integration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."Integration" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    integration_id character varying,
    name text,
    integration_tag text,
    product_id uuid NOT NULL
);


ALTER TABLE public."Integration" OWNER TO "postgres";

--
-- TOC entry 214 (class 1259 OID 16687)
-- Name: IntegrationService; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."IntegrationService" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    integration_service_id character varying,
    state_of_integration_service_id uuid NOT NULL,
    platform_service_id uuid NOT NULL,
    integration_id uuid NOT NULL,
    name text,
    service_params json,
    data_integration boolean NOT NULL
);


ALTER TABLE public."IntegrationService" OWNER TO "postgres";

--
-- TOC entry 219 (class 1259 OID 17741)
-- Name: OutboxMessage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."OutboxMessage" (
    id uuid DEFAULT public.uuid_generate_v1() NOT NULL,
    outbox_message_type_id uuid NOT NULL,
    target json NOT NULL,
    ordering_key character varying,
    message json NOT NULL,
    sent boolean NOT NULL
);


ALTER TABLE public."OutboxMessage" OWNER TO "postgres";

--
-- TOC entry 218 (class 1259 OID 17735)
-- Name: OutboxMessageType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."OutboxMessageType" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name public.outbox_message_type NOT NULL
);


ALTER TABLE public."OutboxMessageType" OWNER TO "postgres";

--
-- TOC entry 201 (class 1259 OID 16525)
-- Name: Platform; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."Platform" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    platform_id character varying,
    name text,
    description text,
    url text
);


ALTER TABLE public."Platform" OWNER TO "postgres";

--
-- TOC entry 211 (class 1259 OID 16621)
-- Name: PlatformService; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."PlatformService" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    platform_service_id character varying,
    platform_id uuid NOT NULL,
    platform_service_category_id uuid NOT NULL,
    name text,
    service_params_schema json,
    tag_required boolean DEFAULT true NOT NULL
);


ALTER TABLE public."PlatformService" OWNER TO "postgres";

--
-- TOC entry 202 (class 1259 OID 16536)
-- Name: PlatformServiceCategory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."PlatformServiceCategory" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    platform_service_category_id character varying,
    name text
);


ALTER TABLE public."PlatformServiceCategory" OWNER TO "postgres";

--
-- TOC entry 213 (class 1259 OID 16662)
-- Name: Product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."Product" (
    id uuid NOT NULL,
    product_id character varying,
    name text,
    state_of_product_id uuid NOT NULL,
    serving_method_id uuid NOT NULL,
    site_infra_service_id uuid NOT NULL,
    sitetag_domain character varying NOT NULL,
    et_data_received boolean DEFAULT false NOT NULL
);


ALTER TABLE public."Product" OWNER TO "postgres";

--
-- TOC entry 203 (class 1259 OID 16547)
-- Name: RevenueReportService; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."RevenueReportService" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name text,
    tableau_account_id character varying,
    service_id character varying NOT NULL,
    media_owner_id character varying NOT NULL
);


ALTER TABLE public."RevenueReportService" OWNER TO "postgres";

--
-- TOC entry 204 (class 1259 OID 16560)
-- Name: ServingMethod; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."ServingMethod" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name public.serving_method NOT NULL
);


ALTER TABLE public."ServingMethod" OWNER TO "postgres";

--
-- TOC entry 205 (class 1259 OID 16566)
-- Name: Site; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."Site" (
    id uuid NOT NULL,
    site_id character varying,
    name text,
    site_tag text,
    media_owner_id character varying NOT NULL,
    domain text
);


ALTER TABLE public."Site" OWNER TO "postgres";

--
-- TOC entry 212 (class 1259 OID 16642)
-- Name: SiteInfraService; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."SiteInfraService" (
    id uuid NOT NULL,
    site_infra_service_id character varying,
    name text,
    state_of_infra_integration_service_id uuid NOT NULL,
    site_id uuid NOT NULL,
    site_infra_service_tag text
);


ALTER TABLE public."SiteInfraService" OWNER TO "postgres";

--
-- TOC entry 220 (class 1259 OID 19831)
-- Name: SiteTagStatus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."SiteTagStatus" (
    id uuid DEFAULT public.uuid_generate_v1() NOT NULL,
    site_id uuid NOT NULL,
    status public.site_tag_status_type NOT NULL
);


ALTER TABLE public."SiteTagStatus" OWNER TO "postgres";

--
-- TOC entry 206 (class 1259 OID 16576)
-- Name: StateOfInfraIntegrationService; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."StateOfInfraIntegrationService" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name public.state_of_infra_integration_service NOT NULL
);


ALTER TABLE public."StateOfInfraIntegrationService" OWNER TO "postgres";

--
-- TOC entry 207 (class 1259 OID 16588)
-- Name: StateOfIntegrationService; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."StateOfIntegrationService" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name public.state_of_integration_service NOT NULL
);


ALTER TABLE public."StateOfIntegrationService" OWNER TO "postgres";

--
-- TOC entry 208 (class 1259 OID 16594)
-- Name: StateOfProduct; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public."StateOfProduct" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name public.state_of_product NOT NULL
);


ALTER TABLE public."StateOfProduct" OWNER TO "postgres";

--
-- TOC entry 209 (class 1259 OID 16600)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE IF NOT EXISTS public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO "postgres";

--
-- TOC entry 3820 (class 0 OID 17440)
-- Dependencies: 217
-- Data for Name: AnalyticService; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3818 (class 0 OID 17414)
-- Dependencies: 215
-- Data for Name: AnalyticServiceAccount; Type: TABLE DATA; Schema: public; Owner: postgres
--


--
-- TOC entry 3819 (class 0 OID 17429)
-- Dependencies: 216
-- Data for Name: AnalyticServiceCategory; Type: TABLE DATA; Schema: public; Owner: postgres
--

--
-- TOC entry 3813 (class 0 OID 16605)
-- Dependencies: 210
-- Data for Name: Integration; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3817 (class 0 OID 16687)
-- Dependencies: 214
-- Data for Name: IntegrationService; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3822 (class 0 OID 17741)
-- Dependencies: 219
-- Data for Name: OutboxMessage; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3821 (class 0 OID 17735)
-- Dependencies: 218
-- Data for Name: OutboxMessageType; Type: TABLE DATA; Schema: public; Owner: postgres
--

-- Create a temporary table
CREATE TEMP TABLE tmp_OutboxMessageType (id UUID, name public.outbox_message_type);

-- Copy data into the temporary table
COPY tmp_OutboxMessageType (id, name) FROM stdin;
4dbf6fc1-df21-418c-b914-e8a6cf7b4e84	PUBSUB
afd94968-d3b3-4e0c-ba5c-65fc664f292c	API
\.

-- Insert data from the temporary table into the actual table, excluding duplicates
INSERT INTO public."OutboxMessageType" (id, name)
SELECT id, name
FROM tmp_OutboxMessageType
WHERE NOT EXISTS (
    SELECT 1 FROM public."OutboxMessageType" WHERE id = tmp_OutboxMessageType.id
);

-- Drop the temporary table if no longer needed
DROP TABLE tmp_OutboxMessageType;


--
-- TOC entry 3804 (class 0 OID 16525)
-- Dependencies: 201
-- Data for Name: Platform; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3814 (class 0 OID 16621)
-- Dependencies: 211
-- Data for Name: PlatformService; Type: TABLE DATA; Schema: public; Owner: postgres
--


--
-- TOC entry 3805 (class 0 OID 16536)
-- Dependencies: 202
-- Data for Name: PlatformServiceCategory; Type: TABLE DATA; Schema: public; Owner: postgres
--

--
-- TOC entry 3816 (class 0 OID 16662)
-- Dependencies: 213
-- Data for Name: Product; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3806 (class 0 OID 16547)
-- Dependencies: 203
-- Data for Name: RevenueReportService; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3807 (class 0 OID 16560)
-- Dependencies: 204
-- Data for Name: ServingMethod; Type: TABLE DATA; Schema: public; Owner: postgres
--
-- Create a temporary table
CREATE TEMP TABLE tmp_ServingMethod (id UUID, name public.serving_method);

-- Copy data into the temporary table
COPY tmp_ServingMethod (id, name) FROM stdin;
72e8359e-b428-4385-8e98-c65c04407bae	SITE
7cc44252-2464-4582-85bc-a0b3e85973a9	HEADERTAG
\.

-- Insert data from the temporary table into the actual table, excluding duplicates
INSERT INTO public."ServingMethod" (id, name)
SELECT id, name
FROM tmp_ServingMethod
WHERE NOT EXISTS (
    SELECT 1 FROM public."ServingMethod" WHERE id = tmp_ServingMethod.id
);

-- Drop the temporary table if no longer needed
DROP TABLE tmp_ServingMethod;


--
-- TOC entry 3808 (class 0 OID 16566)
-- Dependencies: 205
-- Data for Name: Site; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3815 (class 0 OID 16642)
-- Dependencies: 212
-- Data for Name: SiteInfraService; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3823 (class 0 OID 19831)
-- Dependencies: 220
-- Data for Name: SiteTagStatus; Type: TABLE DATA; Schema: public; Owner: postgres
--


--
-- TOC entry 3809 (class 0 OID 16576)
-- Dependencies: 206
-- Data for Name: StateOfInfraIntegrationService; Type: TABLE DATA; Schema: public; Owner: postgres
--
-- Create a temporary table
CREATE TEMP TABLE tmp_StateOfInfraIntegrationService (id UUID, name public.state_of_infra_integration_service);

-- Copy data into the temporary table
COPY tmp_StateOfInfraIntegrationService (id, name) FROM stdin;
1fa3080f-9cc1-4351-9a17-1ee5d33761cd	DISABLED
ee0dd787-b234-4d96-898a-fe75c0bceb36	ENABLED
a285089b-62a1-42e6-84d8-39594fa0fea3	INFRA_INTEGRATED
\.

-- Insert data from the temporary table into the actual table, excluding duplicates
INSERT INTO public."StateOfInfraIntegrationService" (id, name)
SELECT id, name
FROM tmp_StateOfInfraIntegrationService
WHERE NOT EXISTS (
    SELECT 1 FROM public."StateOfInfraIntegrationService" WHERE id = tmp_StateOfInfraIntegrationService.id
);

-- Drop the temporary table if no longer needed
DROP TABLE tmp_StateOfInfraIntegrationService;


--
-- TOC entry 3810 (class 0 OID 16588)
-- Dependencies: 207
-- Data for Name: StateOfIntegrationService; Type: TABLE DATA; Schema: public; Owner: postgres

-- Create a temporary table
CREATE TEMP TABLE tmp_StateOfIntegrationService (id UUID, name public.state_of_integration_service);

-- Copy data into the temporary table
COPY tmp_StateOfIntegrationService (id, name) FROM stdin;
58e6a74e-6b3a-4b0f-b40a-e6af08807e1c	INIT
ee54a17e-5548-43cc-ac85-f8c49c418a53	ACTIVATED
b6db534d-5df7-4c7c-bd66-67e57efdeceb	ACTIVATING
a9b74495-0204-46de-8751-1f1fcca0dee9	DEACTIVATED
d3c49c30-e0db-4f8e-9352-7dac0bae5230	DEACTIVATING
\.

-- Insert data from the temporary table into the actual table, excluding duplicates
INSERT INTO public."StateOfIntegrationService" (id, name)
SELECT id, name
FROM tmp_StateOfIntegrationService
WHERE NOT EXISTS (
    SELECT 1 FROM public."StateOfIntegrationService" WHERE id = tmp_StateOfIntegrationService.id
);

-- Drop the temporary table if no longer needed
DROP TABLE tmp_StateOfIntegrationService;--


--
-- TOC entry 3811 (class 0 OID 16594)
-- Dependencies: 208
-- Data for Name: StateOfProduct; Type: TABLE DATA; Schema: public; Owner: postgres
--
-- Create a temporary table
CREATE TEMP TABLE tmp_StateOfProduct (id UUID, name public.state_of_product);

-- Copy data into the temporary table
COPY tmp_StateOfProduct (id, name) FROM stdin;
377dd515-2c8a-4306-8bac-cd37166a96ea	DISABLED
3678df0e-c853-46b9-8fd8-a83ba57019b0	ENABLING
ab345671-44d6-4084-9977-2568186011f9	ENABLED
583edc75-2296-427f-9a60-9e66144ce290	SITETAG_ONBOARDED
b5d7c000-5537-4853-b53b-a53684c02555	ACTIVATED
\.

-- Insert data from the temporary table into the actual table, excluding duplicates
INSERT INTO public."StateOfProduct" (id, name)
SELECT id, name
FROM tmp_StateOfProduct
WHERE NOT EXISTS (
    SELECT 1 FROM public."StateOfProduct" WHERE id = tmp_StateOfProduct.id
);

-- Drop the temporary table if no longer needed
DROP TABLE tmp_StateOfProduct;--

--
-- TOC entry 3812 (class 0 OID 16600)
-- Dependencies: 209
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3634 (class 2606 OID 17424)
-- Name: AnalyticServiceAccount AnalyticServiceAccount_analytic_service_account_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'AnalyticServiceAccount_analytic_service_account_id_key'
    ) THEN
        ALTER TABLE ONLY public."AnalyticServiceAccount"
            ADD CONSTRAINT "AnalyticServiceAccount_analytic_service_account_id_key" UNIQUE (analytic_service_account_id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'AnalyticServiceAccount_pkey'
    ) THEN
        ALTER TABLE ONLY public."AnalyticServiceAccount"
            ADD CONSTRAINT "AnalyticServiceAccount_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'AnalyticServiceAccount_tableau_account_id_key'
    ) THEN
        ALTER TABLE ONLY public."AnalyticServiceAccount"
            ADD CONSTRAINT "AnalyticServiceAccount_tableau_account_id_key" UNIQUE (tableau_account_id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'AnalyticServiceCategory_analytic_service_category_id_key'
    ) THEN
        ALTER TABLE ONLY public."AnalyticServiceCategory"
            ADD CONSTRAINT "AnalyticServiceCategory_analytic_service_category_id_key" UNIQUE (analytic_service_category_id);
    END IF;
END
$$;

--
-- TOC entry 3644 (class 2606 OID 17437)
-- Name: AnalyticServiceCategory AnalyticServiceCategory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'AnalyticServiceCategory_pkey'
    ) THEN
        ALTER TABLE ONLY public."AnalyticServiceCategory"
            ADD CONSTRAINT "AnalyticServiceCategory_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'AnalyticService_pkey'
    ) THEN
        ALTER TABLE ONLY public."AnalyticService"
            ADD CONSTRAINT "AnalyticService_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'AnalyticService_service_id_key'
    ) THEN
        ALTER TABLE ONLY public."AnalyticService"
            ADD CONSTRAINT "AnalyticService_service_id_key" UNIQUE (service_id);
    END IF;
END
$$;
--
-- TOC entry 3630 (class 2606 OID 16697)
-- Name: IntegrationService IntegrationService_integration_service_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'IntegrationService_integration_service_id_key'
    ) THEN
        ALTER TABLE ONLY public."IntegrationService"
            ADD CONSTRAINT "IntegrationService_integration_service_id_key" UNIQUE (integration_service_id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'IntegrationService_pkey'
    ) THEN
        ALTER TABLE ONLY public."IntegrationService"
            ADD CONSTRAINT "IntegrationService_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'Integration_integration_id_key'
    ) THEN
        ALTER TABLE ONLY public."Integration"
            ADD CONSTRAINT "Integration_integration_id_key" UNIQUE (integration_id);
    END IF;
END
$$;

--
-- TOC entry 3616 (class 2606 OID 16613)
-- Name: Integration Integration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'Integration_pkey'
    ) THEN
        ALTER TABLE ONLY public."Integration"
            ADD CONSTRAINT "Integration_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'OutboxMessageType_pkey'
    ) THEN
        ALTER TABLE ONLY public."OutboxMessageType"
            ADD CONSTRAINT "OutboxMessageType_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'OutboxMessage_pkey'
    ) THEN
        ALTER TABLE ONLY public."OutboxMessage"
            ADD CONSTRAINT "OutboxMessage_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

--
-- TOC entry 3590 (class 2606 OID 16544)
-- Name: PlatformServiceCategory PlatformServiceCategory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'PlatformServiceCategory_pkey'
    ) THEN
        ALTER TABLE ONLY public."PlatformServiceCategory"
            ADD CONSTRAINT "PlatformServiceCategory_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'PlatformServiceCategory_platform_service_category_id_key'
    ) THEN
        ALTER TABLE ONLY public."PlatformServiceCategory"
            ADD CONSTRAINT "PlatformServiceCategory_platform_service_category_id_key" UNIQUE (platform_service_category_id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'PlatformService_pkey'
    ) THEN
        ALTER TABLE ONLY public."PlatformService"
            ADD CONSTRAINT "PlatformService_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

--
-- TOC entry 3620 (class 2606 OID 16631)
-- Name: PlatformService PlatformService_platform_service_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'PlatformService_platform_service_id_key'
    ) THEN
        ALTER TABLE ONLY public."PlatformService"
            ADD CONSTRAINT "PlatformService_platform_service_id_key" UNIQUE (platform_service_id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'Platform_pkey'
    ) THEN
        ALTER TABLE ONLY public."Platform"
            ADD CONSTRAINT "Platform_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'Platform_platform_id_key'
    ) THEN
        ALTER TABLE ONLY public."Platform"
            ADD CONSTRAINT "Platform_platform_id_key" UNIQUE (platform_id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'Product_pkey'
    ) THEN
        ALTER TABLE ONLY public."Product"
            ADD CONSTRAINT "Product_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'Product_product_id_key'
    ) THEN
        ALTER TABLE ONLY public."Product"
            ADD CONSTRAINT "Product_product_id_key" UNIQUE (product_id);
    END IF;
END
$$;

--
-- TOC entry 3594 (class 2606 OID 16555)
-- Name: RevenueReportService RevenueReportService_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'RevenueReportService_pkey'
    ) THEN
        ALTER TABLE ONLY public."RevenueReportService"
            ADD CONSTRAINT "RevenueReportService_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'RevenueReportService_service_id_key'
    ) THEN
        ALTER TABLE ONLY public."RevenueReportService"
            ADD CONSTRAINT "RevenueReportService_service_id_key" UNIQUE (service_id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'RevenueReportService_tableau_account_id_key'
    ) THEN
        ALTER TABLE ONLY public."RevenueReportService"
            ADD CONSTRAINT "RevenueReportService_tableau_account_id_key" UNIQUE (tableau_account_id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'ServingMethod_pkey'
    ) THEN
        ALTER TABLE ONLY public."ServingMethod"
            ADD CONSTRAINT "ServingMethod_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'SiteInfraService_pkey'
    ) THEN
        ALTER TABLE ONLY public."SiteInfraService"
            ADD CONSTRAINT "SiteInfraService_pkey" PRIMARY KEY (id);
    END IF;
END
$$;

--
-- TOC entry 3624 (class 2606 OID 16651)
-- Name: SiteInfraService SiteInfraService_site_infra_service_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'SiteInfraService_site_infra_service_id_key'
    ) THEN
        ALTER TABLE ONLY public."SiteInfraService"
    ADD CONSTRAINT   "SiteInfraService_site_infra_service_id_key" UNIQUE (site_infra_service_id);

    END IF;
END
$$;


--
-- TOC entry 3656 (class 2606 OID 19836)
-- Name: SiteTagStatus SiteTagStatus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'SiteTagStatus_pkey'
    ) THEN
        ALTER TABLE ONLY public."SiteTagStatus"
    ADD CONSTRAINT   "SiteTagStatus_pkey" PRIMARY KEY (id);

    END IF;
END
$$;



--
-- TOC entry 3658 (class 2606 OID 19838)
-- Name: SiteTagStatus SiteTagStatus_site_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'SiteTagStatus_site_id_key'
    ) THEN
        ALTER TABLE ONLY public."SiteTagStatus"
    ADD CONSTRAINT   "SiteTagStatus_site_id_key" UNIQUE (site_id);

    END IF;
END
$$;


--
-- TOC entry 3602 (class 2606 OID 16573)
-- Name: Site Site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'Site_pkey'
    ) THEN
        ALTER TABLE ONLY public."Site"
    ADD CONSTRAINT   "Site_pkey" PRIMARY KEY (id);

    END IF;
END
$$;


--
-- TOC entry 3604 (class 2606 OID 16575)
-- Name: Site Site_site_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'Site_site_id_key'
    ) THEN
        ALTER TABLE ONLY public."Site"
    ADD CONSTRAINT   "Site_site_id_key" UNIQUE (site_id);
    END IF;
END
$$;


--
-- TOC entry 3606 (class 2606 OID 16581)
-- Name: StateOfInfraIntegrationService StateOfInfraIntegrationService_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'StateOfInfraIntegrationService_pkey'
    ) THEN
        ALTER TABLE ONLY public."StateOfInfraIntegrationService"
    ADD CONSTRAINT   "StateOfInfraIntegrationService_pkey" PRIMARY KEY (id);

    END IF;
END
$$;


--
-- TOC entry 3608 (class 2606 OID 16593)
-- Name: StateOfIntegrationService StateOfIntegrationService_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'StateOfIntegrationService_pkey'
    ) THEN
        ALTER TABLE ONLY public."StateOfIntegrationService"
    ADD CONSTRAINT   "StateOfIntegrationService_pkey" PRIMARY KEY (id);

    END IF;
END
$$;

--
-- TOC entry 3610 (class 2606 OID 16599)
-- Name: StateOfProduct StateOfProduct_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'StateOfProduct_pkey'
	) THEN
		ALTER TABLE ONLY public."StateOfProduct"
	ADD CONSTRAINT   "StateOfProduct_pkey" PRIMARY KEY (id);

	END IF;
END
$$;
--
-- TOC entry 3612 (class 2606 OID 16604)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'alembic_version_pkc'
	) THEN
		ALTER TABLE ONLY public.alembic_version
	ADD CONSTRAINT   alembic_version_pkc PRIMARY KEY (version_num);

	END IF;
END
$$;


--
-- TOC entry 3650 (class 2606 OID 17452)
-- Name: AnalyticService as_account_category_uc; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'as_account_category_uc'
	) THEN
		ALTER TABLE ONLY public."AnalyticService"
	ADD CONSTRAINT   as_account_category_uc UNIQUE (analytic_service_account_id, analytic_service_category_id);

	END IF;
END
$$;


--
-- TOC entry 3640 (class 2606 OID 17428)
-- Name: AnalyticServiceAccount as_media_owner_tableau_account_uc; Type: CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'as_media_owner_tableau_account_uc'
	) THEN
		ALTER TABLE ONLY public."AnalyticServiceAccount"
	ADD CONSTRAINT   as_media_owner_tableau_account_uc UNIQUE (media_owner_id, tableau_account_id);

	END IF;
END
$$;


--
-- TOC entry 3670 (class 2606 OID 17453)
-- Name: AnalyticService AnalyticService_analytic_service_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'AnalyticService_analytic_service_account_id_fkey'
	) THEN
		ALTER TABLE ONLY public."AnalyticService"
	ADD CONSTRAINT   "AnalyticService_analytic_service_account_id_fkey" FOREIGN KEY (analytic_service_account_id) REFERENCES public."AnalyticServiceAccount"(id);

	END IF;
END
$$;


--
-- TOC entry 3671 (class 2606 OID 17458)
-- Name: AnalyticService AnalyticService_analytic_service_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'AnalyticService_analytic_service_category_id_fkey'
	) THEN
		ALTER TABLE ONLY public."AnalyticService"
	ADD CONSTRAINT   "AnalyticService_analytic_service_category_id_fkey" FOREIGN KEY (analytic_service_category_id) REFERENCES public."AnalyticServiceCategory"(id);

	END IF;
END
$$;


--
-- TOC entry 3667 (class 2606 OID 16698)
-- Name: IntegrationService IntegrationService_integration_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'IntegrationService_integration_id_fkey'
	) THEN
		ALTER TABLE ONLY public."IntegrationService"
	ADD CONSTRAINT   "IntegrationService_integration_id_fkey" FOREIGN KEY (integration_id) REFERENCES public."Integration"(id);

	END IF;
END
$$;


--
-- TOC entry 3668 (class 2606 OID 16703)
-- Name: IntegrationService IntegrationService_platform_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'IntegrationService_platform_service_id_fkey'
	) THEN
		ALTER TABLE ONLY public."IntegrationService"
	ADD CONSTRAINT   "IntegrationService_platform_service_id_fkey" FOREIGN KEY (platform_service_id) REFERENCES public."PlatformService"(id);

	END IF;
END
$$;


--
-- TOC entry 3669 (class 2606 OID 16713)
-- Name: IntegrationService IntegrationService_state_of_integration_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'IntegrationService_state_of_integration_service_id_fkey'
	) THEN
		ALTER TABLE ONLY public."IntegrationService"
	ADD CONSTRAINT   "IntegrationService_state_of_integration_service_id_fkey" FOREIGN KEY (state_of_integration_service_id) REFERENCES public."StateOfIntegrationService"(id);

	END IF;
END
$$;


--
-- TOC entry 3659 (class 2606 OID 17755)
-- Name: Integration Integration_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'Integration_product_id_fkey'
	) THEN
		ALTER TABLE ONLY public."Integration"
	ADD CONSTRAINT   "Integration_product_id_fkey" FOREIGN KEY (product_id) REFERENCES public."Product"(id);

	END IF;
END
$$;


--
-- TOC entry 3672 (class 2606 OID 17750)
-- Name: OutboxMessage OutboxMessage_outbox_message_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'OutboxMessage_outbox_message_type_id_fkey'
	) THEN
		ALTER TABLE ONLY public."OutboxMessage"
	ADD CONSTRAINT   "OutboxMessage_outbox_message_type_id_fkey" FOREIGN KEY (outbox_message_type_id) REFERENCES public."OutboxMessageType"(id);

	END IF;
END
$$;


--
-- TOC entry 3660 (class 2606 OID 16632)
-- Name: PlatformService PlatformService_platform_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'PlatformService_platform_id_fkey'
	) THEN
		ALTER TABLE ONLY public."PlatformService"
	ADD CONSTRAINT   "PlatformService_platform_id_fkey" FOREIGN KEY (platform_id) REFERENCES public."Platform"(id);

	END IF;
END
$$;


--
-- TOC entry 3661 (class 2606 OID 16637)
-- Name: PlatformService PlatformService_platform_service_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'PlatformService_platform_service_category_id_fkey'
	) THEN
		ALTER TABLE ONLY public."PlatformService"
	ADD CONSTRAINT   "PlatformService_platform_service_category_id_fkey" FOREIGN KEY (platform_service_category_id) REFERENCES public."PlatformServiceCategory"(id);

	END IF;
END
$$;


--
-- TOC entry 3664 (class 2606 OID 16672)
-- Name: Product Product_serving_method_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'Product_serving_method_id_fkey'
	) THEN
		ALTER TABLE ONLY public."Product"
	ADD CONSTRAINT   "Product_serving_method_id_fkey" FOREIGN KEY (serving_method_id) REFERENCES public."ServingMethod"(id);

	END IF;
END
$$;


--
-- TOC entry 3665 (class 2606 OID 16677)
-- Name: Product Product_site_infra_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'Product_site_infra_service_id_fkey'
	) THEN
		ALTER TABLE ONLY public."Product"
	ADD CONSTRAINT   "Product_site_infra_service_id_fkey" FOREIGN KEY (site_infra_service_id) REFERENCES public."SiteInfraService"(id);

	END IF;
END
$$;


--
-- TOC entry 3666 (class 2606 OID 16682)
-- Name: Product Product_state_of_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'Product_state_of_product_id_fkey'
	) THEN
		ALTER TABLE ONLY public."Product"
	ADD CONSTRAINT   "Product_state_of_product_id_fkey" FOREIGN KEY (state_of_product_id) REFERENCES public."StateOfProduct"(id);

	END IF;
END
$$;


--
-- TOC entry 3662 (class 2606 OID 16652)
-- Name: SiteInfraService SiteInfraService_site_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'SiteInfraService_site_id_fkey'
	) THEN
		ALTER TABLE ONLY public."SiteInfraService"
	ADD CONSTRAINT   "SiteInfraService_site_id_fkey" FOREIGN KEY (site_id) REFERENCES public."Site"(id);

	END IF;
END
$$;

--
-- TOC entry 3663 (class 2606 OID 16657)
-- Name: SiteInfraService SiteInfraService_state_of_infra_integration_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'SiteInfraService_state_of_infra_integration_service_id_fkey'
	) THEN
		ALTER TABLE ONLY public."SiteInfraService"
	ADD CONSTRAINT   "SiteInfraService_state_of_infra_integration_service_id_fkey" FOREIGN KEY (state_of_infra_integration_service_id) REFERENCES public."StateOfInfraIntegrationService"(id);

	END IF;
END
$$;


--
-- TOC entry 3673 (class 2606 OID 19839)
-- Name: SiteTagStatus SiteTagStatus_site_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1
		FROM pg_constraint
		WHERE conname = 'SiteTagStatus_site_id_fkey'
	) THEN
		ALTER TABLE ONLY public."SiteTagStatus"
	ADD CONSTRAINT   "SiteTagStatus_site_id_fkey" FOREIGN KEY (site_id) REFERENCES public."Site"(id);

	END IF;
END
$$;


--
-- TOC entry 3829 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: cloudsqlsuperuser
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2024-07-05 09:54:29 EEST

--
-- PostgreSQL database dump complete
--

