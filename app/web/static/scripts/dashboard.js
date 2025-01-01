document.addEventListener('DOMContentLoaded', () => {
    const serviceButtons = document.querySelectorAll('.service-select-button');

    serviceButtons.forEach(button => {
        button.addEventListener('click', async (event) => {
            // Remove 'selected' class from all buttons
            serviceButtons.forEach(btn => btn.classList.remove('selected'));

            // Add 'selected' class to the clicked button
            event.target.classList.add('selected');
            
            const service = event.target.getAttribute('data-service');

            try {
                // Fetch tables for the selected service
                const response = await fetch(`/dashboard/tables?service=${service}`);
                const tables = await response.json();

                const serviceHeader = document.querySelector('.service-data-header');
                const serviceContent = document.querySelector('.service-data-content');

                if (response.ok && tables.length > 0) {
                    // Clear previous header and content
                    serviceHeader.innerHTML = '';
                    serviceContent.innerHTML = '<p class="flash-message">Выберите таблицу, чтобы увидеть данные.</p>';

                    // Render buttons for tables
                    tables.forEach(table => {
                        const tableButton = document.createElement('button');
                        tableButton.className = 'table-select-button';
                        tableButton.textContent = table.name;
                        tableButton.dataset.table = table.name;

                        // Attach event listener to fetch table data
                        tableButton.addEventListener('click', async (event) => {
                            const tableButtons = document.querySelectorAll('.table-select-button');
                            tableButtons.forEach(btn => btn.classList.remove('selected'));
                            event.target.classList.add('selected');

                            await fetchTableData(service, table.name)
                        });

                        serviceHeader.appendChild(tableButton);
                    });
                } else {
                    serviceHeader.innerHTML = '<p class="flash-message error">Нет доступных таблиц для данного сервиса.</p>';
                    serviceContent.innerHTML = '';
                }
            } catch (error) {
                console.error('Error fetching tables:', error);
                const serviceHeader = document.querySelector('.service-data-header');
                serviceHeader.innerHTML = '<p class="flash-message error">Произошла ошибка. Пожалуйста, попробуйте еще раз.</p>';
            };
        });
    });
});

