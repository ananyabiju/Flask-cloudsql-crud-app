
output "email" {
  value = google_service_account.proxy_account.email
}

output "private_key" {
  value     = base64decode(google_service_account_key.key.private_key)
  sensitive = true
}
