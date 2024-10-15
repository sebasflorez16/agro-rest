import { fetchWithoutToken, fetchWithToken } from 'static/js/fetch.js';   

// Función para el login
export const startLogin = (username, password) => {
    console.log('Redirigiendo al dashboard......')
    return async (dispatch) => {
        try {
            const response = await fetchWithoutToken('/login/', { username, password }, 'POST');
            console.log('aca puede estar el error')
            const body = await response.json(); // Obtiene el cuerpo de la respuesta
            console.log('Response body:', body);

            // Almacena el token en el localStorage
            localStorage.setItem('accessToken', body.access);
            localStorage.setItem('refreshToken', body.refresh);
            localStorage.setItem('username', body.user.username);

            console.log('Token almacenado en localStorage:', localStorage.getItem('accessToken'));

            // Redirige al dashboard
            console.log('Redirigiendo al dashboard......')
            window.location.href = 'dashboard/';
        } catch (error) {
            console.error('Error during login:', error);
            alert('Login failed. Please check your credentials and try again.');
        }
    };
};

// Función para acceder a rutas protegidas, por ejemplo el dashboard
export const getDashboardData = async () => {
    try {
        const response = await fetchWithToken('dashboard/'); // Usa fetchWithToken para acceder al dashboard

        if (response.ok) {
            const data = await response.json();  // Maneja los datos del dashboard aquí
            console.log('Dashboard data:', data);
        } else {
            if (response.status === 401) {
                alert('La sesion expiró. Por favor, inicia sesión nuevamente.');
                window.location.href = '/login/';
            } else {
                throw new Error('Error en el fetch de dashboard');
            }
        }
    } catch (error) {
        console.error('Error en el fetch de dashboard:', error);
    }
};

// Función para hacer logout (opcional)
export const logout = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('username');
    window.location.href = '/login/';
};