import logging
import pytest
import allure
from conftest import get_with_retry, attach_json


# На публичном Petstore POST /pet/{petId} через form-data не принимает частичные обновления (только name или только status)
# и стабильно отдаёт 405/400, а не 200.

@pytest.mark.regression
@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize(
    "new_name,new_status",
    [
        pytest.param("Nora", "pending", id="name+status"),
    ],
)
@allure.feature("Pet")
@allure.story("Update pet via form-data (parametrized)")
def test_pet_update_via_form(api_client, unique_pet_id, make_pet, new_name, new_status, cleanup):
    logging.info(f"[UPDATE-FORM] START pet_id={unique_pet_id}")
    with allure.step("Создать питомца для form-data обновления"):
        make_pet(unique_pet_id, status="available", name="Chaya")

        # добавляем элемент в cleanup
        cleanup["pet"].append(unique_pet_id)

    kwargs = {}
    if new_name is not None:
        kwargs["name"] = new_name
    if new_status is not None:
        kwargs["status"] = new_status

    with allure.step("Выполнить form-data обновление питомца"):
        resp = api_client.update_pet_form(unique_pet_id, **kwargs)
        attach_json("Request kwargs", kwargs)
        if resp.status_code == 200:
            attach_json("Response", resp.json())

    # Публичный PetStore флаки на form-data update:
    # 200 = всё ок, обновил
    # 400 / 405 = "я не принял форму" (часто так отвечает, но питомец может при этом всё равно обновиться)
    # 404 = PetStore говорит "нет такого питомца", хотя мы его только что создали — это жёсткий флейк
    allowed = {200, 400, 405}

    # Если вернулся 404 — это тот случай, где дальше проверять уже нечего.
    if resp.status_code == 404:
        with allure.step("PetStore вернул 404 на form-data update (флейк эндпойнта)"):
            pytest.xfail(
                f"PetStore form-data update returned 404 for pet_id={unique_pet_id}"
            )

    # Любой другой неожиданный код (например 500) — это уже реальный баг, пусть падает.
    assert resp.status_code in allowed, (
        f"Неожиданный код при обновлении через form-data: {resp.status_code}"
    )

    logging.info(f"[UPDATE-FORM] sent: {kwargs}, got={resp.status_code}")

    # Раньше мы сразу делали xfail при любом !=200.
    # Теперь НЕ делаем xfail на 400/405 — пробуем проверить через GET, возможно апдейт применился.

    with allure.step("Проверить обновление питомца через GET"):
        resp = get_with_retry(api_client, unique_pet_id, field="status", expected=new_status)
        attach_json("GET response", resp.json())

        # Если даже после retry PetStore не отдаёт питомца — это уже критично.
        assert resp.status_code == 200, "PetStore не вернул питомца после form-data update"

        pet = resp.json()
        logging.info(f"[UPDATE-FORM] got: name={pet.get('name')}, status={pet.get('status')}")

        assert pet.get("status") == new_status
        assert pet.get("name") in {new_name, "Chaya"}

    logging.info("[UPDATE-FORM] DONE")


@pytest.mark.regression
@pytest.mark.flaky(reruns=2, reruns_delay=1)
@allure.feature("Pet")
@allure.story("Upload pet image")
def test_pet_upload_image(api_client, unique_pet_id, make_pet, temp_image_file, cleanup):
    logging.info(f"[UPLOAD] START pet_id={unique_pet_id}")
    with allure.step("Создать питомца перед загрузкой изображения"):
        make_pet(unique_pet_id, status="available", name="Gosha")

        # добавляем элемент в cleanup
        cleanup["pet"].append(unique_pet_id)

    with allure.step("Загрузить изображение питомца через POST /pet/{id}/uploadImage"):
        resp = api_client.upload_pet_image(unique_pet_id, temp_image_file)
        attach_json("Upload response", resp.json())
    assert resp.status_code == 200, "Ошибка при загрузке изображения"
    msg = (resp.json().get("message") or "").lower()
    logging.info(f"[UPLOAD] response: {msg}")
    assert ("test metadata" in msg) or (str(unique_pet_id) in msg) or ("uploaded" in msg)

    logging.info("[UPLOAD] DONE")
