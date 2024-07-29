// File: MySdk.js

class MySdk {
    constructor(config) {
        if (!config.apiKey || !config.apiBaseUrl) {
            throw new Error('API key and Base URL must be provided');
        }
        this.apiKey = config.apiKey;
        this.apiBaseUrl = config.apiBaseUrl;
    }

    async fetchApi(endpoint, method = 'GET', data = null) {
        try {
            const options = {
                method,
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.apiKey}`
                }
            };

            if (data) {
                options.body = JSON.stringify(data);
            }

            const response = await fetch(`${this.apiBaseUrl}/${endpoint}`, options);

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            return await response.json();
        } catch (error) {
            console.error('Fetch error:', error);
            throw error;
        }
    }

    getUsers() {
        return this.fetchApi('users');
    }

    createUser(userData) {
        return this.fetchApi('users', 'POST', userData);
    }
}

// Expose to global scope
window.MySdk = MySdk;
