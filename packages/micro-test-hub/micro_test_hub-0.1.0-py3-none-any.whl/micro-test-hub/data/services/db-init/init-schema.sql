--
-- PostgreSQL database dump
--

-- Dumped from database version 13.5 (Debian 13.5-1.pgdg110+1)
-- Dumped by pg_dump version 16.3 (Ubuntu 16.3-0ubuntu0.24.04.1)

-- Started on 2024-07-02 12:27:33 EEST

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
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 2 (class 3079 OID 16385)
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- TOC entry 3219 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


--
-- TOC entry 652 (class 1247 OID 16397)
-- Name: feature_type; Type: TYPE; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'feature_type') THEN
        CREATE TYPE public.feature_type AS ENUM (
                                                    'BOOLEAN',
                                                    'LIMIT',
                                                    'RANGE',
                                                    'QUOTAS',
                                                    'SET',
                                                    'EXTENSION'
                                                );
    END IF;
END
$$;


ALTER TYPE public.feature_type OWNER TO postgres;

--
-- TOC entry 655 (class 1247 OID 16410)
-- Name: ondemand_quota_type; Type: TYPE; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'ondemand_quota_type') THEN
        CREATE TYPE public.ondemand_quota_type AS ENUM (
                                                            'PAGEVIEWS',
                                                            'API_CONNECTORS',
                                                            'USERS'
                                                        );
    END IF;
END
$$;

ALTER TYPE public.ondemand_quota_type OWNER TO postgres;

--
-- TOC entry 658 (class 1247 OID 16418)
-- Name: plan_type; Type: TYPE; Schema: public; Owner: postgres
--

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'plan_type') THEN
        CREATE TYPE public.plan_type AS ENUM (
                                                'iMOC',
                                                'dMOC',
                                                'MOC',
                                                'sMOC',
                                                'cMOC',
                                                'BETA_MO',
                                                'BETA_SITE'
                                            );
    END IF;
END
$$;



ALTER TYPE public.plan_type OWNER TO postgres;

--
-- TOC entry 661 (class 1247 OID 16434)
-- Name: product_status_type; Type: TYPE; Schema: public; Owner: postgres
--
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'product_status_type') THEN
        CREATE TYPE public.product_status_type AS ENUM (
                                                            'DISABLED',
                                                            'ENABLING',
                                                            'ENABLED',
                                                            'SITETAG_ONBOARDED',
                                                            'ACTIVATED'
                                                        );
    END IF;
END
$$;

ALTER TYPE public.product_status_type OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
        EXECUTE 'DROP TABLE IF EXISTS public.' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP;
END $$;
--
-- TOC entry 201 (class 1259 OID 16445)
-- Name: CostPolicy; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."CostPolicy" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    cost_policy_id character varying,
    feature character varying,
    lower_bound integer DEFAULT 0.0 NOT NULL,
    upper_bound integer DEFAULT 0.0 NOT NULL,
    cost double precision DEFAULT 0.0 NOT NULL
);


ALTER TABLE public."CostPolicy" OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16455)
-- Name: Feature; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Feature" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    feature_id character varying,
    name text NOT NULL,
    target character varying[],
    feature_set_id uuid NOT NULL,
    cost double precision DEFAULT 0.0 NOT NULL,
    multiplier integer DEFAULT 1 NOT NULL,
    beta boolean DEFAULT false NOT NULL
);


ALTER TABLE public."Feature" OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16465)
-- Name: FeatureSet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."FeatureSet" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    feature_set_id character varying,
    name text NOT NULL,
    type_id uuid NOT NULL
);


ALTER TABLE public."FeatureSet" OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16472)
-- Name: FeatureType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."FeatureType" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name public.feature_type NOT NULL
);


ALTER TABLE public."FeatureType" OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16476)
-- Name: MOPlan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."MOPlan" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    mo_plan_id character varying,
    name character varying NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    media_owner_id uuid NOT NULL,
    discount double precision DEFAULT 0.0 NOT NULL
);


ALTER TABLE public."MOPlan" OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16484)
-- Name: MOPlanMOSubscription; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."MOPlanMOSubscription" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    mo_plan_id uuid NOT NULL,
    mo_subscription_id_id uuid NOT NULL
);


ALTER TABLE public."MOPlanMOSubscription" OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16488)
-- Name: MOPlanSiteSubscription; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."MOPlanSiteSubscription" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    mo_plan_id uuid NOT NULL,
    site_subscription_id_id uuid NOT NULL
);


ALTER TABLE public."MOPlanSiteSubscription" OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16492)
-- Name: MOSubscription; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."MOSubscription" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    mo_subscription_id character varying NOT NULL,
    media_owner_id uuid NOT NULL,
    subscription_id uuid NOT NULL
);


ALTER TABLE public."MOSubscription" OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16499)
-- Name: MediaOwner; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."MediaOwner" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    media_owner_id character varying,
    name text NOT NULL,
    company_name text NOT NULL,
    company_type text NOT NULL,
    company_vat_registration_office text NOT NULL,
    company_registration_number text NOT NULL,
    company_country text NOT NULL,
    company_address text NOT NULL,
    company_city text NOT NULL,
    company_zip_code text NOT NULL,
    contact_first_name text NOT NULL,
    contact_last_name text NOT NULL,
    contact_email text NOT NULL,
    contact_phone text NOT NULL,
    currency character varying NOT NULL,
    pa_id integer NOT NULL
);


ALTER TABLE public."MediaOwner" OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16506)
-- Name: OndemandQuota; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."OndemandQuota" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    ondemand_quota_id character varying,
    "limit" integer NOT NULL,
    payment_datetime timestamp without time zone NOT NULL,
    type_id uuid NOT NULL,
    subscription_id uuid NOT NULL
);


ALTER TABLE public."OndemandQuota" OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16513)
-- Name: OndemandQuotaType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."OndemandQuotaType" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name public.ondemand_quota_type NOT NULL,
    cost double precision NOT NULL
);


ALTER TABLE public."OndemandQuotaType" OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16517)
-- Name: Package; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Package" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    package_id character varying,
    name character varying NOT NULL,
    is_free boolean NOT NULL
);


ALTER TABLE public."Package" OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16524)
-- Name: Plan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Plan" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    plan_id character varying,
    name text NOT NULL,
    description text NOT NULL,
    custom boolean NOT NULL,
    type_id uuid NOT NULL,
    package_id uuid NOT NULL
);


ALTER TABLE public."Plan" OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16531)
-- Name: PlanFeature; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PlanFeature" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    feature_id uuid NOT NULL,
    plan_id uuid NOT NULL
);


ALTER TABLE public."PlanFeature" OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16535)
-- Name: PlanType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PlanType" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name public.plan_type NOT NULL,
    level text,
    description text
);


ALTER TABLE public."PlanType" OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16542)
-- Name: Site; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Site" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    site_id character varying NOT NULL,
    name character varying,
    domain character varying,
    pa_domain_id integer,
    media_owner_id uuid NOT NULL
);


ALTER TABLE public."Site" OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16549)
-- Name: SiteSubscription; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."SiteSubscription" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    site_subscription_id character varying NOT NULL,
    pageviews integer NOT NULL,
    site_id uuid NOT NULL,
    subscription_id uuid NOT NULL
);


ALTER TABLE public."SiteSubscription" OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16556)
-- Name: Subscription; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Subscription" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    subscription_id character varying,
    name text NOT NULL,
    plan_id uuid NOT NULL,
    payment_datetime timestamp without time zone NOT NULL,
    expiration_datetime timestamp without time zone NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE public."Subscription" OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16563)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 2985 (class 2606 OID 16567)
