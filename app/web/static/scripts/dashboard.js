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
    } catch (error) {
        console.error('Error fetching table data:', error);
        const serviceData = document.querySelector('.service-data-content');
        serviceData.innerHTML = '<p class="flash-message error">Произошла ошибка. Пожалуйста, попробуйте еще раз.</p>';
    };
};