import { fetchWithoutToken} from "./fetch.js";

// función para el login
export const startLogin = (username, password) => {
    return async (dispatch) => {
        try {
            // Llama a fetchWithoutToken para realizar el POST al endpoint de login
            const response = await fetchWithoutToken('login/', { username, password }, 'POST');

            // Verifica si la respuesta es exitosa
            if (response.ok) {
                const body = await response.json();  // Obtén el cuerpo de la respuesta
                console.log('Response body:', body);

                // Almacena el token en el localStorage
                localStorage.setItem('accessToken', body.access);
                localStorage.setItem('refreshToken', body.refresh);
                localStorage.setItem('username', body.user.username);

                console.log('Token almacenado en localStorage:', localStorage.getItem('accessToken'));

                // Redirige al dashboard
                window.location.href = 'dashboard/';
            } else {
                console.error('Login failed:', await response.json());
            }
        } catch (error) {
            console.error('Error during login:', error);
        }
    }
}