-- Name: CostPolicy CostPolicy_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."CostPolicy"
    ADD CONSTRAINT "CostPolicy_pkey" PRIMARY KEY (id);


--
-- TOC entry 2993 (class 2606 OID 16569)
-- Name: FeatureSet FeatureSet_feature_set_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FeatureSet"
    ADD CONSTRAINT "FeatureSet_feature_set_id_key" UNIQUE (feature_set_id);


--
-- TOC entry 2995 (class 2606 OID 16571)
-- Name: FeatureSet FeatureSet_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FeatureSet"
    ADD CONSTRAINT "FeatureSet_name_key" UNIQUE (name);


--
-- TOC entry 2997 (class 2606 OID 16573)
-- Name: FeatureSet FeatureSet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FeatureSet"
    ADD CONSTRAINT "FeatureSet_pkey" PRIMARY KEY (id);


--
-- TOC entry 2999 (class 2606 OID 16575)
-- Name: FeatureType FeatureType_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FeatureType"
    ADD CONSTRAINT "FeatureType_name_key" UNIQUE (name);


--
-- TOC entry 3001 (class 2606 OID 16577)
-- Name: FeatureType FeatureType_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FeatureType"
    ADD CONSTRAINT "FeatureType_pkey" PRIMARY KEY (id);


--
-- TOC entry 2987 (class 2606 OID 16579)
-- Name: Feature Feature_feature_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Feature"
    ADD CONSTRAINT "Feature_feature_id_key" UNIQUE (feature_id);


--
-- TOC entry 2989 (class 2606 OID 16581)
-- Name: Feature Feature_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Feature"
    ADD CONSTRAINT "Feature_name_key" UNIQUE (name);


--
-- TOC entry 2991 (class 2606 OID 16583)
-- Name: Feature Feature_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Feature"
    ADD CONSTRAINT "Feature_pkey" PRIMARY KEY (id);


--
-- TOC entry 3007 (class 2606 OID 16585)
-- Name: MOPlanMOSubscription MOPlanMOSubscription_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOPlanMOSubscription"
    ADD CONSTRAINT "MOPlanMOSubscription_pkey" PRIMARY KEY (id, mo_plan_id, mo_subscription_id_id);


--
-- TOC entry 3009 (class 2606 OID 16587)
-- Name: MOPlanSiteSubscription MOPlanSiteSubscription_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOPlanSiteSubscription"
    ADD CONSTRAINT "MOPlanSiteSubscription_pkey" PRIMARY KEY (id, mo_plan_id, site_subscription_id_id);


--
-- TOC entry 3003 (class 2606 OID 16589)
-- Name: MOPlan MOPlan_mo_plan_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOPlan"
    ADD CONSTRAINT "MOPlan_mo_plan_id_key" UNIQUE (mo_plan_id);


--
-- TOC entry 3005 (class 2606 OID 16591)
-- Name: MOPlan MOPlan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOPlan"
    ADD CONSTRAINT "MOPlan_pkey" PRIMARY KEY (id);


--
-- TOC entry 3011 (class 2606 OID 16593)
-- Name: MOSubscription MOSubscription_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOSubscription"
    ADD CONSTRAINT "MOSubscription_pkey" PRIMARY KEY (id);


--
-- TOC entry 3013 (class 2606 OID 16595)
-- Name: MediaOwner MediaOwner_media_owner_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MediaOwner"
    ADD CONSTRAINT "MediaOwner_media_owner_id_key" UNIQUE (media_owner_id);


--
-- TOC entry 3015 (class 2606 OID 16597)
-- Name: MediaOwner MediaOwner_pa_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MediaOwner"
    ADD CONSTRAINT "MediaOwner_pa_id_key" UNIQUE (pa_id);


--
-- TOC entry 3017 (class 2606 OID 16599)
-- Name: MediaOwner MediaOwner_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MediaOwner"
    ADD CONSTRAINT "MediaOwner_pkey" PRIMARY KEY (id);


--
-- TOC entry 3023 (class 2606 OID 16601)
-- Name: OndemandQuotaType OndemandQuotaType_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."OndemandQuotaType"
    ADD CONSTRAINT "OndemandQuotaType_name_key" UNIQUE (name);


--
-- TOC entry 3025 (class 2606 OID 16603)
-- Name: OndemandQuotaType OndemandQuotaType_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."OndemandQuotaType"
    ADD CONSTRAINT "OndemandQuotaType_pkey" PRIMARY KEY (id);


--
-- TOC entry 3019 (class 2606 OID 16605)
-- Name: OndemandQuota OndemandQuota_ondemand_quota_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."OndemandQuota"
    ADD CONSTRAINT "OndemandQuota_ondemand_quota_id_key" UNIQUE (ondemand_quota_id);


--
-- TOC entry 3021 (class 2606 OID 16607)
-- Name: OndemandQuota OndemandQuota_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."OndemandQuota"
    ADD CONSTRAINT "OndemandQuota_pkey" PRIMARY KEY (id);


--
-- TOC entry 3027 (class 2606 OID 16609)
-- Name: Package Package_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Package"
    ADD CONSTRAINT "Package_name_key" UNIQUE (name);


--
-- TOC entry 3029 (class 2606 OID 16611)
-- Name: Package Package_name_key1; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Package"
    ADD CONSTRAINT "Package_name_key1" UNIQUE (name);


--
-- TOC entry 3031 (class 2606 OID 16613)
-- Name: Package Package_package_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Package"
    ADD CONSTRAINT "Package_package_id_key" UNIQUE (package_id);


--
-- TOC entry 3033 (class 2606 OID 16615)
-- Name: Package Package_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Package"
    ADD CONSTRAINT "Package_pkey" PRIMARY KEY (id);


--
-- TOC entry 3043 (class 2606 OID 16617)
-- Name: PlanFeature PlanFeature_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PlanFeature"
    ADD CONSTRAINT "PlanFeature_pkey" PRIMARY KEY (id, feature_id, plan_id);


--
-- TOC entry 3045 (class 2606 OID 16619)
-- Name: PlanType PlanType_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PlanType"
    ADD CONSTRAINT "PlanType_name_key" UNIQUE (name);


--
-- TOC entry 3047 (class 2606 OID 16621)
-- Name: PlanType PlanType_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PlanType"
    ADD CONSTRAINT "PlanType_pkey" PRIMARY KEY (id);


--
-- TOC entry 3035 (class 2606 OID 16623)
-- Name: Plan Plan_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Plan"
    ADD CONSTRAINT "Plan_name_key" UNIQUE (name);


--
-- TOC entry 3037 (class 2606 OID 16625)
-- Name: Plan Plan_name_key1; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Plan"
    ADD CONSTRAINT "Plan_name_key1" UNIQUE (name);


--
-- TOC entry 3039 (class 2606 OID 16627)
-- Name: Plan Plan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Plan"
    ADD CONSTRAINT "Plan_pkey" PRIMARY KEY (id);


--
-- TOC entry 3041 (class 2606 OID 16629)
-- Name: Plan Plan_plan_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Plan"
    ADD CONSTRAINT "Plan_plan_id_key" UNIQUE (plan_id);


--
-- TOC entry 3057 (class 2606 OID 16631)
-- Name: SiteSubscription SiteSubscription_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SiteSubscription"
    ADD CONSTRAINT "SiteSubscription_pkey" PRIMARY KEY (id);


