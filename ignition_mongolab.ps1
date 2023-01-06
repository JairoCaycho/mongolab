param ($ExecutionGroup = '')

$MongoLabPath = $PSScriptRoot
. cd $MongoLabPath


function ignition_branch ($selected_group) {
    $CurrentBranch = git branch --show-current
    if ($CurrentBranch -ne $selected_group) {
        . git checkout $selected_group
        $CurrentBranch = git branch --show-current
    }
    # maybe the second if is unnecesary, can be skiped and go directly to else?
    if ($CurrentBranch -ne $selected_group) {
        Write-Host "ERROR while checking to selected branch." -ForegroundColor DarkRed
        Exit
    }
    else {
        Write-Host "`t1. Execution branch: $CurrentBranch" -ForegroundColor Magenta
    }
}


function proper_venv ($working_env) {
    if ($env:VIRTUAL_ENV -eq "$StategyBuilderPath\environments\$working_env") {
        Write-Host "`t2. Working virtual environment: <$working_env>" -ForegroundColor DarkBlue
    }
    else {
        if (Test-Path env:VIRTUAL_ENV) {
            Write-Host "`t2. Deactivating ... >>> Activatig $working_env..." -ForegroundColor DarkBlue
            deactivate
        }
        else {
            Write-Host "`t2. Activatig $working_env..." -ForegroundColor DarkBlue
        }
        . $MongoLabPath\environments\$working_env\Scripts\Activate.ps1
    }
}


function mongolab_ignition {
    . py .\src\__main__.py
}

function checkpoint_confirmation ($ExecutionGroup) {
    if ($ExecutionGroup -eq 'master') {
        mongolab_ignition
    }
    else {
        $confirmation = Read-Host -Prompt "ARE YOU SURE? [YES/n]"
        if ($confirmation -eq 'YES') {
            mongolab_ignition
        }
        else {
            . cd $MongoLabPath
            Write-Host "`t`t`t`tnope! ==== THE END."
        }
    }
}


# INIT: validation of group parameter, if it's empty execution is terminated
if ($ExecutionGroup -eq '') {
    return "Execution Group must be provided."
}
else {
    Write-Host "MONGODB LAB" -ForegroundColor DarkRed
    if ($ExecutionGroup -eq 'main') {
        $WorkingEnvironment = 'production'
        ignition_branch $ExecutionGroup
    }
    else {
        $WorkingEnvironment = 'dev'
        ignition_branch $WorkingEnvironment
    }
    proper_venv $WorkingEnvironment
    checkpoint_confirmation $ExecutionGroup
}