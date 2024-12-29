document.addEventListener('DOMContentLoaded', () => {
    const serviceButtons = document.querySelectorAll('.service-select-button');

    serviceButtons.forEach(button => {
        button.addEventListener('click', async (event) => {
            const service = event.target.getAttribute('data-service');

            try {
                // Fetch tables for the selected service
                const response = await fetch(`/api/tables?service=${service}`);
                const tables = await response.json();

                const serviceHeader = document.querySelector('.service-data-header');
                const serviceContent = document.querySelector('.service-data-content');

                if (response.ok && tables.length > 0) {
                    // Clear previous header and content
                    serviceHeader.innerHTML = '';
                    serviceContent.innerHTML = '<p>Выберите таблицу, чтобы увидеть данные.</p>';

                    // Render buttons for tables
                    tables.forEach(table => {
                        const tableButton = document.createElement('button');
                        tableButton.className = 'table-select-button';
                        tableButton.textContent = table.name;
                        tableButton.dataset.table = table.name;

                        // Attach event listener to fetch table data
                        tableButton.addEventListener('click', () => fetchTableData(service, table.name));
                        serviceHeader.appendChild(tableButton);
                    });
                } else {
                    serviceHeader.innerHTML = '<p>Нет доступных таблиц для данного сервиса.</p>';
                    serviceContent.innerHTML = '';
                }
            } catch (error) {
                console.error('Error fetching tables:', error);
            }
        });
    });

    // Function to fetch and display table data
    async function fetchTableData(service, tableName) {
        const serviceContent = document.querySelector('.service-data-content');

        try {
            const response = await fetch(`/api/table-data?service=${service}&table=${tableName}`);
            const rows = await response.json();

            if (response.ok && rows.length > 0) {
                let table = `<table>
                    <thead>
                        <tr>${Object.keys(rows[0]).map(key => `<th>${key}</th>`).join('')}</tr>
                    </thead>
                    <tbody>`;

                rows.forEach(row => {
                    table += `<tr>${Object.values(row).map(value => `<td>${value}</td>`).join('')}</tr>`;
                });

                table += `</tbody></table>`;
                serviceContent.innerHTML = table;
            } else {
                serviceContent.innerHTML = '<p>Данные таблицы не найдены.</p>';
            }
        } catch (error) {
            console.error('Error fetching table data:', error);
            serviceContent.innerHTML = '<p>Ошибка загрузки данных таблицы.</p>';
        }
    }
});
