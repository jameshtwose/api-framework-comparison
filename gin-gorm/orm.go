package main

import (
	"time"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type ComplaintsTable struct {
	// gorm.Model
	date_received                time.Time
	product                      string
	sub_product                  string
	issue                        string
	sub_issue                    string
	consumer_complaint_narrative string
	company_public_response      string
	company                      string
	state                        string
	zip_code                     string
	tags                         string
	consumer_consent_provided    string
	submitted_via                string
	date_sent_to_company         time.Time
	company_response_to_consumer string
	timely_response              bool
	consumer_disputed            bool
	complaint_id                 uint `gorm:"primary_key"`
}

func (ComplaintsTable) TableName() string {
	return "complaints_table"
}

func main() {
	dsn := "host=localhost user=postgres password=changeme dbname=postgres port=5432 sslmode=disable TimeZone=Europe/Amsterdam"
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	var complaint ComplaintsTable
	// db.First(&complaint, 1) // find product with id 1

	// // Get first matched record
	db.First(&complaint, "product = ?", "Debt collection") // find product with code l1212

	// // Get all matched records
	// db.Find(&complaint, "product = ?", "Debt collection") // find product with code l1212

	// // Get all records
	// db.Find(&complaint) // find all product

	// // Get first matched record ordered by primary key (order by primary key desc)
	// db.Take(&complaint, 1) // find product with id 1

	// // Get last matched record ordered by primary key (order by primary key asc)
	// db.Last(&complaint, "product = ?", "Debt collection") // find product with id 1

	// // Get all matched records ordered by primary key (order by primary key asc)
	// db.Find(&complaint, "product = ?", "Debt collection") // find product with id 1
}
