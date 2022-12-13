// db module

resource "google_sql_database" "main" {
  name     = "employeedb"
  instance = google_sql_database_instance.main_primary.name
  project = var.project_id
}

resource "google_sql_database_instance" "main_primary" {
  name             = "crud-app"
  database_version = "MYSQL_8_0"
  depends_on       = [var.db_depends_on]
  deletion_protection = false
  settings {
    tier              = var.instance_type
    availability_type = "ZONAL" # use "REGIONAL" for prod to distribute data storage across zones

    ip_configuration {
      ipv4_enabled    = false        # don't give the db a public IPv4
      private_network = var.vpc_link # the VPC where the db will be assigned a private IP
    }
  }
  project = var.project_id
}

resource "google_sql_user" "db_user" {
  name     = var.user
  instance = google_sql_database_instance.main_primary.name
  password = var.password
  project = var.project_id
}
