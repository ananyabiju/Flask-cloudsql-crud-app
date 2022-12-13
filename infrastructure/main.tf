module "vpc" {
  source = "./modules/vpc"

  vpc_name = "test-net-1"
  project_id=var.project_id
}


module "db" {
  source = "/Users/ananya.biju/Documents/Flask-cloudsql-crud-app/infrastructure/modules/db"

  disk_size     = 10
  instance_type = "db-f1-micro"
  password      = var.db_password # This is a variable because it's a secret. It's stored here: https://app.terraform.io/app/<YOUR-ORGANIZATION>/workspaces/<WORKSPACE>/variables
  user          = var.db_username
  vpc_name      = module.vpc.name
  vpc_link      = module.vpc.link
  project_id    = var.project_id
  # There's a dependency relationship between the db and the VPC that
  # terraform can't figure out. The db instance depends on the VPC because it
  # uses a private IP from a block of IPs defined in the VPC. If we just giving
  # the db a public IP, there wouldn't be a dependency. The dependency exists
  # because we've configured private services access. We need to explicitly
  # specify the dependency here. For details, see the note in the docs here:
  #   https://www.terraform.io/docs/providers/google/r/sql_database_instance.html#private-ip-instance
  db_depends_on = module.vpc.private_vpc_connection
}

#module "dbproxy" {
  #source = "./modules/dbproxy"

  #machine_type     = "f1-micro"
  #db_instance_name = module.db.connection_name # e.g. my-project:us-central1:my-db
  #project_id       = var.project_id
  #gcp_region = var.gcp_region
  #gcp_zone=var.gcp_zone

  # By passing the VPC name as the output of the VPC module we ensure the VPC
  # will be created before the proxy.
  #vpc_name = module.vpc.name
  #depends_on = [
  #  module.vpc
 # ]
#}
#module "wrkload"{
 # source                     = "/Users/abindas.devadas/Desktop/pro-nw/modules/wrkload"
  #project_id                 = var.project_id

  #depends_on = [
   # module.gke
#]

#}

module "gke" {
  source                     = "terraform-google-modules/kubernetes-engine/google"
  project_id                 = var.project_id
  name                       = var.gke_cluster_name
  region                     = var.gke_regions
  regional                   = false
  ip_range_pods              = ""
  ip_range_services          = ""
  zones                      = var.gke_zones
  network                    = "test-net-1"
  subnetwork                 = "test-subnetwork"
  http_load_balancing        = true
  network_policy             = false
  horizontal_pod_autoscaling = true
  filestore_csi_driver       = false
  depends_on = [
    module.vpc
]
  node_pools = [
    {
      name                      = var.gke_default_nodepool_name
      machine_type              = "e2-medium"
      node_locations            = "us-west1-b,us-west1-c"
      min_count                 = 1
      max_count                 = 3
      local_ssd_count           = 0
      spot                      = false
      disk_size_gb              = 100
      disk_type                 = "pd-standard"
      image_type                = "COS_CONTAINERD"
      enable_gcfs               = false
      enable_gvnic              = false
      auto_repair               = true
      auto_upgrade              = true
      create_service_account    = false
      #service_account           = var.gke_service_account_name
      preemptible               = true
      initial_node_count        = 1
      deletion_protection       = false
    },
  ]

  node_pools_oauth_scopes = {
    all = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }

  node_pools_labels = {
    all = {}

    default-node-pool = {
      default-node-pool = true
    }
  }

  node_pools_metadata = {
    all = {}

    default-node-pool = {
      node-pool-metadata-custom-value = "my-node-pool"
    }
  }

  node_pools_taints = {
    all = []

    default-node-pool = [
      {
        key    = "default-node-pool"
        value  = true
        effect = "PREFER_NO_SCHEDULE"
      },
    ]
  }

  node_pools_tags = {
    all = []

    default-node-pool = [
      "default-node-pool",
    ]
  }
}
