using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;



var builder = WebApplication.CreateBuilder(args);
// add the services for swagger
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
// add the postgresql connection
builder.AddNpgsqlDataSource("postgresdb");
// builder.AddNpgsqlDbContext<ApiDbContext>("postgresdb");

var app = builder.Build();

// add the endpoints
// Get the root path of the app
// it will return {"Hello": "Welcome to the ASP.NET - Entity API"}
app.MapGet("/", () => Results.Ok(new { Hello = "Welcome to the ASP.NET - Entity API" }));

// Get the first X rows from the complaints_table table
// app.MapGet("/complaints", async (ApiDbContext dbContext) =>
// {
//     var complaints = await dbContext.complaints_table.Take(10).ToListAsync();
//     return Results.Ok(complaints);
// });

// run swagger
app.UseSwagger();
app.UseSwaggerUI();
// run the app
app.Run();
