import os
import random
import time
from datetime import datetime
from time import sleep

import requests
from google.cloud import firestore

expected_site_names = ["24h.com.cy", "balla.com.cy", "stylista.com.cy"]
expected_mo_plan = {
    "cost": 0.0,
    "discount": 0.0,
    "media_owner_id": "nikodea-eqkmy",
    "mo_plan_id": None,
    "packages": [
        {
            "expiration_date": "2032-12-31",
            "is_free": True,
            "package_id": "46e587b9-f130-4c5a-aeed-c6c6901f8386",
            "package_name": "free_trial",
            "subscriptions": [
                {
                    "active": True,
                    "expiration_date": "2032-12-31",
                    "level": "SITE",
                    "pageviews": 0,
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "site_id": "24hcomcy-e7rjr",
                    "type": "iMOC",
                },
                {
                    "active": True,
                    "expiration_date": "2032-12-31",
                    "level": "SITE",
                    "pageviews": 0,
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "site_id": "24hcomcy-e7rjr",
                    "type": "BETA_SITE",
                },
                {
                    "active": True,
                    "expiration_date": "2032-12-31",
                    "level": "SITE",
                    "pageviews": 0,
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "site_id": "ballacomcy-4wrmj",
                    "type": "iMOC",
                },
                {
                    "active": True,
                    "expiration_date": "2032-12-31",
                    "level": "SITE",
                    "pageviews": 0,
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "site_id": "ballacomcy-4wrmj",
                    "type": "BETA_SITE",
                },
                {
                    "active": True,
                    "expiration_date": "2032-12-31",
                    "level": "SITE",
                    "pageviews": 0,
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "site_id": "stylistacomcy-c2g1y",
                    "type": "iMOC",
                },
                {
                    "active": True,
                    "expiration_date": "2032-12-31",
                    "level": "SITE",
                    "pageviews": 0,
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "site_id": "stylistacomcy-c2g1y",
                    "type": "BETA_SITE",
                },
                {
                    "active": True,
                    "expiration_date": "2042-12-29",
                    "level": "MO",
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "type": "MOC",
                },
                {
                    "active": True,
                    "expiration_date": "2032-12-31",
                    "level": "MO",
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "type": "BETA_MO",
                },
                {
                    "active": True,
                    "expiration_date": "2033-01-30",
                    "level": "MO",
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "type": "cMOC",
                },
                {
                    "active": True,
                    "expiration_date": "2033-03-31",
                    "level": "MO",
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "type": "sMOC",
                },
                {
                    "active": True,
                    "expiration_date": "2032-12-31",
                    "level": "MO",
                    "payment_date": datetime.now().strftime("%Y-%m-%d"),
                    "type": "dMOC",
                },
            ],
        }
    ],
    "updated_at": None,
}

expected_products = [
    {
        "et_data_received": False,
        "id": "c1428634-989e-4d40-ba0b-27825ea65007",
        "media_owner_id": "nikodea-5pi5n",
        "name": "nikodea-5pi5n_24hcomcy-cgfvz",
        "pa_domain_id": 1765,
        "serving_method": "SITE",
        "site_id": "24hcomcy-cgfvz",
        "site_tag": '<script async src="https://moc-sitetags-dev.projectagora.info/sites/24hcomcy-cgfvz/tags/pamoc_loader"></script>',
        "sitetag_domain": "https://moc-sitetags-dev.projectagora.info",
        "status": "ACTIVATED",
    },
    {
        "et_data_received": False,
        "id": "2a821619-6e1e-42bf-9f0d-51efcd7449ec",
        "media_owner_id": "nikodea-5pi5n",
        "name": "nikodea-5pi5n_ballacomcy-f6757",
        "pa_domain_id": 1766,
        "serving_method": "SITE",
        "site_id": "ballacomcy-f6757",
        "site_tag": '<script async src="https://moc-sitetags-dev.projectagora.info/sites/ballacomcy-f6757/tags/pamoc_loader"></script>',
        "sitetag_domain": "https://moc-sitetags-dev.projectagora.info",
        "status": "ACTIVATED",
    },
    {
        "et_data_received": False,
        "id": "742ea2c7-4dbb-4be6-852e-874861ae9e5c",
        "media_owner_id": "nikodea-5pi5n",
        "name": "nikodea-5pi5n_stylistacomcy-9x5mx",
        "pa_domain_id": 1767,
        "serving_method": "SITE",
        "site_id": "stylistacomcy-9x5mx",
        "site_tag": '<script async src="https://moc-sitetags-dev.projectagora.info/sites/stylistacomcy-9x5mx/tags/pamoc_loader"></script>',
        "sitetag_domain": "https://moc-sitetags-dev.projectagora.info",
        "status": "ACTIVATED",
    },
]

