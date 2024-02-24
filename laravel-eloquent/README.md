### Laravel + Eloquent
- `brew install php` - Installs PHP
- `brew install composer` - Installs Composer
- `cd laravel-eloquent` - Changes the current directory to laravel-eloquent
- `composer create-project laravel/laravel .` - Creates a new Laravel project
- set the following in `.env`:
```
DB_CONNECTION=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
DB_DATABASE=postgres
DB_USERNAME=postgres
DB_PASSWORD=changeme
```
- `php artisan serve --port=8005` - Starts the Laravel server
- `php artisan make:model Complaints` - Creates a new model