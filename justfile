#    <one line to give the program's name and a brief idea of what it does.>  
#    Copyright © 2024 Charudatta
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#    email contact: 152109007c@gmailcom

set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]

default:
    @just --choose

# create files and directories
init:
    #!pwsh
    git init
    New-Item -ItemType "file" -Path ".env", ".gitattribute", "main.py", "requirements.yaml"
    New-Item -ItemType "directory" -Path "docs", "src", "tests"
    gig gen python > .gitignore 
    Add-LicenseHeader
    7z a archives.7z .gitignore

# set configuration variables
config:
    #!pwsh
    SetEnvVar

# add documentation to repo
docs:
    #!pwsh
    conda activate blog
    python -m mkdocs new .

# genearte and readme to repo    
readme:
    #!pwsh
    conda activate w
    python C:/Users/$env:username/Documents/GitHub/readmeGen/main.py

# version control repo with git
commit message="init":
    #!pwsh
    git add .
    git commit -m {{message}}

# create windows executable
exe file_name:
    #!pwsh
    pyinstaller src/{{file_name}} --onefile

# run python unit test 
tests:
    #!pwsh
    python -m unittest discover -s tests

# Add custom tasks, enviroment variables

exit:
    #!pwsh
    write-Host "Copyright © 2024 Charudatta"
    Write-Host "email contact: 152109007c@gmailcom"
    Write-Host "Exiting Folder" 
    [System.IO.Path]::GetFileName($(Get-Location))

run file_name:
    #!pwsh
    iverilog -o build/{{file_name}}.vvp src/{{file_name}}.v tests/test_{{file_name}}.v
    vvp build/{{file_name}}.vvp
    gtkwave build/{{file_name}}.vcd

runx:
    #!pwsh
    #conda activate n
    #python ../src/gan.py 
    cd build
    iverilog -o gan.vvp test_gan.v
    vvp gan.vvp
    gtkwave gan.vcd 


        