expected_firestore_docs = {
    "_24hcomcy-7t9y0": {
        "_0.1": {
            "built_time": 1720537457123,
            "event_tracker_url": "https%3A%2F%2Fevent-tracker-library.mediaownerscloud.com%2Fmain%2F1.0.4%2Fpa_et.min.js",
            "integrations": [{"tag": "", "service": "infra_service"}],
            "core_api_version": "0.0.40",
            "canary_probability": 0,
            "status": "STABLE",
            "event_tracker_version": "1.0.4",
        },
        'serving_method': 'SITE',
        "product_active": True,
    },
    "_ballacomcy-5qanh": {
        "_0.1": {
            "built_time": 1720537457404,
            "event_tracker_url": "https%3A%2F%2Fevent-tracker-library.mediaownerscloud.com%2Fmain%2F1.0.4%2Fpa_et.min.js",
            "integrations": [{"tag": "", "service": "infra_service"}],
            "core_api_version": "0.0.40",
            "canary_probability": 0,
            "status": "STABLE",
            "event_tracker_version": "1.0.4",
        },
        'serving_method': 'SITE',
        "product_active": True,
    },
    "_stylistacomcy-2v2x3": {
        "_0.1": {
            "built_time": 1720537457641,
            "event_tracker_url": "https%3A%2F%2Fevent-tracker-library.mediaownerscloud.com%2Fmain%2F1.0.4%2Fpa_et.min.js",
            "integrations": [{"tag": "", "service": "infra_service"}],
            "core_api_version": "0.0.40",
            "canary_probability": 0,
            "status": "STABLE",
            "event_tracker_version": "1.0.4",
        },
        'serving_method': 'SITE',
        "product_active": True,
    },
}

expected_bucket_object = {
    "kind": "storage#objects",
    "items": [
        {
            "kind": "storage#object",
            "name": "sitetags/MOC_24hcomcy-e9b3x/0.1/site-tag.min.js",
            "id": "prj-p-moc-a2c2-sitetags-emulator/sitetags/MOC_24hcomcy-e9b3x/0.1/site-tag.min.js",
            "bucket": "prj-p-moc-a2c2-sitetags-emulator",
            "size": "1283",
            "contentType": "application/javascript",
            "crc32c": "aeD1ew==",
            "acl": [
                {
                    "bucket": "prj-p-moc-a2c2-sitetags-emulator",
                    "entity": "projectOwner-test-project",
                    "etag": "RVRhZw==",
                    "kind": "storage#objectAccessControl",
                    "object": "sitetags/MOC_24hcomcy-e9b3x/0.1/site-tag.min.js",
                    "projectTeam": {},
                    "role": "OWNER",
                }
            ],
            "md5Hash": "2O950JlV1SxMCxFfQ5YjrA==",
            "etag": "2O950JlV1SxMCxFfQ5YjrA==",
            "storageClass": "STANDARD",
            "timeCreated": "2024-07-09T15:45:26.461597Z",
            "timeStorageClassUpdated": "2024-07-09T15:45:26.461601Z",
            "updated": "2024-07-09T15:45:26.461601Z",
            "generation": "1720539926461601",
            "selfLink": "https://0.0.0.0:4443/storage/v1/b/prj-p-moc-a2c2-sitetags-emulator/o/sitetags%2FMOC_24hcomcy-e9b3x%2F0.1%2Fsite-tag.min.js",
            "mediaLink": "https://0.0.0.0:4443/download/storage/v1/b/prj-p-moc-a2c2-sitetags-emulator/o/sitetags%2FMOC_24hcomcy-e9b3x%2F0.1%2Fsite-tag.min.js?alt=media",
            "metageneration": "1",
        }
    ],
}
# Point to the Firestore emulator
os.environ["FIRESTORE_EMULATOR_HOST"] = "firestore-emulator:8080"
# Specify your project ID here
project_id = "your-project-id"
# Initialize Firestore client
db = firestore.Client(project=project_id)


