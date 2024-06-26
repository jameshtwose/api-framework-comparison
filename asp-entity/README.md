### ASP.NET (8.0) + Entity Framework
- Tutorial: https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api?view=aspnetcore-8.0&tabs=visual-studio-code
- Initial setup: `dotnet new web -o asp-entity` (run once)
- `cd asp-entity`
- `dotnet add package Microsoft.EntityFrameworkCore.InMemory`
- `dotnet add package Microsoft.AspNetCore.Diagnostics.EntityFrameworkCore`
- Get the pgsql package compatible with .NET 8.0
    - `dotnet add package Aspire.Npgsql.EntityFrameworkCore.PostgreSQL --version 8.0.0-preview.2.23619.3`
- `dotnet add package Swashbuckle.AspNetCore`
- `dotnet dev-certs https --trust` 
- `dotnet run --launch-profile https`
- `http://localhost:5259/swagger/index.html` (Swagger UI)

### Docker
- `docker build -t asp-entity .`
- `docker run -d -p 8085:8080 --name asp-entity asp-entity`