--
-- TOC entry 3049 (class 2606 OID 16633)
-- Name: Site Site_domain_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Site"
    ADD CONSTRAINT "Site_domain_key" UNIQUE (domain);


--
-- TOC entry 3051 (class 2606 OID 16635)
-- Name: Site Site_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Site"
    ADD CONSTRAINT "Site_name_key" UNIQUE (name);


--
-- TOC entry 3053 (class 2606 OID 16637)
-- Name: Site Site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Site"
    ADD CONSTRAINT "Site_pkey" PRIMARY KEY (id);


--
-- TOC entry 3055 (class 2606 OID 16639)
-- Name: Site Site_site_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Site"
    ADD CONSTRAINT "Site_site_id_key" UNIQUE (site_id);


--
-- TOC entry 3059 (class 2606 OID 16641)
-- Name: Subscription Subscription_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Subscription"
    ADD CONSTRAINT "Subscription_pkey" PRIMARY KEY (id);


--
-- TOC entry 3061 (class 2606 OID 16643)
-- Name: Subscription Subscription_subscription_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Subscription"
    ADD CONSTRAINT "Subscription_subscription_id_key" UNIQUE (subscription_id);


--
-- TOC entry 3063 (class 2606 OID 16645)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 3065 (class 2606 OID 16646)
-- Name: FeatureSet FeatureSet_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FeatureSet"
    ADD CONSTRAINT "FeatureSet_type_id_fkey" FOREIGN KEY (type_id) REFERENCES public."FeatureType"(id);


--
-- TOC entry 3064 (class 2606 OID 16651)
-- Name: Feature Feature_feature_set_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Feature"
    ADD CONSTRAINT "Feature_feature_set_id_fkey" FOREIGN KEY (feature_set_id) REFERENCES public."FeatureSet"(id);


--
-- TOC entry 3067 (class 2606 OID 16656)
-- Name: MOPlanMOSubscription MOPlanMOSubscription_mo_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOPlanMOSubscription"
    ADD CONSTRAINT "MOPlanMOSubscription_mo_plan_id_fkey" FOREIGN KEY (mo_plan_id) REFERENCES public."MOPlan"(id) ON DELETE CASCADE;


--
-- TOC entry 3068 (class 2606 OID 16661)
-- Name: MOPlanMOSubscription MOPlanMOSubscription_mo_subscription_id_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOPlanMOSubscription"
    ADD CONSTRAINT "MOPlanMOSubscription_mo_subscription_id_id_fkey" FOREIGN KEY (mo_subscription_id_id) REFERENCES public."MOSubscription"(id);


--
-- TOC entry 3069 (class 2606 OID 16666)
-- Name: MOPlanSiteSubscription MOPlanSiteSubscription_mo_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOPlanSiteSubscription"
    ADD CONSTRAINT "MOPlanSiteSubscription_mo_plan_id_fkey" FOREIGN KEY (mo_plan_id) REFERENCES public."MOPlan"(id) ON DELETE CASCADE;


--
-- TOC entry 3070 (class 2606 OID 24577)
-- Name: MOPlanSiteSubscription MOPlanSiteSubscription_site_subscription_id_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOPlanSiteSubscription"
    ADD CONSTRAINT "MOPlanSiteSubscription_site_subscription_id_id_fkey" FOREIGN KEY (site_subscription_id_id) REFERENCES public."SiteSubscription"(id) ON DELETE CASCADE;


--
-- TOC entry 3066 (class 2606 OID 16676)
-- Name: MOPlan MOPlan_media_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOPlan"
    ADD CONSTRAINT "MOPlan_media_owner_id_fkey" FOREIGN KEY (media_owner_id) REFERENCES public."MediaOwner"(id);


--
-- TOC entry 3071 (class 2606 OID 16681)
-- Name: MOSubscription MOSubscription_media_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOSubscription"
    ADD CONSTRAINT "MOSubscription_media_owner_id_fkey" FOREIGN KEY (media_owner_id) REFERENCES public."MediaOwner"(id);


--
-- TOC entry 3072 (class 2606 OID 16686)
-- Name: MOSubscription MOSubscription_subscription_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MOSubscription"
    ADD CONSTRAINT "MOSubscription_subscription_id_fkey" FOREIGN KEY (subscription_id) REFERENCES public."Subscription"(id);


--
-- TOC entry 3073 (class 2606 OID 16691)
-- Name: OndemandQuota OndemandQuota_subscription_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."OndemandQuota"
    ADD CONSTRAINT "OndemandQuota_subscription_id_fkey" FOREIGN KEY (subscription_id) REFERENCES public."Subscription"(id);


--
-- TOC entry 3074 (class 2606 OID 16696)
-- Name: OndemandQuota OndemandQuota_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."OndemandQuota"
    ADD CONSTRAINT "OndemandQuota_type_id_fkey" FOREIGN KEY (type_id) REFERENCES public."OndemandQuotaType"(id);


--
-- TOC entry 3077 (class 2606 OID 16701)
-- Name: PlanFeature PlanFeature_feature_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PlanFeature"
    ADD CONSTRAINT "PlanFeature_feature_id_fkey" FOREIGN KEY (feature_id) REFERENCES public."Feature"(id);


--
-- TOC entry 3078 (class 2606 OID 16706)
-- Name: PlanFeature PlanFeature_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PlanFeature"
    ADD CONSTRAINT "PlanFeature_plan_id_fkey" FOREIGN KEY (plan_id) REFERENCES public."Plan"(id) ON DELETE CASCADE;


--
-- TOC entry 3075 (class 2606 OID 16711)
-- Name: Plan Plan_package_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Plan"
    ADD CONSTRAINT "Plan_package_id_fkey" FOREIGN KEY (package_id) REFERENCES public."Package"(id);


--
-- TOC entry 3076 (class 2606 OID 16716)
-- Name: Plan Plan_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Plan"
    ADD CONSTRAINT "Plan_type_id_fkey" FOREIGN KEY (type_id) REFERENCES public."PlanType"(id);


--
-- TOC entry 3080 (class 2606 OID 16721)
-- Name: SiteSubscription SiteSubscription_site_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SiteSubscription"
    ADD CONSTRAINT "SiteSubscription_site_id_fkey" FOREIGN KEY (site_id) REFERENCES public."Site"(id);


--
-- TOC entry 3081 (class 2606 OID 16726)
-- Name: SiteSubscription SiteSubscription_subscription_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SiteSubscription"
    ADD CONSTRAINT "SiteSubscription_subscription_id_fkey" FOREIGN KEY (subscription_id) REFERENCES public."Subscription"(id);


--
-- TOC entry 3079 (class 2606 OID 16731)
-- Name: Site Site_media_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Site"
    ADD CONSTRAINT "Site_media_owner_id_fkey" FOREIGN KEY (media_owner_id) REFERENCES public."MediaOwner"(id) ON DELETE CASCADE;


--
-- TOC entry 3082 (class 2606 OID 16736)
-- Name: Subscription Subscription_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Subscription"
    ADD CONSTRAINT "Subscription_plan_id_fkey" FOREIGN KEY (plan_id) REFERENCES public."Plan"(id);


--
-- TOC entry 3218 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;

