### Gin + Gorm implementation
#### Go
- `go run main.go`

#### Docker
- `docker build -t gin-gorm .`
- `docker run -d -p 8083:8083 gin-gorm`

#### Go initial setup
- `go mod init gin-gorm`
- `go get -u github.com/gin-gonic/gin`
- `go get -u gorm.io/gorm`
- `go get -u gorm.io/driver/postgres`
<!-- swag -->
- `go install github.com/swaggo/swag/cmd/swag@latest`
    - `export PATH=$(go env GOPATH)/bin:$PATH` - add go bin to path (for swag if not working)
- `go get -u github.com/swaggo/gin-swagger`
- `go get -u github.com/swaggo/files`
- `swag init`