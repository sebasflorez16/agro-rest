const API_URL = 'http://localhost:8000';  // URL base del backend

// Función para hacer peticiones sin token (ejemplo: login)
export const fetchWithoutToken = async (endpoint, data, method = 'GET') => {
    const url = `${API_URL}/${endpoint}`;  // Concatena la URL base con el endpoint

    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
        },
    };

    // Si no es un método GET, añade el cuerpo de la petición con los datos
    if (method !== 'GET') {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(url, options);  // Realiza la petición
        if (!response.ok) {
            throw new Error('Network response was not ok');  // Si no es exitosa, lanza un error
        }
        return response;  // Devuelve la respuesta
    } catch (error) {
        console.error('Error in fetchWithoutToken:', error);
        throw error;
    }
};

// Función para hacer peticiones con token (requiere estar autenticado)
export const fetchWithToken = async (endpoint, data = {}, method = 'GET') => {
    const url = `${API_URL}/${endpoint}`;
    const token = localStorage.getItem('accessToken');  // Recupera el JWT token almacenado en el localStorage

    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,  // Añade el token en la cabecera
        },
    };

    if (method !== 'GET') {
        options.body = JSON.stringify(data);  // Si no es GET, añade el cuerpo con los datos
    }

    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response;
    } catch (error) {
        console.error('Error in fetchWithToken:', error);
        throw error;
    }
};
