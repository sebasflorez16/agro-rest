import { API_URL } from './config.js';

// Función para hacer peticiones sin token (por ejemplo, login)
export const fetchWithoutToken = (endpoint, data, method = 'GET') => {
    const url = `${API_URL}/${endpoint}`;

    if (method === 'GET') {
        return fetch(url);
    } else {
        return fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
    }
};

// Función para hacer peticiones con token (requiere estar autenticado)
export const fetchWithToken = (endpoint, data = {}, method = 'GET') => {
    const url = `${API_URL}/${endpoint}`;
    const token = localStorage.getItem('accessToken'); // JWT token de acceso

    if (!token) {
        console.error('No se encontró el token en localStorage');
        window.location.href = '/login/';
        return;
    }

    if (method === 'GET') {
        return fetch(url, {
            method,
            headers: {
                'Authorization': `Bearer ${token}`,
            }
        });
    } else {
        return fetch(url, {
            method,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`,
            },
            body: JSON.stringify(data)
        });
    }
};

// Redireccionar al dashboard si está autenticado
document.addEventListener('DOMContentLoaded', function () {
    const currentPath = window.location.pathname;

    if (currentPath === '/dashboard/') {
        fetchWithToken('dashboard/')
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else if (response.status === 401) {
                    window.location.href = '/login/'; // Redirige si no está autenticado
                } else {
                    throw new Error('Error fetching dashboard data');
                }
            })
            .then(data => {
                console.log('Dashboard data:', data); // Aquí puedes manejar la data del dashboard
            })
            .catch(error => console.error('Error:', error));
    }
});
