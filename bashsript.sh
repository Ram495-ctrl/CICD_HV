#!/bin/bash

# Path to your repository and target directory
REPO_DIR="/home/ubuntu/repo"
TARGET_DIR="/var/www/app1"

# Add the repository directory to Git safe directories
git config --global --add safe.directory $REPO_DIR

# Navigate to the repository directory
cd $REPO_DIR || { echo "Repository directory not found"; exit 1; }

# Pull the latest changes from the main branch
sudo git pull origin main

# Ensure the target directory exists
sudo mkdir -p $TARGET_DIR

# Copy the index.html file to the target directory
sudo cp $REPO_DIR/index.html $TARGET_DIR/index.html

# Set the correct ownership and permissions
# Assuming you want the 'www-data' user (default for Nginx) to own the files
sudo chown www-data:www-data $TARGET_DIR/index.html

# Set permissions (644 for files)
sudo chmod 644 $TARGET_DIR/index.html

# Restart Nginx to apply the changes
sudo systemctl restart nginx

echo "Deployment complete!"

