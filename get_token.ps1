# get_token.ps1
try {
    # Login interativo usando Device Code
    Write-Host "Autenticando no Power BI..."
    Connect-PowerBIServiceAccount -Device

    # Obter o token de acesso após a autenticação bem-sucedida
    $token = Get-PowerBIAccessToken -AsString
    Write-Output $token
} catch {
    Write-Error $_.Exception.Message
}
