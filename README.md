<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="_PetStore_API_Tests_0"></a>🧪 PetStore API Tests</h1>
<p class="has-line-data" data-line-start="2" data-line-end="4">Автоматизированное тестирование публичного REST API <strong>Swagger PetStore</strong><br>
с использованием <strong>Pytest</strong>, <strong>Requests</strong> и <strong>Allure</strong>.</p>
<hr>
<h2 class="code-line" data-line-start=7 data-line-end=8 ><a id="___7"></a>🎯 Цель проекта</h2>
<ul>
<li class="has-line-data" data-line-start="8" data-line-end="9">Проверить корректность CRUD-операций для сущностей <strong>User</strong>, <strong>Pet</strong> и <strong>Store</strong>.</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">Продемонстрировать использование фикстур, параметризации и клиентской обёртки над API.</li>
<li class="has-line-data" data-line-start="10" data-line-end="12">Настроить отчётность через <strong>Allure</strong> и параллельное выполнение тестов.</li>
</ul>
<hr>
<h2 class="code-line" data-line-start=14 data-line-end=15 ><a id="___14"></a>⚙️ Стек технологий</h2>
<ul>
<li class="has-line-data" data-line-start="15" data-line-end="16"><strong>Python 3.11+</strong></li>
<li class="has-line-data" data-line-start="16" data-line-end="17"><strong>Pytest</strong></li>
<li class="has-line-data" data-line-start="17" data-line-end="18"><strong>Requests</strong></li>
<li class="has-line-data" data-line-start="18" data-line-end="19"><strong>Allure-Pytest</strong></li>
<li class="has-line-data" data-line-start="19" data-line-end="20"><strong>pytest-xdist</strong> (параллельный запуск)</li>
<li class="has-line-data" data-line-start="20" data-line-end="21"><strong>pytest-rerunfailures</strong> (повтор неустойчивых тестов)</li>
<li class="has-line-data" data-line-start="21" data-line-end="23"><strong>Makefile</strong> (управление командами)</li>
</ul>
<hr>
<h2 class="code-line" data-line-start=25 data-line-end=26 ><a id="___25"></a>📁 Структура проекта</h2>
<p class="has-line-data" data-line-start="26" data-line-end="44">PetStoreProject/<br>
│<br>
├── tests/                          - Каталог с тестами<br>
│   ├── test_user_crud.py           - Тесты CRUD для пользователей<br>
│   ├── test_store_order.py         - Тесты заказов<br>
│   ├── test_store_inventory.py     - Тесты инвентаря<br>
│   ├── test_pet_crud.py            - CRUD-тесты питомцев<br>
│   └── test_pet_find_and_upload.py - Загрузка и поиск питомцев<br>
│<br>
├── utils/<br>
│   └── api_client.py               - Клиент для работы с API<br>
│<br>
├── pytest.ini                      - Конфигурация Pytest<br>
├── ./conftest.py                     - Общие фикстуры<br>
├── requirements.txt                - Зависимости<br>
├── Makefile                        - Команды для запуска<br>
├── .gitignore                      - Игнорируемые файлы<br>
└── ./README.md                       - Документация</p>
<hr>
<h2 class="code-line" data-line-start=47 data-line-end=48 ><a id="___47"></a>✅ Покрытие тестов</h2>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Модуль</th>
<th>Проверяемые сценарии</th>
<th>Типы кейсов</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Pet</strong></td>
<td>Создание, чтение, обновление, удаление, загрузка фото</td>
<td>Валидные и невалидные CRUD</td>
</tr>
<tr>
<td><strong>User</strong></td>
<td>Создание, чтение, обновление, удаление, логин/логаут</td>
<td>Валидные и невалидные данные</td>
</tr>
<tr>
<td><strong>Store</strong></td>
<td>Создание заказа, удаление, проверка инвентаря</td>
<td>Валидные и невалидные ID</td>
</tr>
</tbody>
</table>
<p class="has-line-data" data-line-start="55" data-line-end="57"><strong>Всего тестов:</strong> 27<br>
<strong>Из них:</strong></p>
<ul>
<li class="has-line-data" data-line-start="57" data-line-end="58">✅ Валидные сценарии — 17</li>
<li class="has-line-data" data-line-start="58" data-line-end="60">⚠️ Невалидные сценарии — 10</li>
</ul>
<hr>
<h2 class="code-line" data-line-start=62 data-line-end=63 ><a id="___62"></a>🧩 Используемые подходы</h2>
<h3 class="code-line" data-line-start=64 data-line-end=65 ><a id="_Fixture_64"></a>🔹 Fixture</h3>
<p class="has-line-data" data-line-start="65" data-line-end="66">Используются для:</p>
<ul>
<li class="has-line-data" data-line-start="66" data-line-end="67">создания и удаления тестовых пользователей, питомцев и заказов;</li>
<li class="has-line-data" data-line-start="67" data-line-end="68">подготовки данных перед выполнением тестов;</li>
<li class="has-line-data" data-line-start="68" data-line-end="69">повторных GET-запросов с ожиданием результата (<code>get_with_retry</code>);</li>
<li class="has-line-data" data-line-start="69" data-line-end="71">автоматической очистки ресурсов после тестов (<code>cleanup</code>).</li>
</ul>
<h3 class="code-line" data-line-start=71 data-line-end=72 ><a id="_Parametrize_71"></a>🔹 Parametrize</h3>
<p class="has-line-data" data-line-start="72" data-line-end="73">Применяется для:</p>
<ul>
<li class="has-line-data" data-line-start="73" data-line-end="74">тестирования разных комбинаций входных данных (например, <code>userStatus</code>, <code>petStatus</code>, <code>orderId</code>);</li>
<li class="has-line-data" data-line-start="74" data-line-end="75">проверки API с валидными и невалидными параметрами;</li>
<li class="has-line-data" data-line-start="75" data-line-end="77">сокращения однотипных тестов и увеличения покрытия.</li>
</ul>
<p class="has-line-data" data-line-start="77" data-line-end="78">💡 Такой подход делает код <strong>гибким, читаемым и поддерживаемым</strong> — при добавлении новых сценариев достаточно расширить параметры, не дублируя тесты.</p>
<hr>
<h2 class="code-line" data-line-start=81 data-line-end=82 ><a id="______81"></a>🚀 Установка и запуск проекта (локально)</h2>
<blockquote>
<p class="has-line-data" data-line-start="83" data-line-end="84">Требования: <strong>Python 3.11+</strong>, установленный <strong>Allure CLI</strong></p>
</blockquote>
<h3 class="code-line" data-line-start=85 data-line-end=86 ><a id="1_____85"></a>1️⃣ Перейдите в корень проекта</h3>
<p class="has-line-data" data-line-start="86" data-line-end="87">Убедитесь, что находитесь там, где лежат <code>pytest.ini</code>, <code>requirements.txt</code>, <code>Makefile</code>.</p>
<h3 class="code-line" data-line-start=88 data-line-end=89 ><a id="2____88"></a>2️⃣ Создайте виртуальное окружение</h3>
<p class="has-line-data" data-line-start="89" data-line-end="92"><strong>macOS / Linux</strong><br>
python3 -m venv .venv<br>
source .venv/bin/activate</p>
<p class="has-line-data" data-line-start="93" data-line-end="96"><strong>Windows</strong><br>
python -m venv .venv<br>
..venv\Scripts\Activate.ps1</p>
<h3 class="code-line" data-line-start=97 data-line-end=98 ><a id="2___97"></a>2️⃣ Установите зависимости</h3>
<p class="has-line-data" data-line-start="98" data-line-end="99"><strong>pip install -r requirements.txt</strong></p>
<h3 class="code-line" data-line-start=100 data-line-end=101 ><a id="3___100"></a>3️⃣ Запуск тестов</h3>
<p class="has-line-data" data-line-start="101" data-line-end="104"><strong>pytest -v</strong><br>
или параллельно:<br>
<strong>pytest -v -n auto</strong></p>
<h3 class="code-line" data-line-start=105 data-line-end=106 ><a id="4___Allure_105"></a>4️⃣ Генерация отчёта Allure</h3>
<p class="has-line-data" data-line-start="106" data-line-end="108"><strong>pytest --alluredir=allure-results</strong><br>
<strong>allure serve allure-results</strong></p>
<p class="has-line-data" data-line-start="109" data-line-end="112">Если allure не найден:<br>
•   macOS → <strong>brew install allure</strong><br>
•   Windows → <strong>choco install allure или scoop install allure</strong></p>
<hr>
<h2 class="code-line" data-line-start=115 data-line-end=116 ><a id="__115"></a>📊 Отчётность</h2>
<p class="has-line-data" data-line-start="116" data-line-end="117">После выполнения тестов можно открыть отчёт: <strong>allure serve allure-results</strong></p>
<p class="has-line-data" data-line-start="118" data-line-end="123">Allure формирует интерактивный отчёт с вкладками:<br>
•   <strong>Suites</strong> — тестовые наборы по файлам<br>
•   <strong>Behaviors</strong> — группировка по фичам (@allure.feature, @allure.story)<br>
•   <strong>Graphs / Timeline</strong> — графики успешности и времени выполнения<br>
•   <strong>Attachments</strong> — JSON-ответы, логи и статус-коды</p>
<p class="has-line-data" data-line-start="124" data-line-end="128">Отчёт включает:<br>
•   Статистику выполнения тестов<br>
•   Список успешных и упавших тестов<br>
•   Детали запросов и ответов (JSON, статус-коды, время выполнения)</p>
<p class="has-line-data" data-line-start="129" data-line-end="130">Для чистого отчёта каждый запуск автоматически очищает предыдущие результаты: <strong>make report</strong></p>
<hr>
<h2 class="code-line" data-line-start=133 data-line-end=134 ><a id="__Makefile_133"></a>🧠 Команды Makefile</h2>
<p class="has-line-data" data-line-start="134" data-line-end="139"><strong>make smoke</strong>       - Запуск smoke-тестов с меткой MARK=smoke и формирование отчёта<br>
<strong>make regression</strong>  - Запуск регрессионных тестов с меткой MARK=regression<br>
<strong>make report</strong>      - Полный прогон: очистка, запуск тестов, генерация Allure-отчёта и его открытие<br>
<strong>make clean</strong>       - Удаление временных директорий allure-results и allure-report<br>
<strong>make open-report</strong> - Открытие уже сгенерированного Allure-отчёта без повторного запуска тестов</p>
<hr>
<h2 class="code-line" data-line-start=142 data-line-end=143 ><a id="__142"></a>👩‍💻 Автор</h2>
<p class="has-line-data" data-line-start="143" data-line-end="146">Сулейменова Ирина<br>
QA Engineer | Python | API &amp; Web Testing<br>
📫 GitHub: iwtzmn</p>
