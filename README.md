# arrival
Чеклист arrival.txt, разметка markdown. Он специально сделан достаточно атомарным, при реальных проверках их можно комбинировать, напрмер, используя pairwise.

Для автотестов добавлен allure.
yaml используетсся для хранения данных о хостах и окружениях. 

Запуск автотестов:
 - py.test --alluredir [path_to_report_dir] - где  [path_to_report_dir], папка в которую будут сложены результаты тестов
 - allure serve [path_to_report_dir] - отчет откроется на локальном хосте

