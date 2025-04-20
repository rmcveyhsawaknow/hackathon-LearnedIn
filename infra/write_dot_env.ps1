# Clear the contents of the .env file
Set-Content -Path .env -Value ""

# Retrieve values
$azureTenantId = azd env get-value AZURE_TENANT_ID
$azureOpenAiService = azd env get-value AZURE_OPENAI_SERVICE
$azureOpenAiEndpoint = azd env get-value AZURE_OPENAI_ENDPOINT
$azureOpenAiChatDeployment = azd env get-value AZURE_OPENAI_CHAT_DEPLOYMENT
$azureOpenAiChatModel = azd env get-value AZURE_OPENAI_CHAT_MODEL
$azureOpenAiEmbeddingDeployment = azd env get-value AZURE_OPENAI_EMBEDDING_DEPLOYMENT
$azureOpenAiEmbeddingModel = azd env get-value AZURE_OPENAI_EMBEDDING_MODEL

# Check if values are set and append to .env file
Add-Content -Path .env -Value "API_HOST=azure"
Write-Host "API_HOST=azure"

if (-not [string]::IsNullOrEmpty($azureTenantId)) {
    Add-Content -Path .env -Value "AZURE_TENANT_ID=$azureTenantId"
    Write-Host "AZURE_TENANT_ID=$azureTenantId"
} else {
    Write-Host "AZURE_TENANT_ID is not set."
}

if (-not [string]::IsNullOrEmpty($azureOpenAiService)) {
    Add-Content -Path .env -Value "AZURE_OPENAI_SERVICE=$azureOpenAiService"
    Write-Host "AZURE_OPENAI_SERVICE=$azureOpenAiService"
} else {
    Write-Host "AZURE_OPENAI_SERVICE is not set."
}

if (-not [string]::IsNullOrEmpty($azureOpenAiEndpoint)) {
    Add-Content -Path .env -Value "AZURE_OPENAI_ENDPOINT=$azureOpenAiEndpoint"
    Write-Host "AZURE_OPENAI_ENDPOINT=$azureOpenAiEndpoint"
} else {
    Write-Host "AZURE_OPENAI_ENDPOINT is not set."
}

Add-Content -Path .env -Value "AZURE_OPENAI_VERSION=2024-10-21"
Write-Host "AZURE_OPENAI_VERSION=2024-10-21"

if (-not [string]::IsNullOrEmpty($azureOpenAiChatDeployment)) {
    Add-Content -Path .env -Value "AZURE_OPENAI_CHAT_DEPLOYMENT=$azureOpenAiChatDeployment"
    Write-Host "AZURE_OPENAI_CHAT_DEPLOYMENT=$azureOpenAiChatDeployment"
} else {
    Write-Host "AZURE_OPENAI_CHAT_DEPLOYMENT is not set."
}

if (-not [string]::IsNullOrEmpty($azureOpenAiChatModel)) {
    Add-Content -Path .env -Value "AZURE_OPENAI_CHAT_MODEL=$azureOpenAiChatModel"
    Write-Host "AZURE_OPENAI_CHAT_MODEL=$azureOpenAiChatModel"
} else {
    Write-Host "AZURE_OPENAI_CHAT_MODEL is not set."
}

if (-not [string]::IsNullOrEmpty($azureOpenAiEmbeddingDeployment)) {
    Add-Content -Path .env -Value "AZURE_OPENAI_EMBEDDING_DEPLOYMENT=$azureOpenAiEmbeddingDeployment"
    Write-Host "AZURE_OPENAI_EMBEDDING_DEPLOYMENT=$azureOpenAiEmbeddingDeployment"
} else {
    Write-Host "AZURE_OPENAI_EMBEDDING_DEPLOYMENT is not set."
}

if (-not [string]::IsNullOrEmpty($azureOpenAiEmbeddingModel)) {
    Add-Content -Path .env -Value "AZURE_OPENAI_EMBEDDING_MODEL=$azureOpenAiEmbeddingModel"
    Write-Host "AZURE_OPENAI_EMBEDDING_MODEL=$azureOpenAiEmbeddingModel"
} else {
    Write-Host "AZURE_OPENAI_EMBEDDING_MODEL is not set."
}