def read_bucket_objects(site_ids):
    base_url = "http://gcs_storage_proxy:5050"
    bucket_name = "prj-p-moc-a2c2-sitetags-emulator"
    # Construct the URL for listing objects with the folder_name as a prefix
    bucket_objects = {}
    for site_id, site_name in site_ids:
        url = f"{base_url}/storage/v1/b/{bucket_name}/o?prefix=sitetags/MOC_{site_id}"

        # Make the GET request
        response = requests.get(
            url, verify=False
        )  # verify=False may be necessary if using self-signed SSL certificates

        # Parse the response to check if any objects exist with the specified prefix
        if response.status_code == 200:
            data = response.json()
            if "items" in data and len(data["items"]) > 0:
                # print(f"Folder {data}")
                bucket_objects.update({site_id: data})
            else:
                print(f"Folder does not exist in bucket '{bucket_name}'.")
                return False
        else:
            print(
                f"Failed to check folder. Status code: {response.status_code}, Message: {response.text}"
            )
            return False
    return bucket_objects


def read_site_tag_configuration():
    # for site_id, site_name in site_ids:
    # # Reference to the collection
    site_tag_config_ref = db.collection("site_tag_configuration")
    #     print(f'site_tag_dict: {site_tag_dict}', flush=True)
    # Fetch all documents in the collection
    docs = site_tag_config_ref.stream()
    docs_dicts = {}
    # Iterate through the documents and print them (or process as needed)
    for doc in docs:
        # print(f"{doc.id} => {doc.to_dict()}", flush=True)
        docs_dicts.update({doc.id: doc.to_dict()})
    return docs_dicts


def get_mo_by_mo_id_from_sfm(media_owner_id: str) -> (int, dict):
    res = requests.get(f'http://web_gateway/v1.0/media-owners/{media_owner_id}')
    if res.status_code == 200:
        return res.status_code, res.json()
    else:
        return res.status_code, None


def get_mo_id(publisher_id):
    response = requests.get(
        f"http://web_gateway/v1.0/media-owners?publisher_id={publisher_id}"
    )
    # try catch json
    try:
        return response.json()[0]["media_owner_id"]
    except ValueError:  # catches JSON decoding errors
        print("Failed to decode JSON from response", flush=True)
        return False


def get_mo_plan_id(mo_id):
    response = requests.get(f"http://web_gateway/v1.0/media-owners/{mo_id}/mo-plans")
    # try catch json
    try:
        return response.json()[0]["mo_plan_id"]
    except ValueError:  # catches JSON decoding errors
        print("Failed to decode JSON from response", flush=True)
        return False


def get_mo_plan(mo_id):
    response = requests.get(f"http://web_gateway/v1.0/media-owners/{mo_id}/mo-plans")
    # try catch json
    try:
        return response.json()[0]
    except ValueError:  # catches JSON decoding errors
        print("Failed to decode JSON from response", flush=True)
        return False


def delete_mo_plan(mo_id, mo_plan_id):
    response = requests.delete(
        f"http://web_gateway/v1.0/media-owners/{mo_id}/mo-plans/{mo_plan_id}"
    )
    return response.status_code


def delete_mo(mo_id):
    response = requests.delete(f"http://web_gateway/v1.0/media-owners/{mo_id}")
    return response.status_code


def get_sites(mo_id):
    response = requests.get(f"http://web_gateway/v1.0/media-owners/{mo_id}/sites")
    # try catch json
    try:
        return [(site["site_id"], site["name"]) for site in response.json()]
    except ValueError:  # catches JSON decoding errors
        print("Failed to decode JSON from response", flush=True)
        return False


def get_products(mo_id):
    response = requests.get(f"http://web_gateway/v1.0/media-owners/{mo_id}/products")
    # try catch json
    try:
        return response.json()
    except ValueError:  # catches JSON decoding errors
        print("Failed to decode JSON from response", flush=True)
        return False


def delete_site(mo_id, site_id):
    response = requests.delete(
        f"http://web_gateway/v1.0/media-owners/{mo_id}/sites/{site_id}"
    )
    return response.status_code


def add_site(mo_id):
    site = {
        "domain": "testaro.gr",
        "name": "testaro",
        "pa_domain_id": 2,
        "site_id": "site_id_testaro",
    }
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    response = requests.post(
        f"http://web_gateway/v1.0/media-owners/{mo_id}/sites",
        headers=headers,
        json=site,
    )
    return response.status_code