INSERT INTO public."CostPolicy" (id,cost_policy_id,feature,lower_bound,upper_bound,"cost") VALUES
	 ('4edcec05-5f2c-4b12-a251-7e7de26d121b','b221c87a-9835-45ce-8f5f-140c6eb03407
065d9c37-b63c-4615-9ec2-54f039c3a239
f8863fb4-9c74-4478-a125-4de2e0e9087c
a92cfd61-b866-4ae5-9957-0e6e8b6ec198
d8ff9fbc-171d-4c98-8a18-9d9be2af2af6
f56acb8d-982d-4ec8-b250-afcf5d706286','PAGEVIEWS',0,5000000,0.00004),
	 ('b20c520e-9eab-45a2-bf25-a32e47d71f9c','b1f01ec3-adb8-48a1-8c3d-0fe68738c395','PAGEVIEWS',10000000,50000000,0.000008),
	 ('3e5f35f9-f11d-4e05-8d58-d448b2bb8202','b2f87f96-030a-4adb-bf83-0f5f3f7c0ae0','PAGEVIEWS',5000000,10000000,0.00002),
	 ('20a0ae17-081f-4f42-b02c-0da2c09ff667','ceab06ef-7c63-42e3-a71b-bf8a8c857f5e','PAGEVIEWS',50000000,1000000000,0.000004),
	 ('207c949d-b494-40f6-9184-475d2f9c041c','3ff2e4ea-1ee0-4c4d-a0d6-b5059ea700a5','API_CONNECTORS',0,5,300.0),
	 ('e4853446-16d8-4e9e-b5c6-e633d6a53594','96519600-cb0c-49d2-b7ec-cabead88d9a7','API_CONNECTORS',5,100,200.0);

INSERT INTO public."FeatureType" (id,"name") VALUES
	 ('e1d17777-df94-4576-a405-e74ac842a6f7','BOOLEAN'),
	 ('58e1ee3c-36a9-40e7-964c-5c531ccf6dea','LIMIT'),
	 ('521341ee-865d-4965-afde-a4d417d36e38','RANGE'),
	 ('cf01cfb7-a739-4345-925a-47f01e23af21','QUOTAS'),
	 ('1fd8d2bc-0e57-475a-a93f-e25c6d467e99','SET'),
	 ('8d815cb6-541c-4a95-88f4-51fc92772b4f','EXTENSION');

INSERT INTO public."OndemandQuotaType" (id,"name","cost") VALUES
	 ('8b77140b-80b7-4bbd-aaa6-cbf088f31ef9','USERS',20.0),
	 ('bed33273-5060-4abc-93b6-defe094784c2','PAGEVIEWS',2.0),
	 ('a77ddf4d-bcbd-4e05-8184-ed364cc103ea','API_CONNECTORS',10.0);

INSERT INTO public."Package" (id,package_id,"name",is_free) VALUES
	 ('a05f7dec-fddb-4673-b5d9-ce41c2fc7177','46e587b9-f130-4c5a-aeed-c6c6901f8386','free_trial',true),
	 ('8866f0a4-c6a4-4016-8a39-e886d534c47d','97c75079-0625-4872-94e3-85cfa355c8e5','premium',false),
	 ('614b388b-227c-479a-9e8c-f30a33ed83ff','aa2b556f-3ba8-4892-bfd0-4ff0a74d0f33','standard',false);

INSERT INTO public."PlanType" (id,"name","level",description) VALUES
	 ('bd104bc4-7958-4f0a-a825-5e1d18da3191','iMOC','SITE',NULL),
	 ('d4329392-3fd7-4f7d-ae4b-189f37a97505','dMOC','MO',NULL),
	 ('3feb80eb-1de3-42c7-a538-7d79462b44de','MOC','MO',NULL),
	 ('45b2f268-8094-405d-9113-2c9193b71c20','sMOC','MO',NULL),
	 ('013e8a1d-c93e-413a-8e5b-9fda87fe5352','cMOC','MO',NULL),
	 ('f815f343-08ad-4901-8d86-e6270a9a4349','BETA_MO','MO','Beta Plan for Media Owner'),
	 ('597ad646-2849-46b3-99a0-c1e59f6af063','BETA_SITE','SITE','Beta Plan for Site');

INSERT INTO public."FeatureSet" (id,feature_set_id,"name",type_id) VALUES
	 ('371a0ea7-c1b7-4303-a868-932a3c364b74','fc95d1a0-5f76-4367-ae90-fcf85010a6cb','SERVICE_CATALOG','1fd8d2bc-0e57-475a-a93f-e25c6d467e99'),
	 ('61c9fe50-4516-41df-a2a8-f0319441c26a','6422b395-bbfb-4915-8cc7-66225deeda92','UPTIME_MONITORS','58e1ee3c-36a9-40e7-964c-5c531ccf6dea'),
	 ('b3e17517-e224-4d4e-9bca-bb80f3b62a28','15a238c0-1f9a-4ed1-97a5-b4d96981013f','WEBSITE_HEALTH','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('9544c96d-a445-406d-988d-6dea0d59e581','6c9b5245-d320-42d1-a1c2-6ca5e00b0004','UPTIME_POLL_FREQUENCY','1fd8d2bc-0e57-475a-a93f-e25c6d467e99'),
	 ('9dda62fe-e73b-47f7-b992-3376ba177703','9d063564-eb69-4270-ae77-9e7c474092b9','UPTIME_USERS','58e1ee3c-36a9-40e7-964c-5c531ccf6dea'),
	 ('1eb617b0-c0a4-4495-ae60-d134b09c19ff','1a49b72d-f624-4035-83c9-615934c373c4','ANALYTICS_REPORTS','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('c09f6cc0-51f7-4d85-a025-d7ca8ad5fda9','829097aa-cf87-4837-a6ed-15fd71293d44','ANALYTICS_HISTORICAL_DATA','58e1ee3c-36a9-40e7-964c-5c531ccf6dea'),
	 ('d85762c7-7bdd-4cb8-b195-1ffb8e69248d','a06687fb-45ec-4466-be74-f4ab82fb26e7','SUPPORTED_DATA_SOURCES','1fd8d2bc-0e57-475a-a93f-e25c6d467e99'),
	 ('11c1dccb-6e69-4b5d-928f-188ac41c4522','bc698e86-d8c2-4dd1-adbb-8845358b12d4','API_CONNECTORS','58e1ee3c-36a9-40e7-964c-5c531ccf6dea'),
	 ('172bd3b2-4f8a-427e-9278-216aecbc67b4','e73060df-7b5a-4b7d-8c2f-c604b61c758a','SYNC_DAY_FREQUENCY','58e1ee3c-36a9-40e7-964c-5c531ccf6dea');
INSERT INTO public."FeatureSet" (id,feature_set_id,"name",type_id) VALUES
	 ('5ffd029e-4ddc-4e36-b48c-655bd56c083b','46649448-cd17-4879-a623-b21ddab7a542','SECURITY_AND_GOVERNANCE','1fd8d2bc-0e57-475a-a93f-e25c6d467e99'),
	 ('94cfa955-cdea-4ec8-a10c-2eaca5188838','65d49518-2ce6-4efb-bf7b-13e11093d940','DISPLAY_PROMO_MESSAGE','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('48c0ee20-0afb-4f40-8f6c-9876aae267da','fd8d42e7-bd7f-4fd2-90a9-8dcbd3ef627a','UPTIME_MONITORS_GRAPH','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('8d334aaa-cfa4-48e4-b650-1ea4222e6604','8ec736e2-2291-473c-8501-5ec18223a126','UPTIME_MONITORS_SMS','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('ceb0e776-032f-457b-ac28-7d2bbee76e68','134bd0f7-ffdc-4210-9fd9-798448f86e70','MONITORING_AND_ALERTING','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('de08a69e-e237-4d4f-b613-5ff6f6e3a1eb','631c0248-3c50-471f-965e-c47110723f07','PARTNER_CENTER','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('8f2bf5c6-1a64-401b-a63e-48c1159dedcb','17219e5e-15cd-4dfb-a6aa-9f9c13046540','PARTNER_DIRECTORY','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('a9c44798-883a-4f0b-bb68-2733f64ab4e3','88571adf-0821-484d-b14d-867549cce6fa','OVERVIEW_METRICS','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('6277ae77-c67d-4aa1-b188-e0b5385d6a11','5f8baf9a-1b1c-41ea-9edd-c0ccfd8b787a','PERFORMANCE_METRICS','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('cb80bd6a-3912-4d22-aab2-3b233beac918','f4603f1e-4fa8-4ffc-9cdb-5dd4049a1c20','EXTENSION','8d815cb6-541c-4a95-88f4-51fc92772b4f');
INSERT INTO public."FeatureSet" (id,feature_set_id,"name",type_id) VALUES
	 ('142c1ee9-c129-47f1-aed0-48493ab05c29','cbe17392-df6c-4cd9-bc42-4555d55ce329','VULNERABILITIES_SCAN','e1d17777-df94-4576-a405-e74ac842a6f7'),
	 ('c008ea93-feed-4419-911c-d312e919e921','a7e61902-7d6b-4c03-a9af-49d00087542b','VULNERABILITIES_EXPORT','e1d17777-df94-4576-a405-e74ac842a6f7');


INSERT INTO public."Feature" (id,feature_id,"name",target,feature_set_id,"cost",multiplier,beta) VALUES
	 ('74f0b5e6-0789-4339-857f-6c55c23f659d','86635834-a196-490a-a117-99b76e7e7492','DISPLAY_PROMO_MESSAGE_SCALE','{1}','94cfa955-cdea-4ec8-a10c-2eaca5188838',0.0,1,false),
	 ('d77f646c-d4fb-4365-ba6b-1cede22917e4','dccb05d9-2a2f-463b-9da0-8c0dec32e374','AD_REVENUE_REPORT','{1}','1eb617b0-c0a4-4495-ae60-d134b09c19ff',0.0,1,false),
	 ('6cbb0f4c-0534-4d55-a493-93be90573e7a','bba86955-6e37-4614-95da-da0b91f4b519','AUDIENCE_REPORT','{1}','1eb617b0-c0a4-4495-ae60-d134b09c19ff',0.0,1,false),
	 ('eb549c5a-e881-451d-8be7-725d8a166baa','759bbb67-b997-4f4b-8070-69f7cffac973','MONITORING_AND_ALERTING_PAGE','{1}','ceb0e776-032f-457b-ac28-7d2bbee76e68',0.0,1,false),
	 ('c581d4be-edd3-49f4-acb3-78fad9b17608','5d9ff7bd-2958-4abd-a0f5-275bbdf2812c','PARTNER_DIRECTORY_PAGE','{1}','8f2bf5c6-1a64-401b-a63e-48c1159dedcb',0.0,1,false),
	 ('5d2bfb8e-7cf1-431c-9b84-74664badc3c0','7619a467-fb83-404f-9866-59023d637d89','PERFORMANCE_PAGE','{1}','6277ae77-c67d-4aa1-b188-e0b5385d6a11',0.0,1,false),
	 ('e20e8a8a-5054-4a9a-9480-5ef8b00bc49d','cac53880-8e13-4260-a2c7-6d9f0ed344f0','UPTIME_MONITORS_FREE','{2}','61c9fe50-4516-41df-a2a8-f0319441c26a',0.0,1,false),
	 ('f7a20386-5bd1-4cf5-92d4-5f7522913be3','a7b3d355-9fb0-4548-8425-d07944c8b9c4','PARTNER_CENTER_PAGE','{1}','de08a69e-e237-4d4f-b613-5ff6f6e3a1eb',0.0,1,false),
	 ('313dfe9b-8fdf-4463-8bdd-0ca824106f34','e8beb0fe-81fc-4494-af48-9723659e12ce','API_CONNECTORS_SCALE','{5}','11c1dccb-6e69-4b5d-928f-188ac41c4522',0.0,1,false),
	 ('d5af8ff0-3e6f-4923-93d4-fec13d50a926','75bffb98-13e2-49cc-9381-d618089675cf','API_CONNECTORS_FREE','{2}','11c1dccb-6e69-4b5d-928f-188ac41c4522',0.0,1,false);
INSERT INTO public."Feature" (id,feature_id,"name",target,feature_set_id,"cost",multiplier,beta) VALUES
	 ('399e6292-a997-4820-acea-cc42e754aca6','82d3085c-71fc-4276-9232-6ef1c7a35a53','SERVICE_CATALOG_BASIC','{PA,Izooto,Dynatrace,MouseFlow,SocialFlow,SourcePoint,Serpstat}','371a0ea7-c1b7-4303-a868-932a3c364b74',0.0,1,false),
	 ('960acd50-98ce-4b68-ba0c-41c7eb9568b3','80a1d37b-31f4-48d8-ba8d-836cd00789fe','SERVICE_CATALOG_SCALE','{PA,Izooto,Dynatrace,MouseFlow,SocialFlow,SourcePoint,Serpstat}','371a0ea7-c1b7-4303-a868-932a3c364b74',0.0,1,false),
	 ('ce761732-7e67-4e8c-8837-f4b4b8c476bb','1848ce3d-b0c4-4847-afb2-b8f5089de114','UPTIME_USERS_GLOBAL','{2}','9dda62fe-e73b-47f7-b992-3376ba177703',0.0,1,false),
	 ('06cdc471-27d8-466c-afa3-0417c0736b0b','1d2c9f9e-1a96-4c58-98fe-0e3240dbdd09','UPTIME_MONITORS_SMS_GLOBAL','{1}','8d334aaa-cfa4-48e4-b650-1ea4222e6604',0.0,1,false),
	 ('dd444756-ce01-42b2-8add-17b6625e4a8c','113eb355-6ed4-423a-843e-736c7e4cc9d4','DISPLAY_PROMO_MESSAGE_STARTER','{1}','94cfa955-cdea-4ec8-a10c-2eaca5188838',0.0,1,false),
	 ('98c3a7d8-ce72-4519-b8db-0ed4c24d1629','46459130-ce75-497b-8a1e-35722c2faf62','DISPLAY_PROMO_MESSAGE_FREE','{1}','94cfa955-cdea-4ec8-a10c-2eaca5188838',0.0,1,false),
	 ('5fae3939-a7e0-4648-a7c7-9dfb9ec41f46','37b3e8aa-7e96-465c-ba6b-56872ce0bf6b','SERVICE_CATALOG_FREE','{""}','371a0ea7-c1b7-4303-a868-932a3c364b74',0.0,1,false),
	 ('b3b41610-6f56-42b8-8803-dc8e72965462','4dd6c972-53f6-4bf0-a3cb-b59575515490','UPTIME_POLL_FREQUENCY_FREE','{10,15}','9544c96d-a445-406d-988d-6dea0d59e581',0.0,1,false),
	 ('533a6ef1-616a-443a-8b3d-b31343e6821b','da626a65-cd98-4613-a873-0ae28b0bd711','UPTIME_POLL_FREQUENCY_BASIC','{10,15}','9544c96d-a445-406d-988d-6dea0d59e581',0.0,1,false),
	 ('27bc90a5-d1a4-488e-9496-ddeba0349cc4','ba653250-d8a5-47dc-96d2-85c73ed29ffc','UPTIME_POLL_FREQUENCY_SCALE','{10,15}','9544c96d-a445-406d-988d-6dea0d59e581',0.0,1,false);
INSERT INTO public."Feature" (id,feature_id,"name",target,feature_set_id,"cost",multiplier,beta) VALUES
	 ('90abd025-7030-46f6-8b3f-0d24d8de5fe4','0234df0e-104d-423b-a148-966ca392e2d6','OVERVIEW_PAGE_IMOC','{1}','a9c44798-883a-4f0b-bb68-2733f64ab4e3',0.0,1,false),
	 ('90abd025-7131-46f6-8b3f-0d24d8de5fe4','0234df0e-114d-423b-a148-966ca392e2d6','OVERVIEW_PAGE_DMOC','{1}','a9c44798-883a-4f0b-bb68-2733f64ab4e3',0.0,1,false),
	 ('e41994f1-8139-41ee-9797-8238b7662b23','aebdba2f-f6f1-4f0f-a479-70b2249e1378','UPTIME_MONITORS_BASIC','{2}','61c9fe50-4516-41df-a2a8-f0319441c26a',0.0,1,false),
	 ('4e5b5265-0c26-45d5-ad73-11b5bb7d5b93','3682ae05-0677-4c4a-a345-7c32f95be96b','UPTIME_MONITORS_SCALE','{2}','61c9fe50-4516-41df-a2a8-f0319441c26a',0.0,1,false),
	 ('6287d6a1-4dd6-462f-af56-1034c5feeb2f','a8d63b9c-4620-4f1a-9509-b18cb4654a8e','COLLECT_DATA','{30}','cb80bd6a-3912-4d22-aab2-3b233beac918',0.0,1,false),
	 ('098663ad-e4f5-4956-af00-f8ddc227f417','91f7edae-3460-46f7-a3f9-2318ac3c2c8f','STORE_DATA','{90}','cb80bd6a-3912-4d22-aab2-3b233beac918',0.0,1,false),
	 ('eda17139-fc48-4b0b-b7e6-1a2ab8a47513','b35ad961-a151-4bd2-9f53-9084baf2fcab','VULNERABILITIES_EXPORT','{1}','c008ea93-feed-4419-911c-d312e919e921',0.0,1,true),
	 ('919f66d8-2955-4bb4-838e-2cad1341deb5','bab94ef0-8315-4520-8eca-d4e84cc8d338','VULNERABILITIES_SCAN','{1}','142c1ee9-c129-47f1-aed0-48493ab05c29',0.0,1,true),
	 ('f7a20386-5bd1-4cf5-92d4-5f7522913be1','a7b3d355-9fb0-4548-8425-d07944c8b9c5','PARTNER_CENTER_PAGE_EXTENSION','{3650}','cb80bd6a-3912-4d22-aab2-3b233beac918',0.0,1,false);

INSERT INTO public."Plan" (id,plan_id,"name",description,custom,type_id,package_id) VALUES
	 ('ae21d6d4-865a-4bf0-9390-dd1b645d197a','6d5ef5cd-d38f-4b84-8a91-2ef7e9b1dbb0','Media Owners Cloud BETA_SITE BASIC','Beta Plan for Site BASIC',false,'597ad646-2849-46b3-99a0-c1e59f6af063','614b388b-227c-479a-9e8c-f30a33ed83ff'),
	 ('785a1864-28d3-4c37-8599-048570b1ce9a','67d9814d-608c-4c6f-8352-17d538f5997b','Media Owners Cloud BETA_MO SCALE','Beta Plan for Media Owner SCALE',false,'f815f343-08ad-4901-8d86-e6270a9a4349','8866f0a4-c6a4-4016-8a39-e886d534c47d'),
	 ('836f67a2-ea87-49df-860d-468d6a24cd67','91b8aa15-3831-4756-931f-75d23cd70cde','Media Owners Cloud BETA_SITE SCALE','Beta Plan for Site SCALE',false,'597ad646-2849-46b3-99a0-c1e59f6af063','8866f0a4-c6a4-4016-8a39-e886d534c47d'),
	 ('829967a2-ab76-49aa-a1a6-3dd400225d06','8c73c1e7-4811-4ce8-acac-ade4baa1c5bb','Media Owners Cloud iMOC BASIC','Media Owners Cloud iMOC BASIC plan description',false,'bd104bc4-7958-4f0a-a825-5e1d18da3191','614b388b-227c-479a-9e8c-f30a33ed83ff'),
	 ('8960aeef-67a3-4b3b-807a-1f643440de2e','b46c4b14-c40e-4082-a76f-3a3d8b060c68','Media Owners Cloud dMOC SCALE','Media Owners Cloud dMOC SCALE plan description',false,'d4329392-3fd7-4f7d-ae4b-189f37a97505','8866f0a4-c6a4-4016-8a39-e886d534c47d'),
	 ('0d4d4715-505b-4fef-92ea-ea899ddb45fa','12c882b1-c8e8-4aa2-a572-a86f90b32c8f','Media Owners Cloud dMOC FREE','Media Owners Cloud dMOC FREE plan description',false,'d4329392-3fd7-4f7d-ae4b-189f37a97505','a05f7dec-fddb-4673-b5d9-ce41c2fc7177'),
	 ('149f0c58-68ef-4562-8f6c-748153a7e0b0','4d14ac18-4d3b-414f-bf27-6c5ffd2b5655','Media Owners Cloud dMOC BASIC','Media Owners Cloud dMOC BASIC plan description',false,'d4329392-3fd7-4f7d-ae4b-189f37a97505','614b388b-227c-479a-9e8c-f30a33ed83ff'),
	 ('55d22ef4-1ee3-465c-bcc6-89430e798283','7bc11c7f-9256-4f71-b46e-1d29ac7df763','Media Owners Cloud iMOC SCALE','Media Owners Cloud iMOC SCALE plan description',false,'bd104bc4-7958-4f0a-a825-5e1d18da3191','8866f0a4-c6a4-4016-8a39-e886d534c47d'),
	 ('a40ad30e-7d33-4bd5-afae-b70e0f45fb08','445d4dd9-84b9-47bf-9b7f-194c18322b94','Media Owners Cloud iMOC FREE','Media Owners Cloud iMOC FREE plan description',false,'bd104bc4-7958-4f0a-a825-5e1d18da3191','a05f7dec-fddb-4673-b5d9-ce41c2fc7177'),
	 ('829967a2-ab76-49aa-a1a6-3dd400225d10','8c73c1e7-4811-4ce8-acac-ade4baa1c5aa','Media Owners Cloud MOC BASIC','Media Owners Cloud MOC BASIC plan description',false,'3feb80eb-1de3-42c7-a538-7d79462b44de','614b388b-227c-479a-9e8c-f30a33ed83ff');
INSERT INTO public."Plan" (id,plan_id,"name",description,custom,type_id,package_id) VALUES
	 ('8960aeef-67a3-4b3b-807a-1f643440de11','b46c4b14-c40e-4082-a76f-3a3d8b060c88','Media Owners Cloud MOC SCALE','Media Owners Cloud MOC SCALE plan description',false,'3feb80eb-1de3-42c7-a538-7d79462b44de','8866f0a4-c6a4-4016-8a39-e886d534c47d'),
	 ('0d4d4715-505b-4fef-92ea-ea899ddb45ff','12c882b1-c8e8-4aa2-a572-a86f90b32c88','Media Owners Cloud MOC FREE','Media Owners Cloud MOC FREE plan description',false,'3feb80eb-1de3-42c7-a538-7d79462b44de','a05f7dec-fddb-4673-b5d9-ce41c2fc7177'),
	 ('f57978ef-f4c5-4132-9f76-2905bb834f64','f466dda3-bd18-4fa4-9eff-546ff1317a6e','Media Owners Cloud sMOC FREE','Data Storage Retention Policy FREE',false,'45b2f268-8094-405d-9113-2c9193b71c20','a05f7dec-fddb-4673-b5d9-ce41c2fc7177'),
	 ('6aa9c516-cbc7-4a40-b13b-c7699ac87d1f','2fea7f19-1a20-4cca-81be-8e67e624f1cb','Media Owners Cloud cMOC FREE','Data Collection Retention Policy FREE',false,'013e8a1d-c93e-413a-8e5b-9fda87fe5352','a05f7dec-fddb-4673-b5d9-ce41c2fc7177'),
	 ('11dc4797-4484-4b5c-a793-f56c7cf30158','3778cb43-2ab8-416f-993d-026425cee040','Media Owners Cloud sMOC BASIC','Data Storage Retention Policy BASIC',false,'45b2f268-8094-405d-9113-2c9193b71c20','614b388b-227c-479a-9e8c-f30a33ed83ff'),
	 ('e6fdff82-9d2f-4fb6-9167-0f5686d4e37f','59e4df9f-056e-4adb-8953-f024fcafa60a','Media Owners Cloud cMOC BASIC','Data Collection Retention Policy BASIC',false,'013e8a1d-c93e-413a-8e5b-9fda87fe5352','614b388b-227c-479a-9e8c-f30a33ed83ff'),
	 ('b2b43fd5-fcb4-47fd-abe4-41011c25f3f7','00a155f9-5456-4155-8989-8bc12455bc00','Media Owners Cloud sMOC SCALE','Data Storage Retention Policy SCALE',false,'45b2f268-8094-405d-9113-2c9193b71c20','8866f0a4-c6a4-4016-8a39-e886d534c47d'),
	 ('89cc67da-6e11-4add-8429-a61905495936','037fc001-88a6-48b4-adfa-49df18573531','Media Owners Cloud cMOC SCALE','Data Collection Retention Policy SCALE',false,'013e8a1d-c93e-413a-8e5b-9fda87fe5352','8866f0a4-c6a4-4016-8a39-e886d534c47d'),
	 ('c683735b-cb2f-4031-8122-7abe9d2f7dd5','5f83d50e-44d9-4349-8d92-6262d40b377a','Media Owners Cloud BETA_MO FREE','Beta Plan for Media Owner FREE',false,'f815f343-08ad-4901-8d86-e6270a9a4349','a05f7dec-fddb-4673-b5d9-ce41c2fc7177'),
	 ('b62d6bc8-6aa2-472c-882b-5116d02cb232','e2178954-09a2-41a2-8dff-0e6bb0f89c90','Media Owners Cloud BETA_SITE FREE','Beta Plan for Site FREE',false,'597ad646-2849-46b3-99a0-c1e59f6af063','a05f7dec-fddb-4673-b5d9-ce41c2fc7177');
INSERT INTO public."Plan" (id,plan_id,"name",description,custom,type_id,package_id) VALUES
	 ('d352efd9-905c-4658-a65b-b215e547745b','fa2c54bf-e370-42e4-b4bf-518323e25ff0','Media Owners Cloud BETA_MO BASIC','Beta Plan for Media Owner BASIC',false,'f815f343-08ad-4901-8d86-e6270a9a4349','614b388b-227c-479a-9e8c-f30a33ed83ff');


INSERT INTO public."PlanFeature" (id,feature_id,plan_id) VALUES
	 ('3a28fd1e-c871-4892-8fee-82da9b4c65d2','d77f646c-d4fb-4365-ba6b-1cede22917e4','8960aeef-67a3-4b3b-807a-1f643440de2e'),
	 ('16c953cd-a3c9-4a79-83f0-f0e86b73c970','6cbb0f4c-0534-4d55-a493-93be90573e7a','8960aeef-67a3-4b3b-807a-1f643440de2e'),
	 ('9b754195-e874-42a2-b189-754ce8803b88','d77f646c-d4fb-4365-ba6b-1cede22917e4','0d4d4715-505b-4fef-92ea-ea899ddb45fa'),
	 ('f2fdc2af-41b1-49ff-8e91-cb26120893ac','6cbb0f4c-0534-4d55-a493-93be90573e7a','0d4d4715-505b-4fef-92ea-ea899ddb45fa'),
	 ('057f57e4-75bf-4427-99b7-2062f42c264d','313dfe9b-8fdf-4463-8bdd-0ca824106f34','8960aeef-67a3-4b3b-807a-1f643440de2e'),
	 ('0d206f60-f846-41c4-a707-1c0109ca6556','d5af8ff0-3e6f-4923-93d4-fec13d50a926','0d4d4715-505b-4fef-92ea-ea899ddb45fa'),
	 ('c15fb83b-4f2e-4e7d-bd5f-f837e16f06ed','399e6292-a997-4820-acea-cc42e754aca6','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('83762616-9f5e-40ac-a4df-fc163c6235f7','5fae3939-a7e0-4648-a7c7-9dfb9ec41f46','a40ad30e-7d33-4bd5-afae-b70e0f45fb08'),
	 ('6de4d5b4-4d30-437d-ae7e-726f640ede1d','90abd025-7030-46f6-8b3f-0d24d8de5fe4','a40ad30e-7d33-4bd5-afae-b70e0f45fb08'),
	 ('b5716adf-bd48-4e4b-82ea-80679f8a3769','eb549c5a-e881-451d-8be7-725d8a166baa','a40ad30e-7d33-4bd5-afae-b70e0f45fb08');

INSERT INTO public."PlanFeature" (id,feature_id,plan_id) VALUES
	 ('87d1bd38-0679-4133-bf1d-c9305b2ea00c','c581d4be-edd3-49f4-acb3-78fad9b17608','a40ad30e-7d33-4bd5-afae-b70e0f45fb08'),
	 ('8e1f618b-176f-4f38-a052-2aafe0585126','5d2bfb8e-7cf1-431c-9b84-74664badc3c0','a40ad30e-7d33-4bd5-afae-b70e0f45fb08'),
	 ('1ac5aa81-e60d-4109-b646-fa61af982c66','e20e8a8a-5054-4a9a-9480-5ef8b00bc49d','a40ad30e-7d33-4bd5-afae-b70e0f45fb08'),
	 ('895cdabd-8657-4056-bff0-88288e25afdc','90abd025-7030-46f6-8b3f-0d24d8de5fe4','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('a079745f-1d29-4de9-be86-81cddf00cf2c','eb549c5a-e881-451d-8be7-725d8a166baa','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('48ac1215-3c49-415f-92db-d108945889a3','c581d4be-edd3-49f4-acb3-78fad9b17608','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('29e0ddff-3637-4bd7-b7e3-286450005c2a','5d2bfb8e-7cf1-431c-9b84-74664badc3c0','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('5bb446b9-291e-4eef-8071-24e01aabfd0e','4e5b5265-0c26-45d5-ad73-11b5bb7d5b93','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('57aa6c68-9cef-45cf-8b08-e6177787b220','960acd50-98ce-4b68-ba0c-41c7eb9568b3','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('51f44eb9-0a2e-4bae-a6f7-ab7895da9b93','90abd025-7030-46f6-8b3f-0d24d8de5fe4','829967a2-ab76-49aa-a1a6-3dd400225d06');

INSERT INTO public."PlanFeature" (id,feature_id,plan_id) VALUES
	 ('0d09ab96-22ff-4030-8a16-ef225bc590eb','eb549c5a-e881-451d-8be7-725d8a166baa','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('394ca905-e6ab-4066-85c1-7727c1da5372','c581d4be-edd3-49f4-acb3-78fad9b17608','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('ba39227e-b0fa-43f9-8c5e-adf162a1d63b','5d2bfb8e-7cf1-431c-9b84-74664badc3c0','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('b6ef6ff7-c5f5-42ab-b16e-103b7c78098d','e41994f1-8139-41ee-9797-8238b7662b23','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('63e4cf20-a44e-4183-9469-032fff27388d','ce761732-7e67-4e8c-8837-f4b4b8c476bb','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('216c07c9-7a8f-40ba-9729-eb00d066b27e','06cdc471-27d8-466c-afa3-0417c0736b0b','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('685d4585-4d80-4d8d-96d1-bfd2b316ec78','ce761732-7e67-4e8c-8837-f4b4b8c476bb','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('ac47ee07-b66e-4291-8f8c-6892e89c7093','06cdc471-27d8-466c-afa3-0417c0736b0b','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('719ad8ad-c367-4c12-90d8-b179143f5583','ce761732-7e67-4e8c-8837-f4b4b8c476bb','a40ad30e-7d33-4bd5-afae-b70e0f45fb08'),
	 ('fc8b5535-5688-4569-b044-ff6880136031','06cdc471-27d8-466c-afa3-0417c0736b0b','a40ad30e-7d33-4bd5-afae-b70e0f45fb08');
INSERT INTO public."PlanFeature" (id,feature_id,plan_id) VALUES
	 ('4639791f-29fc-47ff-b0d6-d80aa918dbe1','98c3a7d8-ce72-4519-b8db-0ed4c24d1629','a40ad30e-7d33-4bd5-afae-b70e0f45fb08'),
	 ('df3962b8-26db-46cc-9592-3b01f75fe65c','74f0b5e6-0789-4339-857f-6c55c23f659d','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('4cc4fde0-fadf-4267-8804-b89489649adc','dd444756-ce01-42b2-8add-17b6625e4a8c','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('4cc4fde0-fadf-3367-8804-b89489649adc','27bc90a5-d1a4-488e-9496-ddeba0349cc4','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('4cc4fde0-fadf-1167-8804-b89489649adc','b3b41610-6f56-42b8-8803-dc8e72965462','a40ad30e-7d33-4bd5-afae-b70e0f45fb08'),
	 ('4cc4fde0-fadf-2267-8804-b89489649adc','533a6ef1-616a-443a-8b3d-b31343e6821b','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('16c953cd-a3c9-4a79-83f1-f0e86b73c971','90abd025-7131-46f6-8b3f-0d24d8de5fe4','0d4d4715-505b-4fef-92ea-ea899ddb45fa'),
	 ('16c953cd-a3c9-4a79-83f2-f0e86b73c972','90abd025-7131-46f6-8b3f-0d24d8de5fe4','149f0c58-68ef-4562-8f6c-748153a7e0b0'),
	 ('16c953cd-a3c9-4a79-83f3-f0e86b73c973','90abd025-7131-46f6-8b3f-0d24d8de5fe4','8960aeef-67a3-4b3b-807a-1f643440de2e'),
	 ('34177740-8a2c-4f9b-89ce-96ccb9a2802d','919f66d8-2955-4bb4-838e-2cad1341deb5','a40ad30e-7d33-4bd5-afae-b70e0f45fb08');
INSERT INTO public."PlanFeature" (id,feature_id,plan_id) VALUES
	 ('0cbe5830-1446-441c-ac82-30b85abbc7e0','919f66d8-2955-4bb4-838e-2cad1341deb5','829967a2-ab76-49aa-a1a6-3dd400225d06'),
	 ('fd8546fa-f5f8-4127-a37b-6191c7bfdb22','eda17139-fc48-4b0b-b7e6-1a2ab8a47513','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('d6d7cc64-2c87-40b9-9f0f-74dd153b6c2f','919f66d8-2955-4bb4-838e-2cad1341deb5','55d22ef4-1ee3-465c-bcc6-89430e798283'),
	 ('16c953cd-a3c9-4a79-83f0-f0e86b73c971','f7a20386-5bd1-4cf5-92d4-5f7522913be1','0d4d4715-505b-4fef-92ea-ea899ddb45ff'),
	 ('16c953cd-a3c9-4a79-83f0-f0e86b73c972','f7a20386-5bd1-4cf5-92d4-5f7522913be1','829967a2-ab76-49aa-a1a6-3dd400225d10'),
	 ('16c953cd-a3c9-4a79-83f0-f0e86b73c963','f7a20386-5bd1-4cf5-92d4-5f7522913be1','8960aeef-67a3-4b3b-807a-1f643440de11'),
	 ('70eefecc-ed1b-442c-8fed-05599525b27d','eda17139-fc48-4b0b-b7e6-1a2ab8a47513','a40ad30e-7d33-4bd5-afae-b70e0f45fb08'),
	 ('5bf58785-9fb0-4ecd-8be6-22d47ac307e0','f7a20386-5bd1-4cf5-92d4-5f7522913be3','0d4d4715-505b-4fef-92ea-ea899ddb45ff'),
	 ('f6ad865a-d1d8-4b02-bc15-caad42f46d9f','f7a20386-5bd1-4cf5-92d4-5f7522913be3','829967a2-ab76-49aa-a1a6-3dd400225d10'),
	 ('fd68d475-77d7-452d-bb87-3722a74f7e44','f7a20386-5bd1-4cf5-92d4-5f7522913be3','8960aeef-67a3-4b3b-807a-1f643440de11');
INSERT INTO public."PlanFeature" (id,feature_id,plan_id) VALUES
	 ('e63c3dd3-49b3-4d25-9e42-db3f806cff7c','098663ad-e4f5-4956-af00-f8ddc227f417','f57978ef-f4c5-4132-9f76-2905bb834f64'),
	 ('2b4f0891-76c0-403d-ba01-329c956ecf30','6287d6a1-4dd6-462f-af56-1034c5feeb2f','6aa9c516-cbc7-4a40-b13b-c7699ac87d1f'),
	 ('46ccb925-9fb1-4292-a0da-d8c7002a89ae','098663ad-e4f5-4956-af00-f8ddc227f417','11dc4797-4484-4b5c-a793-f56c7cf30158'),
	 ('0dd24a1b-3c49-48e0-b7b9-157f209006e4','6287d6a1-4dd6-462f-af56-1034c5feeb2f','e6fdff82-9d2f-4fb6-9167-0f5686d4e37f'),
	 ('b63a240e-1fc1-4d04-84d3-0024d02c364a','098663ad-e4f5-4956-af00-f8ddc227f417','b2b43fd5-fcb4-47fd-abe4-41011c25f3f7'),
	 ('e9be1e68-7efd-4129-9b9b-f2a7ead0c287','6287d6a1-4dd6-462f-af56-1034c5feeb2f','89cc67da-6e11-4add-8429-a61905495936');



-- Completed on 2024-07-02 12:27:36 EEST

--
-- PostgreSQL database dump complete
--

