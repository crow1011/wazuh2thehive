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
**name** - название итегратора(не нужно изменять)
**hook_url** - адрес TheHive
**api\_key** - API ключ TheHive пользователя. Сгенериоровать ключ можно на странице управления пользователями, авторизовавшись от администратора. Для безопасности разрешите api-пользователю только создание alert.
**alert\_format** - формат, в котором wazuh передает в интегратор alert(не нужно изменять)

после настройки примените примените изменения командой:
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
Vadim M.