def mo_migrate(publisher_id, dry_run=False):
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    response = requests.post(
        "http://web_gateway/v1.0/media-owners/migrate",
        headers=headers,
        json={"publisher_id": str(publisher_id), "dry_run": dry_run},
    )
    print("end of MO MIGRATE", flush=True)
    return response.status_code


def prepare_expected_mo_plan(mo_plan, site_ids):
    expected_mo_plan["updated_at"] = mo_plan["updated_at"]
    expected_mo_plan["mo_plan_id"] = mo_plan["mo_plan_id"]
    expected_mo_plan["media_owner_id"] = mo_plan["media_owner_id"]
    for index, subscription in enumerate(
            expected_mo_plan["packages"][0]["subscriptions"]
    ):
        for site_id, site_name in site_ids:
            if "site_id" in subscription:
                if subscription["site_id"].split("-")[0] == site_id.split("-")[0]:
                    expected_mo_plan["packages"][0]["subscriptions"][index][
                        "site_id"
                    ] = site_id
    return expected_mo_plan


def prepare_expected_products(products, site_ids):
    for index, product in enumerate(products):
        for site_id, site_name in site_ids:
            if expected_products[index]["site_id"].split("-")[0] == site_id.split("-")[0]:
                expected_products[index]["site_id"] = site_id
                expected_products[index][
                    "name"
                ] = f"{product['media_owner_id']}_{site_id}"
                expected_products[index][
                    "site_tag"
                ] = f'<script async src="https://moc-sitetags-dev.projectagora.info/sites/{site_id}/tags/pamoc_loader"></script>'
        for index, expected_product in enumerate(expected_products):
            if expected_product["site_id"].split("-")[0] == product["site_id"].split("-")[0]:
                expected_products[index]["id"] = product["id"]
                expected_products[index]["media_owner_id"] = product["media_owner_id"]
    return expected_products


def assert_nodes():
    mo_id = get_mo_id(6)
    site_ids = get_sites(mo_id)
    print(f"assert_nodes site_ids:{site_ids}", flush=True)
    for site_id, site_name in site_ids:
        assert (
                site_name in expected_site_names
        ), f"Expected site name {site_name} not found"
    mo_plan = get_mo_plan(mo_id)
    exp_mo_plan = prepare_expected_mo_plan(mo_plan, site_ids)
    assert mo_plan == exp_mo_plan, f"Expected mo_plan {exp_mo_plan} not found"
    time.sleep(5)
    print("assert_nodes WAKE UP from sleep", flush=True)
    products = get_products(mo_id)
    print(f"products:{products}", flush=True)
    exp_products = prepare_expected_products(products, site_ids)
    assert sorted(products, key=lambda x: x['id']) == sorted(exp_products, key=lambda x: x['id']), f"Expected products {exp_products} not found"
    firestore_docs = read_site_tag_configuration()
    print(f"firestore_docs:{firestore_docs}", flush=True)
    bucket_objects = read_bucket_objects(site_ids)
    print(f"bucket_objects:{bucket_objects}", flush=True)
    for site_id, site_name in site_ids:
        assert (
                f"_{site_id}" in firestore_docs
        ), f"Expected firestore doc {site_id} not found"
        expected_firestore_docs["_24hcomcy-7t9y0"]["_0.1"]["built_time"] = (
            firestore_docs[f"_{site_id}"]["_0.1"]["built_time"]
        )
        print(f"expected_firestore_docs:{expected_firestore_docs}", flush=True)
        assert (
                firestore_docs[f"_{site_id}"] == expected_firestore_docs["_24hcomcy-7t9y0"]
        ), f"firestore doc {site_id} not equal to expected value"
        assert (
                site_id in bucket_objects
        ), f"Expected bucket object {site_id} not found"
        assert (
                bucket_objects[site_id]["items"][0]["name"]
                == f"sitetags/MOC_{site_id}/0.1/site-tag.min.js"
        ), f"Expected bucket object {site_id} not found"
        assert (
                bucket_objects[site_id]["items"][0]["id"]
                == f"prj-p-moc-a2c2-sitetags-emulator/sitetags/MOC_{site_id}/0.1/site-tag.min.js"
        ), f"Expected bucket object {site_id} not found"
        assert (
                bucket_objects[site_id]["items"][0]["acl"][0]["object"]
                == f"sitetags/MOC_{site_id}/0.1/site-tag.min.js"
        ), f"Expected bucket object {site_id} not found"
        print(f"site_id, site_name:{site_id}, {site_name}", flush=True)

