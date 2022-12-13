// serviceaccount module


resource "google_service_account" "proxy_account" {
  account_id  = var.sa_name
  description = "The service account used by Cloud SQL Proxy to connect to the db"
  project = var.project_id
}

resource "google_project_iam_member" "role" {
  project = var.project_id
  role    = var.sa_role
  member  = "serviceAccount:${google_service_account.proxy_account.email}"
}

resource "google_service_account_key" "key" {
  service_account_id = google_service_account.proxy_account.name
}
