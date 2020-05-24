_en_
## Wazuh and TheHive integration
This project integrates SIEM Wazuh and TheHive. Use the following instructions to configure:
 
```sh
$ cd /opt/
$ sudo git clone https://github.com/crow1011/wazuh2thehive.git
$ sudo /var/ossec/framework/python/bin/pip3 install -r /opt/wazuh2thehive/requirements.txt
$ sudo cp /opt/wazuh2thehive/custom-w2thive.py /var/ossec/integrations/custom-w2thive.py
$ sudo cp /opt/wazuh2thehive/custom-w2thive /var/ossec/integrations/custom-w2thive
$ sudo chmod 755 /var/ossec/integrations/custom-w2thive.py
$ sudo chmod 755 /var/ossec/integrations/custom-w2thive
$ sudo chown root:ossec /var/ossec/integrations/custom-w2thive.py
$ sudo chown root:ossec /var/ossec/integrations/custom-w2thive
$ sudo nano /var/ossec/etc/ossec.conf
```
insert the following snippet into the ossec_config block:
```xml
<integration>
    <name>custom-w2thive</name>
    <hook_url>http://localhost:9000</hook_url>
    <api_key>123456790</api_key>
    <alert_format>json</alert_format>
</integration>
```
lines description:

**name** - integration name(no need to change)

**hook_url** - TheHive host

**api\_key** - TheHive user's API key. You can generate the key on the user management page by logging in as administrator. For security, allow the api-user to create only an alert.

**alert\_format** - format that wazuh sends alert to the integrator(no need to change)

after configuration, apply the changes with this command:
```sh
/var/ossec/bin/ossec-control restart
```
Finally, check the /var/ossec/log/integrations.log file for errors. If there is not enough information from the errors, you can enable debug_mode by changing the line in the file custom-w2thive.py 
```python
debug_enabled = False
```
to 
```python
debug_enabled = True
```
If you receive too many events, you can set a severity threshold for events that will be send to TheHive. Set the value of the lvl_threshold variable in the file /var/ossec/integrations/custom-w2thive.py
```python
lvl_threshold = 0
```
Events with a severity level equal to or greater will be sent to TheHive. You can read more about event classification in Wazuh here: [wazuh-rules-classification](https://documentation.wazuh.com/3.12/user-manual/ruleset/rules-classification.html)

Vadim M.

_ru_
## Wazuh and TheHive integration
Этот проект интегрирует SIEM Wazuh и TheHive. Для настройки воспользуйтесь следующими инструкциями:
 
```sh
$ cd /opt/
$ sudo git clone https://github.com/crow1011/wazuh2thehive.git
$ sudo /var/ossec/bin/python/pip3 install -r /opt/wazuh2thehive/requirements.txt
$ sudo cp /opt/wazuh2thehive/custom-w2thive.py /var/ossec/integration/custom-w2thive.py
$ sudo cp /opt/wazuh2thehive/custom-w2thive /var/ossec/integration/custom-w2thive
$ sudo chmod 755 /var/ossec/integration/custom-w2thive.py
$ sudo chmod 755 /var/ossec/integration/custom-w2thive
$ sudo chown root:ossec /var/ossec/integration/custom-w2thive.py
$ sudo chown root:ossec /var/ossec/integration/custom-w2thive
$ sudo nano /var/ossec/etc/ossec.conf
```
вставьте в блок ossec_config следующий фрагмент:
```xml
<integration>
    <name>custom-w2thive</name>
    <hook_url>http://localhost:9000</hook_url>
    <api_key>123456790</api_key>
    <alert_format>json</alert_format>
</integration>
```
где:

**name** - название интегратора(не нужно изменять)

**hook_url** - адрес TheHive

**api\_key** - API ключ TheHive пользователя. Сгенериоровать ключ можно на странице управления пользователями, авторизовавшись от администратора. Для безопасности разрешите api-пользователю только создание alert.

**alert\_format** - формат, в котором wazuh передает в интегратор alert(не нужно изменять)

после настройки примените изменения командой:
```sh
/var/ossec/bin/ossec_control restart
```
В конце проверьте файл /var/ossec/log/integrations.log на присутствие ошибок. Если информации из ошибки недостаточно, вы можете включить debug_mode, поменяв в файле custom-w2thive.py строчку
```python
debug_enabled = False
```
на 
```python
debug_enabled = True
```
Если вы получаете слишком много событий, вы можете задать порог критичности отправляемых в TheHive событий. Для того чтобы его установить этот порог, задайте значение переменной lvl_threshold в файле /var/ossec/integrations/custom-w2thive.py
```python
lvl_threshold = 0
```
В TheHive будут отправлены события с уровнем критичности равным или большим. Подробнее про классификацию событий в Wazuh можно прочитать здесь: [wazuh-rules-classification](https://documentation.wazuh.com/3.12/user-manual/ruleset/rules-classification.html)
Vadim M.