def test_no_mo_exist_migrate():
    print("TEST1: test_no_mo_exist_migrate", flush=True)

    mo_id = get_mo_id(6)
    print(f"TEST1: mo_id={mo_id}", flush=True)
    if mo_id:
        mo_pla_id = get_mo_plan_id(mo_id)
        if mo_pla_id:
            delete_mo_plan(mo_id, mo_pla_id)
        delete_mo(mo_id)
    print("TEST1: start of mo migrate", flush=True)    
    status_code = mo_migrate(6, dry_run=False)
    print("TEST1: end of  mo migrate", flush=True)
    assert status_code == 201, f"Expected status code 201, got {status_code}"
    assert_nodes()


def test_mo_exist_no_sites_migrate():
    print("TEST2: test_mo_exist_no_sites_migrate", flush=True)
    mo_id = get_mo_id(6)
    if mo_id:
        site_ids = get_sites(mo_id)
        if site_ids:
            for site_id, site_name in site_ids:
                status_code = delete_site(mo_id, site_id)
                print(status_code, flush=True)
    status_code = mo_migrate(6, dry_run=False)
    assert status_code == 201, f"Expected status code 201, got {status_code}"
    assert_nodes()


def test_mo_exist_one_more_site_migrate():
    print("TEST3: test_mo_exist_one_more_site_migrate", flush=True)
    mo_id = get_mo_id(6)
    if mo_id:
        add_site(mo_id)
    status_code = mo_migrate(6, dry_run=False)
    assert status_code == 201, f"Expected status code 201, got {status_code}"
    assert_nodes()


def create_mo(mo_id: str, mo_name: str, pa_id: int) -> (int, dict):
    new_mo = {
        "media_owner_id": mo_id,
        "name": mo_name,
        "sites": [],
        "company_details": {
            "name": 'company_name',
            "type": "Company",
            "vat_registration_office": "1423424234",
            "registration_number": "1423424234",
            "country": "Greece",
            "address": "14o xlm E.O. Athinon - Lamias, 14564, Kifisia",
            "city": "Athens",
            "zip_code": "12345",
        },
        "contact_details": {
            "first_name": "Sofia",
            "last_name": "Kontopyraki",
            "email": "s.kontopyraki@dpg.gr",
            "phone": "+306947435188",
        },
        "currency": "EUR",
        "pa_id": pa_id,
    }
    response = requests.post(f"http://web_gateway/v1.0/media-owners", json=new_mo)
    if response.status_code == 201:
        return response.status_code, response.json()
    else:
        return response.status_code, None


def create_a_new_site(mo_id: str, site_domain: str, site_name: str, site_pa_domain_id: int, site_id: str) -> (int, dict):
    new_site = {
        "domain": site_domain,
        "name": site_name,
        "pa_domain_id": site_pa_domain_id,
        "site_id": site_id,
    }
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    response = requests.post(
        f"http://web_gateway/v1.0/media-owners/{mo_id}/sites",
        headers=headers,
        json=new_site,
    )
    if response.status_code == 201:
        return response.status_code, response.json()
    else:
        return response.status_code, None