async function fetchTableData(service, table) {
    try {
        const response = await fetch(`/dashboard/table?service=${service}&table=${table}`);
        const data = await response.json();

        const serviceData = document.querySelector('.service-data-content');
        serviceData.innerHTML = '';

        let columnOrder = [];
        let columnTranslations = {};
        let cellTranslations = {};

        if (service === 'services' && table === 'Пользователи') {
            columnOrder = [
                'telegram_id',
                'services_name',
                'services_role',
                'rate',
                'experience',
                'services_registration_date',
                'registered_in_services'
            ];

            columnTranslations = {
                'telegram_id': 'Телеграм ID',
                'services_name': 'Имя',
                'services_role': 'Роль',
                'rate': 'Ставка ₽/час',
                'experience': 'Опыт (в годах)',
                'services_registration_date': 'Дата регистрации'
            };

            cellTranslations = {
                'customer': 'Заказчик',
                'performer': 'Исполнитель'
            };
        } else if (service === 'services' && table === 'Заказы') {
            columnOrder = [
                'id',
                'customer_telegram_id',
                'customer_name',
                'city',
                'description',
                'deadline_from',
                'deadline_to',
                'instrument_provided',
                'closed'
            ];

            columnTranslations = {
                'id': 'ID',
                'customer_telegram_id': 'Телеграм ID заказчика',
                'customer_name': 'Имя заказчика',
                'city': 'Город',
                'description': 'Описание',
                'deadline_from': 'Дата начала',
                'deadline_to': 'Дата окончания',
                'instrument_provided': 'Предоставляется инструмент',
                'closed': 'Закрыта'
            };

            cellTranslations = {
                'true': 'Да',
                'false': 'Нет'
            };
        } else if (service === 'delivery' && table === 'Пользователи') {
            columnOrder = [
                'telegram_id',
                'delivery_name',
                'delivery_role',
                'date_of_birth',
                'has_car',
                'car_model',
                'car_width',
                'car_length',
                'car_height',
                'delivery_registration_date',
                'registered_in_delivery'
            ];

            columnTranslations = {
                'telegram_id': 'Телеграм ID',
                'delivery_name': 'Имя',
                'delivery_role': 'Роль',
                'date_of_birth': 'Дата рождения',
                'has_car': 'Есть машина',
                'car_model': 'Модель машины',
                'car_width': 'Ширина машины',
                'car_length': 'Длина машины',
                'car_height': 'Высота машины',
                'delivery_registration_date': 'Дата регистрации'
            };

            cellTranslations = {
                'customer': 'Заказчик',
                'courier': 'Курьер',
                'true': 'Да',
                'false': 'Нет'
            };
        } else if (service === 'delivery' && table === 'Доставки') {
            columnOrder = [
                'id',
                'customer_telegram_id',
                'customer_name',
                'city',
                'description',
                'deliver_from',
                'deliver_to',
                'closed'
            ];

            columnTranslations = {
                'id': 'ID',
                'customer_telegram_id': 'Телеграм ID заказчика',
                'customer_name': 'Имя заказчика',
                'city': 'Город',
                'description': 'Описание',
                'deliver_from': 'Откуда доставить',
                'deliver_to': 'Куда доставить',
                'closed': 'Закрыта'
            };

            cellTranslations = {
                'true': 'Да',
                'false': 'Нет'
            };
        } else if (service === 'game' && table === 'Игровые сессии') {
            columnOrder = [
                'id',
                'session_date',
                'players_amount',
                'finished'
            ];

            columnTranslations = {
                'id': 'ID',
                'session_date': 'Дата игровой сессии',
                'players_amount': 'Количество игроков',
                'finished': 'Сессия завершена'
            };

            cellTranslations = {
                'true': 'Да',
                'false': 'Нет'
            };
        };

        if (response.ok && data.length > 0) {
            const filteredData = data.filter(row => {
                if (service === 'services' && table === 'Пользователи') {
                    return row.registered_in_services === true;
                } else if (service === 'delivery' && table === 'Пользователи') {
                    return row.registered_in_delivery === true;
                } else {
                    return true;
                };
            });
            console.log(filteredData);
            const excludedColumns = ['registered_in_services', 'registered_in_delivery'];
            const displayedColumns = columnOrder.filter(column => !excludedColumns.includes(column));

            const tableElement = document.createElement('table');
            tableElement.className = 'data-table';

            const headerRow = document.createElement('tr');
            headerRow.className = 'data-table-header';
            displayedColumns.forEach(column => {
                const th = document.createElement('th');
                th.className = 'data-table-header-cell';
                th.textContent = columnTranslations[column] || column;
                headerRow.appendChild(th);
            });
            tableElement.appendChild(headerRow);

            filteredData.forEach(row => {
                const tableRow = document.createElement('tr');
                tableRow.className = 'data-table-row';
                displayedColumns.forEach(column => {
                    const td = document.createElement('td');
                    td.className = 'data-table-cell';
                    
                    if (column === 'services_role') {
                        td.textContent = cellTranslations[row[column]] || row[column];
                    } else if (column === 'closed' || column === 'instrument_provided') {
                        const booleanValue = row[column] === true ? 'true' : 'false';
                        td.textContent = cellTranslations[booleanValue] || booleanValue;
                    } else if (column === 'delivery_role') {
                        td.textContent = cellTranslations[row[column]] || row[column];
                    } else if (column === 'has_car' && row['delivery_role'] === 'customer') {
                        return;
                    } else if (column === 'has_car') {
                        const booleanValue = row[column] === true ? 'true' : 'false';
                        td.textContent = cellTranslations[booleanValue] || booleanValue;
                    } else if (column === 'session_date') {
                        const date = new Date(row[column]).toISOString().split('T')[0];
                        const time = new Date(row[column]).toISOString().split('T')[1].split('.')[0];
                        td.textContent = `${date} ${time}`;
                    } else if (column === 'finished') {
                        const booleanValue = row[column] === true ? 'true' : 'false';
                        td.textContent = cellTranslations[booleanValue] || booleanValue;
                    } else {
                        td.textContent = row[column] || '';
                    };

                    tableRow.appendChild(td);
                });
            tableElement.appendChild(tableRow);
        });

            serviceData.appendChild(tableElement);
        } else {
            serviceData.innerHTML = '<p class="flash-message error">Нет данных для данной таблицы.</p>';
        };
    } catch (error) {
        console.error('Error fetching table data:', error);
        const serviceData = document.querySelector('.service-data-content');
        serviceData.innerHTML = '<p class="flash-message error">Произошла ошибка. Пожалуйста, попробуйте еще раз.</p>';
    };
};
