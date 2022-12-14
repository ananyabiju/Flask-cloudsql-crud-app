// serviceaccount module

variable "sa_name" {
  description = "The service account name (e.g. cloud-sql-proxy)"
  type        = string
}

variable "sa_role" {
  description = "The role assigned to the service account (e.g. roles/cloudsql.editor)"
  type        = string
}

variable "project_id" {

}