def create_a_new_mo_plan(mo_id, site_id) -> (int, dict):
    new_mo_plan = {
        "cost": 0.0,
        "discount": 0.0,
        "media_owner_id": mo_id,
        # "mo_plan_id": None,
        "packages": [
            {
                "expiration_date": "2032-12-31",
                "is_free": True,
                "package_id": "46e587b9-f130-4c5a-aeed-c6c6901f8386",
                "package_name": "free_trial",
                "subscriptions": [
                    {
                        "active": True,
                        "expiration_date": "2032-12-31",
                        "level": "SITE",
                        "pageviews": 0,
                        "payment_date": datetime.now().strftime("%Y-%m-%d"),
                        "site_id": site_id,
                        "type": "iMOC",
                    },
                    {
                        "active": True,
                        "expiration_date": "2032-12-31",
                        "level": "SITE",
                        "pageviews": 0,
                        "payment_date": datetime.now().strftime("%Y-%m-%d"),
                        "site_id": site_id,
                        "type": "BETA_SITE",
                    },
                    {
                        "active": True,
                        "expiration_date": "2042-12-29",
                        "level": "MO",
                        "payment_date": datetime.now().strftime("%Y-%m-%d"),
                        "type": "MOC",
                    },
                    {
                        "active": True,
                        "expiration_date": "2032-12-31",
                        "level": "MO",
                        "payment_date": datetime.now().strftime("%Y-%m-%d"),
                        "type": "BETA_MO",
                    },
                    {
                        "active": True,
                        "expiration_date": "2033-01-30",
                        "level": "MO",
                        "payment_date": datetime.now().strftime("%Y-%m-%d"),
                        "type": "cMOC",
                    },
                    {
                        "active": True,
                        "expiration_date": "2033-03-31",
                        "level": "MO",
                        "payment_date": datetime.now().strftime("%Y-%m-%d"),
                        "type": "sMOC",
                    },
                    {
                        "active": True,
                        "expiration_date": "2032-12-31",
                        "level": "MO",
                        "payment_date": datetime.now().strftime("%Y-%m-%d"),
                        "type": "dMOC",
                    },
                ],
            }
        ],
        "updated_at": None,
    }
    res = requests.post(f'http://web_gateway/v1.0/media-owners/{mo_id}/mo-plans', json=new_mo_plan)
    if res.status_code == 201:
        return res.status_code, res.json()
    else:
        return res.status_code, None


def test_create_a_new_media_owner():
    print("TEST4: test_create_a_new_media_owner", flush=True)
    new_mo_id = f'media_owner_id_{str(random.randint(0, 1000))}'
    new_mo_name = f'media_owner_name_{str(random.randint(0, 1000))}'
    new_mo_pa_id = random.randint(0, 1000)
    status_code, mo = get_mo_by_mo_id_from_sfm(media_owner_id=new_mo_id)
    assert status_code != 200
    assert mo is None
    print(f'Media owner with id:{new_mo_id} actually does not exist initially', flush=True)
    status_code, mo = create_mo(mo_id=new_mo_id, mo_name=new_mo_name, pa_id=new_mo_pa_id)
    assert status_code == 201
    assert mo is not None
    print(f'Media owner with id:{new_mo_id} was created', flush=True)
    status_code, mo = get_mo_by_mo_id_from_sfm(media_owner_id=new_mo_id)
    assert status_code == 200
    assert mo is not None
    print(f'Media owner with id:{new_mo_id} now actually exists in the database', flush=True)

    # Add a site
    site_domain = f'site_domain_{str(random.randint(0, 1000))}'
    site_name = f'site_name_{str(random.randint(0, 1000))}'
    site_pa_domain_id = random.randint(0, 1000)
    site_id = f'site_id_{str(random.randint(0, 1000))}'
    status_code, _site = create_a_new_site(mo_id=new_mo_id, site_domain=site_domain, site_name=site_name, site_pa_domain_id=site_pa_domain_id, site_id=site_id)
    assert status_code == 201
    assert _site is not None
    print(f'Added a site with id:{site_id} to MO:{new_mo_id}', flush=True)
    status_code, mo = get_mo_by_mo_id_from_sfm(media_owner_id=new_mo_id)
    assert status_code == 200
    assert len(mo['sites']) == 1
    assert mo['sites'][0]['site_id'] == site_id
    print(f'Site with id:{site_id} actually exists in the DB', flush=True)

    # Create a MO-Plan for MO
    get_products_response = get_products(mo_id=new_mo_id)
    assert get_products_response is False
    print(f'Media Owner:{new_mo_id} does not currently have a Product', flush=True)
    status_code, mo_plan = create_a_new_mo_plan(mo_id=new_mo_id, site_id=site_id)
    assert status_code == 201
    assert mo_plan is not None
    print(f'Created a Mo-Plan for MO:{new_mo_id}', flush=True)
    time.sleep(30)

    # check if SM created a product
    get_products_response = get_products(mo_id=new_mo_id)
    assert get_products_response is not False
    print(f'{get_products_response=}', flush=True)
    assert isinstance(get_products_response, list)
    assert len(get_products_response) == 1
    print(f'Media Owner:{new_mo_id} now has a Product', flush=True)


if __name__ == "__main__":
    print("TESTS STARTED", flush=True)
    test_no_mo_exist_migrate()
    test_mo_exist_no_sites_migrate()
    test_mo_exist_one_more_site_migrate()
    test_create_a_new_media_owner()
    print("FINISHED", flush=True)
    sleep(5)
